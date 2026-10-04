#!/usr/bin/env python3
"""Actual cache image/version, denial, resource and bounded eviction qualification."""
import json
import os
import re
import tempfile
import uuid
from pathlib import Path
from stack_common import ROOT, STATE, NAMES, INSTANCE, podman, valkey, read_private, wait_for
from stack_resources import owned
from stack_vault import runtime_values
from smoke_probe import require
from valkey_image import selected_image, rules
from valkey_probe_wire import CacheProbe


def configuration(info, image):
    expected = podman('image', 'inspect', image, '--format', '{{.Id}}').stdout.strip()
    require(info.get('Image', '').removeprefix('sha256:') == expected.removeprefix('sha256:') and expected,
            'Valkey executed image mismatch')
    host = info['HostConfig']
    user = info['Config'].get('User', '')
    require(re.fullmatch(r'[0-9]+:[0-9]+', user) is not None and int(user.split(':')[0]) != 0,
            'Valkey must run as a nonroot numeric UID')
    require(user == f'{os.getuid()}:{os.getgid()}', 'Valkey user mismatch')
    require(host.get('ReadonlyRootfs') is True and host.get('Privileged') is False, 'Valkey root/privilege drift')
    require('no-new-privileges' in (host.get('SecurityOpt') or []), 'Valkey escalation policy drift')
    require(not info.get('EffectiveCaps') and not info.get('BoundingCaps'), 'Valkey capabilities remain')
    require(host.get('Memory') == 536870912 and host.get('PidsLimit') == 128 and
            host.get('CpuPeriod') == 100000 and host.get('CpuQuota') == 100000, 'Valkey resource limits drift')
    ports = info.get('NetworkSettings', {}).get('Ports', {}).get('6379/tcp')
    require(ports == [{'HostIp': '127.0.0.1', 'HostPort': '16379'}], 'Valkey publication drift')
    mounts = info.get('Mounts', [])
    require(len(mounts) == 1 and mounts[0].get('Destination') == '/config/valkey.conf' and
            mounts[0].get('Source') == str(STATE / 'valkey.conf') and mounts[0].get('RW') is False,
            'Valkey delivery mount drift')
    lines = read_private(STATE / 'valkey.conf').splitlines()
    for setting in ('save ""', 'appendonly no', 'maxmemory 64mb', 'maxmemory-policy allkeys-lru', 'user default off'):
        require(lines.count(setting) == 1, 'Valkey cache policy drift')


def kernel(info):
    pid = info['State']['Pid']
    require(type(pid) is int and pid > 0, 'Invalid Valkey host process')
    proc = Path('/proc') / str(pid)
    status = dict(line.split(':', 1) for line in (proc / 'status').read_text().splitlines() if ':' in line)
    require(status.get('NoNewPrivs', '').strip() == '1', 'Valkey kernel permits privilege escalation')
    for key in ('CapEff', 'CapPrm', 'CapBnd'):
        require(status.get(key, '').strip() == '0000000000000000', 'Valkey kernel capabilities remain')
    group = (proc / 'cgroup').read_text().strip()
    require(group.startswith('0::/'), 'Valkey unified cgroup unavailable')
    path = Path('/sys/fs/cgroup') / group[4:]
    for key, expected in {'memory.max': '536870912', 'pids.max': '128', 'cpu.max': '100000 100000'}.items():
        require((path / key).read_text().strip() == expected, 'Valkey live resource limit drift')


def memory_and_denials():
    client = CacheProbe()
    prefix = 'runasmidja:qualification:' + str(uuid.uuid4()) + ':'
    count = 1536
    try:
        require(client.request('AUTH', 'runasmidja', 'invalid-public-negative-fixture').startswith(b'-WRONGPASS'),
                'Valkey accepted wrong credentials')
        password = runtime_values()['valkey_password']
        require(client.request('AUTH', 'runasmidja', password) == b'+OK', 'Valkey scoped authentication failed')
        for command in (('CONFIG', 'GET', '*'), ('ACL', 'LIST'), ('INFO',), ('FLUSHALL',), ('SAVE',),
                        ('SET', 'foreign:qualification', 'denied'), ('GET', 'foreign:qualification')):
            require(client.request(*command).startswith(b'-NOPERM'), 'Valkey ACL denial failed')
        payload = b'x' * 65500
        for index in range(count):
            require(client.request('SET', prefix + str(index), payload) == b'+OK', 'Bounded cache fill failed')
        missing = 0
        for index in range(count):
            value = client.request('GET', prefix + str(index))
            if value is None: missing += 1
            else: require(value == payload, 'Cache value changed')
        require(0 < missing < count, 'Valkey maxmemory eviction was not observed')
        for index in range(count):
            require(client.request('DEL', prefix + str(index)) in (b':0', b':1'), 'Cache cleanup failed')
    finally:
        client.close()
    print('Valkey wrong-auth/command/key denials and real bounded maxmemory eviction: PASS')


def qualify():
    from stack_common import require_rootless
    require_rootless()
    image = selected_image(INSTANCE)
    info = owned('container', NAMES['valkey'], 'valkey')
    require(info and info['State']['Running'], 'Owned Valkey fixture is unavailable')
    configuration(info, image); kernel(info)
    version = json.loads((ROOT / 'docs/upstream-lock.json').read_text())['github_releases']['valkey-io/valkey']
    output = podman('exec', NAMES['valkey'], 'valkey-server', '--version').stdout
    require(re.search(r'\bv=' + re.escape(version) + r'\s', output), 'Valkey version differs from reviewed release')
    if image == rules()['valkey']['image']:
        with tempfile.TemporaryDirectory(dir=STATE) as folder:
            target = Path(folder) / 'os-release'
            podman('cp', NAMES['valkey'] + ':/etc/os-release', str(target))
            require(target.stat().st_size < 4096 and 'ID=wolfi' in target.read_text().splitlines(),
                    'Valkey base differs from Wolfi')
    memory_and_denials()
    values = runtime_values()
    require(valkey('SET', 'runasmidja:restart-check', 'disposable') == b'+OK', 'Cache restart setup failed')
    identity = info['Id']
    require(owned('container', NAMES['valkey'], 'valkey')['Id'] == identity, 'Valkey restart ownership changed')
    podman('stop', identity)
    try:
        try: valkey('PING')
        except (ConnectionError, OSError): pass
        else: raise RuntimeError('Stopped Valkey responded')
    finally:
        require(owned('container', NAMES['valkey'], 'valkey')['Id'] == identity, 'Valkey restart ownership changed')
        podman('start', identity)
    wait_for(lambda: valkey('PING') == b'+PONG')
    require(runtime_values() == values, 'Cache restart changed vault secret versions')
    require(valkey('GET', 'runasmidja:restart-check') is None, 'Disposable cache unexpectedly persisted')
    configuration(owned('container', NAMES['valkey'], 'valkey'), image)
    print('Valkey exact version/base, kernel limits, outage/restart and nonpersistence: PASS')


if __name__ == '__main__':
    from stack_files import fixture_lock
    with fixture_lock(): qualify()
