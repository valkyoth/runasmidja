"""Local admission, transitive checks and same-repository containment."""
from test_workflow_policy import WorkflowFixture, workflow, ACTION, SHA
from workflow_policy import check
import unittest


class LocalWorkflowTests(WorkflowFixture, unittest.TestCase):
    def action(self, name='build', uses=ACTION):
        folder = self.root / '.github/actions' / name
        folder.mkdir(parents=True, exist_ok=True)
        (folder / 'action.yml').write_text('runs:\n  using: composite\n  steps:\n    - uses: ' + uses)
        return folder

    def admit(self, actions=(), workflows=()):
        self.policy.write_text('version = 1\n[local_actions]\n' +
                              ''.join(f'"{p}" = "reviewed test fixture"\n' for p in actions) +
                              '[local_workflows]\n' +
                              ''.join(f'"{p}" = "reviewed test fixture"\n' for p in workflows))

    def test_local_action_requires_review_and_recurses(self):
        self.action()
        self.verify(workflow('uses: ./.github/actions/build'), False)
        self.admit(actions=['./.github/actions/build'])
        self.verify(workflow('uses: ./.github/actions/build'), True)
        self.action(uses='evil/action@main')
        self.verify(workflow('uses: ./.github/actions/build'), False)

    def test_local_workflow_and_transitive_action(self):
        self.action()
        self.admit(actions=['./.github/actions/build'], workflows=['./.github/workflows/reuse.yaml'])
        (self.workflows / 'reuse.yaml').write_text(workflow('uses: ./.github/actions/build'))
        (self.workflows / 'ci.yml').write_text('jobs:\n  reuse:\n    uses: ./.github/workflows/reuse.yaml')
        self.assertEqual(check(self.root), [])
        self.action(uses='github/codeql-action/init@' + SHA)
        self.assertTrue(check(self.root))

    def test_local_cycles_and_depth(self):
        self.admit(actions=['./.github/actions/build'])
        self.action(uses='./.github/actions/build')
        self.verify(workflow('uses: ./.github/actions/build'), False)
        paths = ['./.github/actions/a' + str(i) for i in range(34)]
        self.admit(actions=paths)
        for i in range(34):
            self.action('a' + str(i), paths[i + 1] if i < 33 else ACTION)
        self.verify(workflow('uses: ' + paths[0]), False)

    def test_local_noncanonical_paths_and_missing_manifest(self):
        for value in ('./.github/actions/../build', './.github/actions//build',
                      './.github/actions/build/', './.github/actions/build@main',
                      './.github/actions/./build', './.github/actions/%2e%2e/build',
                      './outside', './.github/actions/build\\sub'):
            self.admit(actions=[value])
            self.verify(workflow('uses: ' + value), False)
        self.admit(actions=['./.github/actions/missing'])
        self.verify(workflow('uses: ./.github/actions/missing'), False)

    def test_local_symlink_and_ambiguous_manifest(self):
        folder = self.action()
        self.admit(actions=['./.github/actions/build'])
        (folder / 'action.yaml').write_text('runs: {}')
        self.verify(workflow('uses: ./.github/actions/build'), False)
        (folder / 'action.yaml').unlink()
        (folder / 'action.yml').unlink()
        (self.root / 'external.yml').write_text('runs: {}')
        (folder / 'action.yml').symlink_to(self.root / 'external.yml')
        self.verify(workflow('uses: ./.github/actions/build'), False)

    def test_unused_reviewed_action_is_still_checked(self):
        self.action(uses='evil/action@main')
        self.admit(actions=['./.github/actions/build'])
        self.verify(workflow('uses: ' + ACTION), False)

    def test_other_local_runtimes_not_admitted(self):
        folder = self.action()
        self.admit(actions=['./.github/actions/build'])
        for using in ('node24', 'docker', '${{ inputs.runtime }}'):
            (folder / 'action.yml').write_text('runs:\n  using: ' + using + '\n  main: code.js')
            self.verify(workflow('uses: ./.github/actions/build'), False)
