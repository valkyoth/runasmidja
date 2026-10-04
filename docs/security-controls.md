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
| Verified tool compilation | Implemented; maintainer retest accepted | CI compiles exact verified archive offline; corrupt/offline/traversal regressions |
| Wolfi static probe qualification | Implemented; maintainer accepted v0.2.1 | Signed base/platform, exact archive/executable binding, live kernel limits/capabilities, owned cleanup; native/scratch regressions |
| Fixture image provenance/inventory | Implemented; v0.2.0 accepted, v0.2.2 retest required | Signed OpenBao/Wolfi index-to-leaf binding, signed Wolfi Valkey index (exact official exception only for rollback), source-built PostgreSQL config/layer binding, per-image inventory and UNKNOWN/HIGH/CRITICAL rejection; only evidence-bound expiring UNKNOWN not-affected reviews; original PostgreSQL remains blocked |
| Public build containment | Implemented; maintainer retest accepted | Checked CPU/memory/PID owned cgroup and build-step limits, private 3 GiB store, pre-write 512 MiB atomic archive cap; actual build/kernel/tmpfs and failure regressions |
| Public SBOM privacy | Implemented; maintainer retest accepted | Stable image names; generator/repository rejection of home/macOS/Windows/workspace paths |
| Scanner completion and build publication | Implemented; maintainer retest accepted | Nonzero scanner exits always reject; findings evaluated only after completion; candidate scan/import/identity checks precede final receipt; failure/retry and previous-artifact preservation regressions |
| Process cleanup identity | Implemented; maintainer retest accepted | No signal after leader reaping; real flood/deadline/pipe-descendant regressions; dedicated build cgroup |
| Child/log/audit resource bounds | Implemented; maintainer retest accepted | Concurrent child budgets/kill/reap, 1 MiB log rotation, 16 MiB live audit tmpfs, two bounded no-follow snapshots; real Podman bounds qualification |
| Local custody durability | Implemented; maintainer retest accepted | File and parent fsync for create/rename/unlink, fault regressions; remote init/local capture remains non-atomic |
| GitHub CodeQL | External setting required | GitHub Default setup only; no advanced workflow |
| Local secret isolation | Implemented harness | Ignored .local state, private permissions, limited container mounts |
| OpenBao test bootstrap | Implemented harness | TLS validation, declarative audit, KV v2, AppRole, root revoke |
| OpenBao source for all project secrets | Implemented for v0.2 fixture passwords; wider policy pending | Vault-first random/KV issuance and scoped reads; private delivery/build/release qualification pending; see [policy](SECRETS_POLICY.md) |
| Search optionality and live authorization | Planned | Early SearchService, repository/Meilisearch profiles, metadata allowlist, outbox and current-authority rechecks; see [design](SEARCH_DESIGN.md) |
| PostgreSQL/Valkey test controls | Implemented harness | Runtime DB role, cache ACL/prefix/TTL/memory, loopback ports |
| Release metadata readiness | Configured; limited | Report shape/digest/lineage/SBOM-presence only; no assessor/artifact authentication; trusted review required |
| Workflow/graph enforcement hardening | Required; planned | Reproduced .yaml action/CodeQL omission and no_std comment spoof; versioned rejection/admission owners in [reconciliation](gap-reconciliation-2026-10-03.md) |
| Fixture ownership/drift | Minimum ownership implemented; full drift pending v0.5 | Project/service/instance labels before network/volume/container reuse and stop; pinned image ID checked. Full fingerprints and inspect/mutate races unqualified |
| Wolfi Valkey fixture | Implemented; v0.2.2 retest required | Exact version/base, auth/ACL/key denials, real eviction, kernel restrictions, outage/restart/nonpersistence and preserved-instance-only official rollback; nonzero host/container UID and selected-engine rootless enforcement |
| Valkey expiry evidence | Required; planned | Current smoke accepts EX then deletes; actual TTL/countdown/expiry qualification remains pending |
| Product security controls | Planned | Browser, API, recipe, worker, provider and recovery milestones |
| Smoke evidence integrity | Implemented; maintainer retest accepted | Optimization-safe checks, actual child's announced ephemeral port, bounded/flushed readiness and pre/post liveness; 34 Python tests plus optimized actual probes |
| Browser origin-compromise boundary | Design remediation; runtime planned | Separate local/remote origins, independently verified signed offline/network-disabled profile and exact document/worker headers with [versioned owners](BROWSER_SECURITY_PROFILES.md) |

A configured workflow is not evidence that GitHub settings or remote CI passed.
A local service smoke test is not a production security assessment. See
[threat model](threat-model.md) and [testing](testing.md).

Build/probe follow-up (v0.2.2, retest required): all host Podman command paths
share the rootless guard, including archive export and PostgreSQL import. The
build checks its explicit local engine before unshare; its namespace worker
requires the nonroot host UID mapping and owned resource cgroup. The Python AST
gate prevents accidental raw command paths, not arbitrary hostile source changes.
