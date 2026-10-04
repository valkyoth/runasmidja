"""Platform-setting denials and minimal workflow bootstrap ordering regressions."""
import json
import subprocess
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import check_github_policy as policy
from workflow_yaml import load

ROOT = Path(__file__).resolve().parent.parent
GOOD = {'enabled': True, 'sha_pinning_required': True, 'allowed_actions': 'all'}


class GitHubPolicyTests(unittest.TestCase):
    def test_platform_setting_requires_boolean_true(self):
        policy.validate(GOOD)
        for field in ('enabled', 'sha_pinning_required'):
            for value in (False, None, 'true', 1, [], {}):
                data = dict(GOOD, **{field: value})
                with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                    policy.validate(data)
            data = dict(GOOD); del data[field]
            with self.assertRaises(ValueError): policy.validate(data)
        for value in (None, [], 'true', {}):
            with self.assertRaises(ValueError): policy.validate(value)

    def test_allowlist_can_be_more_restrictive(self):
        for mode in ('all', 'selected', 'local_only'):
            policy.validate(dict(GOOD, allowed_actions=mode))
        for mode in ('unknown', None, ''):
            with self.assertRaises(ValueError): policy.validate(dict(GOOD, allowed_actions=mode))

    def test_live_checker_is_read_only_and_fails_closed(self):
        with patch.object(policy.subprocess, 'run', return_value=SimpleNamespace(stdout=json.dumps(GOOD))) as run:
            policy.check()
            args, options = run.call_args
            self.assertEqual(args[0], ['gh', 'api', '--hostname', 'github.com', policy.ENDPOINT])
            self.assertTrue(options['check'])
            self.assertEqual(options['timeout'], 30)
        for output in ('{', '{}', json.dumps(dict(GOOD, sha_pinning_required=False))):
            with patch.object(policy.subprocess, 'run', return_value=SimpleNamespace(stdout=output)):
                with self.assertRaises(ValueError): policy.check()
        for error in (subprocess.CalledProcessError(1, 'gh'), subprocess.TimeoutExpired('gh', 30)):
            with patch.object(policy.subprocess, 'run', side_effect=error):
                with self.assertRaises(type(error)): policy.check()

    def test_current_workflows_validate_before_workload(self):
        # Single-job contract: adding independent jobs requires explicit review
        # and a needs dependency on a minimal policy job before this test changes.
        paths = sorted((ROOT / '.github/workflows').glob('*.y*ml'))
        self.assertEqual({p.name for p in paths}, {'ci.yml', 'freshness.yml', 'release.yml'})
        for path in paths:
            with self.subTest(path=path.name):
                data = load(path)
                self.assertEqual(data['permissions'], {'contents': 'read'})
                self.assertEqual(len(data['jobs']), 1)
                job = next(iter(data['jobs'].values()))
                self.assertNotIn('uses', job)
                self.assertNotIn('container', job)
                self.assertNotIn('services', job)
                steps = job['steps']
                self.assertEqual(steps[0]['uses'], 'actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1')
                self.assertEqual(steps[0]['with']['persist-credentials'], 'false')
                self.assertEqual(steps[1], {'run': 'scripts/install_python_tools.sh'})
                self.assertEqual(steps[2], {'run': '.local/check-tools/bin/python3 scripts/workflow_policy.py'})
                self.assertLessEqual(int(job['timeout-minutes']), 15)
