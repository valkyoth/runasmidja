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
| Verified tool compilation | Implemented; retest required | CI compiles exact verified archive offline; corrupt/offline/traversal regressions |
| Fixture image provenance/inventory | Implemented gate; PostgreSQL blocked | Signed OpenBao index-to-leaf binding, exact PostgreSQL/Valkey unsigned exceptions, per-image OS/Go/C/native SBOM and HIGH/CRITICAL rejection |
| Child/log/audit resource bounds | Implemented; retest required | Concurrent child budgets/kill/reap, 1 MiB log rotation, 16 MiB live audit tmpfs, two bounded no-follow snapshots; real Podman bounds qualification |
| Local custody durability | Implemented; retest required | File and parent fsync for create/rename/unlink, fault regressions; remote init/local capture remains non-atomic |
| GitHub CodeQL | External setting required | GitHub Default setup only; no advanced workflow |
| Local secret isolation | Implemented harness | Ignored .local state, private permissions, limited container mounts |
| OpenBao test bootstrap | Implemented harness | TLS validation, declarative audit, KV v2, AppRole, root revoke |
| OpenBao source for all project secrets | Implemented for v0.2 fixture passwords; wider policy pending | Vault-first random/KV issuance and scoped reads; private delivery/build/release qualification pending; see [policy](SECRETS_POLICY.md) |
| Search optionality and live authorization | Planned | Early SearchService, repository/Meilisearch profiles, metadata allowlist, outbox and current-authority rechecks; see [design](SEARCH_DESIGN.md) |
| PostgreSQL/Valkey test controls | Implemented harness | Runtime DB role, cache ACL/prefix/TTL/memory, loopback ports |
| Release metadata readiness | Configured; limited | Report shape/digest/lineage/SBOM-presence only; no assessor/artifact authentication; trusted review required |
| Workflow/graph enforcement hardening | Required; planned | Reproduced .yaml action/CodeQL omission and no_std comment spoof; versioned rejection/admission owners in [reconciliation](gap-reconciliation-2026-10-03.md) |
| Fixture ownership/drift | Minimum ownership implemented; full drift pending v0.5 | Project/service/instance labels before network/volume/container reuse and stop; pinned image ID checked. Full fingerprints and inspect/mutate races unqualified |
| Valkey expiry evidence | Required; planned | Current smoke accepts EX then deletes; actual TTL/countdown/expiry qualification remains pending |
| Product security controls | Planned | Browser, API, recipe, worker, provider and recovery milestones |
| Smoke evidence integrity | Implemented; maintainer retest accepted | Optimization-safe checks, actual child's announced ephemeral port, bounded/flushed readiness and pre/post liveness; 34 Python tests plus optimized actual probes |
| Browser origin-compromise boundary | Design remediation; runtime planned | Separate local/remote origins, independently verified signed offline/network-disabled profile and exact document/worker headers with [versioned owners](BROWSER_SECURITY_PROFILES.md) |

A configured workflow is not evidence that GitHub settings or remote CI passed.
A local service smoke test is not a production security assessment. See
[threat model](threat-model.md) and [testing](testing.md).
