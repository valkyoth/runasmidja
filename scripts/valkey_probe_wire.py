"""Bounded persistent RESP2 connection for local cache qualification, not an SDK."""
import socket
import time


class CacheProbe:
    def __init__(self):
        self.deadline = time.monotonic() + 180
        self.stream = socket.create_connection(('127.0.0.1', 16379), timeout=5)
        try:
            self.reader = self.stream.makefile('rb')
        except BaseException:
            self.stream.close()
            raise
        self.commands = 0

    def close(self):
        try:
            self.reader.close()
        finally:
            self.stream.close()

    def receive(self, size):
        result = bytearray()
        while len(result) < size:
            remaining = self.deadline - time.monotonic()
            if remaining <= 0:
                raise RuntimeError('Cache qualification total deadline exceeded')
            self.stream.settimeout(min(5, remaining))
            chunk = self.reader.read1(size - len(result))
            if not chunk:
                raise RuntimeError('Cache qualification reply truncated')
            result.extend(chunk)
        return bytes(result)

    def request(self, *parts):
        self.commands += 1
        remaining = self.deadline - time.monotonic()
        if remaining <= 0 or self.commands > 5000 or not 1 <= len(parts) <= 5:
            raise RuntimeError('Cache qualification work budget exceeded')
        chunks = [part if isinstance(part, bytes) else str(part).encode() for part in parts]
        if any(len(part) > 65536 for part in chunks):
            raise RuntimeError('Cache qualification request exceeds budget')
        wire = b'*' + str(len(chunks)).encode() + b'\r\n' + b''.join(
            b'$' + str(len(part)).encode() + b'\r\n' + part + b'\r\n' for part in chunks)
        self.stream.settimeout(min(5, remaining))
        self.stream.sendall(wire)
        line = bytearray()
        while len(line) <= 4096 and not line.endswith(b'\r\n'):
            line.extend(self.receive(1))
        if len(line) > 4096:
            raise RuntimeError('Cache qualification reply framing rejected')
        line = bytes(line)
        if line == b'$-1\r\n': return None
        if line.startswith(b'$'):
            size = int(line[1:-2])
            if not 0 <= size <= 65536:
                raise RuntimeError('Cache qualification reply exceeds budget')
            value = self.receive(size + 2)
            if len(value) != size + 2 or not value.endswith(b'\r\n'):
                raise RuntimeError('Cache qualification bulk reply truncated')
            return value[:-2]
        if line[:1] not in (b'+', b'-', b':'):
            raise RuntimeError('Cache qualification reply type rejected')
        return line[:-2]
