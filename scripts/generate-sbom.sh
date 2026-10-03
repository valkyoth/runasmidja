#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
cargo sbom --output-format cyclone_dx_json_1_5 > sbom/runasmidja.cdx.json
