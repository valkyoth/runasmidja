#!/usr/bin/env python3
"""Validate file limits, portable graph, documentation links and workflow pins."""
import json
import re
import subprocess
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def check(root=ROOT):
    errors = []
    for base in (root,):
        for path in base.rglob("*"):
            if any(part in {"target", ".git", ".local", "__pycache__", ".cargo-deny-advisory-dbs"} for part in path.parts):
                continue
            if path.suffix not in {".rs", ".py", ".sh", ".yml", ".yaml", ".toml", ".js", ".ts", ".css", ".html"}:
                continue
            content = path.read_text()
            if len(content.splitlines()) > 500:
                errors.append(f"{path}: exceeds 500 lines")
            if path.suffix == ".yml":
                for action in re.findall(r"uses:\s*([^\s#]+)", content):
                    if not re.fullmatch(r"[^@]+@[0-9a-f]{40}", action):
                        errors.append(f"{path}: unpinned action {action}")
                if "codeql" in content.lower():
                    errors.append(f"{path}: CodeQL must use GitHub Default setup")
    for path in root.rglob("*.md"):
        if any(part in {"target", ".git", ".local", ".cargo-deny-advisory-dbs"} for part in path.parts):
            continue
        for target in re.findall(r"\[[^\]]*\]\((<[^>\n]+>|[^\s)]+)\)", path.read_text()):
            if target.startswith('<') and target.endswith('>'):
                target = target[1:-1]
            if target.startswith(("http:", "https:", "#", "mailto:")):
                continue
            if not (path.parent / target.split("#", 1)[0]).exists():
                errors.append(f"{path}: missing link {target}")
    for manifest in (root / "crates").glob("*/Cargo.toml"):
        config = tomllib.loads(manifest.read_text())
        if config.get("package", {}).get("name") == "runasmidja-server":
            continue
        source = manifest.parent / "src/lib.rs"
        if "#![no_std]" not in source.read_text():
            errors.append(f"{source}: missing no_std")
        for dependency in config.get("dependencies", {}).values():
            if not isinstance(dependency, dict) or "path" not in dependency:
                errors.append(f"{manifest}: external dependency in portable foundation")
    return errors

if __name__ == "__main__":
    issues = check()
    if issues:
        raise SystemExit("\n".join(issues))
    metadata = json.loads(subprocess.check_output(["cargo", "metadata", "--locked", "--offline", "--format-version", "1"], cwd=ROOT))
    if len(metadata["packages"]) != len(metadata["workspace_members"]):
        raise SystemExit("Unexpected external dependency; review admission policy")
    print("Repository policy: PASS")
