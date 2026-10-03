# Phase A: Foundation and useful vertical slice

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

Verification checklists apply only to introduced or retained behavior in the reviewed bounded scope. Record absent later capabilities as pending with numbered owners; contract fixtures never attest their runtime PASS. A prerequisite needed by this pass must be implemented and verified first, rather than deferred. Every future owner still owes its full acceptance before exposure/1.0.

## v0.14.0 — Executable seed

**Status:** planned.

**Setup:** baseline 0.13.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Executable seed.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Pin Rust 1.99.0; create kernel, engine, browser and native host packages; run one hex operation from a real browser worker. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Native and browser fixtures agree; the example needs neither PostgreSQL nor a sibling repository. Actual browser worker and native byte-transform outputs agree; prove UI-thread separation, malformed-input rejection, and offline/no-upload behavior for the frozen seed. The seed is one bounded hex operation, not the future scheduler: use the seed vocabulary/profile, finite positive fuel, explicit EOF/counts and a supervisor deadline; freeze minimal version/run/generation/length messages and no persistence/effects. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.14.0 implementation stop reached. Run pentest for this exact commit.

## v0.15.0 — Reference baseline

**Status:** planned.

**Setup:** baseline 0.14.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Reference baseline.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Resolve the reviewed tag and adopted current-source deltas to immutable commits; inventory operations, arguments, workflow features and licenses, including observed certificate-bundle parsing. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Every discovered operation has a stable tracking record; the reference commit and file hashes are recorded, not guessed. Resolve v11.5.0 and adopted deltas to immutable commits; inventory every distinct operation, alias, argument/default, and target with fixture/license provenance. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.15.0 implementation stop reached. Run pentest for this exact commit.

## v0.16.0 — Application contracts

**Status:** planned.

**Setup:** baseline 0.15.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Application contracts.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Define operation IDs, semantic revisions, structured errors, recipe envelopes, artifact references and local EngineClient commands. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Round-trip tests reject unknown required fields and preserve large offsets without JavaScript number truncation. Compile independent local/native clients against owned DTOs; reject host/provider type leakage, lossy offsets, missing grants, and malformed schemas. Use the already-tested seed value/budget vocabulary; do not assume the later full scheduler/IR exists. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.16.0 implementation stop reached. Run pentest for this exact commit.

## v0.17.0 — OpenBao SDK admission

**Status:** planned.

**Setup:** baseline 0.16.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OpenBao SDK admission.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Admit the latest stable openbao SDK into a dedicated std adapter with minimal reviewed features and server compatibility checks; keep it outside portable defaults. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Use the real TLS OpenBao fixture and compatibility policy; token and error diagnostics are redacted; no SDK transport types reach application APIs. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.17.0 implementation stop reached. Run pentest for this exact commit.

## v0.18.0 — Application secret references

**Status:** planned.

**Setup:** baseline 0.17.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Application secret references.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Define service/build SecretRef resolution through scoped OpenBao identity, bounded delivery and lease/version metadata; inventory database/cache/search/bootstrap, session/signing/encryption, external integration and release credentials. Exclude user operation keys from default persistence. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Missing, expired and revoked credentials fail closed; no root token or recovery key is delivered to API/worker/build processes; cross-workspace secret requests fail; no host/SDK type enters portable contracts and no hardcoded/environment/file secret fallback exists. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.18.0 implementation stop reached. Run pentest for this exact commit.

## v0.19.0 — Secret rotation lifecycle

**Status:** planned.

**Setup:** baseline 0.18.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Secret rotation lifecycle.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Implement token renewal, AppRole re-provisioning, credential rotation and restart convergence behind secret-store contracts. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Expiry, rotation during work, OpenBao outage and audit failure are exercised; old grants cannot be reused and no static secret fallback appears. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.19.0 implementation stop reached. Run pentest for this exact commit.

## v0.20.0 — Search service contracts

**Status:** planned.

**Setup:** baseline 0.19.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Search service contracts.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Define portable SearchService request/results, bounds, opaque cursors and declared capabilities during application contracts. Keep operation-picker search local. Plan repository and optional Meilisearch saved-metadata adapters with unchanged UI/API/schema and a std-only feature/runtime selector. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Default no_std graph admits no Meilisearch dependency; offline catalogue search and both hosted-backend contract fixtures cover query bounds, metadata projection and authorization. Ranking differences are explicit; filters/SDK types stay adapter-owned and unavailable features return declared errors. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.20.0 implementation stop reached. Run pentest for this exact commit.

## v0.21.0 — Portable kernel

**Status:** planned.

