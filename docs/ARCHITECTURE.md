# Runasmidja Architecture

Status: product contract; only the foundation is implemented.

The supplied [architecture](reference/workbench-plan/ARCHITECTURE.md) and
[risk register](reference/workbench-plan/PARITY_AND_RISK_REGISTER.md) are design
inputs. This document records Runasmidja-specific decisions; the implementation
and release plans are authoritative when a source-bundle version differs.

## Dependency direction

```mermaid
flowchart TD
  UI[Online Rust web UI] --> Local[Browser worker client]
  UI --> Remote[Explicit remote API client]
  Local --> App[Portable application contract]
  Remote --> HTTP[Replaceable HTTP adapter]
  HTTP --> App
  App --> Recipe[Recipe compiler and bounded control flow]
  Recipe --> Engine[Deterministic execution and resource ledger]
  Engine --> Ops[Descriptors and operation packs]
  App --> Ports[Application-owned host ports]
  Ports --> PG[PostgreSQL metadata adapter]
  Ports --> Artifacts[Staged artifact storage]
  Ports --> Secrets[OpenBao SDK adapter]
  Ports --> Cache[Optional Valkey cache]
  Ports --> Search[SearchService]
  Search --> Repository[Repository metadata search]
  Search --> Meili[Optional Meilisearch adapter]
```

Core types never expose database rows, Tokio handles, framework requests,
browser objects or provider-owned TLS types. Browser/native execution shares
operation semantics, not necessarily serialization or thread bounds.

## Data and execution

Typed values distinguish raw bytes, encoded text, records, lossless structure,
tables/media, file collections and scoped artifact handles. Offsets are checked
64-bit values; JSON uses exact representations instead of unsafe JavaScript
number conversion. SecretRef values are scoped capabilities; derived sensitivity
propagates unless an explicitly reviewed rule permits declassification.

A step reports consumed/produced counts and NeedInput/NeedOutput/Yield/Finished.
Streaming, reduction, bounded-window, seekable and whole-input operations have
distinct resource declarations. EOF, finish, errors and cancellation are explicit
states. Transport partitions must not change results. Charge allocation capacity,
provider memory, carry buffers, queues, fan-out lifetime, previews and artifacts.

Use deterministic cooperative execution with bounded queues and fair joins.
Backwards jumps and nested flow use bounded IR regions or a compatibility
interpreter with total-work/output limits. Every run owns child work and cleanup.
The browser can terminate/recreate workers; the server can terminate isolated
worker processes. Stale generations/fencing tokens cannot publish successful
artifacts. Authenticated decryption stays staged until final integrity succeeds.

## Privacy and UI

Serve a normal online website. Default processing happens in a real Dedicated
Worker. Network/upload, local persistence, sharing and secret use are separate
capabilities. Failure never silently uploads. Generated descriptor metadata
feeds forms, catalogue, docs and schemas; avoid duplicated argument definitions.

Preserve simple input/recipe/output panes, keyboard navigation, accessible DOM,
manual Run, undo/redo, debugging and paged viewers. A graph is optional.
Raw transformed data cannot become trusted application HTML. Active document
previews receive isolated origins/sandbox policies and no ambient credentials.
Offline bundles include selected packs/models; no hidden third-party CDN fetch.

## Services

PostgreSQL 19 beta 4 is the development baseline, with private runtime/migration
roles and portable repository methods. Durable metadata is separate from bulk
artifacts. Real MySQL conformance and bidirectional logical migration prove the
seam before 1.0; an in-memory fake cannot supply that proof.

OpenBao 2.7.1 is the required source for every project-operated initialization,
runtime, private-build and release secret. Public Rust builds need no credentials.
The current dev harness initializes it over TLS, with declarative audit, KV v2,
AppRole and revoked bootstrap root, but generates service passwords locally
first. The next pass replaces that sequence with Bao-first provisioning and
vault-sourced credentials. Early application-contract passes admit the current
stable openbao SDK and qualify SecretRef/rotation. Runtime processes
never receive recovery shares/root privileges. Production TLS, identity,
renewal, rotation, dynamic DB leases, audit failure and recovery custody require
separate qualification. Single-share local custody is strictly a test shortcut.
Vault startup trust and independent recovery custody are the minimal explicit
bootstrap boundary; they cannot depend solely on a sealed vault. Follow
[secret lifecycle](SECRETS_POLICY.md) for scoped delivery and failure behavior.

Valkey 9.1.2 is optional cache acceleration, with scoped ACLs, TTL and byte limits.
Only completed deterministic nonsensitive results or bounded metadata are eligible.
Cache identity includes semantic/provider/data revisions and canonical framing;
it is partition-independent and workspace scoped. Permission checks use
current authority. Cold cache/outage/eviction cannot lose authoritative data.

Operation and browser-local recipe search stay local. Early SearchService
contracts own saved-server-metadata queries; implement both repository and
optional Meilisearch adapters with hosted persistence/authorization. A std-only
feature and runtime selector preserve the same UI/API/domain schema with the
service enabled or disabled. Measurements guide deployment and limits.

Project only approved nonsensitive metadata; inputs, outputs, operation arguments
and secrets never enter an index. Transactional revisioned outbox/replay makes
it rebuildable. Tenant filters plus current database permission/revision checks
govern every returned hit and visible aggregate; asynchronous index grants are
never authority. Meilisearch startup/scoped keys come through OpenBao. See
[search design](SEARCH_DESIGN.md) for switching, outages and qualification.

## Future extraction

HTML/HTTP behavior stays behind Runasmidja-owned seams for Vef. Analysis crypto,
secret lifecycles and native/database TLS stay isolated for Brynja. Neither
sibling API is fabricated and neither directory is a default dependency.
Inventory all hidden outbound HTTP/TLS consumers, including SDKs and identity
metadata. Adapter tests cover framing, backpressure, cancellation, trust/name
verification, ALPN, redirects, errors and protocol-specific database negotiation.
Browser TLS cannot be replaced by a Wasm TLS provider.

## Detailed acceptance contracts

The [execution contract](EXECUTION_CONTRACTS.md) defines explicit EOF/counts,
orthogonal execution shape/capabilities, positive whole-run fuel, bounded regions
and sensitivity/publication. A small checked vocabulary/profile precedes the
first real-worker hex seed; later scheduling/IR work is not assumed present.

The [browser/performance contract](BROWSER_PERFORMANCE.md) defines task-level
cancellation yields, supervisor-owned staging cleanup, bounded page/progress
protocols, measured copies and early pack/resource admission. Kernel, JS, Wasm,
UI/provider and disk costs have separate measured envelopes.

The [storage/host contract](STORAGE_HOST_CONTRACTS.md) defines cross-store crash
cuts, actual artifact prerequisites, byte-read migration integrity, runnable
transport replacement, kernel sandbox fault evidence and DNS/connect/redirect
binding. Early API development never grants public job exposure before the
integrated authority/admission/fencing/egress/TLS/recovery gates.
See [reviewed owners](gap-reconciliation-2026-10-03.md) and
[strict verification](VERIFICATION_GATES.md); no new runtime claim is made.
