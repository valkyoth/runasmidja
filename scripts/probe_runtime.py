"""Owned, ephemeral-port runtime qualification of an exact scanned probe image."""
import json
import re
from pathlib import Path
from process_limits import run_bounded
from podman_guard import podman, require_rootless
from postgres_image import bounded_hash
from probe_image import MAX_BINARY
from smoke_probe import require, verify

LABEL = 'io.runasmidja.probe-qualification'


def inspect(identity):
    result = json.loads(podman(run_bounded, 'inspect', identity).stdout)
    require(len(result) == 1, 'Probe inspection is ambiguous')
    return result[0]


def owned(identity, owner):
    info = inspect(identity)
    require(info.get('Id') == identity and info.get('Config', {}).get('Labels', {}).get(LABEL) == owner,
            'Probe cleanup ownership mismatch')
    return info


def configuration(info, image):
    require(re.fullmatch(r'sha256:[0-9a-f]{64}', image) and
            info.get('Image') in (image, image[7:]), 'Probe image identity changed')
    config, host = info['Config'], info['HostConfig']
    require(config.get('User') == '65532:65532', 'Probe user drift')
    require(config.get('Entrypoint') == ['/runasmidja-server'] and
            config.get('Cmd') == ['18080', '--container'], 'Probe execution configuration drift')
    require(host.get('ReadonlyRootfs') is True, 'Probe root is writable')
    require('no-new-privileges' in (host.get('SecurityOpt') or []), 'Probe privilege escalation enabled')
    require(not info.get('EffectiveCaps') and not info.get('BoundingCaps'), 'Probe capabilities remain')
    require(host.get('Memory') == 32 * 1024 * 1024 and host.get('MemorySwap') == 32 * 1024 * 1024,
            'Probe memory limit drift')
    require(host.get('PidsLimit') == 16 and host.get('CpuPeriod') == 100000 and
            host.get('CpuQuota') == 100000, 'Probe CPU/process limit drift')
    require(not host.get('Privileged') and not info.get('Mounts'), 'Probe gained privileges or mounts')


def port(info):
    ports = info.get('NetworkSettings', {}).get('Ports', {})
    require(set(ports) == {'18080/tcp'}, 'Unexpected probe port publication')
    entries = ports['18080/tcp']
    require(isinstance(entries, list) and len(entries) == 1, 'Ambiguous probe port publication')
    require(entries[0].get('HostIp') == '127.0.0.1', 'Probe is publicly exposed')
    number = entries[0].get('HostPort', '')
    require(isinstance(number, str) and re.fullmatch(r'[0-9]{1,5}', number), 'Invalid probe port')
    require(0 < int(number) <= 65535, 'Invalid probe port')
    return int(number)


def kernel_limits(info):
    """Local Linux profile: verify live kernel state, not only requested configuration."""
    pid = info['State']['Pid']
    require(type(pid) is int and pid > 0, 'Invalid probe host PID')
    process = Path('/proc') / str(pid)
    status = dict(line.split(':', 1) for line in (process / 'status').read_text().splitlines() if ':' in line)
    require(status.get('NoNewPrivs', '').strip() == '1', 'Kernel permits privilege escalation')
    for key in ('CapEff', 'CapPrm', 'CapBnd'):
        require(status.get(key, '').strip() == '0000000000000000', 'Kernel probe capabilities remain')
    groups = (process / 'cgroup').read_text().splitlines()
    require(len(groups) == 1 and groups[0].startswith('0::/'), 'Unified probe cgroup missing')
    group = Path('/sys/fs/cgroup') / groups[0][4:]
    expected = {'memory.max': '33554432', 'memory.swap.max': '0',
                'pids.max': '16', 'cpu.max': '100000 100000'}
    for name, value in expected.items():
        require((group / name).read_text().strip() == value, 'Kernel probe limit drift: ' + name)


def qualify(image, digest, state, owner):
    result = podman(run_bounded, 'create', '--name', 'runasmidja-probe-' + owner,
        '--label', LABEL + '=' + owner, '--read-only', '--cap-drop', 'ALL',
        '--security-opt', 'no-new-privileges', '--memory', '32m', '--memory-swap', '32m',
        '--pids-limit', '16', '--cpu-period', '100000', '--cpu-quota', '100000',
        '--log-driver', 'none', '-p', '127.0.0.1::18080', image)
    identity = result.stdout.strip()
    require(re.fullmatch(r'[0-9a-f]{64}', identity), 'Invalid created probe identity')
    try:
        configuration(owned(identity, owner), image)
        binary = state / 'copied-executable'
        podman(run_bounded, 'cp', identity + ':/runasmidja-server', str(binary))
        require(bounded_hash(binary, MAX_BINARY) == digest, 'Image executable differs from built executable')
        os_release = state / 'os-release'
        podman(run_bounded, 'cp', identity + ':/etc/os-release', str(os_release))
        require(os_release.stat().st_size < 4096 and 'ID=wolfi' in os_release.read_text().splitlines(),
                'Probe runtime is not the admitted Wolfi profile')
        podman(run_bounded, 'start', identity)
        info = owned(identity, owner)
        configuration(info, image)
        require(info['State']['Running'], 'Probe exited before testing')
        kernel_limits(info)
        verify(port(info))
        require(owned(identity, owner)['State']['Running'], 'Probe exited during testing')
    finally:
        owned(identity, owner)
        podman(run_bounded, 'rm', '-f', identity)