**Setup:** baseline 0.20.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Portable kernel.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Separate no_std/no-alloc kernel, alloc-enabled compiler and std hosts; establish feature and target matrices. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Bare-metal-style compile checks catch std leakage; unsafe code is forbidden in first-party portable core by default. Fixed-buffer kernels build on bare metal without std/alloc; checked offsets/limits and all boundary/overflow paths have executable tests. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.21.0 implementation stop reached. Run pentest for this exact commit.

## v0.22.0 — Bounded buffer contract

**Status:** planned.

**Setup:** baseline 0.21.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Bounded buffer contract.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add caller-provided input/output windows, consumed/produced counts, partial progress, cancellation checkpoints and finish states. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Zero-sized windows, short writes, empty inputs and repeated finish calls have defined results without panics. Assert counts and statuses on every step; test zero windows, every EOF state, repeated finish, output expansion, and provider/carry reservation. Execution shape and capabilities are orthogonal; synchronous steps never conceal host I/O/secret waits, zero-progress consumes fuel, and multi-port counts are explicit when supported. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.22.0 implementation stop reached. Run pentest for this exact commit.

## v0.23.0 — Operation descriptors

**Status:** planned.

**Setup:** baseline 0.22.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Operation descriptors.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Define typed arguments, defaults, help, execution class, secret fields and capabilities; generate a minimal catalogue. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** One new operation registers once and appears in catalogue, validation, documentation and generated argument controls. Catalogue/forms/schema derive from one descriptor; missing types, semantic revisions, execution limits, arguments, or capabilities fail validation. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.23.0 implementation stop reached. Run pentest for this exact commit.

## v0.24.0 — Linear execution

**Status:** planned.

**Setup:** baseline 0.23.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Linear execution.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Compile and run a sequence of hex, text and XOR operations with explicit byte/text conversion. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Chunk partitions do not alter outputs; invalid intermediate types fail before execution where statically knowable. Execute frozen linear fixtures through the same operations on native/browser; failures stop subsequent steps and cannot publish successful output. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.24.0 implementation stop reached. Run pentest for this exact commit.

## v0.25.0 — Worker protocol

**Status:** planned.

**Setup:** baseline 0.24.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Worker protocol.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Introduce versioned worker messages, input transfers, job generations, progress and error events. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Processing runs outside the UI thread; stale generations and malformed messages cannot update active results. Real workers reject protocol mismatch/oversize/duplicate frames; bounded transfer credits and stale-generation suppression pass race fixtures. Task-level yields, bounded progress/page credits and measured transfer/Wasm copies preserve cancellation responsiveness; transferring a buffer is not a universal zero-copy guarantee. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.25.0 implementation stop reached. Run pentest for this exact commit.

## v0.26.0 — Cancellation lifecycle

**Status:** planned.

**Setup:** baseline 0.25.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Cancellation lifecycle.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Implement cooperative cancellation and browser worker termination/recreation for non-cooperative work. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** A cancelled job cannot publish a successful artifact; cancellation leaves the next job usable. Measure cooperative cancellation and hard termination; cancel at input/output waits, provider completion, and publication with no surviving child work. A starved/noncooperative worker is terminated by the UI supervisor; host-owned manifests reconcile staging because terminate does not run cleanup handlers. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.26.0 implementation stop reached. Run pentest for this exact commit.

## v0.27.0 — Browser privacy and secret publication

**Status:** planned.

**Setup:** baseline 0.26.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Browser privacy and secret publication.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Implement sensitivity joins and opaque ephemeral handles at browser serialization/UI/storage boundaries before rich viewers or crypto. Add explicit reveal/export grants, generation rechecks and supervisor-owned cleanup; browser-entered user keys never require OpenBao/upload. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Sentinel inputs/keys/derived material stay absent from IndexedDB/OPFS/CacheStorage, history, URLs, clipboard, search, diagnostics and network by default. Revoked disclosure/stale page/cancel/crash tests deny publication; document unavoidable DOM/JS copies and no guaranteed erasure. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.27.0 implementation stop reached. Run pentest for this exact commit.

## v0.28.0 — First browser workbench

**Status:** planned.

**Setup:** baseline 0.27.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** First browser workbench.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Build accessible input, recipe and output panes, operation search and a manual Run button. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Keyboard-only use completes a sample recipe; raw output is never interpreted as trusted HTML. Run input/recipe/output tasks in actual browsers; importing never runs, hostile output is inert, and transformations generate no payload upload/persistence. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.28.0 implementation stop reached. Run pentest for this exact commit.

## v0.29.0 — Loopback API host

**Status:** planned.

**Setup:** baseline 0.28.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Loopback API host.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Expose capabilities, catalogue, validate, run, status and cancel through a replaceable HTTP adapter. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Local and HTTP clients pass the same contract suite; the development server binds loopback by default. Serve application commands on loopback using an owned HTTP adapter; test framing/body/deadline/disconnect limits and domain-error mapping. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.29.0 implementation stop reached. Run pentest for this exact commit.

