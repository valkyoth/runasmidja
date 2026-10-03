# Phase A: Foundation and useful vertical slice

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

## v0.7.0 — Executable seed

**Status:** planned.

**Setup:** baseline 0.6.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Executable seed.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Pin Rust 1.99.0; create kernel, engine, browser and native host packages; run one hex operation from a real browser worker. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Native and browser fixtures agree; the example needs neither PostgreSQL nor a sibling repository. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.7.0 implementation stop reached. Run pentest for this exact commit.

## v0.8.0 — Reference baseline

**Status:** planned.

**Setup:** baseline 0.7.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Reference baseline.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Resolve the reviewed tag and adopted current-source deltas to immutable commits; inventory operations, arguments, workflow features and licenses, including observed certificate-bundle parsing. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Every discovered operation has a stable tracking record; the reference commit and file hashes are recorded, not guessed. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.8.0 implementation stop reached. Run pentest for this exact commit.

## v0.9.0 — Application contracts

**Status:** planned.

**Setup:** baseline 0.8.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Application contracts.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Define operation IDs, semantic revisions, structured errors, recipe envelopes, artifact references and local EngineClient commands. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Round-trip tests reject unknown required fields and preserve large offsets without JavaScript number truncation. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.9.0 implementation stop reached. Run pentest for this exact commit.

## v0.10.0 — Portable kernel

**Status:** planned.

**Setup:** baseline 0.9.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Portable kernel.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Separate no_std/no-alloc kernel, alloc-enabled compiler and std hosts; establish feature and target matrices. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Bare-metal-style compile checks catch std leakage; unsafe code is forbidden in first-party portable core by default. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.10.0 implementation stop reached. Run pentest for this exact commit.

## v0.11.0 — Bounded buffer contract

**Status:** planned.

**Setup:** baseline 0.10.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Bounded buffer contract.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add caller-provided input/output windows, consumed/produced counts, partial progress, cancellation checkpoints and finish states. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Zero-sized windows, short writes, empty inputs and repeated finish calls have defined results without panics. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.11.0 implementation stop reached. Run pentest for this exact commit.

## v0.12.0 — Operation descriptors

**Status:** planned.

**Setup:** baseline 0.11.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Operation descriptors.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Define typed arguments, defaults, help, execution class, secret fields and capabilities; generate a minimal catalogue. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** One new operation registers once and appears in catalogue, validation, documentation and generated argument controls. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.12.0 implementation stop reached. Run pentest for this exact commit.

## v0.13.0 — Linear execution

**Status:** planned.

**Setup:** baseline 0.12.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Linear execution.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Compile and run a sequence of hex, text and XOR operations with explicit byte/text conversion. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Chunk partitions do not alter outputs; invalid intermediate types fail before execution where statically knowable. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.13.0 implementation stop reached. Run pentest for this exact commit.

## v0.14.0 — Worker protocol

**Status:** planned.

**Setup:** baseline 0.13.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Worker protocol.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Introduce versioned worker messages, input transfers, job generations, progress and error events. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Processing runs outside the UI thread; stale generations and malformed messages cannot update active results. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.14.0 implementation stop reached. Run pentest for this exact commit.

## v0.15.0 — Cancellation lifecycle

**Status:** planned.

**Setup:** baseline 0.14.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Cancellation lifecycle.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Implement cooperative cancellation and browser worker termination/recreation for non-cooperative work. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** A cancelled job cannot publish a successful artifact; cancellation leaves the next job usable. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.15.0 implementation stop reached. Run pentest for this exact commit.

## v0.16.0 — First browser workbench

**Status:** planned.

**Setup:** baseline 0.15.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** First browser workbench.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Build accessible input, recipe and output panes, operation search and a manual Run button. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Keyboard-only use completes a sample recipe; raw output is never interpreted as trusted HTML. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.16.0 implementation stop reached. Run pentest for this exact commit.

## v0.17.0 — Loopback API host

**Status:** planned.

**Setup:** baseline 0.16.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Loopback API host.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Expose capabilities, catalogue, validate, run, status and cancel through a replaceable HTTP adapter. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Local and HTTP clients pass the same contract suite; the development server binds loopback by default. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.17.0 implementation stop reached. Run pentest for this exact commit.

## v0.18.0 — Regex compatibility feasibility

**Status:** planned.

