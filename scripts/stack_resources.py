"""Minimum project/service/instance ownership before fixture mutations."""
import json
import os
from stack_common import STATE, NETWORK, NAMES, podman, private, read_private


def labels(service):
    identity = json.loads(read_private(STATE / 'owner.json'))['instance']
    return {'io.runasmidja.scope': 'development', 'io.runasmidja.project': 'runasmidja',
            'io.runasmidja.service': service, 'io.runasmidja.instance': identity}


def owned(kind, name, service):
    if podman(kind, 'exists', name, allowed=(0, 1)).returncode:
        return None
    info = json.loads(podman(kind, 'inspect', name).stdout)[0]
    actual = (info.get('Config', {}).get('Labels', {}) if kind == 'container'
              else info.get('labels', {}) if kind == 'network' else info.get('Labels', {}))
    if not isinstance(actual, dict) or any(actual.get(k) != v for k, v in labels(service).items()):
        raise RuntimeError(f'Refusing unowned {kind} fixture')
    return info


def preflight():
    owned('network', NETWORK, 'network')
    owned('volume', NAMES['postgres'], 'postgres')
    for service, name in NAMES.items():
        owned('container', name, service)


def label_args(service):
    args = []
    for key, value in labels(service).items():
        args += ['--label', key + '=' + value]
    return args


def infrastructure():
    if not owned('network', NETWORK, 'network'):
        podman('network', 'create', '--internal', *label_args('network'), NETWORK)
    if not owned('volume', NAMES['postgres'], 'postgres'):
        podman('volume', 'create', *label_args('postgres'), NAMES['postgres'])


def start_container(service, image, args):
    name = NAMES[service]
    info = owned('container', name, service)
    if info:
        expected = podman('image', 'inspect', image, '--format', '{{.Id}}').stdout.strip()
        if not expected or info.get('Image', '').removeprefix('sha256:') != expected.removeprefix('sha256:'):
            raise RuntimeError('Refusing fixture image drift')
        log = info.get('HostConfig', {}).get('LogConfig', {})
        # Podman reports the effective size as a display string and Config=null.
        size = (log.get('Config') or {}).get('max-size', log.get('Size'))
        if log.get('Type') != 'k8s-file' or size not in ('1048576', '1.049MB'):
            raise RuntimeError('Fixture needs explicit security-bounds upgrade')
        if service == 'openbao':
            options = set(info.get('HostConfig', {}).get('Tmpfs', {}).get('/audit', '').split(','))
            if not {'rw', 'noexec', 'nosuid', 'nodev'}.issubset(options) or not (
                    {'size=16777216', 'size=16m'} & options):
                raise RuntimeError('Vault needs bounded audit sink upgrade')
        if not info['State']['Running']:
            podman('start', name)
        return
    from valkey_image import arguments
    command = arguments(image) if service == 'valkey' else ['server', '-config=/config/bao.hcl'] if service == 'openbao' else []
    podman('run', '-d', '--name', name, *label_args(service),
        '--log-driver', 'k8s-file', '--log-opt', 'max-size=1048576',
        '--network', NETWORK, '--memory', '512m', '--cpus', '1', '--pids-limit', '128',
        '--security-opt', 'no-new-privileges', *args, image,
        *command)


def stop():
    # Check everything before stopping anything; collisions never cause partial mutation.
    preflight()
    for service, name in NAMES.items():
        info = owned('container', name, service)
        if info and info['State']['Running']:
            if service == 'openbao':
                from audit_evidence import snapshot_audit
                snapshot_audit(info)
            podman('stop', name)
    print('Owned test containers stopped; data retained.')


def upgrade_bounds(images):
    """Explicitly recreate only verified fixture containers; retain all data/custody."""
    preflight()
    for service, name in NAMES.items():
        info = owned('container', name, service)
        if not info:
            continue
        expected = podman('image', 'inspect', images[service], '--format', '{{.Id}}').stdout.strip()
        if info.get('Image', '').removeprefix('sha256:') != expected.removeprefix('sha256:'):
            raise RuntimeError('Image drift blocks bounds upgrade')
        mounts = {m['Destination']: m for m in info.get('Mounts', [])}
        if service == 'postgres' and mounts.get('/var/lib/postgresql', {}).get('Name') != NAMES['postgres']:
            raise RuntimeError('Database volume drift blocks bounds upgrade')
        if service == 'openbao' and mounts.get('/data', {}).get('Source') != str(STATE / 'bao-data'):
            raise RuntimeError('Vault data drift blocks bounds upgrade')
    stop()
    for service, name in NAMES.items():
        if owned('container', name, service):
            podman('rm', name)
    print('Verified fixture containers removed for bounds upgrade; all data/custody retained.')
