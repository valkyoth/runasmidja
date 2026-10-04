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
| Wolfi Valkey | 20 | 0 | Signed Chainguard index binds exact platform leaf |
| Official Valkey (rollback) | 24 | 0 | Exact unsigned-image exception approved by maintainer |
| Wolfi base | 20 | 0 | Signed Chainguard index binds exact platform leaf |
| Original official PostgreSQL (historical) | 151 | 42 HIGH/CRITICAL | BLOCKED; not executed by current fixture |

The qualified local PostgreSQL image ID is
`sha256:1c2b3174ef094bf8344a587a74c79bb130af033ccb3e11cb2bf5e738fe0bdf9d`.
Its scanned Docker archive SHA-256 is
`feb3101d0fbdefe7276326e985e0c0b854cd51949f25032ce5f44d45daeaacc8`.
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
Heavy qualification and evidence retention are local, not GitHub CI. Committed
snapshots are evidence for these specific images and scanner database, not future
rebuilds or advisory databases.
Public root component names are stable image identities; generation and
repository checks reject private home/Windows/workspace paths elsewhere.

## Probe inventories (available since v0.2.1)

`probe-base.cdx.json` records the signed Wolfi static base; `probe.cdx.json`
records the locally assembled exact scanned image and the first-party probe's
executable hash/EUPL-1.2 license. Base package license identifiers are retained
from scanner evidence; see each component's licenses. The scanner does not
recover Rust dependency metadata from our stripped executable: the Cargo SBOM
and advisory audit remain required separate evidence. Qualification runs locally,
not in GitHub container CI. No registry image is published by generating SBOMs.

`valkey.cdx.json` inventories the v0.2.2 signed Wolfi default.
`valkey-official-v0.2.1.cdx.json` preserves the exact rollback image inventory.
The rollback exception does not apply to the new image. See the
[Valkey provenance and operating profile](../../deploy/podman/valkey/README.md).
