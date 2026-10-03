# Phase D: Modern browser workbench

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

Verification checklists apply only to introduced or retained behavior in the reviewed bounded scope. Record absent later capabilities as pending with numbered owners; contract fixtures never attest their runtime PASS. A prerequisite needed by this pass must be implemented and verified first, rather than deferred. Every future owner still owes its full acceptance before exposure/1.0.

## v0.88.0 — Workspace shell

**Status:** planned.

**Setup:** baseline 0.87.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Workspace shell.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add responsive resizable panes, themes, remembered non-sensitive preferences and command navigation. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Layout remains usable at narrow widths and high zoom; theme preference does not capture input content. Workspace tasks remain keyboard-accessible and responsive during worker load; local/remote/persistence effects are visibly distinct. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.88.0 implementation stop reached. Run pentest for this exact commit.

## v0.89.0 — Recipe editing

**Status:** planned.

**Setup:** baseline 0.88.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Recipe editing.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add drag/drop with keyboard alternatives, undo/redo, duplicate, disable, reorder and parameter validation. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Editing preserves stable node identities and annotations; purely visual movement does not rerun processing. Undo/redo/reorder/disable/import edits preserve one IR and semantic revisions; secret parameters/history are redacted and imports remain inert. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.89.0 implementation stop reached. Run pentest for this exact commit.

## v0.90.0 — Generated operation inspector

**Status:** planned.

**Setup:** baseline 0.89.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Generated operation inspector.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Render argument forms, examples, defaults, capability warnings and semantic-version details from descriptors. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** New descriptors require no handwritten duplicate API schema or form definition for supported field types. Typed forms match descriptor defaults/enums/ranges; invalid values fail before running, and secret fields never enter ordinary saved UI state. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.90.0 implementation stop reached. Run pentest for this exact commit.

## v0.91.0 — Safe automatic preview

**Status:** planned.

**Setup:** baseline 0.90.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Safe automatic preview.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add debounced, bounded previews for permitted pure operations and an explicit full-run action. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Imported recipes and effectful/expensive operations never start merely because they were pasted or opened. Only approved pure cheap previews autorun; sample/input/output/work caps hold, stale generations drop, and reductions are visibly partial. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.91.0 implementation stop reached. Run pentest for this exact commit.

## v0.92.0 — Paged text viewer

**Status:** planned.

**Setup:** baseline 0.91.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Paged text viewer.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add incremental decoding, line indexing, search, selection and bounded text previews. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Large single lines and invalid UTF sequences do not force a full document string allocation. Page through split codepoints and extremely long lines at exact offsets; bounded decoding/cache/search survives cancellation without whole-file strings. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.92.0 implementation stop reached. Run pentest for this exact commit.

## v0.93.0 — Virtual hex viewer

**Status:** planned.

**Setup:** baseline 0.92.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Virtual hex viewer.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add range-backed hex/ASCII viewing, exact offset navigation, selection and export. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Offsets above 32-bit ranges remain correct; UI memory is measured separately from underlying artifact storage. Use synthetic range/DTO boundaries beyond 2^53 plus actual feasible large-artifact pages; offsets stay lossless, out-of-range JS indices reject, and DOM/cache/export work is bounded. No multi-petabyte browser file claim follows from synthetic offset tests. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.93.0 implementation stop reached. Run pentest for this exact commit.

## v0.94.0 — Structured and table viewers

**Status:** planned.

**Setup:** baseline 0.93.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Structured and table viewers.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add lossless tree/table views, typed cell rendering, pagination and safe copy/export. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Large integers and binary values remain exact; untrusted strings cannot inject markup or spreadsheet formulas without warning. Lossless numbers/records and bounded nesting/rows render as inert DOM; hostile fields, infinite tables, and stale page updates cannot escape limits. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.94.0 implementation stop reached. Run pentest for this exact commit.

## v0.95.0 — Graph editor

**Status:** planned.

