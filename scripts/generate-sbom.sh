#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
cargo sbom --output-format cyclone_dx_json_1_5 > sbom/runasmidja.cdx.json
# Fixture OS/Go/C/native inventories are generated and gated by image_gate.py,
# retained locally under .local/image-evidence; review before copying public SBOMs.
# This Cargo inventory alone does not establish fixture supply-chain readiness.
