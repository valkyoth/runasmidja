#!/usr/bin/env python3
"""Real Podman logging/tmpfs bounds using only an individually admitted clean image."""
import json
import uuid
from image_gate import ROOT, tool, provenance, scan
from stack_common import podman


def qualify():
    from stack_common import require_rootless
    require_rootless()
    policy = json.loads((ROOT / 'deploy/podman/image-policy.json').read_text())
    image = policy['wolfi-base']['image']
    provenance('wolfi-base', image, policy, tool('cosign'))
    clean, _count = scan('wolfi-base', image, tool('trivy'))
    if not clean:
        raise RuntimeError('Bounds test image not admitted')
    identity = str(uuid.uuid4())
    name = 'runasmidja-bounds-' + identity
    created = False
    try:
        podman('run', '-d', '--name', name, '--label', 'io.runasmidja.qualification=' + identity,
            '--log-driver', 'k8s-file', '--log-opt', 'max-size=1048576',
            '--network', 'none', '--read-only', '--cap-drop', 'ALL', '--security-opt', 'no-new-privileges',
            '--memory', '64m', '--pids-limit', '32', '--tmpfs', '/audit:rw,noexec,nosuid,nodev,size=16777216',
            '--entrypoint', 'sh', image, '-c', 'sleep 120')
        created = True
        info = json.loads(podman('inspect', name).stdout)[0]
        print('Actual bounded log configuration: ' + json.dumps(info['HostConfig']['LogConfig']), flush=True)
        from stack_resources import start_container
        from unittest.mock import patch
        import stack_resources
        # Exercise the actual inspect representation through production reuse validation.
        with patch.object(stack_resources, 'owned', return_value=info):
            start_container('valkey', image, [])
        size = podman('exec', name, 'sh', '-c', "df -Pk /audit | tail -1 | awk '{print $2}'").stdout.strip()
        if size != '16384':
            raise RuntimeError('Live audit tmpfs capacity differs from 16 MiB')
        # ENOSPC must happen in the container tmpfs, never on a host audit bind mount.
        fill = podman('exec', name, 'sh', '-c',
            'dd if=/dev/zero of=/audit/fill bs=1048576 count=17', allowed=(0, 1), timeout=30)
        if fill.returncode == 0:
            raise RuntimeError('Audit capacity did not fail closed')
        podman('exec', name, 'rm', '/audit/fill')
        # Write via PID 1 descriptors so these bytes exercise Podman log storage.
        podman('exec', name, 'sh', '-c',
            'dd if=/dev/zero bs=65536 count=64 > /proc/1/fd/1 2>/proc/1/fd/2', timeout=30)
        info = json.loads(podman('inspect', name).stdout)[0]
        log_path = info['HostConfig']['LogConfig']['Path']
        from pathlib import Path
        # Log rotation can transiently include one write block/record.
        if Path(log_path).stat().st_size > 1048576 + 65536:
            raise RuntimeError('Live container log exceeds bounded record tolerance')
        try:
            podman('logs', '--tail', '2000', name, output_limit=128, timeout=5)
        except RuntimeError:
            pass
        else:
            raise RuntimeError('Actual log flood bypassed capture budget')
        print('Actual 16 MiB audit ENOSPC, 1 MiB log rotation and bounded log capture: PASS')
    finally:
        if created:
            info = json.loads(podman('inspect', name).stdout)[0]
            if info['Config']['Labels'].get('io.runasmidja.qualification') != identity:
                raise RuntimeError('Bounds-test cleanup lost ownership')
            podman('stop', '--time', '1', name)
            podman('rm', name)


if __name__ == '__main__':
    qualify()
