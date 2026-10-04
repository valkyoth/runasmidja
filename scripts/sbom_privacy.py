"""Public evidence uses image identities, never workstation filesystem paths."""
import json
import re
from pathlib import Path

PRIVATE_PATH = re.compile(r'/home/|/Users/|(?<![A-Za-z0-9])[A-Za-z]:[\\/]')


def public_sbom(evidence, service, image, root):
    evidence.setdefault('metadata', {}).setdefault('component', {})['name'] = f'runasmidja/{service}@{image}'
    encoded = json.dumps(evidence, ensure_ascii=False)
    if PRIVATE_PATH.search(encoded) or str(root) in encoded:
        raise RuntimeError('Scanner inventory contains a private filesystem path')
    return evidence


def check_sboms(root):
    errors = []
    for path in (root / 'sbom').rglob('*.json'):
        try:
            content = json.dumps(json.loads(path.read_text()), ensure_ascii=False)
            if PRIVATE_PATH.search(content) or str(root) in content:
                errors.append(f'{path}: private filesystem path in public inventory')
        except (ValueError, OSError):
            errors.append(f'{path}: invalid inventory JSON')
    return errors
