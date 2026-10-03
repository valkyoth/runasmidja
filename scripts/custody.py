"""Bounded no-follow reads and durable private custody mutations."""
import os
import stat

MAX_PRIVATE = 64 * 1024
MAX_AUDIT = 16 * 1024 * 1024


def sync_parent(path):
    descriptor = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def private(path, content, limit=MAX_PRIVATE):
    if type(limit) is not int or not 0 <= limit <= MAX_AUDIT:
        raise ValueError('Invalid custody budget')
    if len(content.encode('utf-8')) > limit:
        raise RuntimeError('Private creation exceeds budget')
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    with os.fdopen(descriptor, 'w') as handle:
        handle.write(content)
        handle.flush()
        os.fsync(handle.fileno())
    sync_parent(path)


def read_owned_regular_bounded(path, limit=MAX_PRIVATE, durable=False):
    if type(limit) is not int or not 0 <= limit <= MAX_AUDIT:
        raise ValueError('Invalid evidence budget')
    descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(descriptor, 'rb') as handle:
        info = os.fstat(handle.fileno())
        if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or info.st_mode & 0o077:
            raise RuntimeError('Private evidence has invalid custody')
        if info.st_size > limit:
            raise RuntimeError('Private evidence exceeds budget')
        value = handle.read(limit + 1)
        if len(value) > limit:
            raise RuntimeError('Private evidence exceeds budget')
        text = value.decode('utf-8')
        if durable:
            os.fsync(handle.fileno())
        return text


def read_private(path):
    # A retry after failed fsync must not treat visible-but-unsynced custody as durable.
    value = read_owned_regular_bounded(path, durable=True)
    sync_parent(path)
    return value


def durable_unlink(path):
    path.unlink()
    sync_parent(path)


def replace_private(path, content, limit=MAX_PRIVATE):
    if type(limit) is not int or not 0 <= limit <= MAX_AUDIT:
        raise ValueError('Invalid custody budget')
    if len(content.encode('utf-8')) > limit:
        raise RuntimeError('Private replacement exceeds budget')
    if path.exists() or path.is_symlink():
        read_owned_regular_bounded(path, limit)
    temporary = path.with_name(path.name + '.next')
    if temporary.exists() or temporary.is_symlink():
        read_owned_regular_bounded(temporary, limit)
        durable_unlink(temporary)
    private(temporary, content, limit=limit)
    os.replace(temporary, path)
    sync_parent(path)
