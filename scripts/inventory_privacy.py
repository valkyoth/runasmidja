"""Known host-path detection, not a proof that arbitrary text is nonsensitive."""
import os
import re
import tempfile
from pathlib import Path

SHARE_URI = re.compile(
    r'(?i)(?<![A-Za-z0-9+.-])(?:file://[^/]|'
    r'(?:smb|cifs|nfs|afp|sshfs)://[^/\s]+(?:/|$))'
)
FILE_URI = re.compile(r'(?i)(?<![A-Za-z0-9+.-])file://')


def json_strings(document):
    pending = [iter((document,))]
    while pending:
        try:
            value = next(pending[-1])
        except StopIteration:
            pending.pop()
            continue
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            pending.append(iter(value.keys())); pending.append(iter(value.values()))
        elif isinstance(value, list):
            pending.append(iter(value))


def private_roots(repository_root, extra_roots=()):
    paths = [repository_root, Path.home(), tempfile.gettempdir(), *extra_roots]
    paths.extend(os.environ[key] for key in ('GITHUB_WORKSPACE', 'RUNNER_TEMP',
        'RUNNER_TOOL_CACHE', 'CARGO_HOME', 'XDG_CACHE_HOME') if os.environ.get(key))
    roots = {'/home', '/Users', '/root', '/tmp', '/var/tmp', '/private/tmp', '/private/var/tmp'}
    for path in paths:
        # Cover both configured spelling and resolved aliases of known roots.
        for candidate in (Path(path).absolute(), Path(path).resolve()):
            value = str(candidate).replace('\\', '/').rstrip('/')
            if value: roots.add(value)
    return roots


def reject_private_paths(document, repository_root, extra_roots=()):
    patterns = [re.compile(r'(?<![A-Za-z0-9_.-])' + re.escape(root) + r'(?=/|$|[\s\"\'])')
                for root in private_roots(repository_root, extra_roots)]
    for value in json_strings(document):
        normalized = value.replace('\\', '/')
        if (re.search(r'(?<![:/])//[^/\s]+/', normalized) or
                SHARE_URI.search(normalized) or
                re.search(r'(?<![A-Za-z0-9])[A-Za-z]:/', normalized)):
            raise RuntimeError('Private network/drive path in public inventory')
        candidates = (normalized, FILE_URI.sub('', normalized))
        if any(pattern.search(candidate) for candidate in candidates for pattern in patterns):
            raise RuntimeError('Known private filesystem path in public inventory')
