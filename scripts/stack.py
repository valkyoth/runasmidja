#!/usr/bin/env python3
"""Idempotent rootless Podman development stack; never a production bootstrap."""
import argparse
import fcntl
import json
import os
import secrets
from stack_common import ROOT, STATE, NETWORK, NAMES, bao, podman, private, run, wait_for


def files():
    STATE.mkdir(parents=True, mode=0o700, exist_ok=True)
    os.chmod(STATE, 0o700)
    for sub in ('bao-data', 'bao-audit', 'bao-config'):
        (STATE / sub).mkdir(mode=0o700, exist_ok=True)
    for name in ('postgres.password', 'app-db.password', 'valkey.password'):
        if not (STATE / name).exists():
            private(STATE / name, secrets.token_hex(32))
    if not (STATE / 'bao.crt').exists():
        run('openssl', 'req', '-x509', '-newkey', 'rsa:3072', '-sha256', '-nodes',
            '-keyout', str(STATE / 'bao.key'), '-out', str(STATE / 'bao.crt'), '-days', '30',
            '-subj', '/CN=localhost', '-addext', 'subjectAltName=DNS:localhost,DNS:openbao,IP:127.0.0.1')
        os.chmod(STATE / 'bao.key', 0o600)
    config = '''ui = false
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
    if not (STATE / 'bao.hcl').exists():
        private(STATE / 'bao.hcl', config)
    elif (STATE / 'bao.hcl').read_text() != config:
        (STATE / 'bao.hcl').write_text(config)
    import shutil
    for name in ('bao.hcl', 'bao.key', 'bao.crt'):
        shutil.copyfile(STATE / name, STATE / 'bao-config' / name)
        os.chmod(STATE / 'bao-config' / name, 0o600)
    if not (STATE / 'valkey.conf').exists():
        password = (STATE / 'valkey.password').read_text()
        private(STATE / 'valkey.conf', f'''bind 0.0.0.0
