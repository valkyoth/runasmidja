# Phase L: Images, media and document presentation

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

## v0.280.0 — Media provider boundary

**Status:** planned.

**Setup:** baseline 0.279.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Media provider boundary.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Define bounded image/frame/audio artifacts, metadata, dimensions and deterministic decode policy. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Pixel/frame/duration limits are checked before allocation; corrupted metadata cannot request unbounded buffers. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.280.0 implementation stop reached. Run pentest for this exact commit.

## v0.281.0 — Image decoding

**Status:** planned.

**Setup:** baseline 0.280.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Image decoding.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add every required input image format and animated variant via reviewed feature-selected providers. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Browser/native decode fixtures record color, alpha and frame semantics; unavailable codecs remain explicit gaps. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.281.0 implementation stop reached. Run pentest for this exact commit.

## v0.282.0 — Image encoding

**Status:** planned.

**Setup:** baseline 0.281.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Image encoding.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add reference output formats, metadata policy and deterministic options where possible. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Quality settings and byte-level nondeterminism are documented; exact output comparisons use the right compatibility criteria. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.282.0 implementation stop reached. Run pentest for this exact commit.

## v0.283.0 — Geometry transforms

**Status:** planned.

**Setup:** baseline 0.282.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Geometry transforms.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add resize, crop, rotate, flip and related inventoried image operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Coordinate bounds, interpolation options, orientation and very large dimensions are fixture-tested. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.283.0 implementation stop reached. Run pentest for this exact commit.

## v0.284.0 — Color transforms

**Status:** planned.

**Setup:** baseline 0.283.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Color transforms.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add channels, grayscale, inversion, brightness/contrast and required color operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Color space, alpha premultiplication and clamping rules are explicit and reproducible. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.284.0 implementation stop reached. Run pentest for this exact commit.

## v0.285.0 — Filters and effects

**Status:** planned.

**Setup:** baseline 0.284.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Filters and effects.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add required blur/sharpen/convolution and other image effects from inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Kernel costs and edge behavior are bounded; arbitrary filter input cannot cause uncontrolled GPU/CPU allocation. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.285.0 implementation stop reached. Run pentest for this exact commit.

## v0.286.0 — Image composition

**Status:** planned.

**Setup:** baseline 0.285.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Image composition.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add layering, text/annotation and inventoried composition helpers. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Fonts/assets are local and versioned; untrusted text remains inert and export respects declared dimensions. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.286.0 implementation stop reached. Run pentest for this exact commit.

## v0.287.0 — Steganography and bit planes

**Status:** planned.

**Setup:** baseline 0.286.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Steganography and bit planes.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add required image byte/bit extraction and embedding operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Capacity limits, channel order and malformed payloads have round-trip and negative tests. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.287.0 implementation stop reached. Run pentest for this exact commit.

## v0.288.0 — QR generation

**Status:** planned.

**Setup:** baseline 0.287.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** QR generation.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.174.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only qr generation within the source workstream: Add required symbologies and rendering options. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Payload capacity, error correction and invalid character sets are checked against reference fixtures. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.288.0 implementation stop reached. Run pentest for this exact commit.

## v0.289.0 — Barcode generation

**Status:** planned.

**Setup:** baseline 0.288.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Barcode generation.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.174.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only barcode generation within the source workstream: Add required symbologies and rendering options. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Payload capacity, error correction and invalid character sets are checked against reference fixtures. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.289.0 implementation stop reached. Run pentest for this exact commit.

## v0.290.0 — QR recognition

**Status:** planned.

**Setup:** baseline 0.289.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** QR recognition.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.175.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only qr recognition within the source workstream: Add local recognition for inventoried formats with deterministic input preprocessing. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Recognition failure is explicit; no image is uploaded to a third-party recognition service. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.290.0 implementation stop reached. Run pentest for this exact commit.

## v0.291.0 — Barcode recognition

