# Phase G: Compression and archives

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

Verification checklists apply only to introduced or retained behavior in the reviewed bounded scope. Record absent later capabilities as pending with numbered owners; contract fixtures never attest their runtime PASS. A prerequisite needed by this pass must be implemented and verified first, rather than deferred. Every future owner still owes its full acceptance before exposure/1.0.

## v0.158.0 — Compression provider contract

**Status:** planned.

**Setup:** baseline 0.157.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Compression provider contract.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Standardize streaming encoder/decoder state, trailing-data policy, dictionary limits and byte counters. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Truncated streams and short output buffers resume or fail deterministically without hiding retained state. Provider adapters expose resource/stream/error contracts; disabled codec features leave core graph and initial bundle independent. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.158.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.159.0 — Deflate

**Status:** planned.

**Setup:** baseline 0.158.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Deflate.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add raw Deflate compression/decompression and reference parameter mapping. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Stored, fixed and dynamic blocks pass reference fixtures across all tested chunk boundaries. Raw Deflate vectors test malformed/truncated streams, sliding-window memory, short outputs and total expansion/cancellation limits. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.159.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.160.0 — Zlib

**Status:** planned.

**Setup:** baseline 0.159.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Zlib.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add wrappers, dictionary handling and checksums with strict and compatibility framing policies. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Header, dictionary-ID and checksum failures are distinguished; limits include dictionary memory. Zlib header/dictionary/checksum variants and bad trailers pass independent vectors; no successful artifact precedes declared integrity completion. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.160.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.161.0 — Gzip

**Status:** planned.

**Setup:** baseline 0.160.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Gzip.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add gzip metadata, concatenated members, checksums and deterministic-output options. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Member boundaries and trailing garbage follow documented semantics; preview cannot skip final integrity validation. Gzip members/headers/trailers/concatenation are explicit; corrupt CRC/ISIZE, oversized metadata and expansion bombs fail within budgets. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.161.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.162.0 — Bzip2

**Status:** planned.

**Setup:** baseline 0.161.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Bzip2.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Deliver required compression/decompression variants through a reviewed provider. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Block limits, corrupt indexes and expansion attacks are tested in browser and native builds. Bzip2 block/work/memory declarations survive corrupt/truncated corpora and tiny windows; hard cancellation covers noncooperative provider calls. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.162.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.163.0 — LZMA and containers

**Status:** planned.

**Setup:** baseline 0.162.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** LZMA and containers.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add the inventory’s LZMA/container variants with configurable but bounded dictionaries. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Dictionary size is validated before allocation; unsupported container variants remain named gaps. Each LZMA/container variant enforces advertised dictionary/size limits before allocation; corrupt headers, unknown sizes and nested expansion are bounded. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.163.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.164.0 — LZ4

**Status:** planned.

**Setup:** baseline 0.163.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** LZ4.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add required block/frame operations, checksums and content-size handling. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Frame flags, dictionaries, short blocks and independent/dependent block behavior match fixtures. LZ4 block/frame/checksum/dictionary variants pass independent vectors; malformed offset/length arithmetic and expansion limits reject correctly. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.164.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.165.0 — LZ string encodings

**Status:** planned.

**Setup:** baseline 0.164.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** LZ string encodings.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add LZ-based string and transport variants present in the reference. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** UTF-16/code-unit behavior is reproduced explicitly rather than replaced with a superficially similar byte codec. LZ-string encoding variants preserve exact upstream text/code-unit semantics; malformed tails and output-growth ceilings pass browser/native fixtures. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.165.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.166.0 — Platform compression families

**Status:** planned.

**Setup:** baseline 0.165.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Platform compression families.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add NT/XPRESS and other inventoried platform-specific formats without calling local shell utilities. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Published/reference samples and malformed streams work identically in the browser and native engine. Every required platform-compression family has a separate provider/variant scope and actual target vectors; native-only helpers remain browser gaps. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.166.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.167.0 — ZIP listing and extraction

**Status:** planned.

**Setup:** baseline 0.166.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** ZIP listing and extraction.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add multi-entry archives, data descriptors, name encodings and password variants required by inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Entry count, expansion, encryption errors and path normalization are bounded; extraction never writes arbitrary host paths. ZIP listing/extraction checks entries, total/per-entry bytes, paths, duplicate names, links, sparse/overlap/encryption flags and corrupt directories. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.167.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.168.0 — ZIP creation

**Status:** planned.

**Setup:** baseline 0.167.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** ZIP creation.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add selected compression methods, metadata mapping and deterministic archive options. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Round trips preserve required names and bytes; archives larger than basic format limits use supported extensions or fail clearly. ZIP creation round trips with an independent reader; ordering/metadata/defaults are frozen and cancellation/partial output never publishes success. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.168.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.169.0 — TAR operations

**Status:** planned.

**Setup:** baseline 0.168.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** TAR operations.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add listing, extraction and creation for required header variants and links. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Traversal, absolute paths, devices, symlinks and hardlinks cannot bypass the artifact namespace. TAR variants test traversal, hard/symbolic links, sparse files, malformed sizes and entry/expanded-byte ceilings with inert extraction paths. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.169.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.170.0 — Nested archive workflows

**Status:** planned.

**Setup:** baseline 0.169.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Nested archive workflows.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Connect archive outputs to file collections and bounded recursive processing. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Total nesting, members, bytes and work are capped across the whole job, not reset per nested archive. Recursive archives share whole-run depth/work/byte/entry/artifact limits; nested ratio tricks cannot reset budgets between containers. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.170.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.171.0 — Archive UX and integrity

**Status:** planned.

**Setup:** baseline 0.170.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Archive UX and integrity.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add per-member inspection, safe selection, artifact exports and verification status. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Incomplete or checksum-failed outputs never appear as verified; selected member export preserves authorization. Archive listing/pages distinguish provisional/verified results; corrupt entries, unsafe names and failed extraction remain inaccessible artifacts. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.171.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.172.0 — Compression qualification

**Status:** planned.

**Setup:** baseline 0.171.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Compression qualification.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Close all compression inventory gaps and run corpus-based fuzzing and expansion stress tests. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Every provider declares measured memory profiles; unsupported methods cannot be omitted from the parity denominator. All codec/archive/argument/target rows pass independent vectors and bomb/truncation/path/cancel tests under measured resource envelopes. Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.172.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.
