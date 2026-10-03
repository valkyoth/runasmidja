# Fixture image inventories

These CycloneDX reports cover the exact Linux/amd64 runtime images selected by
[images.json](../../deploy/podman/images.json), plus their Wolfi build base. They
supplement the separate Cargo-only inventory. The local PostgreSQL marker
resolves to the immutable image ID bound by the private build receipt.

Scanned on 2026-10-03 using reviewed Trivy 0.75.0, with `--scanners vuln`,
HIGH/CRITICAL severity, unfixed findings included and no ignore/VEX policy.
The database was updated at 2026-10-03T14:28:08Z and downloaded at 17:22:49Z.

| Image | Inventory components | Reported HIGH/CRITICAL findings | Execution disposition |
| --- | --- | --- | --- |
| OpenBao | 322 | 0 | Signed index binds exact platform leaf |
| Wolfi/PostgreSQL | 24 | 0 | Authorized public-source build; local archive/config/layer binding |
| Valkey | 24 | 0 | Exact unsigned-image exception approved by maintainer |
| Wolfi base | 20 | 0 | Signed Chainguard index binds exact platform leaf |
| Original official PostgreSQL (historical) | 151 | 42 | BLOCKED; not executed by current fixture |

The qualified local PostgreSQL image ID is
`sha256:1144c0946e8ac0ef9cd2f6fddd6a71e59ba2ad3ca83e25440c1fcd136bdab3bf`.
Its scanned Docker archive SHA-256 is
`37dbebeb0290dcb93b1b812565e689d4abd0c0d3225776f99244a3f8a422ef06`.
The [recipe/source pins](../../deploy/podman/postgres/README.md) describe official
source custody, base publisher verification, current signed APK dependencies,
runtime configuration and the trusted-host receipt limitation. Builds are not
claimed bit-for-bit reproducible or publisher-signed portable artifacts.

The PostgreSQL application is explicitly recorded with the official source hash
and license; Trivy inventories the runtime OS libraries but does not automatically
analyze advisories for compiled PostgreSQL C source. Official upstream security
and release review remains necessary. A zero scanner result is not a pentest PASS.

The original blocked scan is retained in
[postgres-official-blocked-2026-10-03.cdx.json](postgres-official-blocked-2026-10-03.cdx.json).
No CVE waiver, ignore/VEX filter or reachability-based suppression is admitted.
The original provenance exception did not waive those findings.

Run `python3 scripts/install_image_tools.py`, then `python3 scripts/image_gate.py`
to regenerate reports in ignored `.local/image-evidence`. Startup always rescans.
CI retains reports as a 30-day artifact even when qualification fails. Committed
snapshots are evidence for these specific images and scanner database, not future
rebuilds or advisory databases.
