"""Two exact reviewed cache images; rollback is explicit, never an arbitrary override."""
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def profile():
    value = os.environ.get('RUNASMIDJA_VALKEY_PROFILE', 'wolfi')
    if value not in ('wolfi', 'official'):
        raise RuntimeError('Unknown Valkey image profile')
    return value


def rules():
    return json.loads((ROOT / 'deploy/podman/image-policy.json').read_text())


ROLLBACK_INSTANCE = 'v02-admission-ready'


def require_rollback(instance):
    if instance != ROLLBACK_INSTANCE:
        raise RuntimeError('Official Valkey image is restricted to the preserved rollback stack')


def selected_image(instance):
    selected = profile()
    if selected == 'official':
        require_rollback(instance)
    policy = rules()
    return policy['valkey' if selected == 'wolfi' else 'valkey-official']['image']


def admission_policy(images, policy):
    """The old exact digest keeps only its own exception, never the Wolfi policy."""
    image = images['valkey']
    if image == policy['valkey']['image']:
        return policy
    if image == policy['valkey-official']['image']:
        from stack_common import INSTANCE
        require_rollback(INSTANCE)
        return {**policy, 'valkey': policy['valkey-official']}
    raise RuntimeError('Valkey image has no admitted profile')


def arguments(image):
    policy = rules()
    if image == policy['valkey']['image']:
        return ['/config/valkey.conf']  # upstream entrypoint is /usr/bin/valkey-server
    if image == policy['valkey-official']['image']:
        from stack_common import INSTANCE
        require_rollback(INSTANCE)
        return ['valkey-server', '/config/valkey.conf']  # upstream entrypoint wrapper
    raise RuntimeError('Valkey entrypoint has no admitted profile')
