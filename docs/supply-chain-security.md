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
