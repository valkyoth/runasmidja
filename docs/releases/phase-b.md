# Phase B: Bytes, text and foundational encodings

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

## v0.34.0 — Byte inspection

**Status:** planned.

**Setup:** baseline 0.33.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Byte inspection.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add hex dumps, binary, octal, decimal byte views and reversible dump parsing. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Offsets, delimiters, malformed rows and partial final lines match the selected compatibility profile. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.34.0 implementation stop reached. Run pentest for this exact commit.

## v0.35.0 — Integer representations

**Status:** planned.

**Setup:** baseline 0.34.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Integer representations.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.17.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only integer representations within the source workstream: Add charcode, text-integer, arbitrary-width numeric conversion, BCD, float bit views and endianness controls. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Signedness, precision, overflow, NaN payloads and byte-order behavior have explicit tests. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.35.0 implementation stop reached. Run pentest for this exact commit.

## v0.36.0 — Floating-point representations

**Status:** planned.

**Setup:** baseline 0.35.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Floating-point representations.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.17.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only floating-point representations within the source workstream: Add charcode, text-integer, arbitrary-width numeric conversion, BCD, float bit views and endianness controls. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Signedness, precision, overflow, NaN payloads and byte-order behavior have explicit tests. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.36.0 implementation stop reached. Run pentest for this exact commit.

## v0.37.0 — BCD representations

**Status:** planned.

**Setup:** baseline 0.36.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** BCD representations.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.17.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only bcd representations within the source workstream: Add charcode, text-integer, arbitrary-width numeric conversion, BCD, float bit views and endianness controls. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Signedness, precision, overflow, NaN payloads and byte-order behavior have explicit tests. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.37.0 implementation stop reached. Run pentest for this exact commit.

## v0.38.0 — Base64 family

**Status:** planned.

**Setup:** baseline 0.37.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Base64 family.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add configured alphabets, padding policies, URL-safe forms and source/output offset mapping. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** RFC vectors and reference arguments pass across every short-input chunk partition; padding is accepted only in valid positions. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.38.0 implementation stop reached. Run pentest for this exact commit.

## v0.39.0 — Base32 variants

**Status:** planned.

**Setup:** baseline 0.38.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Base32 variants.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.19.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only base32 variants within the source workstream: Add available alphabet variants, whitespace policies and precise invalid-symbol diagnostics. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Case handling, trailing bits and incomplete blocks have separate strict and compatibility fixtures. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.39.0 implementation stop reached. Run pentest for this exact commit.

## v0.40.0 — Base45 variants

**Status:** planned.

**Setup:** baseline 0.39.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Base45 variants.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.19.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only base45 variants within the source workstream: Add available alphabet variants, whitespace policies and precise invalid-symbol diagnostics. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Case handling, trailing bits and incomplete blocks have separate strict and compatibility fixtures. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.40.0 implementation stop reached. Run pentest for this exact commit.

## v0.41.0 — Base58 variants

**Status:** planned.

**Setup:** baseline 0.40.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Base58 variants.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.20.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only base58 variants within the source workstream: Add leading-zero handling, checksummed forms and selected alphabet variants. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Checksums, mixed-case policy, network prefixes and maximum-length limits are enforced without ambiguous repair. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.41.0 implementation stop reached. Run pentest for this exact commit.

## v0.42.0 — Bech32 variants

**Status:** planned.

**Setup:** baseline 0.41.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Bech32 variants.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.20.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only bech32 variants within the source workstream: Add leading-zero handling, checksummed forms and selected alphabet variants. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Checksums, mixed-case policy, network prefixes and maximum-length limits are enforced without ambiguous repair. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.42.0 implementation stop reached. Run pentest for this exact commit.

## v0.43.0 — Base62

**Status:** planned.

**Setup:** baseline 0.42.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Base62.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.21.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only base62 within the source workstream: Add Base62, Base85, Base92 and generic-base operations from the inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Exact alphabets, escaping and output lengths match fixtures; base conversion cannot request unbounded integer storage. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.43.0 implementation stop reached. Run pentest for this exact commit.