**Setup:** baseline 0.94.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Graph editor.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add an optional visual graph for typed ports, branches, joins and structured control regions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Invalid edges are rejected by the engine compiler, not only by visual UI rules; keyboard editing remains possible. Linear/graph editing round trips through one IR; loop regions remain explicit and keyboard/DOM alternatives cover essential graph tasks. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.95.0 implementation stop reached. Run pentest for this exact commit.

## v0.96.0 — Debugging controls

**Status:** planned.

**Setup:** baseline 0.95.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Debugging controls.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add breakpoints, single-step, node diagnostics, intermediate inspection and cancellation status. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Viewing a preview does not prematurely terminate a full output stream or leak a secret artifact into history. Breakpoints/single-step/cached steps preserve ordering and generation; inspection caps and sensitivity rules prevent history/preview leakage. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.96.0 implementation stop reached. Run pentest for this exact commit.

## v0.97.0 — Offset provenance UI

**Status:** planned.

**Setup:** baseline 0.96.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Offset provenance UI.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Show source/output correspondences where transformations provide them, including encoded-byte relationships. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Non-local or lossy transforms say unmappable/approximate explicitly rather than invent exact positions. Exact/approximate/unavailable mappings are distinguished; selection through expanding/contracting operations never invents source positions. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.97.0 implementation stop reached. Run pentest for this exact commit.

## v0.98.0 — Multiple inputs and batches

**Status:** planned.

**Setup:** baseline 0.97.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Multiple inputs and batches.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add named inputs, file sets, deterministic batch ordering and per-item error policy. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** A failed batch item cannot silently discard other results; files are not duplicated into UI state. Bound concurrent inputs, batch queues, aggregate bytes and outputs; one failed/cancelled item follows declared isolation/ordering policy. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.98.0 implementation stop reached. Run pentest for this exact commit.

## v0.99.0 — Local recipe library

**Status:** planned.

**Setup:** baseline 0.98.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Local recipe library.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add folders/tags, favourites, search, revision history and exportable local workspaces. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Persistence is opt-in for sensitive data; recipe export omits secrets and bulk inputs by default. Opt-in local recipe saves survive transaction completion and migration; payload literals/secrets are rejected/redacted and default runs persist nothing. Recipe documents may contain payload literals and secret parameters: inspect/redact/reject them at serialization, not just metadata projection. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.99.0 implementation stop reached. Run pentest for this exact commit.

## v0.100.0 — Sharing and imports

**Status:** planned.

**Setup:** baseline 0.99.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Sharing and imports.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Support recipe-only links/files, explicit input inclusion, compatibility links and import previews. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Users see capabilities and embedded data before running; history and URL exposure are clearly distinguished. Hostile/unknown/versioned imports fail explicitly; URL sharing excludes payload/secrets and requires a deliberate action, with no import autorun. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.100.0 implementation stop reached. Run pentest for this exact commit.

## v0.101.0 — Offline packaging

**Status:** planned.

**Setup:** baseline 0.100.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Offline packaging.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Cache versioned app assets and selected operation packs; provide a complete offline distribution option. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Offline operation availability is visible; service-worker upgrades cannot mix incompatible engine and pack revisions. A selected complete offline pack set runs with networking disabled; integrity/versions/licenses agree and no model/font/CDN request escapes. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.101.0 implementation stop reached. Run pentest for this exact commit.

## v0.102.0 — Browser accessibility gate

**Status:** planned.

**Setup:** baseline 0.101.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Browser accessibility gate.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Test keyboard, screen reader, focus, reduced motion, high contrast and touch-friendly responsive layouts. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Core tasks work without canvas-only controls, GPU acceleration, shared memory or a mouse. Essential real-browser workflows pass keyboard, screen-reader, zoom, narrow-layout and error recovery checks; graph/canvas have alternatives. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.102.0 implementation stop reached. Run pentest for this exact commit.
