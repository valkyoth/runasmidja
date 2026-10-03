#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
task_dir=$(mktemp -d)
trap 'rm -rf "$task_dir"' EXIT
while read -r tool version digest; do
    curl --fail --silent --show-error --location "https://crates.io/api/v1/crates/$tool/$version/download" -o "$task_dir/$tool.crate"
    printf '%s  %s\n' "$digest" "$task_dir/$tool.crate" | sha256sum --check
    cargo install --locked "$tool" --version "=$version"
done < scripts/ci-tools.lock
