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
        if not info['State']['Running']:
            podman('start', name)
        return
    podman('run', '-d', '--name', name, *label_args(service),
        '--network', NETWORK, '--memory', '512m', '--cpus', '1', '--pids-limit', '128',
        '--security-opt', 'no-new-privileges', *args, image,
        *({'openbao': ['server', '-config=/config/bao.hcl'],
           'valkey': ['valkey-server', '/config/valkey.conf']}.get(service, [])))


def stop():
    # Check everything before stopping anything; collisions never cause partial mutation.
    preflight()
    for service, name in NAMES.items():
        info = owned('container', name, service)
        if info and info['State']['Running']:
            podman('stop', name)
    print('Owned test containers stopped; data retained.')
