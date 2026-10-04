#!/usr/bin/env python3
"""Assemble verified upstream static OpenBao on signed Wolfi, without build execution."""
import json
import os
import shutil
from custody import replace_private, sync_parent
from image_gate import provenance, scan, tool, EVIDENCE
from podman_guard import podman, require_rootless, archive as export_archive
from process_limits import run_bounded
from stream_archive import save_bounded_archive
from openbao_material import copied_binary
from openbao_image import STATE, RECIPE, pins, fingerprint, binding


def build():
    require_rootless(run_bounded)
    STATE.mkdir(mode=0o700, parents=True, exist_ok=True)
    EVIDENCE.mkdir(mode=0o700, parents=True, exist_ok=True)
    lock = pins(); started = fingerprint()
    policy = {'platform': 'linux/amd64', 'openbao': lock['upstream'], 'wolfi-base': lock['base']}
    for service in ('openbao', 'wolfi-base'):
        image = policy[service]['image']
        provenance(service, image, policy, tool('cosign'))
        if not scan(service, image, tool('trivy'))[0]:
            raise RuntimeError('OpenBao assembly input scan rejected')
        podman(run_bounded, 'pull', '--platform', 'linux/amd64', image)
    context = STATE / 'context'; context.mkdir(mode=0o700, exist_ok=True)
    copied_binary(lock['upstream']['image'], context / 'bao', lock['binary_sha256'])
    os.chmod(context / 'bao', 0o755)
    for name in ('Containerfile', '.containerignore', 'OPENBAO-LICENSE'):
        shutil.copyfile(RECIPE / name, context / name)
    if (context / 'Containerfile').read_text().splitlines()[1] != 'FROM ' + lock['base']['image']:
        raise RuntimeError('OpenBao base differs from policy')
    podman(run_bounded, 'build', '--network', 'none', '--pull=never', '--layers=false',
        '--inherit-labels=false', '--inherit-annotations=false', '--http-proxy=false',
        '--timestamp', str(lock['timestamp']), '--platform', 'linux/amd64',
        '--label', 'io.runasmidja.openbao-recipe=' + started, '--iidfile', str(STATE / 'image.id'),
        '-f', str(context / 'Containerfile'), str(context))
    image = (STATE / 'image.id').read_text().strip()
    candidate = STATE / 'candidate.tar'
    export_archive(run_bounded, save_bounded_archive, image, candidate)
    digest = binding(candidate, image)
    copied_binary(image, STATE / 'admitted-bao', lock['binary_sha256'])
    if not scan('openbao-wolfi', image, tool('trivy'), archive=candidate,
                archive_check=lambda: binding(candidate, image))[0]:
        raise RuntimeError('OpenBao candidate scan blocked; no receipt published')
    if fingerprint() != started or binding(candidate, image) != digest:
        raise RuntimeError('OpenBao assembly input/archive changed during admission')
    # Publish only after full admission; a failed retry cannot create a valid receipt.
    receipt = STATE / 'receipt.json'
    if receipt.exists():
        from custody import durable_unlink, read_private
        read_private(receipt); durable_unlink(receipt)
    os.replace(candidate, STATE / 'image.tar'); sync_parent(STATE / 'image.tar')
    replace_private(receipt, json.dumps({'schema': 1, 'recipe': started, 'image': image,
        'archive_sha256': digest, 'binary_sha256': lock['binary_sha256'],
        'trust': 'local COPY-only assembly; verified upstream binary/base; not distributed signing'}))
    print('OpenBao verified static binary/Wolfi archive admission: PASS')


if __name__ == '__main__':
    build()
