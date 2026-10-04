"""AST guardrail against introducing raw host Podman command paths."""
import ast
from pathlib import Path


def violations(source, name):
    tree = ast.parse(source)
    errors = []
    parents = {child: parent for parent in ast.walk(tree) for child in ast.iter_child_nodes(parent)}

    class Commands(ast.NodeVisitor):
        function = None

        def visit_FunctionDef(self, node):
            previous = self.function
            self.function = node.name
            self.generic_visit(node)
            self.function = previous

        def visit_Constant(self, node):
            value = node.value
            if not isinstance(value, str):
                return
            # Catch direct executable strings and simple shell commands, including
            # assignment/alias/list forms rather than only subprocess call syntax.
            words = value.strip().split()
            if not words or Path(words[0]).name != 'podman':
                return
            if name == 'podman_policy.py' and isinstance(parents.get(node), ast.Compare):
                return  # this checker compares executable names; it executes none
            if name == 'podman_guard.py':
                return
            if name == 'build_sandbox.py' and self.function == 'worker':
                return  # namespace-only child; parent guard + UID map/cgroup checks
            errors.append(f'{name}:{node.lineno}: raw host Podman command bypasses shared guard')

    Commands().visit(tree)
    return errors


def check(root):
    errors = []
    for path in (root / 'scripts').glob('*.py'):
        if not path.name.startswith('test_'):
            errors.extend(violations(path.read_text(), path.name))
    return errors
