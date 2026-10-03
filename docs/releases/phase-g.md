# Phase G: Compression and archives

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

## v0.145.0 — Compression provider contract

**Status:** planned.

**Setup:** baseline 0.144.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Compression provider contract.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Standardize streaming encoder/decoder state, trailing-data policy, dictionary limits and byte counters. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Truncated streams and short output buffers resume or fail deterministically without hiding retained state. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.145.0 implementation stop reached. Run pentest for this exact commit.

## v0.146.0 — Deflate

**Status:** planned.

**Setup:** baseline 0.145.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Deflate.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add raw Deflate compression/decompression and reference parameter mapping. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Stored, fixed and dynamic blocks pass reference fixtures across all tested chunk boundaries. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.146.0 implementation stop reached. Run pentest for this exact commit.

## v0.147.0 — Zlib

**Status:** planned.

**Setup:** baseline 0.146.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Zlib.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add wrappers, dictionary handling and checksums with strict and compatibility framing policies. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Header, dictionary-ID and checksum failures are distinguished; limits include dictionary memory. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.147.0 implementation stop reached. Run pentest for this exact commit.

## v0.148.0 — Gzip

**Status:** planned.

**Setup:** baseline 0.147.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Gzip.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add gzip metadata, concatenated members, checksums and deterministic-output options. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Member boundaries and trailing garbage follow documented semantics; preview cannot skip final integrity validation. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.148.0 implementation stop reached. Run pentest for this exact commit.

## v0.149.0 — Bzip2

**Status:** planned.

**Setup:** baseline 0.148.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Bzip2.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Deliver required compression/decompression variants through a reviewed provider. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Block limits, corrupt indexes and expansion attacks are tested in browser and native builds. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.149.0 implementation stop reached. Run pentest for this exact commit.

## v0.150.0 — LZMA and containers

**Status:** planned.

**Setup:** baseline 0.149.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** LZMA and containers.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add the inventory’s LZMA/container variants with configurable but bounded dictionaries. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Dictionary size is validated before allocation; unsupported container variants remain named gaps. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.150.0 implementation stop reached. Run pentest for this exact commit.

## v0.151.0 — LZ4

**Status:** planned.

**Setup:** baseline 0.150.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** LZ4.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add required block/frame operations, checksums and content-size handling. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Frame flags, dictionaries, short blocks and independent/dependent block behavior match fixtures. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.151.0 implementation stop reached. Run pentest for this exact commit.

## v0.152.0 — LZ string encodings

**Status:** planned.

**Setup:** baseline 0.151.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** LZ string encodings.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add LZ-based string and transport variants present in the reference. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** UTF-16/code-unit behavior is reproduced explicitly rather than replaced with a superficially similar byte codec. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.152.0 implementation stop reached. Run pentest for this exact commit.

## v0.153.0 — Platform compression families

**Status:** planned.

**Setup:** baseline 0.152.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Platform compression families.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add NT/XPRESS and other inventoried platform-specific formats without calling local shell utilities. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Published/reference samples and malformed streams work identically in the browser and native engine. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.153.0 implementation stop reached. Run pentest for this exact commit.

## v0.154.0 — ZIP listing and extraction

**Status:** planned.

**Setup:** baseline 0.153.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** ZIP listing and extraction.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add multi-entry archives, data descriptors, name encodings and password variants required by inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Entry count, expansion, encryption errors and path normalization are bounded; extraction never writes arbitrary host paths. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.154.0 implementation stop reached. Run pentest for this exact commit.

## v0.155.0 — ZIP creation

**Status:** planned.

**Setup:** baseline 0.154.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** ZIP creation.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add selected compression methods, metadata mapping and deterministic archive options. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Round trips preserve required names and bytes; archives larger than basic format limits use supported extensions or fail clearly. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.155.0 implementation stop reached. Run pentest for this exact commit.

## v0.156.0 — TAR operations

**Status:** planned.

**Setup:** baseline 0.155.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** TAR operations.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add listing, extraction and creation for required header variants and links. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Traversal, absolute paths, devices, symlinks and hardlinks cannot bypass the artifact namespace. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.156.0 implementation stop reached. Run pentest for this exact commit.

## v0.157.0 — Nested archive workflows

**Status:** planned.

**Setup:** baseline 0.156.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Nested archive workflows.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Connect archive outputs to file collections and bounded recursive processing. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Total nesting, members, bytes and work are capped across the whole job, not reset per nested archive. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.157.0 implementation stop reached. Run pentest for this exact commit.

## v0.158.0 — Archive UX and integrity

**Status:** planned.

**Setup:** baseline 0.157.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Archive UX and integrity.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add per-member inspection, safe selection, artifact exports and verification status. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Incomplete or checksum-failed outputs never appear as verified; selected member export preserves authorization. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.158.0 implementation stop reached. Run pentest for this exact commit.

## v0.159.0 — Compression qualification

**Status:** planned.

**Setup:** baseline 0.158.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Compression qualification.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Close all compression inventory gaps and run corpus-based fuzzing and expansion stress tests. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Every provider declares measured memory profiles; unsupported methods cannot be omitted from the parity denominator. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.159.0 implementation stop reached. Run pentest for this exact commit.
