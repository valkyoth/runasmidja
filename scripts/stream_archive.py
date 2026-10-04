"""Bound binary child output before disk writes; preserve old artifacts on failure."""
import os
import selectors
import stat
import subprocess
import time
from custody import sync_parent, durable_unlink
from process_limits import _kill_reap

MAX_ARCHIVE = 512 * 1024 * 1024


def save_bounded_archive(args, target, *, limit=MAX_ARCHIVE, timeout=180, stderr_limit=1024 * 1024):
    if type(limit) is not int or not 0 < limit <= MAX_ARCHIVE or not 0 < timeout <= 1800:
        raise ValueError('Invalid archive budget')
    if type(stderr_limit) is not int or not 0 <= stderr_limit <= 1024 * 1024:
        raise ValueError('Invalid archive diagnostic budget')
    if target.exists() or target.is_symlink():
        fd = os.open(target, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
        try:
            info = os.fstat(fd)
            if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or info.st_size > limit:
                raise RuntimeError('Archive target custody rejected')
        finally:
            os.close(fd)
    temporary = target.with_name(target.name + '.next')
    descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    child = None
    selector = selectors.DefaultSelector()
    deadline = time.monotonic() + timeout
    size, diagnostic = 0, 0
    try:
        with os.fdopen(descriptor, 'wb') as output:
            child = subprocess.Popen(args, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE, start_new_session=True)
            for pipe, name in ((child.stdout, 'archive'), (child.stderr, 'diagnostic')):
                os.set_blocking(pipe.fileno(), False)
                selector.register(pipe, selectors.EVENT_READ, name)
            while selector.get_map():
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise RuntimeError('Archive producer deadline exceeded')
                for key, _event in selector.select(min(remaining, 0.1)):
                    data = os.read(key.fd, 16384)
                    if not data:
                        selector.unregister(key.fileobj)
                    elif key.data == 'archive':
                        if size + len(data) > limit:
                            raise RuntimeError('Archive byte budget exceeded before write')
                        output.write(data)
                        size += len(data)
                    else:
                        diagnostic += len(data)
                        if diagnostic > stderr_limit:
                            raise RuntimeError('Archive diagnostic budget exceeded')
            try:
                result = child.wait(timeout=max(0.001, deadline - time.monotonic()))
            except subprocess.TimeoutExpired:
                raise RuntimeError('Archive producer deadline exceeded') from None
            if result or not size:
                raise RuntimeError('Archive producer failed; diagnostics withheld')
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary, target)
        sync_parent(target)
    finally:
        if child:
            _kill_reap(child)
            child.stdout.close(); child.stderr.close()
        selector.close()
        if temporary.exists():
            durable_unlink(temporary)

