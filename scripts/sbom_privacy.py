"""Public evidence uses image identities, never workstation filesystem paths."""
import json
import os
import stat
import re
from pathlib import Path

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


def load_public_json(path):
    descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK | os.O_CLOEXEC)
    with os.fdopen(descriptor, 'rb') as source:
        info = os.fstat(source.fileno())
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1 or info.st_size > MAX_PUBLIC_SBOM:
            raise RuntimeError('Public inventory has invalid file custody or size')
        content = source.read(MAX_PUBLIC_SBOM + 1)
        if len(content) > MAX_PUBLIC_SBOM:
            raise RuntimeError('Public inventory exceeds size limit')
    return json.loads(content)


def load_canonical_sbom(path):
    report = load_public_json(path)
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
    errors = []
    images = root / 'sbom' / 'images'
    bindings = {images / f'{service}.cdx.json': f'runasmidja/{service}@'
                for service in PUBLIC_SERVICES}
    bindings.update({images / name: prefix for name, prefix in HISTORICAL_IDENTITIES.items()
                     if (images / name).exists() or (images / name).is_symlink()})
    paths = set((root / 'sbom').rglob('*.json')) | set(bindings)
    for path in sorted(paths):
        try:
            # Read each inventory once: no unbounded/privacy reread of rejected files.
            report = load_canonical_sbom(path) if path.name.endswith('.cdx.json') else load_public_json(path)
            if path in bindings:
                name = report.get('metadata', {}).get('component', {}).get('name', '')
                prefix = bindings[path]
                if not isinstance(name, str) or not name.startswith(prefix) or not name[len(prefix):].strip():
                    raise RuntimeError('SBOM service/destination mismatch')
            elif path.parent == images and path.name.endswith('.cdx.json'):
                raise RuntimeError('Image inventory filename has no reviewed service binding')
            content = json.dumps(report, ensure_ascii=False)
            if PRIVATE_PATH.search(content) or str(root) in content:
                errors.append(f'{path}: private filesystem path in public inventory')
        except (ValueError, OSError, RuntimeError, AttributeError, TypeError, RecursionError):
            errors.append(f'{path}: missing or invalid inventory custody, structure or service identity')
    return errors
