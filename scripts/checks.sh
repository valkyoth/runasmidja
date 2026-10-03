#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/check_repository.py
cargo fmt --all -- --check
cargo clippy --locked --workspace --all-targets --all-features -- -D warnings
cargo test --locked --workspace
cargo test --locked --workspace --release
cargo test --locked --workspace --all-features
cargo doc --locked --workspace --no-deps
scripts/check_no_std.sh
python3 -m unittest discover -s scripts -p 'test_*.py'
