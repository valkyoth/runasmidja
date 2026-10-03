"""Real service tests, including unauthorized paths and cache key isolation."""
import json
from stack_common import STATE, NAMES, bao, podman, valkey, read_private
from stack_vault import identity, provisioning_values, read_version, KEYS


def smoke():
    if STATE.stat().st_mode & 0o077:
        raise RuntimeError('Private stack directory permissions are too broad')
    if (STATE / 'bootstrap.json').exists():
        raise RuntimeError('Bootstrap root token retained after provisioning')
    for name in ('recovery.json', 'provision-role.json', 'runtime-role.json', 'postgres.password', 'app-db.password', 'valkey.password', 'bao.key'):
        read_private(STATE / name)
    version = podman('exec', NAMES['postgres'], 'psql', '-U', 'postgres', '-Atc', 'SHOW server_version').stdout.strip()
    if not version.startswith('19beta4'):
        raise RuntimeError('PostgreSQL must be 19 beta 4 for this baseline')
    podman('exec', '-i', NAMES['postgres'], 'psql', '-U', 'postgres', '-d', 'runasmidja', '-v', 'ON_ERROR_STOP=1',
        data='BEGIN; CREATE TEMP TABLE runasmidja_smoke (id bigint PRIMARY KEY); INSERT INTO runasmidja_smoke VALUES (1); ROLLBACK;')
    flags = podman('exec', NAMES['postgres'], 'psql', '-U', 'postgres', '-Atc',
        "SELECT rolsuper OR rolcreatedb OR rolcreaterole FROM pg_roles WHERE rolname='runasmidja'").stdout.strip()
    if flags != 'f':
        raise RuntimeError('Runtime database role has excessive privileges')
    values = provisioning_values()
    admin = podman('exec', '-i', NAMES['postgres'], 'sh', '-c',
        'IFS= read -r PGPASSWORD; export PGPASSWORD; exec psql -h 127.0.0.1 -U postgres -d runasmidja -Atc "SELECT current_user"',
        data=values['postgres_admin_password'] + '\n').stdout.strip()
    if admin != 'postgres':
        raise RuntimeError('Vault-issued administrator credential did not initialize PostgreSQL')
    password = values['database_password']
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
    with identity('runtime') as token:
        data = read_version('runtime', token, KEYS[1:])
        if data['database_password'] != password:
            raise RuntimeError('Secret provisioning mismatch')
        try:
            bao('sys/mounts', token=token)
        except RuntimeError as error:
            if '(403)' not in str(error):
                raise
        else:
            raise RuntimeError('AppRole must not manage mounts')
        try:
            bao('runasmidja/data/provisioning', token=token)
        except RuntimeError as error:
            if '(403)' not in str(error):
                raise
        else:
            raise RuntimeError('AppRole read escaped runtime secret path')
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
    with identity('provision') as token:
        for path, payload in (('sys/mounts', None), ('sys/tools/random', {'bytes': 32, 'format': 'hex'}),
                              ('runasmidja/data/provisioning', {'data': {}})):
            try:
                bao(path, payload, token)
            except RuntimeError as error:
                if '(403)' not in str(error):
                    raise
            else:
                raise RuntimeError('Provisioning identity exceeded read-only scope')
    print('PostgreSQL transaction/role, OpenBao scoped reads/denials, Valkey auth/ACL: PASS (expiry not qualified)')
