#!/usr/bin/env python3
"""Build the public-source PostgreSQL fixture only after verified base admission."""
import hashlib
import json
import shutil
import urllib.request
import re
from pathlib import Path
from image_gate import ROOT, EVIDENCE, tool, provenance, scan
from process_limits import run_bounded
from custody import replace_private, read_private
from postgres_image import fingerprint, record, bounded_hash

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
    if not source.exists():
        with urllib.request.urlopen(SOURCE_URL, timeout=30) as response:
            data = response.read(30_000_001)
        if len(data) > 30_000_000 or hashlib.sha256(data).hexdigest() != SOURCE_SHA:
            raise RuntimeError('PostgreSQL source digest/size rejected')
        source.write_bytes(data)
    if bounded_hash(source, 30_000_000) != SOURCE_SHA:
        raise RuntimeError('PostgreSQL cached source digest rejected')
    for name in ('Containerfile', 'entrypoint.sh', '.containerignore'):
        shutil.copyfile(ROOT / 'deploy/podman/postgres' / name, STATE / name)
    result = run_bounded('podman', 'build', '--format', 'oci', '--layers=false',
        '--platform', 'linux/amd64', '--http-proxy=false', '--inherit-labels=false', '--inherit-annotations=false',
        '--label', 'io.runasmidja.project=runasmidja', '--label', 'io.runasmidja.service=postgres',
        '--label', 'io.runasmidja.recipe=' + started,
        '--iidfile', str(STATE / 'image.id'), '-t', 'localhost/runasmidja-postgres:19beta4-wolfi',
        '-f', str(STATE / 'Containerfile'), str(STATE), timeout=1800, output_limit=1024 * 1024,
        allowed=(0, 1, 125))
    replace_private(STATE / 'build.log', result.stdout + result.stderr, limit=1024 * 1024)
    if result.returncode:
        raise RuntimeError('Public-source build failed; see private bounded build.log')
    image = (STATE / 'image.id').read_text().strip()
    if not re.fullmatch(r'sha256:[0-9a-f]{64}', image) or fingerprint() != started:
        raise RuntimeError('Build image/input binding changed during compilation')
    run_bounded('podman', 'save', '--format', 'docker-archive', '--output', str(STATE / 'image.tar'), image)
    record(image)
    if not scan('postgres', image, tool('trivy'), archive=STATE / 'image.tar')[0]:
        raise RuntimeError('Built PostgreSQL vulnerability gate failed')
    print('Public-source PostgreSQL Wolfi build completed.', flush=True)


if __name__ == '__main__':
    build()
