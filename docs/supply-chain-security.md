# Supply Chain and Toolchain Policy

Pin Rust 1.99.0 and check current stable weekly and before toolchain changes.
Latest upstream does not imply silently executing or admitting an update.
Review release/advisory notes and test the affected matrices before changing
pins; update rust-version/toolchain/CI/docs together. No older MSRV is promised.

Weekly freshness checks query official Rust distribution metadata, crates.io
stable non-yanked versions, upstream action/service releases and the planned
OpenBao SDK. Registry failure is an unavailable check, never a successful current
result. Dependabot independently watches Cargo and Actions. PostgreSQL beta/RC/GA
status is checked against the official source-release directory; add a tested upgrade
pass rather than replacing a beta image in place.

Security tools use exact versions and reviewed crate archive SHA-256 hashes from
Brynja. Installation verifies those hashes, extracts the exact bounded archive,
fetches locked dependencies and installs offline with `--path` from those bytes.
The project root is never fetched again from a registry after verification.
Action uses are full commits, credentials are not persisted and workflow tokens
are read-only. Remote container images are immutable digests with reviewed tag metadata.

Fixture execution additionally requires `scripts/image_gate.py`: exact-image
Trivy vulnerability scans and OS/language/native CycloneDX inventories, plus
reviewed publisher policy. Cosign/Trivy use reviewed official artifact hashes;
Trivy's Sigstore release bundle is verified against its GitHub workflow identity
and issuer. Both tool releases are included in freshness checks.
OpenBao's signed release index must authorize the exact Linux/amd64 leaf.
The maintainer approved unsigned-image exceptions only for the exact official
PostgreSQL/Valkey pins in deploy/podman/image-policy.json, limited to disposable
fixtures. Changing any pin requires renewed review; these exceptions do not
waive vulnerability findings or establish cryptographic publisher identity.
The original PostgreSQL exception is historical and that image remains blocked.
The Valkey exception is rollback-only. Default Valkey verifies its exact signed
Chainguard index, GitHub workflow identity/issuer and Linux/amd64 leaf. Its public
Wolfi starter includes a shell and shared libraries; retain their upstream
inventory and notices rather than claiming a shell-free image. Every startup
scans either selected profile; no scan or provenance fallback is allowed.
Its authorized replacement builds pinned official source on a Wolfi platform
leaf authenticated through the signed Chainguard index. Signed APK packages are
resolved at build time; builds are not bit-for-bit reproducibility claims.
The local receipt binds the reviewed recipe and scanned archive's config and
every layer to the executed immutable image ID. It is not cryptographic publisher
identity for a distributed image. The build context excludes all project secrets.
See the [recipe](../deploy/podman/postgres/README.md); private-build/release signing
and portable artifact attestation remain v0.9 and later distribution owners.

UNKNOWN/HIGH/CRITICAL findings block execution, including unfixed ones. An UNKNOWN
finding can pass only with an exact-image/module/version, evidence-bound
not-affected review valid for at most 30 days. HIGH/CRITICAL cannot use this path.
The OpenBao binary's affected legacy OpenPGP packages are absent; its single
UNKNOWN advisory is retained, not globally ignored. See the
[analysis and expiry](../security/advisories/README.md). Local Trivy
configuration/environment, ignore files/policies and VEX filters cannot remove
findings from this gate. Original PostgreSQL has 42 reported findings; the
qualified Wolfi replacement and both current service images have zero reported
HIGH/CRITICAL findings. No CVE waiver is admitted. PostgreSQL's source-built C
application is recorded explicitly with its source hash; Trivy's OS inventory
does not claim automatic advisory analysis of that compiled C source. Official
PostgreSQL release/advisory review remains required. The Cargo inventory
does not cover these image graphs. See [image evidence](../sbom/images/README.md).
Local pre-push qualification retains per-image SBOMs from completed scans,
including scans whose findings block admission. Review public inventories before
committing them; operational scanner failures do not yield fresh valid evidence.
Trivy uses `--exit-code 0` for completed reports, including reports with findings.
Every nonzero scanner exit is an operational failure and blocks admission before
report parsing. Policy is enforced from the completed report; a reviewed UNKNOWN
can never excuse scanner failure or make partial output admissible.
Public inventory names use immutable image identities. Other private paths
cause generation/repository checks to fail rather than being published.
Public builds use checked cgroup CPU/memory/process ceilings, private bounded
tmpfs storage and a streaming atomic archive writer; see the
[build contract](../deploy/podman/postgres/README.md).

New dependencies need current-version, source, features, license, maintenance,
advisory, unsafe/build-script and target-footprint review plus tests for the
admitted behavior. Default portable crates stay dependency-minimal. Planned
Leptos/Axum/Tokio/Rustls/tokio-postgres choices are outer adapters; their exact
versions are selected live when implemented, not invented today.

The latest openbao SDK is reserved for its own hosted adapter; this setup
exercises the real server API for test bootstrap and admits no runtime SDK yet.
Record SDK-owned HTTP/TLS as a replacement risk. First-party ownership does not
substitute for provider review. Keep EUPL-1.2 SPDX metadata consistent and include
redistribution notices for admitted code/models/fonts/tables/corpora.

Local system packages follow the user-managed daily Tumbleweed updates and do
not block product/service freshness checks. Meilisearch upstream is monitored
as an optional unadmitted service; qualification is required before enabling it.
Both repository search and the optional Meilisearch adapter are required planned
implementations before 1.0; deployment selection is separate. At admission,
verify the current server/client API, license/features, action/image/source
provenance and add the admitted client to weekly crate freshness coverage.

Public toolchain/build checks need no secret. Any project credential for private
initialization, registry access, signing, publishing or deployment comes through
OpenBao under [secret lifecycle policy](SECRETS_POLICY.md), including in CI.
Platform workload identity is scoped authentication proof, not a project-token
storage substitute; trusted jobs retrieve only their own bounded grants.

The planned workflow/feature/target admission and early pack/resource passes in
[gap reconciliation](gap-reconciliation-2026-10-03.md) strengthen the current
scaffold heuristics. Review normal/build/dev/optional/target feature unification
and lint inheritance; first-party unsafe remains forbidden. Pin pack/model/font/
table source, redistribution rights, imports and expanded/compiled memory before
large browser providers. A historical issue or upstream Wasm use does not prove
current browser portability; qualify the exact admitted profile.

Trusted assessment and exact source/artifact/pack/model/SBOM/toolchain/signing
identity bindings require the planned distribution gates. Current source/report
metadata validation authenticates neither assessor nor artifacts. GitHub CodeQL
Default/settings and actual CI evidence remain separate external requirements.
