#!/usr/bin/env python3
"""Explicit same-version vault image switch; preserve custody, never reset data."""
import argparse
import hashlib
import json
import os
from stack_common import STATE, NAMES, INSTANCE, podman, read_private, replace_private
from stack_files import fixture_lock
from stack_resources import owned, preflight, stop
from stack_vault import runtime_values
from openbao_image import pins, selected_image, cached_image
from image_gate import verify_images
from postgres_image import fixture_images


def custody():
    names = ('owner.json', 'bao.key', 'bao.crt', 'recovery.json', 'provision-role.json',
             'runtime-role.json', 'references.json', 'bao-config/bao.hcl')
    return {name: hashlib.sha256(read_private(STATE / name).encode()).hexdigest() for name in names}


def removable(info, images):
    if not info:
        raise RuntimeError('Vault must be an owned container')
    actual = info['Image'].removeprefix('sha256:')
    expected = [podman('image', 'inspect', image, '--format', '{{.Id}}').stdout.strip().removeprefix('sha256:')
                for image in images]
    if actual not in expected:
        raise RuntimeError('Vault switch image is outside the same-version pair')
    mounts = {m['Destination']: m for m in info.get('Mounts', [])}
    if (set(mounts) != {'/config', '/data'} or
            mounts['/data'].get('Source') != str(STATE / 'bao-data') or mounts['/data'].get('RW') is not True or
            mounts['/config'].get('Source') != str(STATE / 'bao-config') or mounts['/config'].get('RW') is not False):
        raise RuntimeError('Vault switch custody mount drift')


def switch(target):
    if INSTANCE != 'v023-wolfi-bao' or target not in ('official', 'wolfi'):
        raise RuntimeError('Switch is limited to the v0.2.3 qualification fixture')
    os.environ['RUNASMIDJA_OPENBAO_PROFILE'] = target
    selected_image()
    verify_images(fixture_images())
    preflight()
    before = custody()
    pending = STATE / 'bao-switch.json'
    if pending.exists():
        record = json.loads(read_private(pending))
        if record['target'] != target or record['custody'] != before:
            raise RuntimeError('Pending switch differs; retry its original target')
    else:
        values = runtime_values()
        record = {'target': target, 'custody': before,
                  'values': hashlib.sha256(json.dumps(values, sort_keys=True).encode()).hexdigest()}
        replace_private(pending, json.dumps(record))
    info = owned('container', NAMES['openbao'], 'openbao')
    # Retrying after removal/start failure uses the same record and preserved data.
    if info:
        wolfi = cached_image()
        removable(info, (pins()['upstream']['image'], wolfi))
        identity = info['Id']
        stop()
        current = owned('container', NAMES['openbao'], 'openbao')
        if current['Id'] != identity or current['State']['Running']:
            raise RuntimeError('Vault switch identity changed')
        podman('rm', identity)
    import stack
    stack.up()
    if custody() != before or hashlib.sha256(json.dumps(runtime_values(), sort_keys=True).encode()).hexdigest() != record['values']:
        raise RuntimeError('Vault switch changed custody or credential versions')
    from custody import durable_unlink
    durable_unlink(pending)
    print('Same-version OpenBao switch to ' + target + ': retained custody and scoped credentials PASS')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('profile', choices=('official', 'wolfi'))
    args = parser.parse_args()
    with fixture_lock(): switch(args.profile)
