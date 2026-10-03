"""Concurrent bounded child I/O; secret input/output never appears in failures."""
import os
import selectors
import signal
import subprocess
import time

MAX_INPUT = 64 * 1024
MAX_OUTPUT = 1024 * 1024


def _kill_reap(child):
    try:
        os.killpg(child.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    child.wait(timeout=5)


def run_bounded(*args, data=None, allowed=(0,), input_limit=MAX_INPUT,
                output_limit=MAX_OUTPUT, timeout=180, env=None):
    if not args or type(input_limit) is not int or type(output_limit) is not int:
        raise ValueError('Invalid child limits')
    if input_limit < 0 or output_limit < 0 or not 0 < timeout <= 1800:
        raise ValueError('Invalid child limits')
    payload = b'' if data is None else data.encode('utf-8') if isinstance(data, str) else data
    if not isinstance(payload, bytes) or len(payload) > input_limit:
        raise RuntimeError('Child input exceeds budget; content withheld')
    deadline = time.monotonic() + timeout
    child = subprocess.Popen(args, stdin=subprocess.PIPE if payload else subprocess.DEVNULL,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True, env=env)
    selector = selectors.DefaultSelector()
    buffers = {'stdout': bytearray(), 'stderr': bytearray()}
    size, offset = 0, 0
    pipes = [child.stdout, child.stderr]
    if payload:
        pipes.append(child.stdin)
    try:
        for name, pipe in (('stdout', child.stdout), ('stderr', child.stderr)):
            os.set_blocking(pipe.fileno(), False)
            selector.register(pipe, selectors.EVENT_READ, name)
        if payload:
            os.set_blocking(child.stdin.fileno(), False)
            selector.register(child.stdin, selectors.EVENT_WRITE, 'stdin')
        while selector.get_map():
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise RuntimeError('Child total deadline exceeded; output withheld')
            for key, _event in selector.select(min(remaining, 0.1)):
                pipe, name = key.fileobj, key.data
                if name == 'stdin':
                    try:
                        offset += os.write(pipe.fileno(), payload[offset:offset + 16384])
                    except BrokenPipeError:
                        selector.unregister(pipe)
                        pipe.close()
                        continue
                    if offset == len(payload):
                        selector.unregister(pipe)
                        pipe.close()
                else:
                    chunk = os.read(pipe.fileno(), min(16384, output_limit - size + 1))
                    if not chunk:
                        selector.unregister(pipe)
                        continue
                    size += len(chunk)
                    if size > output_limit:
                        raise RuntimeError('Child aggregate output exceeds budget; content withheld')
                    buffers[name].extend(chunk)
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise RuntimeError('Child total deadline exceeded; output withheld')
        try:
            returncode = child.wait(timeout=remaining)
        except subprocess.TimeoutExpired:
            raise RuntimeError('Child total deadline exceeded; output withheld') from None
        if returncode not in allowed:
            raise RuntimeError(f'Child failed (exit {returncode}); output withheld')
        if payload and offset != len(payload):
            raise RuntimeError('Child input delivery incomplete; content withheld')
        return subprocess.CompletedProcess(args, returncode,
            buffers['stdout'].decode('utf-8', errors='replace'),
            buffers['stderr'].decode('utf-8', errors='replace'))
    finally:
        _kill_reap(child)
        selector.close()
        for pipe in pipes:
            if pipe is not None and not pipe.closed:
                pipe.close()
