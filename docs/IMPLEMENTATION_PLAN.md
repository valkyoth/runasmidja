# Runasmidja Implementation Plan

Status: planning contract; foundation initialized on 2026-10-03.

The goal is a complete modern CyberChef-style online website, reusable Rust
engine and durable public API. Users visit a normal hosted website; ordinary
transformations execute in a real Dedicated Worker in their browser without
an account, database or payload upload. Explicit remote execution uses isolated
Linux workers. Saving and sharing are independent permissions.

The [release plan](RELEASE_PLAN.md) assigns 363 bounded passes through
0.363.0; additional passes close every mandatory gap before 1.0. The original
240-pass bundle remains preserved in [reference](reference/workbench-plan/README.md).
Every original source version maps to one or more Runasmidja owners in phase
JSON records. Multi-algorithm work is split rather than hidden in a broad title.

## Engineering rules

- Pin current stable Rust 1.99.0, edition 2024/resolver 3. The compiler floor
  follows reviewed stable upgrades; no older MSRV is promised.
- Check upstream versions weekly and before dependency/tool changes. Keep
  exact lockfiles, immutable image references and workflow action commits.
- All code files stay at or below 500 lines, ideally below 300. No exception
  for generated executable code; split generation output as necessary.
- Pure contracts and small transforms use no_std/no allocation. Larger recipe
  and planning state may use no_std + alloc with fallible budgeted growth.
- First-party code forbids unsafe. Any future change requires an isolated,
  explicitly reviewed policy change and applicable safety evidence.
- Minimize dependencies by owning simple transformations and application rules.
  Qualify maintained providers for cryptography, compression and complex parsing;
  reducing dependency count must not override correctness or security.
- Keep framework, database, SDK, TLS and browser types outside portable APIs.
- Test every admitted behavior, malformed path, resource limit and lifecycle.
  Tests, security docs and release notes arrive in the same implementation pass.
- EUPL-1.2 applies to project code. External asset/code rights are reviewed
  independently, including models, tables, signatures, fonts and fixture corpora.

## Crate setup and extraction plan

The initial workspace has six small crates; reserved leaves make the requested
HTML and crypto extraction explicit without inventing unavailable sibling APIs.
Extract the following only when real behavior needs ownership:

| Crate family | Responsibility | Profile |
| --- | --- | --- |
| runasmidja-core | IDs, limits, checked offsets, value kinds, structured errors | no_std/no alloc |
| runasmidja-operation | One descriptor, typed ports, arguments, execution class | no_std; optional alloc |
| runasmidja-recipe | Versioned IR, control regions, validation, migrations | no_std + alloc |
| runasmidja-engine | Cooperative deterministic scheduler, byte credits, cancellation | no_std + alloc |
| runasmidja-application | Use cases and EngineClient semantics | portable |
| runasmidja-api-model | Wire DTOs, lossless offsets, schema negotiation | portable |
| runasmidja-ops-* | Encoding/text/format/archive/crypto/forensics/media packs | smallest applicable profile |
| runasmidja-compat-cyberchef | Pinned recipe dialect, import/export and bounded interpreter | portable |
| runasmidja-html | Inert formatting and owned web-boundary contracts | portable core + host adapter |
| runasmidja-crypto | Secret/provider policy seams, distinct analysis/live security | portable core + host adapter |
| runasmidja-postgres / runasmidja-mysql | Backend-owned migrations and repository conformance | std adapters |
| runasmidja-openbao | Latest reviewed openbao SDK, AppRole and leases | std adapter |
| runasmidja-valkey | Optional bounded cache and invalidation | std adapter |
| runasmidja-browser / runasmidja-web | Wasm worker bindings and accessible Rust DOM UI | browser host |
| runasmidja-server / runasmidja-worker | Control plane and isolated native execution | Linux/std |

No one-crate-per-operation rule. Split families when security dependencies,
provider footprint or review size justify separation. `lib.rs` exports;
`main.rs` initializes and delegates.

## Implementation order

Repository and container fixtures come first so every later hosted feature can
test itself. Then prove one transformation on native and actual browser hosts,
pin the complete CyberChef inventory and establish stable descriptors/contracts.
Investigate regex dialects, query languages, YARA, crypto, compression,
disassembly and OCR in separate feasibility passes before assuming providers.

Common encodings precede execution stress, persistent artifacts and advanced
viewers. Optional hosted persistence/API work follows local contracts and adds
real PostgreSQL repositories, OpenBao SDK/rotation/database leases, Valkey
failure behavior, authentication, isolation and quotas. Production service TLS,
recovery custody and PostgreSQL beta-to-GA migration have explicit owner passes.

Structured formats, archives, modern and historical cryptography, public keys,
forensics and media follow in narrow operation/provider passes. Full recipe
control flow includes backward jumps and bounded compatibility execution;
a DAG alone is insufficient. Plugin and provider replacement proof follows
mature contracts. Real MySQL tests and bidirectional logical migration drills
prove database independence before final qualification.

## Acceptance inventories

Resolve CyberChef v11.5.0 and deliberately adopted current-source deltas to
immutable commits in the early inventory pass. Record every operation, alias,
argument/default, input/output conversion, error and target. Include the supplied
certificate-bundle delta after verifying its source. Later upstream drift has a
separate reviewed backlog and never silently changes frozen 1.0 scope.

Maintain five independent reports: operation coverage, argument/semantic
coverage, whole recipes, workbench features and execution targets. An operation
name, compile-only Wasm build or native-only workaround never closes browser
parity. A safe difference needs explanation and evidence; it cannot hide deleted
analysis functionality. No exact operation count is invented at bootstrap.

## Replacement and portability contracts

Database contracts specify revision concurrency, transaction boundaries,
authorization, deterministic pagination, lease fencing and idempotency.
PostgreSQL-specific SQL/JSON/indexes stay behind its adapter. Bulk payloads
belong to a separate artifact store; staged immutable objects, SQL manifests,
outbox and reconciliation bridge the two stores. MySQL qualification tests the
same semantics on real containers and preserves a tested rollback path.

Separate HTML generation, inbound/outbound HTTP, native TLS and database TLS.
Vef and Brynja integration must consume verified current APIs when ready;
default builds require no sibling directory. The openbao SDK has its own HTTP/TLS
transport: isolate and inventory that replacement risk, rather than pretend it
already uses a Runasmidja connector. Browser Fetch/HTTPS remains browser-owned.
A second adapter and shared contracts prove boundaries even when siblings are
not ready; real integration is never claimed from mocks.

## 1.0 and later platforms

1.0 requires complete declared website/API behavior, supported-browser tests,
security assessment/remediation, no_std graph checks, exact-artifact provenance,
accessible workflows, independent provider vectors, resource/cancellation
measurements and executable deployment/upgrade/recovery documentation.
PostgreSQL 19 must be GA and current supported services must be qualified.

Post-1.0 GUI work: Linux, Windows, BSD and macOS desktop; Android/iOS mobile.
Keep platform handles, files, secure storage and updater policy in adapters.
Aesynx is conditional future work requiring runnable APIs; no support claim now.
