# Phase L: Images, media and document presentation

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

Verification checklists apply only to introduced or retained behavior in the reviewed bounded scope. Record absent later capabilities as pending with numbered owners; contract fixtures never attest their runtime PASS. A prerequisite needed by this pass must be implemented and verified first, rather than deferred. Every future owner still owes its full acceptance before exposure/1.0.

## v0.302.0 — Media provider boundary

**Status:** planned.

**Setup:** baseline 0.301.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Media provider boundary.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Define bounded image/frame/audio artifacts, metadata, dimensions and deterministic decode policy. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Pixel/frame/duration limits are checked before allocation; corrupted metadata cannot request unbounded buffers. Codec/model providers expose owned resource/error contracts; dimensions/frame/tensor limits and license/asset provenance precede invocation. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.302.0 implementation stop reached. Run pentest for this exact commit.

## v0.303.0 — Image decoding

**Status:** planned.

**Setup:** baseline 0.302.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Image decoding.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add every required input image format and animated variant via reviewed feature-selected providers. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Browser/native decode fixtures record color, alpha and frame semantics; unavailable codecs remain explicit gaps. Every decoder bounds dimensions/pixels/frames/metadata/decompression before allocation; malformed/corrupt fixtures and actual browser memory/cancel tests pass. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.303.0 implementation stop reached. Run pentest for this exact commit.

## v0.304.0 — Image encoding

**Status:** planned.

**Setup:** baseline 0.303.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Image encoding.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add reference output formats, metadata policy and deterministic options where possible. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Quality settings and byte-level nondeterminism are documented; exact output comparisons use the right compatibility criteria. Each encoder freezes format/quality/color/metadata defaults with independent decoding; output/work limits and failed-publication rules hold. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.304.0 implementation stop reached. Run pentest for this exact commit.

## v0.305.0 — Geometry transforms

**Status:** planned.

**Setup:** baseline 0.304.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Geometry transforms.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add resize, crop, rotate, flip and related inventoried image operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Coordinate bounds, interpolation options, orientation and very large dimensions are fixture-tested. Resize/crop/rotate variants define coordinate/rounding/interpolation semantics; out-of-bounds/extreme dimensions reject before amplification. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.305.0 implementation stop reached. Run pentest for this exact commit.

## v0.306.0 — Color transforms

**Status:** planned.

**Setup:** baseline 0.305.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Color transforms.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add channels, grayscale, inversion, brightness/contrast and required color operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Color space, alpha premultiplication and clamping rules are explicit and reproducible. Color-space/channel/alpha transforms pin matrices/profiles and rounding/tolerances; independent fixtures and malformed profiles pass. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.306.0 implementation stop reached. Run pentest for this exact commit.

## v0.307.0 — Filters and effects

**Status:** planned.

**Setup:** baseline 0.306.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Filters and effects.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add required blur/sharpen/convolution and other image effects from inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Kernel costs and edge behavior are bounded; arbitrary filter input cannot cause uncontrolled GPU/CPU allocation. Each filter/effect freezes kernel/edge/tolerance semantics; oversized kernels and expensive iteration hit declared work/memory caps. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.307.0 implementation stop reached. Run pentest for this exact commit.

## v0.308.0 — Image composition

**Status:** planned.

**Setup:** baseline 0.307.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Image composition.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add layering, text/annotation and inventoried composition helpers. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Fonts/assets are local and versioned; untrusted text remains inert and export respects declared dimensions. Composition bounds layers/canvas/dimensions and defines alpha/order/blending; hostile combinations cannot exceed aggregate output allocations. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.308.0 implementation stop reached. Run pentest for this exact commit.

## v0.309.0 — Steganography and bit planes

**Status:** planned.

**Setup:** baseline 0.308.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Steganography and bit planes.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add required image byte/bit extraction and embedding operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Capacity limits, channel order and malformed payloads have round-trip and negative tests. Bit-plane/steganography variants have exact embedding/extraction vectors; size/key errors reject and hidden output keeps inherited sensitivity. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.309.0 implementation stop reached. Run pentest for this exact commit.

## v0.310.0 — QR generation

**Status:** planned.

**Setup:** baseline 0.309.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** QR generation.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.174.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only qr generation within the source workstream: Add required symbologies and rendering options. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Payload capacity, error correction and invalid character sets are checked against reference fixtures. Each QR/barcode symbology/version/error-correction argument round trips through an independent reader and rejects capacity excess. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.310.0 implementation stop reached. Run pentest for this exact commit.

## v0.311.0 — Barcode generation

**Status:** planned.

**Setup:** baseline 0.310.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Barcode generation.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.174.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only barcode generation within the source workstream: Add required symbologies and rendering options. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Payload capacity, error correction and invalid character sets are checked against reference fixtures. Each QR/barcode symbology/version/error-correction argument round trips through an independent reader and rejects capacity excess. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.311.0 implementation stop reached. Run pentest for this exact commit.

## v0.312.0 — QR recognition

**Status:** planned.

**Setup:** baseline 0.311.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** QR recognition.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.175.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only qr recognition within the source workstream: Add local recognition for inventoried formats with deterministic input preprocessing. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Recognition failure is explicit; no image is uploaded to a third-party recognition service. Recognition has independent positive/negative/noisy fixtures and bounded image/candidate work; confidence/result ordering and dataset/model revisions are declared. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.312.0 implementation stop reached. Run pentest for this exact commit.

