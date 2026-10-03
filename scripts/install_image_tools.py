#!/usr/bin/env python3
"""Install reviewed image tooling locally; no system package changes."""
import hashlib
import io
import json
import os
import tarfile
import urllib.request
from pathlib import Path
from process_limits import run_bounded

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / '.local/tools'


def download(url, digest):
    with urllib.request.urlopen(url, timeout=30) as response:
        data = response.read(150 * 1024 * 1024 + 1)
    if len(data) > 150 * 1024 * 1024 or hashlib.sha256(data).hexdigest() != digest:
        raise RuntimeError('Image tool artifact digest/size rejected')
    return data


def install():
    TOOLS.mkdir(parents=True, mode=0o700, exist_ok=True)
    pins = json.loads((ROOT / 'scripts/image-tools.lock.json').read_text())
    cosign = TOOLS / 'cosign'
    cosign.write_bytes(download(pins['cosign']['url'], pins['cosign']['binary_sha256']))
    cosign.chmod(0o700)
    archive = TOOLS / 'trivy.tar.gz'
    archive.write_bytes(download(pins['trivy']['url'], pins['trivy']['archive_sha256']))
    bundle = TOOLS / 'trivy.sigstore.json'
    bundle.write_bytes(download(pins['trivy']['signature_url'], pins['trivy']['signature_sha256']))
    run_bounded(str(cosign), 'verify-blob', '--bundle', str(bundle),
                '--certificate-identity-regexp', pins['trivy']['identity_regex'],
                '--certificate-oidc-issuer', 'https://token.actions.githubusercontent.com', str(archive))
    with tarfile.open(fileobj=io.BytesIO(archive.read_bytes()), mode='r:gz') as source:
        member = source.getmember('trivy')
        if not member.isfile() or member.size > 256 * 1024 * 1024:
            raise RuntimeError('Scanner archive member rejected')
        binary = source.extractfile(member).read(256 * 1024 * 1024 + 1)
    if hashlib.sha256(binary).hexdigest() != pins['trivy']['binary_sha256']:
        raise RuntimeError('Scanner extracted binary digest rejected')
    trivy = TOOLS / 'trivy'
    trivy.write_bytes(binary)
    trivy.chmod(0o700)
    print('Pinned Cosign/Trivy and scanner publisher signature verified.')


if __name__ == '__main__':
    install()