**Setup:** baseline 0.17.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Regex compatibility feasibility.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.12.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Qualify regex compatibility in isolated native/browser spikes; record exact semantics, current provider versions, licenses, dependencies, limits and gaps. No production capability is implied. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Record dialect, licensing, dependencies, limits and remaining gaps; unsupported candidates do not become assumed dependencies. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.18.0 implementation stop reached. Run pentest for this exact commit.

## v0.19.0 — Query-language feasibility

**Status:** planned.

**Setup:** baseline 0.18.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Query-language feasibility.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.12.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Qualify query-language in isolated native/browser spikes; record exact semantics, current provider versions, licenses, dependencies, limits and gaps. No production capability is implied. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Record dialect, licensing, dependencies, limits and remaining gaps; unsupported candidates do not become assumed dependencies. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.19.0 implementation stop reached. Run pentest for this exact commit.

## v0.20.0 — YARA feasibility

**Status:** planned.

**Setup:** baseline 0.19.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** YARA feasibility.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.12.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Qualify yara in isolated native/browser spikes; record exact semantics, current provider versions, licenses, dependencies, limits and gaps. No production capability is implied. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Record dialect, licensing, dependencies, limits and remaining gaps; unsupported candidates do not become assumed dependencies. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.20.0 implementation stop reached. Run pentest for this exact commit.

## v0.21.0 — Cryptographic-provider feasibility

**Status:** planned.

**Setup:** baseline 0.20.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Cryptographic-provider feasibility.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.12.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Qualify cryptographic-provider in isolated native/browser spikes; record exact semantics, current provider versions, licenses, dependencies, limits and gaps. No production capability is implied. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Record dialect, licensing, dependencies, limits and remaining gaps; unsupported candidates do not become assumed dependencies. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.21.0 implementation stop reached. Run pentest for this exact commit.

## v0.22.0 — Compression-provider feasibility

**Status:** planned.

**Setup:** baseline 0.21.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Compression-provider feasibility.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.12.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Qualify compression-provider in isolated native/browser spikes; record exact semantics, current provider versions, licenses, dependencies, limits and gaps. No production capability is implied. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Record dialect, licensing, dependencies, limits and remaining gaps; unsupported candidates do not become assumed dependencies. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.22.0 implementation stop reached. Run pentest for this exact commit.

## v0.23.0 — Disassembly feasibility

**Status:** planned.

**Setup:** baseline 0.22.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Disassembly feasibility.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.12.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Qualify disassembly in isolated native/browser spikes; record exact semantics, current provider versions, licenses, dependencies, limits and gaps. No production capability is implied. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Record dialect, licensing, dependencies, limits and remaining gaps; unsupported candidates do not become assumed dependencies. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.23.0 implementation stop reached. Run pentest for this exact commit.

## v0.24.0 — OCR and media feasibility

**Status:** planned.

**Setup:** baseline 0.23.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OCR and media feasibility.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.12.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Qualify ocr and media in isolated native/browser spikes; record exact semantics, current provider versions, licenses, dependencies, limits and gaps. No production capability is implied. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Record dialect, licensing, dependencies, limits and remaining gaps; unsupported candidates do not become assumed dependencies. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.24.0 implementation stop reached. Run pentest for this exact commit.

## v0.25.0 — Differential harness

**Status:** planned.

**Setup:** baseline 0.24.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Differential harness.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Build a reference runner, fixture provenance rules and partitioned-input comparison harness. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Positive, negative, binary and Unicode cases run reproducibly; upstream bugs are recorded rather than blindly copied. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.25.0 implementation stop reached. Run pentest for this exact commit.

## v0.26.0 — First threat review

**Status:** planned.

**Setup:** baseline 0.25.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** First threat review.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Review imported recipes, worker boundaries, preview escaping, logging and dependency graph. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** No payload telemetry or automatic network side effects; hostile samples produce bounded failures. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.26.0 implementation stop reached. Run pentest for this exact commit.

## v0.27.0 — Usable vertical alpha

**Status:** planned.

**Setup:** baseline 0.26.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Usable vertical alpha.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Package a small offline-capable workbench with recipe save/load, loopback API examples and developer operation guide. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** A fresh clone builds and runs without sibling projects or a database; phase A contracts are demonstrated end to end. Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.27.0 implementation stop reached. Run pentest for this exact commit.
