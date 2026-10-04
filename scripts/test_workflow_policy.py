"""Adversarial executable-reference tests independent of policy implementation."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from workflow_policy import check

SHA = '1234567890abcdef1234567890abcdef12345678'
DIGEST = '1234567890abcdef' * 4
ACTION = 'actions/checkout@' + SHA
WORKFLOW = 'owner/repo/.github/workflows/build.yaml@' + SHA
POLICY = 'version = 1\n[local_actions]\n[local_workflows]\n'


def workflow(step):
    return 'on: push\njobs:\n  build:\n    runs-on: ubuntu-latest\n    steps:\n      - ' + step + '\n'


class WorkflowFixture:
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.root = Path(self.folder.name)
        self.workflows = self.root / '.github/workflows'
        self.workflows.mkdir(parents=True)
        self.policy = self.root / '.github/workflow-policy.toml'
        self.policy.write_text(POLICY)

    def verify(self, source, valid, suffix='.yml'):
        for existing in self.workflows.iterdir():
            existing.unlink()
        (self.workflows / ('ci' + suffix)).write_text(source)
        errors = check(self.root)
        self.assertEqual(not errors, valid, errors or source)


class WorkflowTests(WorkflowFixture, unittest.TestCase):
    def test_both_suffixes_and_scalar_representations(self):
        for suffix in ('.yml', '.yaml'):
            for key in ('uses', '"uses"', "'uses'", '"us\\u0065s"'):
                for value in (ACTION, repr(ACTION), '"' + ACTION + '"', '|\n          ' + ACTION,
                              '>\n          ' + ACTION, '>\n          actions/checkout@main'):
                    with self.subTest(suffix=suffix, key=key, value=value):
                        self.verify(workflow(key + ': ' + value), '@main' not in value, suffix)

    def test_flow_mapping_and_escaped_key(self):
        self.verify('jobs: {build: {steps: [{"us\\u0065s": "' + ACTION + '"}]}}', True)
        self.verify('jobs: {build: {steps: [{"uses": "actions/checkout@main"}]}}', False)

    def test_remote_pins_and_malformed_values(self):
        for value in ('actions/checkout@main', 'actions/checkout@v1', 'actions/checkout@1234567',
                      'actions/checkout@' + 'a' * 41, 'actions/checkout@' + 'g' * 40,
                      'actions/checkout@' + 'A' * 40, 'https://github.com/' + ACTION,
                      'owner/repo/../action@' + SHA, 'owner//repo@' + SHA,
                      'owner/repo@' + SHA + '@main', '', '{}', '[]',
                      'owner/repo@${{ inputs.ref }}', '${{ matrix.action }}',
                      '"' + ACTION + ' "', '"actions/checkout@\\n' + SHA + '"'):
            with self.subTest(value=value):
                self.verify(workflow('uses: ' + value), False)
        self.verify(workflow('uses: owner/repo/sub/action@' + SHA), True)

    def test_unrelated_strings_and_comments_are_not_references(self):
        self.verify('name: CodeQL migration notes\n# uses: actions/foo@main\n' +
                    workflow('run: |\n          echo "uses: actions/foo@main"\n          echo codeql') +
                    '        env:\n          uses: actions/not-an-action@main\n', True)
        self.verify(workflow('uses: ' + ACTION + '\n        with:\n          uses: example@main'), True)

    def test_codeql_reference_denied_not_unrelated_name(self):
        for suffix in ('.yml', '.yaml'):
            for ref in ('github/codeql-action/init@', 'GitHub/CodeQL-Action/analyze@',
                        'github/codeql-action@'):
                self.verify(workflow('uses: "' + ref + SHA + '"'), False, suffix)
        self.verify(workflow('uses: owner/codeql-documentation@' + SHA), True)

    def test_reusable_workflows(self):
        for value, valid in ((WORKFLOW, True), ('"' + WORKFLOW + '"', True),
                             (WORKFLOW.replace('@' + SHA, '@main'), False),
                             (ACTION, False), ('owner/repo/folder/build.yml@' + SHA, False),
                             ('docker://alpine@sha256:' + DIGEST, False),
                             ('${{ inputs.workflow }}', False)):
            self.verify('jobs:\n  reuse:\n    uses: ' + value, valid)
        self.verify('jobs:\n  reuse:\n    uses: ' + WORKFLOW + '\n    steps: []', False)

    def test_container_step_job_and_service(self):
        image = 'ghcr.io/owner/image@sha256:' + DIGEST
        for value, valid in ((image, True), ('alpine:latest', False), ('alpine@sha256:abc', False),
                             ('${{ matrix.image }}', False), ('alpine@sha256:' + 'G' * 64, False)):
            self.verify(workflow('uses: docker://' + value), valid)
            self.verify(workflow('run: true') + '    container: ' + value + '\n', valid)
            self.verify(workflow('run: true') + '    container:\n      image: ' + value + '\n', valid)
            self.verify(workflow('run: true') + '    services:\n      cache:\n        image: ' + value, valid)

    def test_yaml_ambiguities_and_invalid_structure(self):
        cases = ['jobs: {}\njobs: {}', 'jobs: {x: {steps: [{uses: ' + ACTION + ', uses: bad}]}}',
                 'jobs: {x: {steps: [{"uses": good, "us\\u0065s": bad}]}}',
                 'jobs: &jobs {}', 'jobs: *missing', 'jobs: {<<: {}}',
                 '!!python/object:thing {}', '!!map {}', '%YAML 1.1\n---\njobs: {}',
                 '---\njobs: {}\n---\njobs: {}', 'jobs: [', '[]', '', 'null',
                 'jobs: {}', 'jobs: []', 'jobs: {x: []}', '? [jobs]\n: {}',
                 'jobs: {x: {steps: []}}', 'jobs: {x: {steps: [{run: x, uses: bad}]}}',
                 'jobs: {x: {steps: [{name: missing}]}}']
        for source in cases:
            with self.subTest(source=source):
                self.verify(source, False)

    def test_byte_depth_and_event_budgets(self):
        self.verify('#' + 'a' * (128 * 1024), False)
        self.verify('x: ' + '[' * 45 + 'x' + ']' * 45, False)
        self.verify('x: [' + ','.join(['a'] * 20_000) + ']', False)

    def test_parser_version_mismatch_fails(self):
        with patch('workflow_yaml.yaml.__version__', '0.0.0'):
            self.verify(workflow('uses: ' + ACTION), False)

    def test_workflow_symlink_rejects(self):
        (self.root / 'outside.yml').write_text(workflow('uses: ' + ACTION))
        (self.workflows / 'ci.yaml').symlink_to(self.root / 'outside.yml')
        self.assertTrue(check(self.root))

    def test_policy_required_and_schema_checked(self):
        (self.workflows / 'ci.yaml').write_text(workflow('uses: ' + ACTION))
        for content in ('', 'version = 2', POLICY + '\nunknown = "x"',
                        POLICY.replace('version = 1', 'version = true'),
                        POLICY.replace('[local_actions]', 'local_actions = []')):
            self.policy.write_text(content)
            self.assertTrue(check(self.root), content)
        self.policy.unlink()
        self.assertTrue(check(self.root))

    def test_document_budget(self):
        for number in range(129):
            (self.workflows / f'{number}.yaml').write_text(workflow('uses: ' + ACTION))
        self.assertTrue(check(self.root))


if __name__ == '__main__':
    unittest.main()
