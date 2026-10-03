"""Real service tests, including unauthorized paths and cache key isolation."""
import json
from stack_common import STATE, NAMES, bao, podman, valkey


def smoke():
    if STATE.stat().st_mode & 0o077:
        raise RuntimeError('Private stack directory permissions are too broad')
    init = json.loads((STATE / 'bao-init.json').read_text())
    if 'root_token' in init:
        raise RuntimeError('Bootstrap root token retained after provisioning')
    for name in ('bao-init.json', 'app-role.json', 'postgres.password', 'app-db.password', 'valkey.password', 'bao.key'):
        if (STATE / name).stat().st_mode & 0o077:
            raise RuntimeError('Private material permissions are too broad')
    version = podman('exec', NAMES['postgres'], 'psql', '-U', 'postgres', '-Atc', 'SHOW server_version').stdout.strip()
    if not version.startswith('19beta4'):
        raise RuntimeError('PostgreSQL must be 19 beta 4 for this baseline')
    podman('exec', '-i', NAMES['postgres'], 'psql', '-U', 'postgres', '-d', 'runasmidja', '-v', 'ON_ERROR_STOP=1',
        data='BEGIN; CREATE TEMP TABLE runasmidja_smoke (id bigint PRIMARY KEY); INSERT INTO runasmidja_smoke VALUES (1); ROLLBACK;')
    flags = podman('exec', NAMES['postgres'], 'psql', '-U', 'postgres', '-Atc',
        "SELECT rolsuper OR rolcreatedb OR rolcreaterole FROM pg_roles WHERE rolname='runasmidja'").stdout.strip()
    if flags != 'f':
        raise RuntimeError('Runtime database role has excessive privileges')
    password = (STATE / 'app-db.password').read_text()
    login = podman('exec', '-i', NAMES['postgres'], 'sh', '-c',
        'IFS= read -r PGPASSWORD; export PGPASSWORD; exec psql -h 127.0.0.1 -U runasmidja -d runasmidja -Atc "SELECT current_user"',
        data=password + '\n').stdout.strip()
    if login != 'runasmidja':
        raise RuntimeError('Runtime database credential login failed')
    denied = podman('exec', '-i', NAMES['postgres'], 'sh', '-c',
        'IFS= read -r PGPASSWORD; export PGPASSWORD; exec psql -h 127.0.0.1 -U runasmidja -d runasmidja -v ON_ERROR_STOP=1 -Atc "SELECT rolpassword FROM pg_authid"',
        data=password + '\n', allowed=(0, 1))
    if denied.returncode == 0:
        raise RuntimeError('Runtime database role can read privileged credentials')
    bad_login = podman('exec', '-i', NAMES['postgres'], 'sh', '-c',
        'IFS= read -r PGPASSWORD; export PGPASSWORD; exec psql -h 127.0.0.1 -U runasmidja -d runasmidja -Atc "SELECT current_user"',
        data='deliberately-invalid-test-password\n', allowed=(0, 2))
    if bad_login.returncode == 0:
        raise RuntimeError('Database accepted an invalid runtime password')
    credentials = json.loads((STATE / 'app-role.json').read_text())
    token = bao('auth/approle/login', credentials)['auth']['client_token']
    try:
        data = bao('runasmidja/data/runtime', token=token)['data']['data']
        if data['database_password'] != (STATE / 'app-db.password').read_text():
            raise RuntimeError('Secret provisioning mismatch')
        try:
            bao('sys/mounts', token=token)
        except RuntimeError as error:
            if '(403)' not in str(error):
                raise
        else:
            raise RuntimeError('AppRole must not manage mounts')
        try:
            bao('runasmidja/data/other', token=token)
        except RuntimeError as error:
            if '(403)' not in str(error):
                raise
        else:
            raise RuntimeError('AppRole read escaped runtime secret path')
    finally:
        bao('auth/token/revoke-self', {}, token)
    if not valkey('PING', authenticated=False).startswith(b'-NOAUTH'):
        raise RuntimeError('Unauthenticated cache request accepted')
    if valkey('PING') != b'+PONG':
        raise RuntimeError('Cache unavailable')
    if valkey('SET', 'other:smoke', 'bad').startswith(b'+'):
        raise RuntimeError('Cache ACL permits foreign prefix')
    if valkey('SET', 'runasmidja:smoke', 'ok', 'EX', '10') != b'+OK':
        raise RuntimeError('Cache write failed')
    if valkey('GET', 'runasmidja:smoke') != b'ok':
        raise RuntimeError('Cache read failed')
    if valkey('DEL', 'runasmidja:smoke') != b':1' or valkey('GET', 'runasmidja:smoke') is not None:
        raise RuntimeError('Cache deletion did not remove the value')
    print('PostgreSQL transaction/role, OpenBao AppRole/denials, Valkey auth/ACL/TTL: PASS')
