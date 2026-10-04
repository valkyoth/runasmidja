"""Local COPY-only OpenBao artifact custody and explicit same-version profiles."""
import hashlib
import json
import os
from pathlib import Path
from custody import read_private
from postgres_image import bounded_hash
from image_archive import verify
from podman_guard import podman, require_rootless
from process_limits import run_bounded

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / '.local/openbao-wolfi'
RECIPE = ROOT / 'deploy/podman/openbao'
MARKER = 'local:openbao-wolfi'


def pins():
    return json.loads((RECIPE / 'image.lock.json').read_text())


def fingerprint():
    files = {name: bounded_hash(RECIPE / name, 65536) for name in
             ('Containerfile', '.containerignore', 'image.lock.json', 'OPENBAO-LICENSE')}
    for name in ('openbao_image.py', 'build_openbao_image.py', 'openbao_material.py',
                 'podman_guard.py', 'stream_archive.py', 'image_archive.py', 'process_limits.py'):
        files[name] = bounded_hash(ROOT / 'scripts' / name, 65536)
    return hashlib.sha256(json.dumps(files, sort_keys=True).encode()).hexdigest()


def binding(path, image):
    verify(path, image)
    return bounded_hash(path, 512 * 1024 * 1024)


def validate_image(image):
    record = json.loads(read_private(STATE / 'receipt.json'))
    if record.get('image') != image or record.get('recipe') != fingerprint():
        raise RuntimeError('OpenBao build receipt/input mismatch')
    archive = STATE / 'image.tar'
    if binding(archive, image) != record.get('archive_sha256'):
        raise RuntimeError('OpenBao archive changed')
    actual = podman(run_bounded, 'image', 'inspect', image, '--format', '{{.Id}}').stdout.strip()
    if actual.removeprefix('sha256:') != image.removeprefix('sha256:'):
        raise RuntimeError('OpenBao loaded image mismatch')
    return archive


def profile():
    value = os.environ.get('RUNASMIDJA_OPENBAO_PROFILE', 'wolfi')
    if value not in ('wolfi', 'official'):
        raise RuntimeError('Unknown OpenBao profile')
    return value


def selected_image():
    require_rootless(run_bounded)
    if profile() == 'official':
        return pins()['upstream']['image']
    if not (STATE / 'receipt.json').exists():
        from build_openbao_image import build
        build()
    image = json.loads(read_private(STATE / 'receipt.json'))['image']
    validate_image(image)
    return image


def admission_policy(images, policy):
    if images['openbao'] == pins()['upstream']['image']:
        if profile() != 'official':
            raise RuntimeError('Official OpenBao requires explicit selection')
        return {**policy, 'openbao': pins()['upstream']}
    validate_image(images['openbao'])
    return {**policy, 'openbao': {'method': 'local-build', 'image': MARKER}}
