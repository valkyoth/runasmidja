#!/usr/bin/env python3
"""Actual-service qualification for v0.2; preserves all fixture data and reports no secrets."""
import json
import ssl
import uuid
import urllib.error
from unittest.mock import patch
from stack_common import STATE, NAMES, BaoError, bao, podman, read_private, replace_private
from stack_resources import owned, stop
import stack_resources
from stack_vault import provisioning_values, runtime_values
import stack
import stack_common
from stack_files import fixture_lock
from stack_smoke import smoke


def require(value, message):
    if not value:
        raise RuntimeError(message)


def no_consumers_running():
    for service in ('postgres', 'valkey'):
        info = owned('container', NAMES[service], service)
        require(not info or not info['State']['Running'], 'Dependent startup escaped vault failure')


def bad_ca():
    system_trust = ssl.create_default_context()
    with patch.object(stack_common.ssl, 'create_default_context', return_value=system_trust):
        try:
            provisioning_values()
        except urllib.error.URLError as error:
            require(isinstance(error.reason, ssl.SSLCertVerificationError), 'Bad-CA test did not fail certificate verification')
        else:
            raise RuntimeError('Wrong vault CA accepted')


def cold_start():
    start = stack.start_container
    def interrupted(service, image, args):
        if service == 'postgres':
            raise RuntimeError('Injected interruption after vault issuance')
        return start(service, image, args)
    with patch.object(stack, 'start_container', side_effect=interrupted):
        try:
            stack.up()
        except RuntimeError as error:
            require(str(error) == 'Injected interruption after vault issuance', 'Unexpected startup failure')
        else:
            raise RuntimeError('Fault injection did not interrupt startup')
    no_consumers_running()
    bad_ca()
    no_consumers_running()
    values = provisioning_values()
    root = json.loads(read_private(STATE / 'bootstrap.json'))['root_token']
    bao('sys/seal', {}, root)
    try:
        provisioning_values()
    except BaoError as error:
        require(error.status == 503, 'Unexpected sealed-vault response')
    else:
        raise RuntimeError('Sealed vault issued credentials')
    no_consumers_running()
    recovery = json.loads(read_private(STATE / 'recovery.json'))['keys_base64'][0]
    bao('sys/unseal', {'key': recovery})
    original = read_private(STATE / 'provision-role.json')
    bad = json.loads(original)
    bad['secret_id'] = 'invalid-public-negative-fixture'
    replace_private(STATE / 'provision-role.json', json.dumps(bad))
    try:
        try:
            stack.up()
        except BaoError as error:
            require(error.status in (400, 403), 'Unexpected identity-denial response')
        else:
            raise RuntimeError('Denied provisioning identity started consumers')
        no_consumers_running()
    finally:
        replace_private(STATE / 'provision-role.json', original)
    stack.up()
    require(provisioning_values() == values, 'Partial retry replaced issued credentials')
    require(not (STATE / 'bootstrap.json').exists(), 'Bootstrap custody was not removed')
    try:
        bao('auth/token/lookup-self', token=root)
    except BaoError as error:
        require(error.status == 403, 'Unexpected revoked-root response')
    else:
        raise RuntimeError('Root remains usable')
    print('Empty-state vault issuance, interrupted retry, seal/identity denials, root revocation: PASS')
    return root


def leakage(values, bootstrap_root=None):
    needles = list(values.values())
    if bootstrap_root:
        needles.append(bootstrap_root)
    for role in ('provision', 'runtime'):
        needles.append(json.loads(read_private(STATE / (role + '-role.json')))['secret_id'])
    needles += json.loads(read_private(STATE / 'recovery.json'))['keys_base64']
    needles.append(read_private(STATE / 'bao.key').splitlines()[1])
    for service, name in NAMES.items():
        require(owned('container', name, service), 'Owned service missing')
        for args in (('inspect', name), ('logs', name)):
            result = podman(*args)
            text = result.stdout + result.stderr
            require(not any(value in text for value in needles), 'Secret found in container metadata/logs')
    audit = (STATE / 'bao-audit/audit.log').read_text()
    require(not any(value in audit for value in needles), 'Secret found in audit log')
    require('random' in audit and 'runasmidja/data/' in audit, 'Required issuance/read audit evidence missing')
    print('Credential/recovery/TLS disclosure scan of container metadata/logs and vault audit: PASS')


