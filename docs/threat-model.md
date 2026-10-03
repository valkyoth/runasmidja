# Runasmidja Threat Model

Status: foundation threat inventory; product controls are planned unless marked
implemented in [security controls](security-controls.md).

Assets: input/output payloads, cryptographic keys, saved recipes, workspace grants,
secret leases, artifact manifests, job integrity, resource availability and
release provenance. Inputs, recipes, links, names, query expressions, formats,
plugins and rendered results are untrusted, including when processing locally.

| Boundary | Main threats | Required evidence |
| --- | --- | --- |
| Browser import/render | XSS, hidden effects, secret persistence, malicious links | Inert output, capability preview, no autorun/upload, real browser negatives |
| Browser code origin | Compromised origin/CDN/deployment account/JavaScript reads input or replaces worker/policies | Separate local/remote applications; independently verified signed immutable offline bundle plus network-disabled host for high assurance; document/worker CSP, Trusted Types, COOP/COEP/CORP, framing and permission negatives |
| Operation execution | Expansion, parser/provider faults, algorithm confusion | Independent vectors, budgets/fuzz/partition tests, explicit revisions |
| Scheduler/control flow | Loops, join deadlock, stale result, cancellation race | Tiny-credit tests, total-work caps, generation fences, hard termination |
| API/authorization | IDOR, CSRF, session replay, quota bypass | Object checks, tenant denial suite, origin/CSRF and aggregate limits |
| Native egress | SSRF, rebinding, redirects, credential forwarding | Resolution/connect checks, IPv4/IPv6/private/metadata deny corpus |
| Artifact/database | Partial publication, traversal, stale worker, lost revisions | Staging/fencing, symlink-safe namespace, transaction/crash/restore tests |
| Cache/search | Cross-tenant inference, stale grants, poison, secret indexing | Scoped keys, authoritative auth, completed manifests, outage/rebuild tests |
| OpenBao | Root leakage, broad grants, expiry, bootstrap/audit failure | Scoped AppRole, root revoke, TLS, rotation/recovery and denials |
| Initialization/build secret supply | Local fallback, CI claim confusion, persistent delivery leaks, sealed-vault dependency cycle | Bao-first provisioning, enumerated startup trust, scoped CI exchange, tmpfs cleanup, source/version provenance |
| Plugin/media | Ambient origin privileges, runaway code, host-call escape | Separate memory/workers, import allowlist, isolated previews, killability |
| Supply/release | Stale vulnerable code, mutable actions/images, forged PASS | Hash/version policy, audits/SBOM, exact-source pentest, signed provenance |

No first-party crypto primitive is written to reduce dependency count casually.
Legacy analysis packs cannot affect TLS, authentication or application encryption.
Parsing, valid signatures and trusted identities remain separate states.

Default logs/metrics exclude payloads, keys, query contents and decoded outputs.
Opaque IDs are not authorization. Content hashes are not public capabilities.
No claim of full erasure from browsers, swap or backups is made.

Dedicated Workers isolate scheduling, not an input from the owning page. CSP
does not make a compromised origin trustworthy. Browser extensions and a
compromised browser/OS remain outside application defense. Hosted local-only
processing makes no classified-data assurance claim. The exact profile/header
contract and implementation owners are in
[browser security profiles](BROWSER_SECURITY_PROFILES.md).

Foundation residual limits: health probe is loopback test tooling, not qualified
HTTP; dev PostgreSQL/Valkey loopback transport is unencrypted; local recovery
shares and service passwords are held together for disposable tests; 30-day
self-signed OpenBao certificates and 24-hour AppRole SecretIDs expire. Production
profiles must reject these shortcuts and implement separate lifecycle gates.
Service passwords are currently generated outside OpenBao before KV seeding;
the next planned pass remediates origin and startup ordering. Mandatory project
secret scope and custody are defined in [secret lifecycle](SECRETS_POLICY.md).
The [search design](SEARCH_DESIGN.md) requires negative evidence for stale-index
hits, snippets, counts and facets, including revoked same-tenant permissions.

The [reviewed gap owners](gap-reconciliation-2026-10-03.md) add concrete closures
for workflow/graph admission bypasses, unsafe fixture reuse/stop assumptions,
unobserved cache expiry and unauthenticated report/artifact metadata. They are
verified gaps with future remediation owners, not exploited production findings.
The [execution](EXECUTION_CONTRACTS.md), [browser/performance](BROWSER_PERFORMANCE.md)
and [storage/host](STORAGE_HOST_CONTRACTS.md) contracts require positive global
fuel, secret publication checks, supervisor cleanup, actual kernel fault evidence,
cross-store crash cuts and DNS/connect/redirect policy before support claims.
