"""Private test-stack helpers. Child failures never echo secret input/output."""
import json
import os
import socket
import ssl
import subprocess
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INSTANCE = os.environ.get('RUNASMIDJA_STACK_ID', 'v02')
if not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,31}', INSTANCE):
    raise RuntimeError('Invalid test stack identifier')
STATE = ROOT / '.local/stacks' / INSTANCE
NETWORK = f'runasmidja-{INSTANCE}'
NAMES = {service: NETWORK + '-' + service for service in ('postgres', 'openbao', 'valkey')}

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def run(*args, data=None, allowed=(0,)):
    result = subprocess.run(args, input=data, text=True, capture_output=True, timeout=180)
    if result.returncode not in allowed:
        raise RuntimeError(f'{args[0]} failed (exit {result.returncode}); output withheld')
    return result

def podman(*args, **kwargs):
    return run('podman', *args, **kwargs)

def private(path, content):
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    with os.fdopen(descriptor, 'w') as handle:
        handle.write(content)
        handle.flush()
        os.fsync(handle.fileno())

def read_private(path):
    import stat
    descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(descriptor, 'rb') as handle:
        info = os.fstat(handle.fileno())
        if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or info.st_mode & 0o077:
            raise RuntimeError('Private fixture file has invalid custody')
        value = handle.read(65537)
        if len(value) > 65536:
            raise RuntimeError('Private fixture file exceeds budget')
        return value.decode('utf-8')

def replace_private(path, content):
    if path.exists() or path.is_symlink():
        read_private(path)
    temporary = path.with_name(path.name + '.next')
    if temporary.exists():
        read_private(temporary)
        temporary.unlink()
    private(temporary, content)
    os.replace(temporary, path)

def wait_for(check):
    deadline = time.monotonic() + 90
    while time.monotonic() < deadline:
        try:
            value = check()
            if value:
                return value
        except (RuntimeError, OSError, urllib.error.URLError):
            pass
        time.sleep(0.3)
    raise RuntimeError('service readiness timed out')

class BaoError(RuntimeError):
    """HTTP status without a secret-bearing response body."""
    def __init__(self, status):
        self.status = status
        super().__init__(f'OpenBao request rejected ({status}); response withheld')

def bao(path, payload=None, token=None, method=None):
    context = ssl.create_default_context(cafile=STATE / 'bao.crt')
    headers = {'Content-Type': 'application/json'}
    if token:
        headers['X-Vault-Token'] = token
    request = urllib.request.Request('https://localhost:18200/v1/' + path,
        data=None if payload is None else json.dumps(payload).encode(),
        headers=headers, method=method)
    # Test endpoints bypass environment proxies to keep credentials on loopback.
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), urllib.request.HTTPSHandler(context=context), NoRedirect())
    try:
        with opener.open(request, timeout=10) as response:
            raw = response.read(1024 * 1024 + 1)
            if len(raw) > 1024 * 1024:
                raise RuntimeError('OpenBao response exceeds test budget')
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as error:
        raise BaoError(error.code) from None

def valkey(*command, authenticated=True):
    with socket.create_connection(('127.0.0.1', 16379), timeout=5) as stream:
        reader = stream.makefile('rb')
        def send(parts):
            wire = b'*' + str(len(parts)).encode() + b'\r\n'
            for value in parts:
                data = str(value).encode()
                wire += b'$' + str(len(data)).encode() + b'\r\n' + data + b'\r\n'
            stream.sendall(wire)
            line = reader.readline(4096)
            if line.startswith(b'$'):
                length = int(line[1:])
                if length < 0:
                    return None
                if length > 65536:
                    raise RuntimeError('Valkey response exceeds test budget')
                return reader.read(length + 2)[:-2]
            return line.rstrip(b'\r\n')
        if authenticated:
            from stack_vault import runtime_values
            if send(('AUTH', 'runasmidja', runtime_values()['valkey_password'])) != b'+OK':
                raise RuntimeError('Valkey authentication failed')
        return send(command)
