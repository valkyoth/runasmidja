"""One persistent filesystem lock for the global OpenBao artifact cache."""
import fcntl
import os
import stat
from contextlib import contextmanager


def custody(info, directory=False):
    valid_type = stat.S_ISDIR(info.st_mode) if directory else stat.S_ISREG(info.st_mode)
    if (not valid_type or info.st_uid != os.getuid() or info.st_mode & 0o077 or
            (not directory and info.st_nlink != 1)):
        raise RuntimeError('OpenBao artifact lock/state has invalid custody')


@contextmanager
def artifact_lock(state, exclusive):
    # Never unlink the lock: waiters must all synchronize on the same inode.
    state.mkdir(mode=0o700, parents=True, exist_ok=True)
    directory = os.open(state, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC)
    try:
        custody(os.fstat(directory), directory=True)
        descriptor = os.open('artifact.lock', os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW |
                             os.O_CLOEXEC | os.O_NONBLOCK, 0o600, dir_fd=directory)
        with os.fdopen(descriptor, 'r+') as handle:
            custody(os.fstat(handle.fileno()))
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX if exclusive else fcntl.LOCK_SH)
            try:
                yield
            finally:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
    finally:
        os.close(directory)
