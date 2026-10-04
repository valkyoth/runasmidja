"""Validate public inventory custody, structure, budgets and known host-path privacy."""
import json
import math
import os
import stat
from pathlib import Path
from contextlib import contextmanager
from inventory_privacy import reject_private_paths

PUBLIC_SERVICES = frozenset(('openbao', 'postgres', 'probe', 'probe-base', 'valkey', 'wolfi-base'))


def public_sbom(evidence, service, image, root, extra_roots=()):
    evidence.setdefault('metadata', {}).setdefault('component', {})['name'] = f'runasmidja/{service}@{image}'
    reject_private_paths(evidence, root, extra_roots)
    return evidence


MAX_PUBLIC_SBOM = 16 * 1024 * 1024
MAX_PUBLIC_ENTRIES = 256
MAX_PUBLIC_TOTAL_BYTES = 128 * 1024 * 1024


class InventoryBudgetExceeded(RuntimeError):
    """Stop the complete traversal when aggregate resources are exhausted."""


def bounded_names(directory, budget):
    names = []
    with os.scandir(directory) as entries:
        for entry in entries:
            budget['entries'] += 1
            if budget['entries'] > MAX_PUBLIC_ENTRIES:
                raise InventoryBudgetExceeded('Public inventory entry limit exceeded')
            names.append(entry.name)
    return sorted(names)

# Formats actually emitted by the reviewed Cargo and image inventory tools.
SUPPORTED_SPEC_VERSIONS = frozenset(('1.5', '1.7'))
HISTORICAL_IDENTITIES = {
    'openbao-official-v0.2.2.cdx.json': 'runasmidja/openbao@',
    'valkey-official-v0.2.1.cdx.json': 'runasmidja/valkey@',
    # Preserve the original scanner identity of the blocked official image.
    'postgres-official-blocked-2026-10-03.cdx.json':
        'docker.io/library/postgres@sha256:',
}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate JSON key')
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError('Non-standard JSON constant')


def finite_float(value):
    parsed = float(value)
    if not math.isfinite(parsed):
        raise ValueError('Non-finite JSON number')
    return parsed


def require_unicode_scalars(document):
    # Iterator frames avoid copying wide objects/arrays into a second worklist.
    pending = [iter((document,))]
    while pending:
        try:
            value = next(pending[-1])
        except StopIteration:
            pending.pop()
            continue
        if isinstance(value, str):
            value.encode('utf-8', errors='strict')
        elif isinstance(value, dict):
            pending.append(iter(value.keys()))
            pending.append(iter(value.values()))
        elif isinstance(value, list):
            pending.append(iter(value))
    return document


@contextmanager
def custody_directory(name, parent=None):
    descriptor = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC,
                         dir_fd=parent)
    try:
        info = os.fstat(descriptor)
        if info.st_uid != os.getuid() or info.st_mode & 0o022:
            raise RuntimeError('Inventory directory has invalid custody')
        yield descriptor
    finally:
        os.close(descriptor)


def load_public_json(name, directory, budget=None):
    if budget is None:
        budget = {'entries': 0, 'bytes': 0}
    remaining = MAX_PUBLIC_TOTAL_BYTES - budget['bytes']
    limit = min(MAX_PUBLIC_SBOM, remaining)
    if not isinstance(name, str) or '/' in name or name in ('', '.', '..'):
        raise ValueError('Invalid inventory filename')
    descriptor = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK | os.O_CLOEXEC,
                         dir_fd=directory)
    with os.fdopen(descriptor, 'rb') as source:
        info = os.fstat(source.fileno())
        if (not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or
                info.st_mode & 0o022 or info.st_nlink != 1 or info.st_size > MAX_PUBLIC_SBOM):
            raise RuntimeError('Public inventory has invalid file custody or size')
        if info.st_size > remaining:
            raise InventoryBudgetExceeded('Public inventory byte limit exceeded')
        content = source.read(limit + 1)
        budget['bytes'] += len(content)
        if len(content) > remaining:
            raise InventoryBudgetExceeded('Public inventory byte limit exceeded')
        if len(content) > MAX_PUBLIC_SBOM:
            raise RuntimeError('Public inventory exceeds size limit')
    # Text input prevents Python's bytes-based UTF-16/32 autodetection. A UTF-8
    # BOM is rejected by the JSON decoder, rather than silently stripped.
    document = json.loads(content.decode('utf-8'), object_pairs_hook=unique_object,
                          parse_constant=reject_constant, parse_float=finite_float)
    return require_unicode_scalars(document)


def load_canonical_sbom(name, directory, budget=None):
    report = load_public_json(name, directory, budget)
    if (not isinstance(report, dict) or report.get('bomFormat') != 'CycloneDX' or
            not isinstance(report.get('specVersion'), str) or
            report['specVersion'] not in SUPPORTED_SPEC_VERSIONS or
            not isinstance(report.get('components'), list) or not report['components']):
        raise RuntimeError('Inventory is not a supported CycloneDX SBOM')
    for component in report['components']:
        if not isinstance(component, dict) or any(
                not isinstance(component.get(field), str) or not component[field].strip()
                for field in ('type', 'name')):
            raise RuntimeError('Inventory contains an invalid component')
    return report


def check_sboms(root, extra_roots=()):
    errors, seen = [], set()
    budget = {'entries': 0, 'bytes': 0}
    bindings = {Path('images') / f'{service}.cdx.json': f'runasmidja/{service}@'
                for service in PUBLIC_SERVICES}
    required = set(bindings)
    bindings.update({Path('images') / name: prefix for name, prefix in HISTORICAL_IDENTITIES.items()})

    def walk(directory, relative):
        if len(relative.parts) > 32:
            raise RuntimeError('Inventory directory nesting exceeds limit')
        for name in bounded_names(directory, budget):
            path = relative / name
            try:
                info = os.stat(name, dir_fd=directory, follow_symlinks=False)
                if stat.S_ISLNK(info.st_mode):
                    raise RuntimeError('Inventory tree contains a symlink')
                if stat.S_ISDIR(info.st_mode):
                    with custody_directory(name, directory) as child:
                        walk(child, path)
                elif name.endswith('.json'):
                    seen.add(path)
                    report = (load_canonical_sbom(name, directory, budget) if name.endswith('.cdx.json')
                              else load_public_json(name, directory, budget))
                    if path in bindings:
                        identity = report.get('metadata', {}).get('component', {}).get('name', '')
                        prefix = bindings[path]
                        if (not isinstance(identity, str) or not identity.startswith(prefix) or
                                not identity[len(prefix):].strip()):
                            raise RuntimeError('SBOM service/destination mismatch')
                    elif path.is_relative_to(Path('images')) and name.endswith('.cdx.json'):
                        raise RuntimeError('Image inventory filename has no reviewed service binding')
                    reject_private_paths(report, root, extra_roots)
            except InventoryBudgetExceeded:
                raise
            except (ValueError, OSError, RuntimeError, AttributeError, TypeError, RecursionError):
                errors.append(f'{root / "sbom" / path}: invalid inventory custody, JSON, structure or identity')

    try:
        # The selected repository root is the trust anchor. All descendants stay
        # relative to verified open descriptors, never a reconstructed pathname.
        with custody_directory(root) as repository:
            with custody_directory('sbom', repository) as directory:
                walk(directory, Path())
    except InventoryBudgetExceeded as error:
        errors.append(f'{root}: {error}')
    except (ValueError, OSError, RuntimeError):
        errors.append(f'{root}: invalid repository/inventory directory custody')
    for path in sorted(required - seen):
        errors.append(f'{root / "sbom" / path}: missing canonical inventory')
    return errors
