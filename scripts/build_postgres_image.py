#!/usr/bin/env python3
"""Build the public-source PostgreSQL fixture only after verified base admission."""
import hashlib
import json
import shutil
import urllib.request
import re
import os
from pathlib import Path
from image_gate import ROOT, EVIDENCE, tool, provenance, scan
from process_limits import run_bounded
from custody import replace_private, read_private
from postgres_image import fingerprint, record, bounded_hash
from build_sandbox import sandbox
from custody import sync_parent

STATE = ROOT / '.local/postgres-wolfi'
PINS = json.loads((ROOT / 'deploy/podman/postgres/source.lock.json').read_text())
SOURCE_URL, SOURCE_SHA = PINS['url'], PINS['sha256']


def build():
    STATE.mkdir(mode=0o700, parents=True, exist_ok=True)
    EVIDENCE.mkdir(mode=0o700, parents=True, exist_ok=True)
    policy = json.loads((ROOT / 'deploy/podman/image-policy.json').read_text())
    base = policy['wolfi-base']['image']
    started = fingerprint()
    provenance('wolfi-base', base, policy, tool('cosign'))
    if not scan('wolfi-base', base, tool('trivy'))[0]:
        raise RuntimeError('Wolfi base vulnerability gate failed')
    source = STATE / 'postgresql-19beta4.tar.bz2'
    if not source.exists() and not source.is_symlink():
        with urllib.request.urlopen(SOURCE_URL, timeout=30) as response:
            data = response.read(30_000_001)
        if len(data) > 30_000_000 or hashlib.sha256(data).hexdigest() != SOURCE_SHA:
            raise RuntimeError('PostgreSQL source digest/size rejected')
        descriptor = os.open(source, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
        with os.fdopen(descriptor, 'wb') as handle:
            handle.write(data); handle.flush(); os.fsync(handle.fileno())
        sync_parent(source)
    if bounded_hash(source, 30_000_000) != SOURCE_SHA:
        raise RuntimeError('PostgreSQL cached source digest rejected')
    for name in ('Containerfile', 'entrypoint.sh', '.containerignore'):
        shutil.copyfile(ROOT / 'deploy/podman/postgres' / name, STATE / name)
    result = sandbox(started)
    replace_private(STATE / 'sandbox.log', result.stdout + result.stderr, limit=1024 * 1024)
    if result.returncode:
        raise RuntimeError('Public-source build failed; see private bounded build.log')
    image = read_private(STATE / 'contained-image.id').strip()
    if not re.fullmatch(r'sha256:[0-9a-f]{64}', image) or fingerprint() != started:
        raise RuntimeError('Build image/input binding changed during compilation')
    record(image)
    if not scan('postgres', image, tool('trivy'), archive=STATE / 'image.tar')[0]:
        raise RuntimeError('Built PostgreSQL vulnerability gate failed')
    run_bounded('podman', 'load', '--input', str(STATE / 'image.tar'), timeout=180)
    from postgres_image import validate_image
    validate_image(image)
    print('Public-source PostgreSQL Wolfi build completed.', flush=True)


if __name__ == '__main__':
    build()