**Status:** planned.

**Setup:** baseline 0.290.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Barcode recognition.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.175.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only barcode recognition within the source workstream: Add local recognition for inventoried formats with deterministic input preprocessing. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Recognition failure is explicit; no image is uploaded to a third-party recognition service. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.291.0 implementation stop reached. Run pentest for this exact commit.

## v0.292.0 — OCR

**Status:** planned.

**Setup:** baseline 0.291.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OCR.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add a local OCR provider and required language/model pack handling with bounded worker execution. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Model availability, accuracy corpus, memory costs and browser support are measured; absent languages are tracked gaps. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.292.0 implementation stop reached. Run pentest for this exact commit.

## v0.293.0 — EXIF metadata

**Status:** planned.

**Setup:** baseline 0.292.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** EXIF metadata.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.177.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only exif metadata within the source workstream: Add EXIF/ID3 and required metadata extraction/editing or display operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Nested metadata, thumbnails and encoding variants are bounded; metadata is not interpreted as trusted markup. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.293.0 implementation stop reached. Run pentest for this exact commit.

## v0.294.0 — ID3 metadata

**Status:** planned.

**Setup:** baseline 0.293.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** ID3 metadata.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.177.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only id3 metadata within the source workstream: Add EXIF/ID3 and required metadata extraction/editing or display operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Nested metadata, thumbnails and encoding variants are bounded; metadata is not interpreted as trusted markup. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.294.0 implementation stop reached. Run pentest for this exact commit.

## v0.295.0 — Residual media metadata

**Status:** planned.

**Setup:** baseline 0.294.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Residual media metadata.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.177.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only residual media metadata within the source workstream: Add EXIF/ID3 and required metadata extraction/editing or display operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Nested metadata, thumbnails and encoding variants are bounded; metadata is not interpreted as trusted markup. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.295.0 implementation stop reached. Run pentest for this exact commit.

## v0.296.0 — Audio and other media operations

**Status:** planned.

**Setup:** baseline 0.295.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Audio and other media operations.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Deliver inventoried playback/visualization/transforms using provider or browser presentation adapters. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** User activation requirements and codec support are visible; playback is never automatic for imported recipes. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.296.0 implementation stop reached. Run pentest for this exact commit.

## v0.297.0 — PDF preview isolation

**Status:** planned.

**Setup:** baseline 0.296.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** PDF preview isolation.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.179.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only pdf preview isolation within the source workstream: Add the presentation behaviors actually required by the reference, with isolated preview surfaces and download fallback. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Active content cannot access app origin, secrets or APIs; no unsupported claim of a full Rust PDF renderer. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.297.0 implementation stop reached. Run pentest for this exact commit.

## v0.298.0 — HTML preview isolation

**Status:** planned.

**Setup:** baseline 0.297.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** HTML preview isolation.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.179.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only html preview isolation within the source workstream: Add the presentation behaviors actually required by the reference, with isolated preview surfaces and download fallback. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Active content cannot access app origin, secrets or APIs; no unsupported claim of a full Rust PDF renderer. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.298.0 implementation stop reached. Run pentest for this exact commit.

## v0.299.0 — Media preview isolation

**Status:** planned.

**Setup:** baseline 0.298.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Media preview isolation.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.179.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only media preview isolation within the source workstream: Add the presentation behaviors actually required by the reference, with isolated preview surfaces and download fallback. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Active content cannot access app origin, secrets or APIs; no unsupported claim of a full Rust PDF renderer. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.299.0 implementation stop reached. Run pentest for this exact commit.

## v0.300.0 — Media qualification

**Status:** planned.

**Setup:** baseline 0.299.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Media qualification.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Close format/argument gaps, compare outputs using declared tolerances and test malicious media corpora. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Baseline use works without WebGPU; optional acceleration produces equivalent results within documented tolerances. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.300.0 implementation stop reached. Run pentest for this exact commit.
