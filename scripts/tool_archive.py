#!/usr/bin/env python3
"""Extract only the already digest-verified crate root into a fresh private directory."""
import os
import re
import sys
import tarfile
import tomllib
from pathlib import Path, PurePosixPath


def extract(archive, destination, name, version):
    if not re.fullmatch(r'[a-z][a-z0-9-]*', name) or not re.fullmatch(r'\d+\.\d+\.\d+', version):
        raise ValueError('Invalid pinned tool identifier')
    prefix = name + '-' + version
    destination.mkdir(mode=0o700)
    total = 0
    with tarfile.open(archive, 'r:gz') as source:
        for count, member in enumerate(source, 1):
            parts = PurePosixPath(member.name).parts
            if count > 20000 or not parts or parts[0] != prefix or '..' in parts or member.name.startswith('/'):
                raise ValueError('Crate archive path/count rejected')
            if not (member.isfile() or member.isdir()):
                raise ValueError('Crate archive links/special files rejected')
            total += member.size
            if member.size < 0 or total > 64 * 1024 * 1024:
                raise ValueError('Crate archive expansion exceeds budget')
            path = destination.joinpath(*parts[1:])
            if member.isdir():
                path.mkdir(mode=0o700, parents=True, exist_ok=True)
            else:
                path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
                with source.extractfile(member) as input_file:
                    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
                    with os.fdopen(descriptor, 'wb') as output_file:
                        while chunk := input_file.read(65536):
                            output_file.write(chunk)
    manifest = tomllib.loads((destination / 'Cargo.toml').read_text())
    if manifest['package']['name'] != name or manifest['package']['version'] != version:
        raise ValueError('Verified crate root identity mismatch')
    if not (destination / 'Cargo.lock').is_file():
        raise ValueError('Verified crate lacks the required lockfile')


if __name__ == '__main__':
    extract(Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3], sys.argv[4])
