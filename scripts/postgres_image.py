"""Local public-source image custody; not distributed signing or production provenance."""
import hashlib
import json
import os
import stat
import re
from pathlib import Path
from custody import read_private, replace_private, durable_unlink, sync_parent
from process_limits import run_bounded

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / '.local/postgres-wolfi'
MARKER = 'local:postgres-wolfi'


def bounded_hash(path, maximum):
    descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(descriptor, 'rb') as source:
        info = os.fstat(source.fileno())
        if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or info.st_size > maximum:
            raise RuntimeError('Local image material custody/size rejected')
        return hashlib.file_digest(source, 'sha256').hexdigest()


def fingerprint():
    recipe = ROOT / 'deploy/podman/postgres'
    pins = json.loads((recipe / 'source.lock.json').read_text())
    policy = json.loads((ROOT / 'deploy/podman/image-policy.json').read_text())['wolfi-base']
    if pins['base'] != policy['image']:
        raise RuntimeError('Build base differs from reviewed publisher policy')
    files = {name: bounded_hash(recipe / name, 64 * 1024) for name in
             ('Containerfile', 'entrypoint.sh', '.containerignore', 'source.lock.json')}
    for name in ('build_postgres_image.py', 'build_sandbox.py', 'stream_archive.py', 'process_limits.py', 'custody.py'):
        files[name] = bounded_hash(ROOT / 'scripts' / name, 64 * 1024)
    files['base_provenance'] = policy
    return hashlib.sha256(json.dumps(files, sort_keys=True).encode()).hexdigest()


def candidate_receipt(path, image, expected_recipe):
    if fingerprint() != expected_recipe:
        raise RuntimeError('Build recipe changed during candidate admission')
    digest = bounded_hash(path, 512 * 1024 * 1024)
    from image_archive import verify
    verify(path, image)
    return {'schema': 1, 'recipe': expected_recipe, 'image': image,
            'archive_sha256': digest,
            'trust': 'local host/build custody only; unsigned and not portable release provenance'}


def verify_loaded_image(image):
    actual = run_bounded('podman', 'image', 'inspect', image, '--format', '{{.Id}}').stdout.strip()
    if 'sha256:' + actual.removeprefix('sha256:') != image:
        raise RuntimeError('Local PostgreSQL image identity drift')


def record(image, expected=None):
    receipt = candidate_receipt(STATE / 'image.tar', image, fingerprint())
    if expected is not None and receipt != expected:
        raise RuntimeError('Published archive differs from admitted candidate')
    replace_private(STATE / 'receipt.json', json.dumps(receipt))


def commit_candidate(receipt):
    candidate = STATE / 'candidate.tar'
    if candidate_receipt(candidate, receipt['image'], receipt['recipe']) != receipt:
        raise RuntimeError('Candidate changed after scan')
    verify_loaded_image(receipt['image'])
    final = STATE / 'receipt.json'
    if final.exists() or final.is_symlink():
        read_private(final)
        durable_unlink(final)
    # A failure during publication leaves no final receipt: ensure_image retries.
    os.replace(candidate, STATE / 'image.tar')
    sync_parent(STATE / 'image.tar')
    record(receipt['image'], expected=receipt)


def validate_image(image, *, require_local=True):
    if not re.fullmatch(r'sha256:[0-9a-f]{64}', image):
        raise RuntimeError('Local build requires immutable image config ID')
    receipt = json.loads(read_private(STATE / 'receipt.json'))
    if receipt.get('schema') != 1 or receipt.get('recipe') != fingerprint() or receipt.get('image') != image:
        raise RuntimeError('Local PostgreSQL build receipt drift')
    if receipt.get('archive_sha256') != bounded_hash(STATE / 'image.tar', 512 * 1024 * 1024):
        raise RuntimeError('Local PostgreSQL image archive tampered')
    from image_archive import verify
    verify(STATE / 'image.tar', image)
    if require_local:
        verify_loaded_image(image)
    return STATE / 'image.tar'


def ensure_image():
    if not (STATE / 'receipt.json').exists():
        from build_postgres_image import build
        build()
    receipt = json.loads(read_private(STATE / 'receipt.json'))
    validate_image(receipt['image'])
    return receipt['image']


def fixture_images():
    images = json.loads((ROOT / 'deploy/podman/images.json').read_text())
    from valkey_image import selected_image
    images['valkey'] = selected_image()
    if images.get('postgres') == MARKER:
        images['postgres'] = ensure_image()
    return images
