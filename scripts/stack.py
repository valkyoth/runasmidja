#!/usr/bin/env python3
"""Rootless OpenBao-first test fixture; never a production bootstrap."""
import argparse
import json
import os
from stack_common import ROOT, STATE, NAMES, podman, read_private, wait_for
from stack_files import files, delivery, fixture_lock
from stack_resources import infrastructure, owned, preflight, start_container, stop, upgrade_bounds
from stack_vault import bootstrap, provisioning_values, runtime_values, revoke_root
from image_gate import verify_images
from postgres_image import fixture_images


def up():
    files()
    preflight()
    images = fixture_images()
    verify_images(images)
    for image in images.values():
        if podman('image', 'exists', image, allowed=(0, 1)).returncode:
            podman('pull', image)
    infrastructure()
    identity = f'{os.getuid()}:{os.getgid()}'
    start_container('openbao', images['openbao'], ['-p', '127.0.0.1:18200:8200',
        '--userns', 'keep-id', '--user', identity, '--cap-drop', 'ALL',
        '-v', f'{STATE}/bao-config:/config:ro,Z', '-v', f'{STATE}/bao-data:/data:Z',
        '--tmpfs', '/audit:rw,noexec,nosuid,nodev,size=16777216,mode=1777'])
    root = bootstrap()
    # No consumer is started and no delivery copy is read without a fresh scoped vault read.
    values = provisioning_values()
    if runtime_values() != {k: values[k] for k in ('database_password', 'valkey_password')}:
        raise RuntimeError('Scoped runtime retrieval mismatch')
    delivery(values)
    start_container('postgres', images['postgres'], ['-p', '127.0.0.1:15432:5432',
        '--userns', 'keep-id:uid=999,gid=999', '--user', '999:999', '--cap-drop', 'ALL', '--read-only',
        '--tmpfs', '/var/run/postgresql:rw,noexec,nosuid,nodev,size=16777216,mode=1777',
        '--tmpfs', '/tmp:rw,noexec,nosuid,nodev,size=33554432,mode=1777',
        '-e', 'POSTGRES_PASSWORD_FILE=/run/secrets/postgres.password', '-e', 'POSTGRES_DB=runasmidja',
        '-e', 'POSTGRES_INITDB_ARGS=--auth-host=scram-sha-256',
        '-v', f'{STATE}/postgres.password:/run/secrets/postgres.password:ro,Z',
        '-v', NAMES['postgres'] + ':/var/lib/postgresql'])
    wait_for(lambda: podman('exec', NAMES['postgres'], 'pg_isready', '-U', 'postgres', allowed=(0, 1, 2)).returncode == 0)
    owned('container', NAMES['postgres'], 'postgres')
    podman('exec', '--user', 'postgres', NAMES['postgres'], 'sh', '-c',
        "sed -i '/^[[:space:]]*host/s/[[:space:]]trust[[:space:]]*$/ scram-sha-256/' \"$PGDATA/pg_hba.conf\"")
    podman('exec', NAMES['postgres'], 'psql', '-U', 'postgres', '-Atc', 'SELECT pg_reload_conf()')
    password = values['database_password']  # exactly 64 lowercase hex, validated before SQL
    sql = f"""SELECT 'CREATE ROLE runasmidja LOGIN' WHERE NOT EXISTS (SELECT FROM pg_roles WHERE rolname='runasmidja')\\gexec
ALTER ROLE runasmidja PASSWORD '{password}';
GRANT CONNECT ON DATABASE runasmidja TO runasmidja;
"""
    podman('exec', '-i', NAMES['postgres'], 'psql', '-U', 'postgres', '-d', 'runasmidja',
        '-v', 'ON_ERROR_STOP=1', data=sql)
    start_container('valkey', images['valkey'], ['-p', '127.0.0.1:16379:6379',
        '--userns', 'keep-id', '--user', identity, '--cap-drop', 'ALL', '--read-only',
        '-v', f'{STATE}/valkey.conf:/config/valkey.conf:ro,Z'])
    from stack_common import valkey
    wait_for(lambda: valkey('PING') == b'+PONG')
    revoke_root(root)
    print('OpenBao-first development stack ready; scoped credentials verified; bootstrap root revoked.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('up', 'stop', 'status', 'smoke', 'upgrade-bounds'))
    action = parser.parse_args().action
    if action == 'status':
        for service, name in NAMES.items():
            result = podman('inspect', '--format', '{{.State.Status}}', name, allowed=(0, 125))
            print(service + ': ' + (result.stdout.strip() or 'absent'))
        return
    with fixture_lock():
        if action == 'up':
            up()
        elif action == 'stop':
            stop()
        elif action == 'upgrade-bounds':
            upgrade_bounds(fixture_images())
        else:
            preflight()
            verify_images(fixture_images())
            from stack_smoke import smoke
            smoke()


if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, KeyError, OSError, ValueError) as error:
        # Typed HTTP errors are redacted; arbitrary parser/OS errors can contain sensitive input.
        raise SystemExit(f'Stack failed ({type(error).__name__}); private diagnostics withheld') from None
