"""Local COPY-only OpenBao artifact custody and explicit same-version profiles."""
import hashlib
import json
import os
from pathlib import Path
from contextlib import contextmanager
from openbao_lock import artifact_lock
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
    for name in ('openbao_image.py', 'build_openbao_image.py', 'openbao_material.py', 'openbao_lock.py', 'image_evidence.py',
                 'podman_guard.py', 'stream_archive.py', 'image_archive.py', 'process_limits.py'):
        files[name] = bounded_hash(ROOT / 'scripts' / name, 65536)
    return hashlib.sha256(json.dumps(files, sort_keys=True).encode()).hexdigest()


def binding(path, image):
    verify(path, image)
    return bounded_hash(path, 512 * 1024 * 1024)


def _validate_image(image):
    """Caller holds the cache lock through every use of the returned archive."""
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


@contextmanager
def artifact(image=None):
    """Keep a coherent receipt/archive pair pinned for the complete read/scan."""
    with artifact_lock(STATE, exclusive=False):
        if image is None:
            image = json.loads(read_private(STATE / 'receipt.json'))['image']
        yield image, _validate_image(image)


def validate_image(image):
    with artifact(image):
        pass  # Validation only; archive consumption must hold artifact() custody.


def cached_image():
    with artifact() as (image, _):
        return image


def profile():
    value = os.environ.get('RUNASMIDJA_OPENBAO_PROFILE', 'wolfi')
    if value not in ('wolfi', 'official'):
        raise RuntimeError('Unknown OpenBao profile')
    return value


def selected_image():
    require_rootless(run_bounded)
    if profile() == 'official':
        return pins()['upstream']['image']
    with artifact_lock(STATE, exclusive=False):
        if (STATE / 'receipt.json').exists():
            image = json.loads(read_private(STATE / 'receipt.json'))['image']
            _validate_image(image)
            return image
    # Release shared custody before requesting exclusive access; the builder
    # rechecks existence so simultaneous cold starts do not both rebuild.
    from build_openbao_image import build
    build(if_missing=True)
    return cached_image()


def admission_policy(images, policy):
    if images['openbao'] == pins()['upstream']['image']:
        if profile() != 'official':
            raise RuntimeError('Official OpenBao requires explicit selection')
        return {**policy, 'openbao': pins()['upstream']}
    validate_image(images['openbao'])
    return {**policy, 'openbao': {'method': 'local-build', 'image': MARKER}}
