#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
for crate in runasmidja runasmidja-core runasmidja-ports runasmidja-html runasmidja-crypto; do
    cargo check --locked -p "$crate" --no-default-features --target thumbv7em-none-eabihf
    cargo check --locked -p "$crate" --no-default-features --target wasm32-unknown-unknown
done
