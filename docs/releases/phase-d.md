# Phase D: Modern browser workbench

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

## v0.73.0 — Workspace shell

**Status:** planned.

**Setup:** baseline 0.72.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Workspace shell.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add responsive resizable panes, themes, remembered non-sensitive preferences and command navigation. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Layout remains usable at narrow widths and high zoom; theme preference does not capture input content. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.73.0 implementation stop reached. Run pentest for this exact commit.

## v0.74.0 — Recipe editing

**Status:** planned.

**Setup:** baseline 0.73.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Recipe editing.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add drag/drop with keyboard alternatives, undo/redo, duplicate, disable, reorder and parameter validation. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Editing preserves stable node identities and annotations; purely visual movement does not rerun processing. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.74.0 implementation stop reached. Run pentest for this exact commit.

## v0.75.0 — Generated operation inspector

**Status:** planned.

**Setup:** baseline 0.74.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Generated operation inspector.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Render argument forms, examples, defaults, capability warnings and semantic-version details from descriptors. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** New descriptors require no handwritten duplicate API schema or form definition for supported field types. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.75.0 implementation stop reached. Run pentest for this exact commit.

## v0.76.0 — Safe automatic preview

**Status:** planned.

**Setup:** baseline 0.75.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Safe automatic preview.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add debounced, bounded previews for permitted pure operations and an explicit full-run action. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Imported recipes and effectful/expensive operations never start merely because they were pasted or opened. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.76.0 implementation stop reached. Run pentest for this exact commit.

## v0.77.0 — Paged text viewer

**Status:** planned.

**Setup:** baseline 0.76.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Paged text viewer.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add incremental decoding, line indexing, search, selection and bounded text previews. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Large single lines and invalid UTF sequences do not force a full document string allocation. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.77.0 implementation stop reached. Run pentest for this exact commit.

## v0.78.0 — Virtual hex viewer

**Status:** planned.

**Setup:** baseline 0.77.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Virtual hex viewer.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add range-backed hex/ASCII viewing, exact offset navigation, selection and export. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Offsets above 32-bit ranges remain correct; UI memory is measured separately from underlying artifact storage. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.78.0 implementation stop reached. Run pentest for this exact commit.

## v0.79.0 — Structured and table viewers

**Status:** planned.

**Setup:** baseline 0.78.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Structured and table viewers.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add lossless tree/table views, typed cell rendering, pagination and safe copy/export. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Large integers and binary values remain exact; untrusted strings cannot inject markup or spreadsheet formulas without warning. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.79.0 implementation stop reached. Run pentest for this exact commit.

## v0.80.0 — Graph editor

**Status:** planned.

**Setup:** baseline 0.79.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Graph editor.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add an optional visual graph for typed ports, branches, joins and structured control regions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Invalid edges are rejected by the engine compiler, not only by visual UI rules; keyboard editing remains possible. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.80.0 implementation stop reached. Run pentest for this exact commit.

## v0.81.0 — Debugging controls

**Status:** planned.

**Setup:** baseline 0.80.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Debugging controls.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add breakpoints, single-step, node diagnostics, intermediate inspection and cancellation status. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Viewing a preview does not prematurely terminate a full output stream or leak a secret artifact into history. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.81.0 implementation stop reached. Run pentest for this exact commit.

## v0.82.0 — Offset provenance UI

**Status:** planned.

**Setup:** baseline 0.81.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Offset provenance UI.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Show source/output correspondences where transformations provide them, including encoded-byte relationships. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Non-local or lossy transforms say unmappable/approximate explicitly rather than invent exact positions. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.82.0 implementation stop reached. Run pentest for this exact commit.

## v0.83.0 — Multiple inputs and batches

**Status:** planned.

**Setup:** baseline 0.82.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Multiple inputs and batches.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add named inputs, file sets, deterministic batch ordering and per-item error policy. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** A failed batch item cannot silently discard other results; files are not duplicated into UI state. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.83.0 implementation stop reached. Run pentest for this exact commit.

## v0.84.0 — Local recipe library

**Status:** planned.

**Setup:** baseline 0.83.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Local recipe library.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add folders/tags, favourites, search, revision history and exportable local workspaces. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Persistence is opt-in for sensitive data; recipe export omits secrets and bulk inputs by default. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.84.0 implementation stop reached. Run pentest for this exact commit.

## v0.85.0 — Sharing and imports

**Status:** planned.

**Setup:** baseline 0.84.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Sharing and imports.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Support recipe-only links/files, explicit input inclusion, compatibility links and import previews. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Users see capabilities and embedded data before running; history and URL exposure are clearly distinguished. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.85.0 implementation stop reached. Run pentest for this exact commit.

## v0.86.0 — Offline packaging

**Status:** planned.

**Setup:** baseline 0.85.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Offline packaging.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Cache versioned app assets and selected operation packs; provide a complete offline distribution option. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Offline operation availability is visible; service-worker upgrades cannot mix incompatible engine and pack revisions. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.86.0 implementation stop reached. Run pentest for this exact commit.

## v0.87.0 — Browser accessibility gate

**Status:** planned.

**Setup:** baseline 0.86.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Browser accessibility gate.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Test keyboard, screen reader, focus, reduced motion, high contrast and touch-friendly responsive layouts. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Core tasks work without canvas-only controls, GPU acceleration, shared memory or a mouse. Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.87.0 implementation stop reached. Run pentest for this exact commit.