## v0.44.0 — Base85

**Status:** planned.

**Setup:** baseline 0.43.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Base85.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.21.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only base85 within the source workstream: Add Base62, Base85, Base92 and generic-base operations from the inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Exact alphabets, escaping and output lengths match fixtures; base conversion cannot request unbounded integer storage. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.44.0 implementation stop reached. Run pentest for this exact commit.

## v0.45.0 — Base92

**Status:** planned.

**Setup:** baseline 0.44.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Base92.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.21.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only base92 within the source workstream: Add Base62, Base85, Base92 and generic-base operations from the inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Exact alphabets, escaping and output lengths match fixtures; base conversion cannot request unbounded integer storage. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.45.0 implementation stop reached. Run pentest for this exact commit.

## v0.46.0 — Generic bounded base conversion

**Status:** planned.

**Setup:** baseline 0.45.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Generic bounded base conversion.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.21.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only generic bounded base conversion within the source workstream: Add Base62, Base85, Base92 and generic-base operations from the inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Exact alphabets, escaping and output lengths match fixtures; base conversion cannot request unbounded integer storage. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.46.0 implementation stop reached. Run pentest for this exact commit.

## v0.47.0 — Percent encoding

**Status:** planned.

**Setup:** baseline 0.46.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Percent encoding.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.22.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only percent encoding within the source workstream: Implement percent encoding/decoding, HTML entities and quoted-printable with explicit byte/text boundaries. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Reserved characters, malformed escapes and newline handling match documented profiles; results remain inert data. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.47.0 implementation stop reached. Run pentest for this exact commit.

## v0.48.0 — HTML entity encoding

**Status:** planned.

**Setup:** baseline 0.47.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** HTML entity encoding.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.22.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only html entity encoding within the source workstream: Implement percent encoding/decoding, HTML entities and quoted-printable with explicit byte/text boundaries. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Reserved characters, malformed escapes and newline handling match documented profiles; results remain inert data. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.48.0 implementation stop reached. Run pentest for this exact commit.

## v0.49.0 — Quoted-printable

**Status:** planned.

**Setup:** baseline 0.48.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Quoted-printable.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.22.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only quoted-printable within the source workstream: Implement percent encoding/decoding, HTML entities and quoted-printable with explicit byte/text boundaries. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Reserved characters, malformed escapes and newline handling match documented profiles; results remain inert data. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.49.0 implementation stop reached. Run pentest for this exact commit.

## v0.50.0 — Unicode escape semantics

**Status:** planned.

**Setup:** baseline 0.49.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Unicode escape semantics.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.23.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only unicode escape semantics within the source workstream: Add Unicode escapes, smart-character handling, normalization and versioned Unicode data. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Surrogate and invalid-sequence policy is explicit; normalization is tested at chunk boundaries and against table versions. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.50.0 implementation stop reached. Run pentest for this exact commit.

## v0.51.0 — Unicode normalization

**Status:** planned.

**Setup:** baseline 0.50.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Unicode normalization.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.23.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only unicode normalization within the source workstream: Add Unicode escapes, smart-character handling, normalization and versioned Unicode data. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Surrogate and invalid-sequence policy is explicit; normalization is tested at chunk boundaries and against table versions. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.51.0 implementation stop reached. Run pentest for this exact commit.

## v0.52.0 — Character encodings

**Status:** planned.

**Setup:** baseline 0.51.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Character encodings.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add an initial encoding-table pack, encode/decode operations and a complete remaining-encoding checklist. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Every enabled encoding has round-trip and lossy-mode tests; unimplemented table variants remain visible gaps. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.52.0 implementation stop reached. Run pentest for this exact commit.

## v0.53.0 — Text transformations

**Status:** planned.

**Setup:** baseline 0.52.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Text transformations.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add case transforms, trimming, diacritic removal, reverse, padding and character/word/line selection. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Byte, Unicode scalar, grapheme and legacy UTF-16 behaviors are not silently interchanged. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.53.0 implementation stop reached. Run pentest for this exact commit.

## v0.54.0 — Lines and collections

