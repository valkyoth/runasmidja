"""Bounded audit snapshots; the live sink is a 16 MiB container tmpfs."""
from stack_common import STATE, NAMES, podman
from custody import MAX_AUDIT, read_owned_regular_bounded, replace_private


def snapshot_audit(info):
    target = STATE / 'bao-audit/audit.log'
    if '/audit' in info.get('HostConfig', {}).get('Tmpfs', {}):
        current = podman('exec', NAMES['openbao'], 'sh', '-c',
            '[ -f /audit/audit.log ] && [ ! -L /audit/audit.log ] && exec cat /audit/audit.log',
            output_limit=MAX_AUDIT, timeout=30).stdout
        if target.exists() or target.is_symlink():
            previous = read_owned_regular_bounded(target, MAX_AUDIT)
            replace_private(target.with_name('audit.previous'), previous, limit=MAX_AUDIT)
        replace_private(target, current, limit=MAX_AUDIT)
    elif target.exists() or target.is_symlink():
        current = read_owned_regular_bounded(target, MAX_AUDIT)
        replace_private(target.with_name('audit.previous'), current, limit=MAX_AUDIT)


def audit_text():
    text = ''
    for name in ('audit.previous', 'audit.log'):
        path = STATE / 'bao-audit' / name
        if path.exists() or path.is_symlink():
            text += read_owned_regular_bounded(path, MAX_AUDIT)
    return text
