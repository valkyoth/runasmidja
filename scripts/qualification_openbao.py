#!/usr/bin/env python3
"""Actual Wolfi vault identity, built-in storage/auth and audit exhaustion checks."""
import json
import os
import tempfile
import uuid
from pathlib import Path
from stack_common import STATE, NAMES, podman, bao, BaoError
from stack_resources import owned
from stack_vault import identity, runtime_values, read_version, KEYS
from openbao_image import selected_image, pins
from openbao_material import static_binary
from smoke_probe import require


def audit_full():
    info = owned('container', NAMES['openbao'], 'openbao')
    captured = info['Id']
    path = '/audit/qualification-' + str(uuid.uuid4())
    before = runtime_values()
    with identity('runtime') as token:
        try:
            fill = podman('exec', captured, 'dd', 'if=/dev/zero', 'of=' + path,
                          'bs=1048576', 'count=17', allowed=(0, 1), timeout=30)
            require(fill.returncode == 1, 'Vault audit tmpfs did not reach ENOSPC')
            try:
                read_version('runtime', token, KEYS[1:])
            except BaoError as error:
                require(error.status in (500, 503), 'Audit-full failure was not a server refusal')
            else:
                raise RuntimeError('Audited vault read succeeded with full audit sink')
        finally:
            require(owned('container', NAMES['openbao'], 'openbao')['Id'] == captured,
                    'Vault audit cleanup ownership changed')
            podman('exec', captured, 'rm', '-f', path)
        require(read_version('runtime', token, KEYS[1:]) == before, 'Audit recovery changed credentials')
    print('Actual vault audit ENOSPC blocks audited access; removal restores scoped access: PASS')


def qualify():
    image = selected_image()
    info = owned('container', NAMES['openbao'], 'openbao')
    require(info and info['State']['Running'], 'Owned vault is unavailable')
    expected = podman('image', 'inspect', image, '--format', '{{.Id}}').stdout.strip()
    require(info['Image'].removeprefix('sha256:') == expected.removeprefix('sha256:'), 'Vault image mismatch')
    require(os.getuid() != 0 and info['Config'].get('User') == f'{os.getuid()}:{os.getgid()}', 'Vault user mismatch')
    require(not info.get('EffectiveCaps') and not info.get('BoundingCaps'), 'Vault capabilities remain')
    from qualification_valkey import kernel
    kernel(info)  # identical 512 MiB / one CPU / 128 PID fixture limits
    host = info['HostConfig']
    require(host.get('Privileged') is False and 'no-new-privileges' in host.get('SecurityOpt', []), 'Vault privilege drift')
    require(host.get('Memory') == 536870912 and host.get('PidsLimit') == 128 and
            host.get('CpuQuota') == 100000, 'Vault limit drift')
    require(bao('sys/health')['version'] == pins()['version'], 'Vault version mismatch')
    with tempfile.TemporaryDirectory(dir=STATE) as folder:
        binary = Path(folder) / 'bao'
        podman('cp', NAMES['openbao'] + ':/usr/bin/bao', str(binary))
        static_binary(binary, pins()['binary_sha256'])
        if image != pins()['upstream']['image']:
            release = Path(folder) / 'os-release'
            podman('cp', NAMES['openbao'] + ':/etc/os-release', str(release))
            require(release.stat().st_size < 4096 and 'ID=wolfi' in release.read_text().splitlines(), 'Vault base mismatch')
    audit_full()
    print('Actual OpenBao version/static executable/base, scoped auth and audit recovery: PASS')


if __name__ == '__main__':
    from stack_files import fixture_lock
    with fixture_lock(): qualify()
