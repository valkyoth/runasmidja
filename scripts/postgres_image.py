"""Local public-source image custody; not distributed signing or production provenance."""
import hashlib
import json
import os
import stat
import re
from pathlib import Path
from custody import read_private, replace_private
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
    files['builder'] = bounded_hash(ROOT / 'scripts/build_postgres_image.py', 64 * 1024)
    files['base_provenance'] = policy
    return hashlib.sha256(json.dumps(files, sort_keys=True).encode()).hexdigest()


def record(image):
    from image_archive import verify
    verify(STATE / 'image.tar', image)
    receipt = {'schema': 1, 'recipe': fingerprint(), 'image': image,
               'archive_sha256': bounded_hash(STATE / 'image.tar', 512 * 1024 * 1024),
               'trust': 'local host/build custody only; unsigned and not portable release provenance'}
    replace_private(STATE / 'receipt.json', json.dumps(receipt))


def validate_image(image):
    if not re.fullmatch(r'sha256:[0-9a-f]{64}', image):
        raise RuntimeError('Local build requires immutable image config ID')
    receipt = json.loads(read_private(STATE / 'receipt.json'))
    if receipt.get('schema') != 1 or receipt.get('recipe') != fingerprint() or receipt.get('image') != image:
        raise RuntimeError('Local PostgreSQL build receipt drift')
    if receipt.get('archive_sha256') != bounded_hash(STATE / 'image.tar', 512 * 1024 * 1024):
        raise RuntimeError('Local PostgreSQL image archive tampered')
    from image_archive import verify
    verify(STATE / 'image.tar', image)
    actual = run_bounded('podman', 'image', 'inspect', image, '--format', '{{.Id}}').stdout.strip()
    if 'sha256:' + actual.removeprefix('sha256:') != image:
        raise RuntimeError('Local PostgreSQL image identity drift')
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
    if images.get('postgres') == MARKER:
        images['postgres'] = ensure_image()
    return images
