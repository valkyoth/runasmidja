"""Bind Docker archive config/layer bytes to the image ID that will execute."""
import hashlib
import json
import re
import tarfile
import os
import stat


def verify(path, image):
    descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(descriptor, 'rb') as source:
        info = os.fstat(source.fileno())
        if not stat.S_ISREG(info.st_mode) or info.st_size > 512 * 1024 * 1024:
            raise RuntimeError('Image archive outer type/size budget rejected')
        _verify(source, image)


def _verify(source, image):
    with tarfile.open(fileobj=source, mode='r') as archive:
        members = {}
        for member in archive:
            legacy_link = (member.issym() and re.fullmatch(r'[0-9a-f]{64}/layer\.tar', member.name)
                           and re.fullmatch(r'\.\./[0-9a-f]{64}\.tar', member.linkname))
            if len(members) >= 4096 or member.name in members or not (member.isfile() or legacy_link):
                raise RuntimeError('Image archive member/type budget rejected')
            members[member.name] = member
        def small(name):
            member = members[name]
            if not member.isfile() or member.size > 1024 * 1024:
                raise RuntimeError('Image archive metadata budget rejected')
            return archive.extractfile(member).read(1024 * 1024 + 1)
        manifest = json.loads(small('manifest.json'))
        if len(manifest) != 1 or not re.fullmatch(r'sha256:[0-9a-f]{64}', image):
            raise RuntimeError('Image archive identity rejected')
        name = manifest[0]['Config']
        if name != image.removeprefix('sha256:') + '.json':
            raise RuntimeError('Scanned image config differs from execution image')
        config = small(name)
        if 'sha256:' + hashlib.sha256(config).hexdigest() != image:
            raise RuntimeError('Image config digest rejected')
        decoded = json.loads(config)
        if decoded.get('os') != 'linux' or decoded.get('architecture') != 'amd64':
            raise RuntimeError('Image archive platform rejected')
        expected = decoded['rootfs']['diff_ids']
        layers = manifest[0]['Layers']
        if len(layers) != len(expected) or not layers or len(layers) > 64:
            raise RuntimeError('Image layer inventory rejected')
        for name, digest in zip(layers, expected):
            if not re.fullmatch(r'sha256:[0-9a-f]{64}', digest) or name != digest[7:] + '.tar':
                raise RuntimeError('Image layer identity rejected')
            member = members[name]
            if not member.isfile() or member.size > 512 * 1024 * 1024:
                raise RuntimeError('Image layer budget rejected')
            with archive.extractfile(member) as data:
                actual = 'sha256:' + hashlib.file_digest(data, 'sha256').hexdigest()
            if actual != digest:
                raise RuntimeError('Scanned layer bytes differ from execution image')
        for member in members.values():
            if member.issym() and member.linkname[3:] not in layers:
                raise RuntimeError('Legacy compatibility link has no verified layer')
