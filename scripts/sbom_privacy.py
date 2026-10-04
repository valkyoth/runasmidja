"""Public evidence uses image identities, never workstation filesystem paths."""
import json
import math
import os
import stat
import re
from pathlib import Path
from contextlib import contextmanager

PRIVATE_PATH = re.compile(r'/home/|/Users/|(?<![A-Za-z0-9])[A-Za-z]:[\\/]')
PUBLIC_SERVICES = frozenset(('openbao', 'postgres', 'probe', 'probe-base', 'valkey', 'wolfi-base'))


def public_sbom(evidence, service, image, root):
    evidence.setdefault('metadata', {}).setdefault('component', {})['name'] = f'runasmidja/{service}@{image}'
    encoded = json.dumps(evidence, ensure_ascii=False)
    if PRIVATE_PATH.search(encoded) or str(root) in encoded:
        raise RuntimeError('Scanner inventory contains a private filesystem path')
    return evidence


MAX_PUBLIC_SBOM = 16 * 1024 * 1024
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


def load_public_json(name, directory):
    if not isinstance(name, str) or '/' in name or name in ('', '.', '..'):
        raise ValueError('Invalid inventory filename')
    descriptor = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK | os.O_CLOEXEC,
                         dir_fd=directory)
    with os.fdopen(descriptor, 'rb') as source:
        info = os.fstat(source.fileno())
        if (not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or
                info.st_mode & 0o022 or info.st_nlink != 1 or info.st_size > MAX_PUBLIC_SBOM):
            raise RuntimeError('Public inventory has invalid file custody or size')
        content = source.read(MAX_PUBLIC_SBOM + 1)
        if len(content) > MAX_PUBLIC_SBOM:
            raise RuntimeError('Public inventory exceeds size limit')
    # Text input prevents Python's bytes-based UTF-16/32 autodetection. A UTF-8
    # BOM is rejected by the JSON decoder, rather than silently stripped.
    return json.loads(content.decode('utf-8'), object_pairs_hook=unique_object,
                      parse_constant=reject_constant, parse_float=finite_float)


def load_canonical_sbom(name, directory):
    report = load_public_json(name, directory)
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


def check_sboms(root):
    errors, seen = [], set()
    bindings = {Path('images') / f'{service}.cdx.json': f'runasmidja/{service}@'
                for service in PUBLIC_SERVICES}
    required = set(bindings)
    bindings.update({Path('images') / name: prefix for name, prefix in HISTORICAL_IDENTITIES.items()})

    def walk(directory, relative):
        if len(relative.parts) > 32:
            raise RuntimeError('Inventory directory nesting exceeds limit')
        for name in sorted(os.listdir(directory)):
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
                    report = (load_canonical_sbom(name, directory) if name.endswith('.cdx.json')
                              else load_public_json(name, directory))
                    if path in bindings:
                        identity = report.get('metadata', {}).get('component', {}).get('name', '')
                        prefix = bindings[path]
                        if (not isinstance(identity, str) or not identity.startswith(prefix) or
                                not identity[len(prefix):].strip()):
                            raise RuntimeError('SBOM service/destination mismatch')
                    elif path.is_relative_to(Path('images')) and name.endswith('.cdx.json'):
                        raise RuntimeError('Image inventory filename has no reviewed service binding')
                    content = json.dumps(report, ensure_ascii=False)
                    if PRIVATE_PATH.search(content) or str(root) in content:
                        raise RuntimeError('Private filesystem path in public inventory')
            except (ValueError, OSError, RuntimeError, AttributeError, TypeError, RecursionError):
                errors.append(f'{root / "sbom" / path}: invalid inventory custody, JSON, structure or identity')

    try:
        # The selected repository root is the trust anchor. All descendants stay
        # relative to verified open descriptors, never a reconstructed pathname.
        with custody_directory(root) as repository:
            with custody_directory('sbom', repository) as directory:
                walk(directory, Path())
    except (ValueError, OSError, RuntimeError):
        errors.append(f'{root}: invalid repository/inventory directory custody')
    for path in sorted(required - seen):
        errors.append(f'{root / "sbom" / path}: missing canonical inventory')
    return errors
