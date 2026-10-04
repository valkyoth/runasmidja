"""Private fixture custody; only vault startup TLS is generated outside OpenBao."""
import json
import os
import stat
import uuid
import fcntl
from contextlib import contextmanager
from stack_common import STATE, private, read_private, replace_private, run
from custody import sync_parent

CONFIG = '''ui = false
disable_mlock = true
api_addr = "https://openbao:8200"
cluster_addr = "https://openbao:8201"
storage "pebbledb" { path = "/data" }
audit "file" "file" {
  options { file_path = "/audit/audit.log" }
}
listener "tcp" {
  address = "0.0.0.0:8200"
  tls_cert_file = "/config/bao.crt"
  tls_key_file = "/config/bao.key"
}
'''


def directory(path):
    pending = []
    current = path
    while not current.exists():
        pending.append(current)
        current = current.parent
    for created in reversed(pending):
        created.mkdir(mode=0o700)
        sync_parent(created)
    info = path.lstat()
    if not stat.S_ISDIR(info.st_mode) or info.st_uid != os.getuid() or info.st_mode & 0o077:
        raise RuntimeError('Private fixture directory has invalid custody')


@contextmanager
def fixture_lock():
    from stack_common import require_rootless, INSTANCE
    from valkey_image import selected_image
    require_rootless()
    selected_image(INSTANCE)
    directory(STATE)
    path = STATE / 'bootstrap.lock'
    descriptor = os.open(path, os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW, 0o600)
    with os.fdopen(descriptor, 'a') as lock:
        info = os.fstat(lock.fileno())
        if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or info.st_mode & 0o077:
            raise RuntimeError('Invalid fixture lock custody')
        fcntl.flock(lock, fcntl.LOCK_EX)
        yield


def files():
    directory(STATE)
    for sub in ('bao-data', 'bao-audit', 'bao-config'):
        directory(STATE / sub)
    if not (STATE / 'owner.json').exists():
        private(STATE / 'owner.json', json.dumps({'instance': str(uuid.uuid4()), 'schema': 2}))
    if not (STATE / 'bao.crt').exists():
        if (STATE / 'bao.key').exists():
            raise RuntimeError('Incomplete vault TLS custody; refusing key replacement')
        run('openssl', 'req', '-x509', '-newkey', 'rsa:3072', '-sha256', '-nodes',
            '-keyout', str(STATE / 'bao.key'), '-out', str(STATE / 'bao.crt'), '-days', '30',
            '-subj', '/CN=localhost', '-addext', 'subjectAltName=DNS:localhost,DNS:openbao,IP:127.0.0.1')
        os.chmod(STATE / 'bao.key', 0o600)
        os.chmod(STATE / 'bao.crt', 0o600)
        for name in ('bao.key', 'bao.crt'):
            descriptor = os.open(STATE / name, os.O_RDONLY | os.O_NOFOLLOW)
            try:
                os.fsync(descriptor)
            finally:
                os.close(descriptor)
            sync_parent(STATE / name)
    for name in ('bao.crt', 'bao.key'):
        value = read_private(STATE / name)
        target = STATE / 'bao-config' / name
        if not target.exists():
            private(target, value)
        elif read_private(target) != value:
            raise RuntimeError('Vault TLS mount drift; refusing silent replacement')
    config = STATE / 'bao-config/bao.hcl'
    if not config.exists():
        private(config, CONFIG)
    elif read_private(config) != CONFIG:
        raise RuntimeError('Vault configuration drift')


def delivery(values):
    # Persistent private copies remain an explicitly bounded v0.8 delivery gap.
    mapping = {'postgres.password': 'postgres_admin_password',
               'app-db.password': 'database_password', 'valkey.password': 'valkey_password'}
    for filename, key in mapping.items():
        path = STATE / filename
        if not path.exists():
            private(path, values[key])
        elif read_private(path) != values[key]:
            raise RuntimeError('Credential delivery drift; refusing service rekey')
    config = '''bind 0.0.0.0
protected-mode yes
port 6379
save ""
appendonly no
maxmemory 64mb
maxmemory-policy allkeys-lru
user default off
user runasmidja on >''' + values['valkey_password'] + ' ~runasmidja:* +get +set +del +ping\n'
    path = STATE / 'valkey.conf'
    if not path.exists():
        private(path, config)
    elif read_private(path) != config:
        raise RuntimeError('Valkey delivery drift')
