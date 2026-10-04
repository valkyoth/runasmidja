#!/usr/bin/env python3
"""Public builds in owned cgroups and private, size-limited tmpfs Podman storage."""
import json
import os
import sys
import tempfile
import uuid
from pathlib import Path
from process_limits import run_bounded
from custody import private, replace_private
from stream_archive import save_bounded_archive

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / '.local/postgres-wolfi'
STORAGE = 3 * 1024 ** 3
MEMORY = 5 * 1024 ** 3
BUILD_LIMITS = ['--memory', '2g', '--memory-swap', '2g', '--cpu-period', '100000',
                '--cpu-quota', '200000', '--ulimit', 'nproc=512:512']


def sandbox(recipe, *, qualify=False):
    identity = str(uuid.uuid4())
    unit = 'runasmidja-build-' + identity + '.service'
    description = 'Runasmidja public build ' + identity
    with tempfile.TemporaryDirectory(prefix='build-arena-', dir=STATE) as arena:
        command = ['systemd-run', '--user', '--pipe', '--wait', '--collect', '--unit', unit,
            '--description', description, '-p', 'CPUQuota=200%', '-p', f'MemoryMax={MEMORY}',
            '-p', 'MemorySwapMax=0', '-p', 'TasksMax=512', '-p', 'Delegate=yes',
            '-p', 'DelegateSubgroup=supervisor',
            '-p', 'RuntimeMaxSec=1800', 'podman', '--remote=false', 'unshare', 'unshare',
            '--mount', '--propagation', 'private', sys.executable, str(Path(__file__).resolve()),
            '--worker', arena, recipe, 'qualify' if qualify else 'build']
        try:
            return run_bounded(*command, timeout=1800, allowed=(0, 1, 125))
        finally:
            # Stop the captured unit, not a possibly recycled PID/process group.
            info = run_bounded('systemctl', '--user', 'show', unit, '-p', 'Description', '--value', allowed=(0, 1))
            if info.stdout.strip() == description:
                run_bounded('systemctl', '--user', 'stop', unit)
            elif info.stdout.strip() not in ('', unit):
                raise RuntimeError('Build unit cleanup ownership mismatch')


def cgroup():
    entries = Path('/proc/self/cgroup').read_text().splitlines()
    parent = next((entry[3:] for entry in entries if entry.startswith('0::')), None)
    if not parent or not parent.endswith('.service/supervisor') or '/runasmidja-build-' not in parent:
        raise RuntimeError('Build is outside its owned cgroup')
    parent = parent.rsplit('/', 1)[0]
    group = Path('/sys/fs/cgroup') / parent.lstrip('/')
    expected = {'memory.max': str(MEMORY), 'memory.swap.max': '0', 'pids.max': '512', 'cpu.max': '200000 100000'}
    if any((group / key).read_text().strip() != value for key, value in expected.items()):
        raise RuntimeError('Actual build cgroup limits differ from policy')
    return parent + '/steps'


def worker(arena, recipe, mode):
    parent = cgroup()
    run_bounded('mount', '-t', 'tmpfs', '-o', f'size={STORAGE},mode=0700,nodev,nosuid', 'runasmidja-build', arena)
    root = Path(arena)
    actual = os.statvfs(root)
    if actual.f_blocks * actual.f_frsize != STORAGE:
        raise RuntimeError('Build storage capacity differs from policy')
    for name in ('store', 'run', 'tmp'):
        (root / name).mkdir(mode=0o700)
    auth = root / 'auth.json'
    private(auth, '{"auths":{}}')
    podman = ['podman', '--remote=false', '--root', str(root / 'store'), '--runroot', str(root / 'run'),
              '--tmpdir', str(root / 'tmp'), '--storage-driver', 'vfs', '--cgroup-manager', 'cgroupfs']
    env = {**os.environ, 'TMPDIR': str(root / 'tmp')}
    if mode == 'qualify':
        probe = root / 'capacity'; probe.mkdir()
        run_bounded('mount', '-t', 'tmpfs', '-o', 'size=16777216,mode=0700', 'runasmidja-capacity', str(probe))
        filled = run_bounded('dd', 'if=/dev/zero', f'of={probe}/fill', 'bs=1048576', 'count=17', allowed=(0, 1))
        if filled.returncode != 1 or (probe / 'fill').stat().st_size > 16777216:
            raise RuntimeError('Actual build storage ENOSPC not enforced')
        context = root / 'context'; context.mkdir()
        base = json.loads((ROOT / 'deploy/podman/postgres/source.lock.json').read_text())['base']
        (context / 'Containerfile').write_text(f'FROM {base}\nRUN test "$(cat /sys/fs/cgroup/memory.max)" = 2147483648 && test "$(cat /sys/fs/cgroup/cpu.max)" = "200000 100000"\n')
        source = context
    else:
        source = STATE
    result = run_bounded(*podman, 'build', *BUILD_LIMITS, '--cgroup-parent', parent,
        '--authfile', str(auth), '--format', 'oci', '--layers=false', '--platform', 'linux/amd64',
        '--http-proxy=false', '--inherit-labels=false', '--inherit-annotations=false',
        '--label', 'io.runasmidja.project=runasmidja', '--label', 'io.runasmidja.service=postgres',
        '--label', 'io.runasmidja.recipe=' + recipe, '--iidfile', str(root / 'image.id'),
        '-f', str(source / 'Containerfile'), str(source), timeout=1500, output_limit=1024 * 1024,
        allowed=(0, 1, 125), env=env)
    replace_private(STATE / 'build.log', result.stdout + result.stderr, limit=1024 * 1024)
    if result.returncode:
        raise RuntimeError('Contained build failed; private bounded build.log retained')
    if mode == 'qualify':
        print('Actual build CPU/memory/process cgroup limits and quota-backed ENOSPC: PASS', flush=True)
        return
    image = (root / 'image.id').read_text().strip()
    save_bounded_archive([*podman, 'save', '--format', 'docker-archive', image], STATE / 'image.tar')
    replace_private(STATE / 'contained-image.id', image)


if __name__ == '__main__':
    if len(sys.argv) == 5 and sys.argv[1] == '--worker':
        worker(*sys.argv[2:])
    elif sys.argv[1:] == ['--qualify']:
        STATE.mkdir(mode=0o700, parents=True, exist_ok=True)
        from image_gate import provenance, scan, tool, EVIDENCE
        policy = json.loads((ROOT / 'deploy/podman/image-policy.json').read_text())
        EVIDENCE.mkdir(mode=0o700, parents=True, exist_ok=True)
        base = policy['wolfi-base']['image']
        provenance('wolfi-base', base, policy, tool('cosign'))
        if not scan('wolfi-base', base, tool('trivy'))[0]:
            raise SystemExit('Build resource probe image not admitted')
        result = sandbox('public-resource-qualification', qualify=True)
        print(result.stdout)
        if result.returncode:
            raise SystemExit('Build containment qualification failed; diagnostics withheld')
    else:
        raise SystemExit('usage: build_sandbox.py --qualify')