def collisions():
    # Deliberately wrong-label test objects have independent, captured cleanup custody.
    owner = str(uuid.uuid4())
    name = 'runasmidja-qualification-' + owner
    image = json.loads((stack.ROOT / 'deploy/podman/images.json').read_text())['postgres']
    made = []
    try:
        for kind in ('network', 'volume', 'container'):
            args = ['network', 'create'] if kind == 'network' else ['volume', 'create'] if kind == 'volume' else ['create', '--name', name]
            args += ['--label', 'io.runasmidja.qualification=' + owner]
            args += [image] if kind == 'container' else [name]
            podman(*args)
            made.append(kind)
            try:
                owned(kind, name, 'postgres')
            except RuntimeError:
                pass
            else:
                raise RuntimeError('Wrong-label real fixture accepted')
        with patch.dict(stack_resources.NAMES, {'postgres': name}):
            try:
                stop()
            except RuntimeError:
                pass
            else:
                raise RuntimeError('Stop accepted unowned fixture')
    finally:
        for kind in reversed(made):
            info = json.loads(podman(kind, 'inspect', name).stdout)[0]
            labels = info['Config']['Labels'] if kind == 'container' else info['labels'] if kind == 'network' else info['Labels']
            require(labels.get('io.runasmidja.qualification') == owner, 'Qualification cleanup ownership changed')
            podman(*(['rm', name] if kind == 'container' else [kind, 'rm', name]))
    print('Real wrong-label container/network/volume and stop denials: PASS')


def qualify():
    bootstrap_root = None
    if not (STATE / 'provision-role.json').exists():
        bootstrap_root = cold_start()
    else:
        print('Retained fixture: initial empty-state test belongs to the first qualification run.')
        stack.up()
    smoke()
    bad_ca()
    values = provisioning_values()
    require(runtime_values() == {k: values[k] for k in ('database_password', 'valkey_password')}, 'Runtime projection mismatch')
    podman('exec', '-i', NAMES['postgres'], 'psql', '-U', 'postgres', '-d', 'runasmidja', '-v', 'ON_ERROR_STOP=1',
        data='CREATE TABLE IF NOT EXISTS fixture_v02 (id integer PRIMARY KEY); INSERT INTO fixture_v02 VALUES (2) ON CONFLICT DO NOTHING;')
    stop()
    # An actual stopped vault must not resolve credentials from private delivery copies.
    try:
        provisioning_values()
    except urllib.error.URLError as error:
        require(isinstance(error.reason, ConnectionRefusedError), 'Outage test did not fail at the stopped vault connection')
    else:
        raise RuntimeError('Unavailable vault resolved credentials')
    no_consumers_running()
    # Neither the scoped provisioning nor runtime identity may use a local fallback.
    identity_path = STATE / 'runtime-role.json'
    original = read_private(identity_path)
    bad = json.loads(original)
    bad['secret_id'] = 'invalid-public-negative-fixture'
    replace_private(identity_path, json.dumps(bad))
    try:
        try:
            stack.up()
        except BaoError as error:
            require(error.status in (400, 403), 'Unexpected runtime-identity denial')
        else:
            raise RuntimeError('Denied runtime identity started consumers')
        no_consumers_running()
    finally:
        replace_private(identity_path, original)
    stack.up()
    require(provisioning_values() == values, 'Restart changed vault credential versions')
    present = podman('exec', NAMES['postgres'], 'psql', '-U', 'postgres', '-d', 'runasmidja', '-Atc',
                     'SELECT count(*) FROM fixture_v02 WHERE id=2').stdout.strip()
    require(present == '1', 'Restart lost database data')
    smoke()
    leakage(values, bootstrap_root)
    collisions()
    print('Real outage, root-revoked restart, version reuse and persistent PostgreSQL data: PASS')


if __name__ == '__main__':
    try:
        with fixture_lock():
            qualify()
    except (RuntimeError, KeyError, OSError, ValueError) as error:
        raise SystemExit(f'Service qualification failed ({type(error).__name__}); diagnostics withheld') from None
