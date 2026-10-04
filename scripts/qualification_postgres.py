#!/usr/bin/env python3
"""Real fixed-profile image denials; public negative inputs are never credentials."""
import json
import tempfile
import uuid
from pathlib import Path
from stack_common import STATE, NAMES, podman
from stack_files import fixture_lock
from postgres_image import ensure_image, validate_image
from stack_resources import owned


def denied(image, folder, case, expected):
    name = 'runasmidja-pg-denial-' + str(uuid.uuid4())
    identity = str(uuid.uuid4())
    root = folder / case
    root.mkdir(mode=0o700)
    secret_dir = root / 'secrets'
    secret_dir.mkdir(mode=0o700)
    # A published literal used only to reach the data-layout denial, never a live login.
    password = secret_dir / 'postgres.password'
    password.write_text('a' * 64)
    password.chmod(0o600)
    data = root / 'data'
    (data / '19').mkdir(mode=0o700, parents=True)
    cluster = data / '19/wolfi'
    cluster.mkdir(mode=0o700)
    env = ['-e', 'POSTGRES_PASSWORD_FILE=/run/secrets/postgres.password', '-e', 'POSTGRES_DB=runasmidja']
    user = '0:0' if case == 'root' else '999:999'
    if case == 'missing-password':
        env = ['-e', 'POSTGRES_DB=runasmidja']
    elif case == 'password-env':
        env += ['-e', 'POSTGRES_PASSWORD=public-negative-fixture']
    elif case == 'bad-password':
        password.write_text('public-negative-fixture')
    elif case == 'password-symlink':
        password.unlink(); password.symlink_to('/dev/zero')
    elif case == 'trust-auth':
        env += ['-e', 'POSTGRES_HOST_AUTH_METHOD=trust']
    elif case == 'legacy':
        (data / '19/docker').mkdir(mode=0o700)
    elif case == 'partial':
        (cluster / 'retain-me').write_text('must not reset unknown data')
    elif case == 'data-symlink':
        cluster.rmdir(); cluster.symlink_to('docker')
    else:
        (cluster / 'PG_VERSION').write_text('18' if case == 'wrong-version' else '19')
        if case != 'incomplete':
            (cluster / '.runasmidja-ready').write_text('wrong' if case == 'wrong-ready' else '19beta4:runasmidja')
    def contents():
        return {str(path.relative_to(root)): ('link', str(path.readlink())) if path.is_symlink()
                else ('file', path.read_bytes()) for path in root.rglob('*') if path.is_symlink() or path.is_file()}
    original = contents()
    created = False
    try:
        podman('create', '--name', name, '--label', 'io.runasmidja.qualification=' + identity,
            '--userns', 'keep-id:uid=999,gid=999', '--user', user, '--network', 'none',
            '--read-only', '--cap-drop', 'ALL', '--security-opt', 'no-new-privileges',
            '--memory', '128m', '--pids-limit', '32', '--log-driver', 'k8s-file', '--log-opt', 'max-size=1048576',
            '-v', f'{secret_dir}:/run/secrets:ro,Z', '-v', f'{data}:/var/lib/postgresql:ro,Z', *env, image)
        created = True
        result = podman('start', '-a', name, allowed=(0, 1, 125), timeout=15)
        info = json.loads(podman('inspect', name).stdout)[0]
        if info['State']['ExitCode'] != 1 or result.returncode != 1:
            raise RuntimeError('PostgreSQL image denial failed: ' + case)
        if expected and expected not in result.stdout + result.stderr:
            raise RuntimeError('PostgreSQL image failed for a different reason: ' + case)
        if contents() != original:
            raise RuntimeError('PostgreSQL image altered rejected fixture data')
    finally:
        if created:
            info = json.loads(podman('inspect', name).stdout)[0]
            if info['Config']['Labels'].get('io.runasmidja.qualification') != identity:
                raise RuntimeError('PostgreSQL denial cleanup ownership lost')
            if info['State']['Running']:
                podman('stop', '--time', '1', name)
            podman('rm', name)


def qualify():
    from stack_common import require_rootless
    require_rootless()
    image = ensure_image()
    validate_image(image)
    info = owned('container', NAMES['postgres'], 'postgres')
    if not info or not info['State']['Running'] or info['Image'].removeprefix('sha256:') != image.removeprefix('sha256:'):
        raise RuntimeError('PostgreSQL runtime does not match admitted local image')
    settings = podman('exec', NAMES['postgres'], 'psql', '-U', 'postgres', '-d', 'runasmidja', '-Atc',
        "SELECT current_setting('server_encoding'), datcollate, datctype FROM pg_database WHERE datname='runasmidja'").stdout.strip()
    if settings != 'UTF8|C.UTF-8|C.UTF-8':
        raise RuntimeError('Actual PostgreSQL locale/encoding differs from qualified profile')
    packages = set(podman('exec', NAMES['postgres'], 'apk', 'info').stdout.splitlines())
    if packages & {'gcc', 'build-base', 'perl', 'gosu'}:
        raise RuntimeError('Compiler/privilege-switch package present in runtime')
    cases = {'root': 'refuses root', 'missing-password': 'Password file required',
             'password-env': 'Password environment refused', 'bad-password': 'Invalid password record',
             'password-symlink': None, 'trust-auth': None, 'legacy': 'Legacy data requires migration',
             'partial': 'Partial database requires recovery', 'data-symlink': 'Database symlink refused',
             'incomplete': 'Incomplete database initialization', 'wrong-version': 'Database version refused',
             'wrong-ready': 'Incomplete database initialization'}
    with tempfile.TemporaryDirectory(prefix='pg-denials-', dir=STATE) as directory:
        for case, expected in cases.items():
            denied(image, Path(directory), case, expected)
    print('Actual PostgreSQL UTF8/locale/runtime inventory and 12 fail-closed initialization profiles: PASS')


if __name__ == '__main__':
    with fixture_lock():
        from image_gate import verify_images
        from postgres_image import fixture_images
        verify_images(fixture_images())
        qualify()
