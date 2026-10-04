"""Copy only the hash-pinned static executable from a verified upstream image."""
import json
import struct
import uuid
from pathlib import Path
from podman_guard import podman
from process_limits import run_bounded
from postgres_image import bounded_hash

MAX_BINARY = 256 * 1024 * 1024


def static_binary(path, expected):
    if bounded_hash(path, MAX_BINARY) != expected:
        raise RuntimeError('OpenBao executable hash mismatch')
    with path.open('rb') as source:
        header = source.read(64)
        if len(header) != 64 or header[:6] != b'\x7fELF\x02\x01' or struct.unpack_from('<H', header, 18)[0] != 62:
            raise RuntimeError('OpenBao requires Linux amd64 ELF64')
        offset = struct.unpack_from('<Q', header, 32)[0]
        size, count = struct.unpack_from('<HH', header, 54)
        if size != 56 or not 1 <= count <= 64 or offset + count * size > path.stat().st_size:
            raise RuntimeError('OpenBao ELF program headers rejected')
        source.seek(offset)
        for _ in range(count):
            entry = source.read(size)
            if len(entry) != size or struct.unpack_from('<I', entry)[0] in (2, 3):
                raise RuntimeError('OpenBao dynamic linkage is not admitted')


def copied_binary(image, path, expected):
    owner = str(uuid.uuid4())
    key = 'io.runasmidja.openbao-material'
    identity = podman(run_bounded, 'create', '--name', 'runasmidja-bao-material-' + owner,
        '--label', key + '=' + owner, '--network', 'none', '--read-only',
        '--cap-drop', 'ALL', image).stdout.strip()
    def owned():
        info = json.loads(podman(run_bounded, 'inspect', identity).stdout)[0]
        actual = podman(run_bounded, 'image', 'inspect', image, '--format', '{{.Id}}').stdout.strip()
        if (info['Id'] != identity or info['Config'].get('Labels', {}).get(key) != owner or
                info['Image'].removeprefix('sha256:') != actual.removeprefix('sha256:')):
            raise RuntimeError('OpenBao material container ownership/image mismatch')
    try:
        owned()
        podman(run_bounded, 'cp', identity + ':/usr/bin/bao', str(path))
        static_binary(path, expected)
    finally:
        owned()
        podman(run_bounded, 'rm', identity)
