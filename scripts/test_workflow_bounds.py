"""Additional parser, graph, and container boundary regressions."""
import unittest
from unittest.mock import patch
from test_workflow_policy import WorkflowFixture, workflow, ACTION, DIGEST
from workflow_policy import check
from workflow_references import reference


class WorkflowBoundaryTests(WorkflowFixture, unittest.TestCase):
    def test_nested_escaped_duplicate_and_tag_rejection(self):
        for source in ('jobs: {build: {steps: [{uses: "' + ACTION + '", "us\\x65s": bad}]}}',
                       'jobs: {build: {steps: [!!map {uses: "' + ACTION + '"}]}}',
                       '%TAG !e! tag:example.com,2026:\n---\njobs: {}',
                       'jobs: {build: {steps: [&step {uses: "' + ACTION + '"}, *step]}}'):
            self.verify(source, False)

    def test_unknown_directive_rejects_without_rejecting_scalar_text(self):
        self.verify('%IGNORED anything\n---\n' + workflow('uses: ' + ACTION), False)
        self.verify(workflow('run: |\n          echo %IGNORED anything'), True)

    def test_unquoted_on_key_preserved(self):
        from workflow_yaml import load
        path = self.root / 'fixture.yml'
        path.write_text('on: push\ntrue: false\n1: 2\n')
        self.assertEqual(load(path), {'on': 'push', 'true': 'false', '1': '2'})

    def test_container_repository_grammar(self):
        for image in ('localhost:5000/team/image', 'registry.example/team/image', 'alpine',
                      'ghcr.io/owner/some_image'):
            self.verify(workflow('uses: docker://' + image + '@sha256:' + DIGEST), True)
        for image in ('https://example/image', 'a::::b', 'a//b', 'a/../b', 'a/b:latest',
                      'registry:999999/team/image', '-a', 'a/', 'A/b'):
            self.verify(workflow('uses: docker://' + image + '@sha256:' + DIGEST), False)

    def test_directory_symlink_rejection(self):
        self.workflows.rmdir()
        outside = self.root / 'elsewhere'
        outside.mkdir()
        self.workflows.symlink_to(outside, target_is_directory=True)
        self.assertTrue(check(self.root))

    def test_policy_symlink_rejection(self):
        original = self.policy.read_bytes()
        self.policy.unlink()
        target = self.root / 'policy.toml'
        target.write_bytes(original)
        self.policy.symlink_to(target)
        self.assertTrue(check(self.root))

    def test_exact_byte_boundary(self):
        from workflow_yaml import MAX_BYTES
        source = workflow('uses: ' + ACTION)
        self.verify(source + '#' + 'a' * (MAX_BYTES - len(source) - 1), True)
        self.verify(source + '#' + 'a' * (MAX_BYTES - len(source)), False)

    def test_token_limit_rejects(self):
        with patch('workflow_yaml.MAX_TOKENS', 10):
            self.verify(workflow('uses: ' + ACTION), False)

    def test_read_failure_is_not_success(self):
        with patch('workflow_policy.load_policy', side_effect=PermissionError('denied')):
            self.assertTrue(check(self.root))

    def test_reusable_workflow_cycles(self):
        self.policy.write_text('version = 1\n[local_actions]\n[local_workflows]\n'
                              '"./.github/workflows/a.yml" = "test cycle"\n'
                              '"./.github/workflows/b.yaml" = "test cycle"\n')
        (self.workflows / 'a.yml').write_text('jobs: {x: {uses: ./.github/workflows/b.yaml}}')
        (self.workflows / 'b.yaml').write_text('jobs: {x: {uses: ./.github/workflows/a.yml}}')
        self.assertTrue(check(self.root))

    def test_codeql_in_remote_reusable_reference_rejects(self):
        with self.assertRaisesRegex(ValueError, 'CodeQL'):
            reference('github/codeql-action/.github/workflows/build.yml@' + 'a' * 40, 'workflow')

    def test_depth_boundary_and_event_exhaustion_report_specific_reason(self):
        from workflow_yaml import load
        path = self.root / 'limits.yml'
        path.write_text('extra: ' + '[' * 39 + 'x' + ']' * 39)
        self.assertIn('extra', load(path))
        path.write_text('extra: ' + '[' * 40 + 'x' + ']' * 40)
        with self.assertRaisesRegex(ValueError, 'depth limit'):
            load(path)
        path.write_text('[' + ','.join(['x'] * 20_000) + ']')
        with patch('workflow_yaml.MAX_TOKENS', 100_000):
            with self.assertRaisesRegex(ValueError, 'event limit'):
                load(path)

    def test_invalid_utf8_is_rejected(self):
        (self.workflows / 'ci.yaml').write_bytes(b'jobs: \xff')
        self.assertTrue(check(self.root))

    def test_local_action_parent_symlink_rejects(self):
        target = self.root / 'action-directory'
        target.mkdir()
        (target / 'action.yaml').write_text('runs: {using: composite, steps: [{run: true}]}')
        actions = self.root / '.github/actions'
        actions.mkdir()
        (actions / 'link').symlink_to(target, target_is_directory=True)
        self.policy.write_text('version = 1\n[local_actions]\n'
                              '"./.github/actions/link" = "review fixture"\n[local_workflows]\n')
        self.verify(workflow('uses: ./.github/actions/link'), False)

    def test_tool_pin_matches_parser_and_hashes_are_required(self):
        from pathlib import Path
        import re
        from workflow_yaml import VERSION
        root = Path(__file__).resolve().parent.parent
        lock = (root / 'scripts/python-tools.lock').read_text()
        self.assertIn('PyYAML==' + VERSION, lock)
        self.assertGreater(len(re.findall(r'--hash=sha256:[0-9a-f]{64}', lock)), 0)
        import json
        inventory = json.loads((root / 'sbom/workflow-tooling.cdx.json').read_text())
        self.assertEqual(inventory['components'][0]['name'], 'PyYAML')
        self.assertEqual(inventory['components'][0]['version'], VERSION)
