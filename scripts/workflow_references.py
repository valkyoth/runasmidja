"""Static reference grammar and explicit local admission for workflow checks."""
import re
from pathlib import Path

SEGMENT = r'[A-Za-z0-9_-][A-Za-z0-9_.-]*'
OWNER = r'[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*'
REMOTE = re.compile(rf'({OWNER})/({SEGMENT})((?:/[A-Za-z0-9_.-]+)*)@([0-9a-f]{{40}})')
COMPONENT = r'[a-z0-9]+(?:(?:[._]|__|-+)[a-z0-9]+)*'
REGISTRY = r'[a-z0-9]+(?:[.-][a-z0-9]+)*(?::[0-9]{1,5})?'
IMAGE = re.compile(rf'(?:{REGISTRY}/)?{COMPONENT}(?:/{COMPONENT})*@sha256:[0-9a-f]{{64}}')


def container(value):
    if not isinstance(value, str) or not IMAGE.fullmatch(value):
        raise ValueError('container image must have a literal SHA256 digest')
    if any(part in ('', '.', '..') for part in value.split('@')[0].split('/')):
        raise ValueError('malformed container repository')


def reference(value, kind):
    """Return normalized value and class; unsupported/dynamic syntax rejects."""
    if not isinstance(value, str):
        raise ValueError('uses must be a scalar string')
    value = value.rstrip('\n')  # Block scalars may end with YAML's newline.
    if not value or '${{' in value or any(char.isspace() for char in value):
        raise ValueError('uses must be a static reference without whitespace')
    if value.startswith('./'):
        return value, 'local'
    if value.startswith('docker://') and kind == 'action':
        container(value[len('docker://'):])
        return value, 'container'
    match = REMOTE.fullmatch(value)
    if not match:
        raise ValueError('remote reference requires owner/repository[/path]@full-commit')
    owner, repo, path, _commit = match.groups()
    if any(part in ('.', '..') for part in path.split('/')):
        raise ValueError('noncanonical remote path')
    if (owner.lower(), repo.lower()) == ('github', 'codeql-action'):
        raise ValueError('CodeQL must use GitHub Default setup')
    if kind == 'workflow' and not re.fullmatch(r'/\.github/workflows/[^/]+\.ya?ml', path):
        raise ValueError('reusable workflow must name .github/workflows/file.yml or .yaml')
    return value, 'remote'


def local_path(root, value, kind):
    """Allow only canonical relative, regular, nonsymlinked repository paths."""
    name = value[2:] if value.startswith('./') else ''
    parts = name.split('/')
    if not name or any(not re.fullmatch(SEGMENT, part) for part in parts):
        # .github is the sole permitted leading-dot path segment.
        if not (parts[0] == '.github' and len(parts) > 1 and
                all(re.fullmatch(SEGMENT, part) for part in parts[1:])):
            raise ValueError('local reference has noncanonical path segments')
    if kind == 'workflow':
        if len(parts) != 3 or parts[:2] != ['.github', 'workflows'] or not re.fullmatch(r'.+\.ya?ml', parts[2]):
            raise ValueError('local reusable workflow must be directly in .github/workflows')
    elif len(parts) < 3 or parts[:2] != ['.github', 'actions']:
        raise ValueError('local actions must be under .github/actions')
    path = Path(root)
    for part in parts:
        path = path / part
        if path.is_symlink():
            raise ValueError('local reference crosses a symlink')
    if kind == 'workflow':
        if not path.is_file():
            raise ValueError('local workflow missing')
        return path
    if any((path / suffix).is_symlink() for suffix in ('action.yml', 'action.yaml')):
        raise ValueError('local action manifest cannot be a symlink')
    manifests = [path / suffix for suffix in ('action.yml', 'action.yaml') if (path / suffix).exists()]
    if len(manifests) != 1 or manifests[0].is_symlink() or not manifests[0].is_file():
        raise ValueError('local action needs exactly one regular action.yml or action.yaml')
    return manifests[0]
