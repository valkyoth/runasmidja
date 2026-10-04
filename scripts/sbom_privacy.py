"""Public evidence uses image identities, never workstation filesystem paths."""
import json
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


def check_sboms(root):
    errors = []
    for service in sorted(PUBLIC_SERVICES):
        path = root / 'sbom' / 'images' / f'{service}.cdx.json'
        try:
            report = json.loads(path.read_text())
            name = report.get('metadata', {}).get('component', {}).get('name', '')
            prefix = f'runasmidja/{service}@'
            if not isinstance(name, str) or not name.startswith(prefix) or not name[len(prefix):].strip():
                errors.append(f'{path}: SBOM service/destination mismatch')
        except (ValueError, OSError, AttributeError, TypeError):
            errors.append(f'{path}: missing or invalid canonical inventory')
    for path in (root / 'sbom').rglob('*.json'):
        try:
            content = json.dumps(json.loads(path.read_text()), ensure_ascii=False)
            if PRIVATE_PATH.search(content) or str(root) in content:
                errors.append(f'{path}: private filesystem path in public inventory')
        except (ValueError, OSError):
            errors.append(f'{path}: invalid inventory JSON')
    return errors
