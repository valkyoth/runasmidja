# Security Controls

| Control | Status | Enforcement/evidence |
| --- | --- | --- |
| Portable default graph | Implemented | Five always-no_std crates, bare-metal/Wasm checks, no external runtime crates |
| First-party unsafe prohibition | Implemented | Workspace forbid lint plus crate attributes |
| Code size | Implemented | scripts/check_repository.py, rejection tests, hard 500-line limit |
| Integer overflow | Implemented | Release overflow-checks, abort policy |
| Dependency/source/license policy | Configured | deny.toml, Cargo.lock, audit gate |
| CI action provenance | Configured | Full commit pins; weekly Actions Dependabot |
| Tool provenance/freshness | Configured | Exact archive SHA-256 and versions; live freshness workflow |
| GitHub CodeQL | External setting required | GitHub Default setup only; no advanced workflow |
| Local secret isolation | Implemented harness | Ignored .local state, private permissions, limited container mounts |
| OpenBao test bootstrap | Implemented harness | TLS validation, declarative audit, KV v2, AppRole, root revoke |
| OpenBao source for all project secrets | Required; remediation planned | Current fixture generates local passwords first; next pass implements Bao-first initialization, then temporary delivery/build gates; see [policy](SECRETS_POLICY.md) |
| Search optionality and live authorization | Planned | Early SearchService, repository/Meilisearch profiles, metadata allowlist, outbox and current-authority rechecks; see [design](SEARCH_DESIGN.md) |
| PostgreSQL/Valkey test controls | Implemented harness | Runtime DB role, cache ACL/prefix/TTL/memory, loopback ports |
| Release metadata readiness | Configured; limited | Report shape/digest/lineage/SBOM-presence only; no assessor/artifact authentication; trusted review required |
| Workflow/graph enforcement hardening | Required; planned | Reproduced .yaml action/CodeQL omission and no_std comment spoof; versioned rejection/admission owners in [reconciliation](gap-reconciliation-2026-10-03.md) |
| Fixture ownership/drift | Required; planned | Existing reuse checks scope label only, stop/volume/network need stronger ownership and desired-spec checks |
| Valkey expiry evidence | Required; planned | Current smoke accepts EX then deletes; actual TTL/countdown/expiry qualification remains pending |
| Product security controls | Planned | Browser, API, recipe, worker, provider and recovery milestones |
| Smoke evidence integrity | Implemented; maintainer retest accepted | Optimization-safe checks, actual child's announced ephemeral port, bounded/flushed readiness and pre/post liveness; 34 Python tests plus optimized actual probes |
| Browser origin-compromise boundary | Design remediation; runtime planned | Separate local/remote origins, independently verified signed offline/network-disabled profile and exact document/worker headers with [versioned owners](BROWSER_SECURITY_PROFILES.md) |

A configured workflow is not evidence that GitHub settings or remote CI passed.
A local service smoke test is not a production security assessment. See
[threat model](threat-model.md) and [testing](testing.md).
