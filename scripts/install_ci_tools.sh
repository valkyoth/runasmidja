#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
task_dir=$(mktemp -d)
trap 'rm -rf "$task_dir"' EXIT
while read -r tool version digest; do
    curl --fail --silent --show-error --location --max-time 120 --max-filesize 16777216 "https://crates.io/api/v1/crates/$tool/$version/download" -o "$task_dir/$tool.crate"
    printf '%s  %s\n' "$digest" "$task_dir/$tool.crate" | sha256sum --check
    source_dir="$task_dir/$tool-$version"
    python3 scripts/tool_archive.py "$task_dir/$tool.crate" "$source_dir" "$tool" "$version"
    cargo fetch --locked --manifest-path "$source_dir/Cargo.toml"
    cargo install --locked --offline --path "$source_dir"
done < scripts/ci-tools.lock
