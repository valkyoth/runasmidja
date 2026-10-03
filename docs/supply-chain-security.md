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
Brynja. Installation verifies those hashes before cargo install --locked.
Action uses are full commits, credentials are not persisted and workflow tokens
are read-only. Container images are immutable digests with reviewed tag metadata.

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
