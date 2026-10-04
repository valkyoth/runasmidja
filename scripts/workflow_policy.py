"""Validate executable reference positions, not comments or arbitrary YAML text."""
import tomllib
from itertools import islice
from pathlib import Path
from workflow_yaml import load, MAX_BYTES
import yaml
from workflow_references import reference, local_path, container

MAX_DOCUMENTS = 128
MAX_LOCAL_DEPTH = 32


def mapping(value, label):
    if not isinstance(value, dict):
        raise ValueError(label + ' must be a mapping')
    return value


def load_policy(root):
    path = root / '.github/workflow-policy.toml'
    if path.is_symlink() or not path.is_file():
        raise ValueError('workflow policy must be a regular file')
    with path.open('rb') as stream:
        raw = stream.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise ValueError('workflow policy exceeds byte limit')
    policy = tomllib.loads(raw.decode('utf-8'))
    if set(policy) != {'version', 'local_actions', 'local_workflows'} or type(policy['version']) is not int or policy['version'] != 1:
        raise ValueError('unsupported workflow policy schema')
    for kind in ('local_actions', 'local_workflows'):
        for name, reason in mapping(policy[kind], kind).items():
            if not name.startswith('./') or not isinstance(reason, str) or not reason.strip():
                raise ValueError('local admission needs a canonical path and review reason')
            local_path(root, name, 'action' if kind == 'local_actions' else 'workflow')
    return policy


class Admission:
    def __init__(self, root, policy):
        self.root, self.policy = root, policy
        self.active = set()
        self.done = set()

    def uses(self, value, kind, depth):
        value, category = reference(value, kind)
        if category != 'local':
            return
        table = self.policy['local_actions' if kind == 'action' else 'local_workflows']
        if value not in table:
            raise ValueError('local reference is not explicitly reviewed: ' + value)
        target = local_path(self.root, value, kind)
        self.document(target, kind, depth + 1)

    def steps(self, steps, depth):
        if not isinstance(steps, list) or not steps:
            raise ValueError('steps must be a nonempty sequence')
        for step in steps:
            step = mapping(step, 'step')
            if ('uses' in step) == ('run' in step):
                raise ValueError('step needs exactly one of run or uses')
            if 'uses' in step:
                self.uses(step['uses'], 'action', depth)
            elif not isinstance(step['run'], str) or not step['run'].strip():
                raise ValueError('run must be a nonempty string')

    def workflow(self, data, depth):
        jobs = mapping(data.get('jobs'), 'jobs')
        if not jobs:
            raise ValueError('workflow needs jobs')
        for job in jobs.values():
            job = mapping(job, 'job')
            if 'uses' in job:
                if any(key in job for key in ('steps', 'runs-on', 'container', 'services')):
                    raise ValueError('reusable workflow job cannot also execute steps/containers')
                self.uses(job['uses'], 'workflow', depth)
                continue
            self.steps(job.get('steps'), depth)
            if 'container' in job:
                image = job['container']
                container(image.get('image') if isinstance(image, dict) else image)
            if 'services' in job:
                for service in mapping(job['services'], 'services').values():
                    container(mapping(service, 'service').get('image'))

    def document(self, path, kind='workflow', depth=0):
        if depth > MAX_LOCAL_DEPTH:
            raise ValueError('local reference depth exceeded')
        if path in self.active:
            raise ValueError('cyclic local workflow/action reference')
        if path in self.done:
            return
        if len(self.done) + len(self.active) >= MAX_DOCUMENTS:
            raise ValueError('workflow document budget exceeded')
        if path.is_symlink() or not path.is_file():
            raise ValueError('workflow/action must be a regular file')
        self.active.add(path)
        data = mapping(load(path), 'document')
        if kind == 'workflow':
            self.workflow(data, depth)
        else:
            runs = mapping(data.get('runs'), 'action runs')
            if runs.get('using') != 'composite':
                raise ValueError('only reviewed local composite actions are admitted')
            self.steps(runs.get('steps'), depth)
        self.active.remove(path)
        self.done.add(path)


def check(root):
    root = Path(root)
    directory = root / '.github/workflows'
    try:
        if (root / '.github').is_symlink() or directory.is_symlink():
            raise ValueError('workflow directory cannot be a symlink')
        if not directory.exists():
            return []
        policy = load_policy(root)
        admission = Admission(root, policy)
        count = 0
        for path in sorted(islice(directory.iterdir(), MAX_DOCUMENTS + 1)):
            count += 1
            if count > MAX_DOCUMENTS:
                raise ValueError('workflow directory entry budget exceeded')
            if path.suffix in ('.yml', '.yaml'):
                admission.document(path)
        # Admitted but currently unused local code is checked as well.
        for table, kind in (('local_actions', 'action'), ('local_workflows', 'workflow')):
            for value in policy[table]:
                admission.document(local_path(root, value, kind), kind)
    except (ValueError, OSError, UnicodeError, yaml.YAMLError, RecursionError) as error:
        return ['Workflow policy: ' + str(error)]
    return []


if __name__ == '__main__':
    errors = check(Path(__file__).resolve().parent.parent)
    if errors:
        raise SystemExit('\n'.join(errors))
    print('Workflow reference policy: PASS')
