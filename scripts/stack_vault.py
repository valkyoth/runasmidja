"""OpenBao-first credential issuance with immutable fixture versions and scoped reads."""
import json
import re
from contextlib import contextmanager
from stack_common import STATE, BaoError, bao, private, read_private, replace_private, wait_for

KEYS = ('postgres_admin_password', 'database_password', 'valkey_password')
REVOKE = 'path "auth/token/revoke-self" { capabilities = ["update"] }\n'
POLICIES = {
    'provision': REVOKE + 'path "runasmidja/data/provisioning" { capabilities = ["read"] }\n'
                 + 'path "runasmidja/data/runtime" { capabilities = ["read"] }',
    'runtime': REVOKE + 'path "runasmidja/data/runtime" { capabilities = ["read"] }',
}


def checked_values(data, keys):
    if not isinstance(data, dict) or set(data) != set(keys):
        raise RuntimeError('Vault credential schema mismatch')
    if any(not isinstance(v, str) or not re.fullmatch('[0-9a-f]{64}', v) for v in data.values()):
        raise RuntimeError('Vault credential encoding/size mismatch')
    return data


def read_version(path, token, keys):
    document = bao('runasmidja/data/' + path, token=token)['data']
    meta = document['metadata']
    if type(meta['version']) is not int or meta['version'] != 1 or meta.get('destroyed') or meta.get('deletion_time'):
        raise RuntimeError('Fixture credential version changed or unavailable')
    return checked_values(document['data'], keys)


def create_once(path, values, root):
    # CAS=0 also refuses tombstones; absence is never permission to overwrite a version.
    try:
        return read_version(path, root, tuple(values))
    except BaoError as error:
        if error.status != 404:
            raise
    bao('runasmidja/data/' + path, {'options': {'cas': 0}, 'data': values}, root)
    return read_version(path, root, tuple(values))


def issue_credentials(root):
    try:
        values = read_version('provisioning', root, KEYS)
    except BaoError as error:
        if error.status != 404:
            raise
        values = {}
        for key in KEYS:
            values[key] = bao('sys/tools/random', {'bytes': 32, 'format': 'hex'}, root)['data']['random_bytes']
        checked_values(values, KEYS)
        values = create_once('provisioning', values, root)
    runtime = create_once('runtime', {k: values[k] for k in KEYS[1:]}, root)
    if runtime != {k: values[k] for k in KEYS[1:]}:
        raise RuntimeError('Vault credential projections disagree')


def configure(root):
    if 'file/' not in bao('sys/audit', token=root)['data']:
        raise RuntimeError('Required OpenBao audit is unavailable')
    mounts = bao('sys/mounts', token=root)['data']
    if 'runasmidja/' not in mounts:
        bao('sys/mounts/runasmidja', {'type': 'kv', 'options': {'version': '2'}}, root)
    elif mounts['runasmidja/']['type'] != 'kv' or mounts['runasmidja/']['options'].get('version') != '2':
        raise RuntimeError('Vault mount type drift')
    if 'approle/' not in bao('sys/auth', token=root)['data']:
        bao('sys/auth/approle', {'type': 'approle'}, root)
    for role, policy in POLICIES.items():
        bao('sys/policies/acl/runasmidja-' + role, {'policy': policy}, root, 'PUT')
        bao('auth/approle/role/runasmidja-' + role, {
            'token_policies': ['runasmidja-' + role], 'token_ttl': '15m',
            'token_max_ttl': '1h', 'secret_id_ttl': '24h', 'secret_id_num_uses': 0,
            'token_no_default_policy': True}, root)
    issue_credentials(root)
    for role in POLICIES:
        path = STATE / (role + '-role.json')
        if not path.exists():
            prefix = 'auth/approle/role/runasmidja-' + role
            role_id = bao(prefix + '/role-id', token=root)['data']['role_id']
            secret_id = bao(prefix + '/secret-id', {}, root)['data']['secret_id']
            private(path, json.dumps({'role_id': role_id, 'secret_id': secret_id}))
    references = {'schema': 2, 'provisioning': {'path': 'runasmidja/data/provisioning', 'version': 1},
                  'runtime': {'path': 'runasmidja/data/runtime', 'version': 1}}
    path = STATE / 'references.json'
    if not path.exists():
        private(path, json.dumps(references))
    elif json.loads(read_private(path)) != references:
        raise RuntimeError('Vault credential reference drift')


def bootstrap():
    wait_for(lambda: bao('sys/init'))
    checkpoint = STATE / 'bootstrap.json'
    recovery = STATE / 'recovery.json'
    if not bao('sys/init')['initialized']:
        if checkpoint.exists() or recovery.exists():
            raise RuntimeError('Vault data missing with retained custody; refusing reinitialization')
        result = bao('sys/init', {'secret_shares': 1, 'secret_threshold': 1})
        # Single atomic checkpoint first; interrupted custody never silently resets a vault.
        private(checkpoint, json.dumps(result))
    if checkpoint.exists():
        result = json.loads(read_private(checkpoint))
        if 'keys_base64' in result:
            if not recovery.exists():
                private(recovery, json.dumps({'keys_base64': result['keys_base64']}))
            replace_private(checkpoint, json.dumps({'root_token': result['root_token']}))
    if not recovery.exists():
        raise RuntimeError('Vault recovery custody missing; refusing reset')
    status = bao('sys/seal-status')
    if status['sealed']:
        key = json.loads(read_private(recovery))['keys_base64'][0]
        bao('sys/unseal', {'key': key})
    if bao('sys/seal-status')['sealed']:
        raise RuntimeError('Vault remains sealed; dependent startup denied')
    root = json.loads(read_private(checkpoint)).get('root_token') if checkpoint.exists() else None
    if root:
        try:
            configure(root)
        except BaoError as error:
            # Revocation may have succeeded immediately before a custody-write interruption.
            if error.status != 403:
                raise
            try:
                bao('auth/token/lookup-self', token=root)
            except BaoError as lookup:
                if lookup.status != 403:
                    raise
            else:
                raise error  # valid root means a real denial: fail closed
    return root


@contextmanager
def identity(role):
    credentials = json.loads(read_private(STATE / (role + '-role.json')))
    token = bao('auth/approle/login', credentials)['auth']['client_token']
    try:
        yield token
    finally:
        bao('auth/token/revoke-self', {}, token)


def provisioning_values():
    with identity('provision') as token:
        values = read_version('provisioning', token, KEYS)
        runtime = read_version('runtime', token, KEYS[1:])
        if runtime != {k: values[k] for k in KEYS[1:]}:
            raise RuntimeError('Vault runtime projection mismatch')
        return values


def runtime_values():
    with identity('runtime') as token:
        return read_version('runtime', token, KEYS[1:])


def revoke_root(root):
    if root:
        try:
            bao('auth/token/revoke-self', {}, root)
        except BaoError as error:
            if error.status != 403:
                raise
        try:
            bao('auth/token/lookup-self', token=root)
        except BaoError as error:
            if error.status != 403:
                raise
        else:
            raise RuntimeError('Bootstrap root revocation not confirmed')
        (STATE / 'bootstrap.json').unlink()