protected-mode yes
port 6379
save ""
appendonly no
maxmemory 64mb
maxmemory-policy allkeys-lru
user default off
user runasmidja on >{password} ~runasmidja:* +get +set +del +ping
''')


def start_container(service, image, args):
    name = NAMES[service]
    if podman('container', 'exists', name, allowed=(0, 1)).returncode == 0:
        info = json.loads(podman('inspect', name).stdout)[0]
        if info.get('Config', {}).get('Labels', {}).get('io.runasmidja.scope') != 'development':
            raise RuntimeError('refusing to reuse unowned container')
        if not info['State']['Running']:
            podman('start', name)
        return
    podman('run', '-d', '--name', name, '--label', 'io.runasmidja.scope=development',
        '--network', NETWORK, '--memory', '512m', '--cpus', '1', '--pids-limit', '128',
        '--security-opt', 'no-new-privileges', *args, image, *({'openbao': ['server', '-config=/config/bao.hcl'],
        'valkey': ['valkey-server', '/config/valkey.conf']}.get(service, [])))


def bootstrap():
    wait_for(lambda: bao('sys/init'))
    initialized = bao('sys/init')['initialized']
    if not initialized:
        init = bao('sys/init', {'secret_shares': 1, 'secret_threshold': 1})
        # Local test only: one share in private state. Production needs independent custody.
        private(STATE / 'bao-init.json', json.dumps(init))
    if not (STATE / 'bao-init.json').exists():
        raise RuntimeError('OpenBao initialized without local recovery material; refusing reset')
    init = json.loads((STATE / 'bao-init.json').read_text())
    status = bao('sys/seal-status')
    if status['sealed']:
        bao('sys/unseal', {'key': init['keys_base64'][0]})
    wait_for(lambda: not bao('sys/seal-status')['sealed'])
    if (STATE / 'app-role.json').exists():
        if init.get('root_token'):
            try:
                bao('auth/token/revoke-self', {}, init['root_token'])
            except RuntimeError as error:
                if '(403)' not in str(error):
                    raise
            init.pop('root_token')
            temporary = STATE / 'bao-init.next'
            private(temporary, json.dumps(init))
            os.replace(temporary, STATE / 'bao-init.json')
        return
    root = init['root_token']
    # Reconcile configuration after a partially completed bootstrap.
    audits = bao('sys/audit', token=root)['data']
    if 'file/' not in audits:
        raise RuntimeError('Declarative audit missing; restart OpenBao before bootstrap')
    mounts = bao('sys/mounts', token=root)['data']
    if 'runasmidja/' not in mounts:
        bao('sys/mounts/runasmidja', {'type': 'kv', 'options': {'version': '2'}}, root)
    auths = bao('sys/auth', token=root)['data']
    if 'approle/' not in auths:
        bao('sys/auth/approle', {'type': 'approle'}, root)
    bao('sys/policies/acl/runasmidja-app', {'policy': 'path "runasmidja/data/runtime" { capabilities = ["read"] }'}, root, 'PUT')
    bao('auth/approle/role/runasmidja', {'token_policies': ['runasmidja-app'], 'token_ttl': '15m',
        'token_max_ttl': '1h', 'secret_id_ttl': '24h', 'secret_id_num_uses': 0}, root)
    bao('runasmidja/data/runtime', {'data': {'database_password': (STATE / 'app-db.password').read_text(),
        'valkey_password': (STATE / 'valkey.password').read_text()}}, root)
    role = bao('auth/approle/role/runasmidja/role-id', token=root)['data']['role_id']
    secret = bao('auth/approle/role/runasmidja/secret-id', {}, root)['data']['secret_id']
    private(STATE / 'app-role.json', json.dumps({'role_id': role, 'secret_id': secret}))
    bao('auth/token/revoke-self', {}, root)
    init.pop('root_token', None)
    temporary = STATE / 'bao-init.next'
    private(temporary, json.dumps(init))
    os.replace(temporary, STATE / 'bao-init.json')


def up():
    files()
    images = json.loads((ROOT / 'deploy/podman/images.json').read_text())
    if podman('network', 'exists', NETWORK, allowed=(0, 1)).returncode:
        podman('network', 'create', '--internal', '--label', 'io.runasmidja.scope=development', NETWORK)
    for service, image in images.items():
        if podman('image', 'exists', image, allowed=(0, 1)).returncode:
            podman('pull', image)
    start_container('postgres', images['postgres'], ['-p', '127.0.0.1:15432:5432',
        '-e', 'POSTGRES_PASSWORD_FILE=/run/secrets/postgres.password', '-e', 'POSTGRES_DB=runasmidja',
        '-e', 'POSTGRES_INITDB_ARGS=--auth-host=scram-sha-256',
        '-v', f'{STATE}/postgres.password:/run/secrets/postgres.password:ro,Z',
        '-v', 'runasmidja-test-postgres:/var/lib/postgresql'])
    identity = f'{os.getuid()}:{os.getgid()}'
    start_container('openbao', images['openbao'], ['-p', '127.0.0.1:18200:8200',
        '--userns', 'keep-id', '--user', identity, '--cap-drop', 'ALL',
        '-v', f'{STATE}/bao-config:/config:ro,Z', '-v', f'{STATE}/bao-data:/data:Z', '-v', f'{STATE}/bao-audit:/audit:Z'])
    start_container('valkey', images['valkey'], ['-p', '127.0.0.1:16379:6379',
        '--userns', 'keep-id', '--user', identity, '--cap-drop', 'ALL', '--read-only',
        '-v', f'{STATE}/valkey.conf:/config/valkey.conf:ro,Z'])
    wait_for(lambda: podman('exec', NAMES['postgres'], 'pg_isready', '-U', 'postgres', allowed=(0, 1, 2)).returncode == 0)
    # Reject image/initdb localhost trust defaults as well as external trust.
    podman('exec', '--user', 'postgres', NAMES['postgres'], 'sh', '-c',
        "sed -i '/^[[:space:]]*host/s/[[:space:]]trust[[:space:]]*$/ scram-sha-256/' \"$PGDATA/pg_hba.conf\"")
    podman('exec', NAMES['postgres'], 'psql', '-U', 'postgres', '-Atc', 'SELECT pg_reload_conf()')
    # Only schema owner bootstrap uses the administrative identity.
    password = (STATE / 'app-db.password').read_text()
    sql = f"""SELECT 'CREATE ROLE runasmidja LOGIN' WHERE NOT EXISTS (SELECT FROM pg_roles WHERE rolname='runasmidja')\\gexec
ALTER ROLE runasmidja PASSWORD '{password}';
GRANT CONNECT ON DATABASE runasmidja TO runasmidja;
"""
    podman('exec', '-i', NAMES['postgres'], 'psql', '-U', 'postgres', '-d', 'runasmidja', '-v', 'ON_ERROR_STOP=1', data=sql)
    bootstrap()
    print('Development stack ready; OpenBao root revoked; application credentials remain private.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('up', 'stop', 'status', 'smoke'))
    action = parser.parse_args().action
    if action == 'up':
        STATE.mkdir(parents=True, mode=0o700, exist_ok=True)
        with (STATE / 'bootstrap.lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            up()
    elif action == 'stop':
        for name in NAMES.values():
            if podman('container', 'exists', name, allowed=(0, 1)).returncode == 0:
                podman('stop', name)
        print('Owned test containers stopped; data retained.')
    elif action == 'smoke':
        from stack_smoke import smoke
        smoke()
    else:
        for service, name in NAMES.items():
            result = podman('inspect', '--format', '{{.State.Status}}', name, allowed=(0, 125))
            print(service + ': ' + (result.stdout.strip() or 'absent'))

if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, KeyError, OSError) as error:
        raise SystemExit(f'Stack failed: {error}') from None