## v0.313.0 — Barcode recognition

**Status:** planned.

**Setup:** baseline 0.312.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Barcode recognition.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.175.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only barcode recognition within the source workstream: Add local recognition for inventoried formats with deterministic input preprocessing. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Recognition failure is explicit; no image is uploaded to a third-party recognition service. Recognition has independent positive/negative/noisy fixtures and bounded image/candidate work; confidence/result ordering and dataset/model revisions are declared. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.313.0 implementation stop reached. Run pentest for this exact commit.

## v0.314.0 — OCR

**Status:** planned.

**Setup:** baseline 0.313.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OCR.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add a local OCR provider and required language/model pack handling with bounded worker execution. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Model availability, accuracy corpus, memory costs and browser support are measured; absent languages are tracked gaps. Each OCR model/language has license/hash/accuracy corpus and actual offline browser tests; decode/tensor/work limits and hard cancellation pass without uploads. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.314.0 implementation stop reached. Run pentest for this exact commit.

## v0.315.0 — EXIF metadata

**Status:** planned.

**Setup:** baseline 0.314.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** EXIF metadata.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.177.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only exif metadata within the source workstream: Add EXIF/ID3 and required metadata extraction/editing or display operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Nested metadata, thumbnails and encoding variants are bounded; metadata is not interpreted as trusted markup. EXIF/ID3/other metadata formats parse bounded fields and malformed offsets; location/private metadata stays sensitive and external references are inert. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.315.0 implementation stop reached. Run pentest for this exact commit.

## v0.316.0 — ID3 metadata

**Status:** planned.

**Setup:** baseline 0.315.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** ID3 metadata.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.177.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only id3 metadata within the source workstream: Add EXIF/ID3 and required metadata extraction/editing or display operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Nested metadata, thumbnails and encoding variants are bounded; metadata is not interpreted as trusted markup. EXIF/ID3/other metadata formats parse bounded fields and malformed offsets; location/private metadata stays sensitive and external references are inert. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.316.0 implementation stop reached. Run pentest for this exact commit.

## v0.317.0 — Residual media metadata

**Status:** planned.

**Setup:** baseline 0.316.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Residual media metadata.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.177.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only residual media metadata within the source workstream: Add EXIF/ID3 and required metadata extraction/editing or display operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Nested metadata, thumbnails and encoding variants are bounded; metadata is not interpreted as trusted markup. EXIF/ID3/other metadata formats parse bounded fields and malformed offsets; location/private metadata stays sensitive and external references are inert. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.317.0 implementation stop reached. Run pentest for this exact commit.

## v0.318.0 — Audio and other media operations

**Status:** planned.

**Setup:** baseline 0.317.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Audio and other media operations.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Deliver inventoried playback/visualization/transforms using provider or browser presentation adapters. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** User activation requirements and codec support are visible; playback is never automatic for imported recipes. Audio/media formats bound samples/rate/duration/frames/decoder output; independent vectors, malformed input and browser/native tolerance policies pass. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.318.0 implementation stop reached. Run pentest for this exact commit.

## v0.319.0 — PDF preview isolation

**Status:** planned.

**Setup:** baseline 0.318.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** PDF preview isolation.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.179.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only pdf preview isolation within the source workstream: Add the presentation behaviors actually required by the reference, with isolated preview surfaces and download fallback. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Active content cannot access app origin, secrets or APIs; no unsupported claim of a full Rust PDF renderer. PDF/HTML/media previews use isolated origin/sandbox/no ambient credentials or network; script/navigation/download/message-origin attacks fail. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.319.0 implementation stop reached. Run pentest for this exact commit.

## v0.320.0 — HTML preview isolation

**Status:** planned.

**Setup:** baseline 0.319.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** HTML preview isolation.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.179.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only html preview isolation within the source workstream: Add the presentation behaviors actually required by the reference, with isolated preview surfaces and download fallback. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Active content cannot access app origin, secrets or APIs; no unsupported claim of a full Rust PDF renderer. PDF/HTML/media previews use isolated origin/sandbox/no ambient credentials or network; script/navigation/download/message-origin attacks fail. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.320.0 implementation stop reached. Run pentest for this exact commit.

## v0.321.0 — Media preview isolation

**Status:** planned.

**Setup:** baseline 0.320.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Media preview isolation.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.179.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only media preview isolation within the source workstream: Add the presentation behaviors actually required by the reference, with isolated preview surfaces and download fallback. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Active content cannot access app origin, secrets or APIs; no unsupported claim of a full Rust PDF renderer. PDF/HTML/media previews use isolated origin/sandbox/no ambient credentials or network; script/navigation/download/message-origin attacks fail. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.321.0 implementation stop reached. Run pentest for this exact commit.

## v0.322.0 — Media qualification

**Status:** planned.

**Setup:** baseline 0.321.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Media qualification.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Close format/argument gaps, compare outputs using declared tolerances and test malicious media corpora. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Baseline use works without WebGPU; optional acceleration produces equivalent results within documented tolerances. All media/argument/target/model rows qualify with actual memory/startup/cancellation and inert-preview evidence; missing browser providers remain blockers. Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.322.0 implementation stop reached. Run pentest for this exact commit.