**Status:** planned.

**Setup:** baseline 0.53.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Lines and collections.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add split/join, line filtering, numbering, deduplication and stable sorting. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Long lines and whole-input sorting obey budgets; ordering and empty-record semantics match fixtures. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.54.0 implementation stop reached. Run pentest for this exact commit.

## v0.55.0 — Search and replace core

**Status:** planned.

**Setup:** baseline 0.54.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Search and replace core.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add literal search, bounded safe-regex mode, captures, replacement and highlighting as structured spans. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Safe-mode syntax is labelled distinctly from full compatibility regex; all highlighting is escaped by renderers. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.55.0 implementation stop reached. Run pentest for this exact commit.

## v0.56.0 — Bitwise and byte arithmetic

**Status:** planned.

**Setup:** baseline 0.55.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Bitwise and byte arithmetic.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add AND, OR, NOT, XOR, shifts, rotates, add/subtract and bounded brute-force primitives. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Key repetition, carry, signedness and integer overflow rules are deterministic across targets. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.56.0 implementation stop reached. Run pentest for this exact commit.

## v0.57.0 — Braille encoding

**Status:** planned.

**Setup:** baseline 0.56.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Braille encoding.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.29.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only braille encoding within the source workstream: Deliver Braille, Punycode, Modhex, COBS, caret/control encodings and MIME decoding from inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Embedded zeroes, invalid framing, malformed labels and nested MIME limits have adversarial fixtures. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.57.0 implementation stop reached. Run pentest for this exact commit.

## v0.58.0 — Punycode encoding

**Status:** planned.

**Setup:** baseline 0.57.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Punycode encoding.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.29.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only punycode encoding within the source workstream: Deliver Braille, Punycode, Modhex, COBS, caret/control encodings and MIME decoding from inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Embedded zeroes, invalid framing, malformed labels and nested MIME limits have adversarial fixtures. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.58.0 implementation stop reached. Run pentest for this exact commit.

## v0.59.0 — Modhex encoding

**Status:** planned.

**Setup:** baseline 0.58.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Modhex encoding.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.29.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only modhex encoding within the source workstream: Deliver Braille, Punycode, Modhex, COBS, caret/control encodings and MIME decoding from inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Embedded zeroes, invalid framing, malformed labels and nested MIME limits have adversarial fixtures. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.59.0 implementation stop reached. Run pentest for this exact commit.

## v0.60.0 — COBS framing

**Status:** planned.

**Setup:** baseline 0.59.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** COBS framing.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.29.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only cobs framing within the source workstream: Deliver Braille, Punycode, Modhex, COBS, caret/control encodings and MIME decoding from inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Embedded zeroes, invalid framing, malformed labels and nested MIME limits have adversarial fixtures. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.60.0 implementation stop reached. Run pentest for this exact commit.

## v0.61.0 — Caret and control encodings

**Status:** planned.

**Setup:** baseline 0.60.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Caret and control encodings.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.29.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only caret and control encodings within the source workstream: Deliver Braille, Punycode, Modhex, COBS, caret/control encodings and MIME decoding from inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Embedded zeroes, invalid framing, malformed labels and nested MIME limits have adversarial fixtures. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.61.0 implementation stop reached. Run pentest for this exact commit.

## v0.62.0 — MIME decoding

**Status:** planned.

**Setup:** baseline 0.61.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** MIME decoding.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.29.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only mime decoding within the source workstream: Deliver Braille, Punycode, Modhex, COBS, caret/control encodings and MIME decoding from inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Embedded zeroes, invalid framing, malformed labels and nested MIME limits have adversarial fixtures. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.62.0 implementation stop reached. Run pentest for this exact commit.

## v0.63.0 — Encoding completeness gate

**Status:** planned.

**Setup:** baseline 0.62.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Encoding completeness gate.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Reconcile every basic encoding and text inventory row, including missing variants discovered during implementation. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** A generated report separates complete operations, argument gaps and intentionally different safe defaults; no hidden omissions. Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.63.0 implementation stop reached. Run pentest for this exact commit.
