# Fixture image inventories

These CycloneDX reports cover the exact Linux/amd64 runtime images selected by
[images.json](../../deploy/podman/images.json), plus their Wolfi build base. They
supplement the separate Cargo-only inventory. The local PostgreSQL marker
resolves to the immutable image ID bound by the private build receipt.

Current images scanned on 2026-10-04 using reviewed Trivy 0.75.0, with
`--scanners vuln`, UNKNOWN/HIGH/CRITICAL severity, unfixed findings included and
no ignore/VEX policy. The historical official PostgreSQL report retains its
2026-10-03 HIGH/CRITICAL scan; it was not regenerated or admitted.
The database was updated at 2026-10-03T14:28:08Z and downloaded at 17:22:49Z.

| Image | Inventory components | Reported findings | Execution disposition |
| --- | --- | --- | --- |
| OpenBao | 322 | 1 UNKNOWN, 0 HIGH/CRITICAL | Signed index; retained exact-image not-affected review, expires 2026-11-02 |
| Wolfi/PostgreSQL | 24 | 0 | Authorized public-source build; local archive/config/layer binding |
| Valkey | 24 | 0 | Exact unsigned-image exception approved by maintainer |
| Wolfi base | 20 | 0 | Signed Chainguard index binds exact platform leaf |
| Original official PostgreSQL (historical) | 151 | 42 HIGH/CRITICAL | BLOCKED; not executed by current fixture |

The qualified local PostgreSQL image ID is
`sha256:ff0f7c9071b8bcbf0d58c52f365853deed5cf5c097560b95023be46aba91f4a9`.
Its scanned Docker archive SHA-256 is
`1a219e5b8cfc3ab417f77b859b079991df81f6158171f572fba67b7d3d3fe3ab`.
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
No CVE waiver or ignore/VEX filter is admitted. OpenBao's UNKNOWN
[GO-2026-5932 review](../../security/advisories/README.md) binds the pinned binary's
complete affected-package absence inventory, exact module/version and expiring
evidence. The advisory remains visible; it is not blanket-ignored. The original
PostgreSQL provenance exception did not waive its findings.

Run `python3 scripts/install_image_tools.py`, then `python3 scripts/image_gate.py`
to regenerate reports in ignored `.local/image-evidence`. Startup always rescans.
CI retains reports as a 30-day artifact even when qualification fails. Committed
snapshots are evidence for these specific images and scanner database, not future
rebuilds or advisory databases.
Public root component names are stable image identities; generation and
repository checks reject private home/Windows/workspace paths elsewhere.