## v0.30.0 — Pack manifest and resource contract

**Status:** planned.

**Setup:** baseline 0.29.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Pack manifest and resource contract.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Define a minimal first-party browser-pack manifest before heavy feasibility providers: operation/engine/ABI revisions, source/hash/license, target/import/capability requirements and transfer/decompressed/compile/memory ceilings. Keep third-party plugin admission separate. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Tampered, incompatible, unlicensed, oversized and forbidden-import pack fixtures reject before activation. Disabled packs have no default dependency or bundle cost; declared required operations remain visible when a pack is absent. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.30.0 implementation stop reached. Run pentest for this exact commit.

## v0.31.0 — Minimal lazy browser pack loader

**Status:** planned.

**Setup:** baseline 0.30.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Minimal lazy browser pack loader.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Implement bounded same-origin loading/installation of reviewed first-party packs in a Dedicated Worker, with cancellation, atomic activation and an explicit selected offline set. Qualify one small pack before large providers; later extensibility passes expand the catalogue/plugin model. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Real browsers exercise failed/interrupted downloads, hash/ABI mismatch, cancellation, quota and offline absence. A failed activation preserves the previous pack set; loading never uploads payloads or fetches hidden CDN assets; measure decode/compile/instantiate/copy and retained-memory costs. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.31.0 implementation stop reached. Run pentest for this exact commit.

## v0.32.0 — Regex compatibility feasibility

**Status:** planned.

**Setup:** baseline 0.31.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Regex compatibility feasibility.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.12.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Qualify regex compatibility in isolated native/browser spikes; record exact semantics, current provider versions, licenses, dependencies, limits and gaps. No production capability is implied. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Record dialect, licensing, dependencies, limits and remaining gaps; unsupported candidates do not become assumed dependencies. Each of regex/query/YARA/crypto/compression/disassembly/OCR has a separate native/browser spike, exact license/provider/limit report, and explicit unresolved gaps. Large browser candidates use the earlier reviewed pack-loader contract; historical provider issues are feasibility warnings, not current support determinations. Non-Rust provider/executable exceptions require explicit project approval. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.32.0 implementation stop reached. Run pentest for this exact commit.

## v0.33.0 — Query-language feasibility

**Status:** planned.

**Setup:** baseline 0.32.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Query-language feasibility.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.12.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Qualify query-language in isolated native/browser spikes; record exact semantics, current provider versions, licenses, dependencies, limits and gaps. No production capability is implied. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Record dialect, licensing, dependencies, limits and remaining gaps; unsupported candidates do not become assumed dependencies. Each of regex/query/YARA/crypto/compression/disassembly/OCR has a separate native/browser spike, exact license/provider/limit report, and explicit unresolved gaps. Large browser candidates use the earlier reviewed pack-loader contract; historical provider issues are feasibility warnings, not current support determinations. Non-Rust provider/executable exceptions require explicit project approval. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.33.0 implementation stop reached. Run pentest for this exact commit.

## v0.34.0 — YARA feasibility

**Status:** planned.

**Setup:** baseline 0.33.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** YARA feasibility.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.12.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Qualify yara in isolated native/browser spikes; record exact semantics, current provider versions, licenses, dependencies, limits and gaps. No production capability is implied. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Record dialect, licensing, dependencies, limits and remaining gaps; unsupported candidates do not become assumed dependencies. Each of regex/query/YARA/crypto/compression/disassembly/OCR has a separate native/browser spike, exact license/provider/limit report, and explicit unresolved gaps. Large browser candidates use the earlier reviewed pack-loader contract; historical provider issues are feasibility warnings, not current support determinations. Non-Rust provider/executable exceptions require explicit project approval. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.34.0 implementation stop reached. Run pentest for this exact commit.

## v0.35.0 — Cryptographic-provider feasibility

**Status:** planned.

**Setup:** baseline 0.34.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Cryptographic-provider feasibility.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.12.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Qualify cryptographic-provider in isolated native/browser spikes; record exact semantics, current provider versions, licenses, dependencies, limits and gaps. No production capability is implied. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Record dialect, licensing, dependencies, limits and remaining gaps; unsupported candidates do not become assumed dependencies. Each of regex/query/YARA/crypto/compression/disassembly/OCR has a separate native/browser spike, exact license/provider/limit report, and explicit unresolved gaps. Large browser candidates use the earlier reviewed pack-loader contract; historical provider issues are feasibility warnings, not current support determinations. Non-Rust provider/executable exceptions require explicit project approval. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.35.0 implementation stop reached. Run pentest for this exact commit.

