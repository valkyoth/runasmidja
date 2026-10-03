# Foundation Verification — 2026-10-03

Scope: 0.1.0 foundation candidate, preserved in the repository initialization
commit. No release tag, publication or pentest PASS was produced. This record
documents executed tests, not an independent audit.

| Check | Executed result |
| --- | --- |
| scripts/checks.sh | PASS: format, strict clippy, debug/release/all-feature tests, docs and target checks |
| Rust probe unit tests | 3 tests PASS in debug/release/feature profiles |
| Python adversarial gate/helper tests | 14 tests PASS, including release rejection, scope coverage, version parsing, file permissions and no redirects |
| Portable graphs | Five crates PASS on thumbv7em-none-eabihf and wasm32-unknown-unknown with no defaults |
| Repository/link/code-size policy | PASS; largest first-party code file 200 lines |
| Native probe | Real loopback process health and rejected routes PASS |
| Container probe | Real static musl scratch/non-root/read-only/init-managed container health and rejected routes PASS |
| PostgreSQL | Actual 19beta4, rollback, runtime login, wrong-password rejection and privileged-table denial PASS |
| OpenBao | Actual 2.7.1, verified TLS, declarative audit, KV v2, scoped AppRole/path denials, private material and root-token removal PASS |
| Valkey | Actual 9.1.2, authenticated TTL set/get/delete, anonymous and foreign-prefix denials PASS |
| Service lifecycle | Repeated start and stop/restart with preserved PostgreSQL/OpenBao state PASS |
| cargo deny check | Advisories/bans/licenses/sources PASS |
| cargo audit --deny warnings | PASS using fetched RustSec database, 1,288 advisories |
| SBOM | CycloneDX 1.5 generated for six first-party workspace packages |
| Release gate rejection | Expected nonzero: pentest report missing (NOT RUN) |

Live product freshness confirms Rust 1.99.0, cargo-deny 0.20.2,
cargo-audit 0.22.2, cargo-sbom 0.10.0, checkout v7.0.1,
OpenBao 2.7.1, planned SDK 2.2.1, Valkey 9.1.2,
PostgreSQL 19beta4 and CyberChef v11.5.0. Meilisearch v1.54.3 is monitored
as optional/unadmitted, with no service dependency enabled.
Local OS/Podman versions follow user-managed daily Tumbleweed updates.

Provenance: image manifests are pinned; original idea and ZIP documents remain
preserved with source hashes. All 240 original roadmap workstreams have mapped
owners among 363 Runasmidja passes. Product browser/UI/operation parity remains
unimplemented and unverified. GitHub settings, remote CI and CodeQL execution
were not asserted or changed by this setup.

Observed bootstrap/test failures were remediated before successful tests: OpenBao
Raft initialization timed out before returning custody material, so that owned
fixture data was retained and a fresh single-node PebbleDB fixture was provisioned;
OpenBao 2.7 requires declarative audit configuration; build-context exclusions
were narrowed to allow only the static probe binary; Podman init now forwards
container shutdown signals. Release-monitor tests cover actual relative
PostgreSQL source-directory links and reject missing metadata. A final incorrect-password
fixture caught PostgreSQL initdb loopback trust defaults; bootstrap now explicitly
selects SCRAM host authentication and reconciles existing host trust rules.
