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
| Release pentest readiness | Configured | Non-PASS evidence blocked by scripts/check_release.py |
| Product security controls | Planned | Browser, API, recipe, worker, provider and recovery milestones |

A configured workflow is not evidence that GitHub settings or remote CI passed.
A local service smoke test is not a production security assessment. See
[threat model](threat-model.md) and [testing](testing.md).