## v0.36.0 — Compression-provider feasibility

**Status:** planned.

**Setup:** baseline 0.35.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Compression-provider feasibility.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.12.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Qualify compression-provider in isolated native/browser spikes; record exact semantics, current provider versions, licenses, dependencies, limits and gaps. No production capability is implied. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Record dialect, licensing, dependencies, limits and remaining gaps; unsupported candidates do not become assumed dependencies. Each of regex/query/YARA/crypto/compression/disassembly/OCR has a separate native/browser spike, exact license/provider/limit report, and explicit unresolved gaps. Large browser candidates use the earlier reviewed pack-loader contract; historical provider issues are feasibility warnings, not current support determinations. Non-Rust provider/executable exceptions require explicit project approval. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.36.0 implementation stop reached. Run pentest for this exact commit.

## v0.37.0 — Disassembly feasibility

**Status:** planned.

**Setup:** baseline 0.36.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Disassembly feasibility.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.12.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Qualify disassembly in isolated native/browser spikes; record exact semantics, current provider versions, licenses, dependencies, limits and gaps. No production capability is implied. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Record dialect, licensing, dependencies, limits and remaining gaps; unsupported candidates do not become assumed dependencies. Each of regex/query/YARA/crypto/compression/disassembly/OCR has a separate native/browser spike, exact license/provider/limit report, and explicit unresolved gaps. Large browser candidates use the earlier reviewed pack-loader contract; historical provider issues are feasibility warnings, not current support determinations. Non-Rust provider/executable exceptions require explicit project approval. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.37.0 implementation stop reached. Run pentest for this exact commit.

## v0.38.0 — OCR and media feasibility

**Status:** planned.

**Setup:** baseline 0.37.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OCR and media feasibility.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.12.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Qualify ocr and media in isolated native/browser spikes; record exact semantics, current provider versions, licenses, dependencies, limits and gaps. No production capability is implied. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Record dialect, licensing, dependencies, limits and remaining gaps; unsupported candidates do not become assumed dependencies. Each of regex/query/YARA/crypto/compression/disassembly/OCR has a separate native/browser spike, exact license/provider/limit report, and explicit unresolved gaps. Large browser candidates use the earlier reviewed pack-loader contract; historical provider issues are feasibility warnings, not current support determinations. Non-Rust provider/executable exceptions require explicit project approval. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.38.0 implementation stop reached. Run pentest for this exact commit.

## v0.39.0 — Differential harness

**Status:** planned.

**Setup:** baseline 0.38.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Differential harness.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Build a reference runner, fixture provenance rules and partitioned-input comparison harness. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Positive, negative, binary and Unicode cases run reproducibly; upstream bugs are recorded rather than blindly copied. Run pinned reference fixtures through independently captured oracle and engine; deliberate semantic corruption fails the comparator, with exact source hashes. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.39.0 implementation stop reached. Run pentest for this exact commit.

## v0.40.0 — First threat review

**Status:** planned.

**Setup:** baseline 0.39.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** First threat review.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Review imported recipes, worker boundaries, preview escaping, logging and dependency graph. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** No payload telemetry or automatic network side effects; hostile samples produce bounded failures. Enumerate assets/trust boundaries and concrete abuse fixtures; each exposed seed behavior has tested negative controls and finding disposition. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.40.0 implementation stop reached. Run pentest for this exact commit.

## v0.41.0 — Usable vertical alpha

**Status:** planned.

**Setup:** baseline 0.40.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Usable vertical alpha.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Package a small offline-capable workbench with recipe save/load, loopback API examples and developer operation guide. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** A fresh clone builds and runs without sibling projects or a database; phase A contracts are demonstrated end to end. Complete the declared seed workflow in supported browsers and native API; all mandatory alpha inventory rows have runtime evidence and no hidden remote dependency. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.41.0 implementation stop reached. Run pentest for this exact commit.

## v0.42.0 — Performance baseline and regression profiles

**Status:** planned.

**Setup:** baseline 0.41.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Performance baseline and regression profiles.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** After the actual alpha, freeze benchmark hardware/corpora, per-profile numeric envelopes and reproducible engine versus File/worker/Wasm/viewer measurements. Start with UI p95 <100 ms and cooperative cancel p95 <200 ms goals; freeze bundle/hard-kill caps from real measurements. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Record correctness and source/artifact/browser/tool identities, repetitions, cold/warm p50/p95/p99/max, JS/Wasm/RSS/disk/copy memory and cleanup. Goals are unmet until measured; budget regressions and event floods fail the gate. No seed measurement claims full-provider/large-input performance. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.42.0 implementation stop reached. Run pentest for this exact commit.
