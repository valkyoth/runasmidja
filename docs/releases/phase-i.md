# Phase I: Legacy cryptography, hashes and classical ciphers

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

## v0.187.0 — Legacy safety separation

**Status:** planned.

**Setup:** baseline 0.186.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Legacy safety separation.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Package historical algorithms with explicit analysis labels and separate features from application security. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Enabling every operation cannot weaken HTTPS, sessions, storage encryption or identity verification. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.187.0 implementation stop reached. Run pentest for this exact commit.

## v0.188.0 — DES analysis

**Status:** planned.

**Setup:** baseline 0.187.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** DES analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.122.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only des analysis within the source workstream: Add modes, padding and historical key conventions required by reference fixtures. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Weak-key and parity-bit handling is documented; outputs match independent known-answer tests. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.188.0 implementation stop reached. Run pentest for this exact commit.

## v0.189.0 — Triple DES analysis

**Status:** planned.

**Setup:** baseline 0.188.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Triple DES analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.122.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only triple des analysis within the source workstream: Add modes, padding and historical key conventions required by reference fixtures. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Weak-key and parity-bit handling is documented; outputs match independent known-answer tests. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.189.0 implementation stop reached. Run pentest for this exact commit.

## v0.190.0 — Blowfish analysis

**Status:** planned.

**Setup:** baseline 0.189.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Blowfish analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.123.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only blowfish analysis within the source workstream: Deliver required modes and parameter variants through reviewed implementations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Key expansion limits, effective key bits and legacy padding have positive and negative fixtures. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.190.0 implementation stop reached. Run pentest for this exact commit.

## v0.191.0 — RC2 analysis

**Status:** planned.

**Setup:** baseline 0.190.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** RC2 analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.123.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only rc2 analysis within the source workstream: Deliver required modes and parameter variants through reviewed implementations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Key expansion limits, effective key bits and legacy padding have positive and negative fixtures. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.191.0 implementation stop reached. Run pentest for this exact commit.

## v0.192.0 — RC4 and drop analysis

**Status:** planned.

**Setup:** baseline 0.191.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** RC4 and drop analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.124.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only rc4 and drop analysis within the source workstream: Add stream variants, RC4-drop controls and exact byte semantics. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: State persists across chunks; skip/drop parameters cannot cause uncontrolled work. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.192.0 implementation stop reached. Run pentest for this exact commit.

## v0.193.0 — Rabbit analysis

**Status:** planned.

**Setup:** baseline 0.192.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Rabbit analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.124.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only rabbit analysis within the source workstream: Add stream variants, RC4-drop controls and exact byte semantics. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: State persists across chunks; skip/drop parameters cannot cause uncontrolled work. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.193.0 implementation stop reached. Run pentest for this exact commit.

## v0.194.0 — TEA analysis

**Status:** planned.

**Setup:** baseline 0.193.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** TEA analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.125.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only tea analysis within the source workstream: Add TEA, XTEA and XXTEA with explicit word order and length conventions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Short messages, padding and unusual variants have independently sourced compatibility cases. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.194.0 implementation stop reached. Run pentest for this exact commit.

## v0.195.0 — XTEA analysis

**Status:** planned.

**Setup:** baseline 0.194.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** XTEA analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.125.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only xtea analysis within the source workstream: Add TEA, XTEA and XXTEA with explicit word order and length conventions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Short messages, padding and unusual variants have independently sourced compatibility cases. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.195.0 implementation stop reached. Run pentest for this exact commit.

## v0.196.0 — XXTEA analysis

**Status:** planned.

**Setup:** baseline 0.195.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** XXTEA analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.125.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only xxtea analysis within the source workstream: Add TEA, XTEA and XXTEA with explicit word order and length conventions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Short messages, padding and unusual variants have independently sourced compatibility cases. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.196.0 implementation stop reached. Run pentest for this exact commit.

## v0.197.0 — RC6 analysis

**Status:** planned.

**Setup:** baseline 0.196.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** RC6 analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.126.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only rc6 analysis within the source workstream: Add required RC6, Twofish, PRESENT and other inventoried block families. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Each algorithm/variant is separately tracked; an unavailable provider causes more 0.x work, not an unlabelled replacement. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.197.0 implementation stop reached. Run pentest for this exact commit.

## v0.198.0 — Twofish analysis

**Status:** planned.

**Setup:** baseline 0.197.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Twofish analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.126.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only twofish analysis within the source workstream: Add required RC6, Twofish, PRESENT and other inventoried block families. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Each algorithm/variant is separately tracked; an unavailable provider causes more 0.x work, not an unlabelled replacement. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.198.0 implementation stop reached. Run pentest for this exact commit.

## v0.199.0 — PRESENT analysis

**Status:** planned.

**Setup:** baseline 0.198.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** PRESENT analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.126.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only present analysis within the source workstream: Add required RC6, Twofish, PRESENT and other inventoried block families. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Each algorithm/variant is separately tracked; an unavailable provider causes more 0.x work, not an unlabelled replacement. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.199.0 implementation stop reached. Run pentest for this exact commit.

## v0.200.0 — Residual block-cipher inventory closure

**Status:** planned.

**Setup:** baseline 0.199.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Residual block-cipher inventory closure.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.126.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only residual block-cipher inventory closure within the source workstream: Add required RC6, Twofish, PRESENT and other inventoried block families. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Each algorithm/variant is separately tracked; an unavailable provider causes more 0.x work, not an unlabelled replacement. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.200.0 implementation stop reached. Run pentest for this exact commit.

## v0.201.0 — SM4 analysis

**Status:** planned.

**Setup:** baseline 0.200.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** SM4 analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.127.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only sm4 analysis within the source workstream: Add required modes and parameter sets with explicit identifiers. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Parameter-set selection is reproducible; names alone cannot choose an incompatible implementation. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.201.0 implementation stop reached. Run pentest for this exact commit.

## v0.202.0 — GOST encryption parameter sets

**Status:** planned.

**Setup:** baseline 0.201.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** GOST encryption parameter sets.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.127.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only gost encryption parameter sets within the source workstream: Add required modes and parameter sets with explicit identifiers. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Parameter-set selection is reproducible; names alone cannot choose an incompatible implementation. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.202.0 implementation stop reached. Run pentest for this exact commit.

## v0.203.0 — Ascon variants

**Status:** planned.

**Setup:** baseline 0.202.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Ascon variants.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add the exact Ascon versions exposed by the pinned reference and separately identify newer variants. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Algorithm revision, nonce/tag lengths and byte-order differences are verified rather than conflated. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.203.0 implementation stop reached. Run pentest for this exact commit.

## v0.204.0 — MD-family historical digests

**Status:** planned.

**Setup:** baseline 0.203.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** MD-family historical digests.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.129.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only md-family historical digests within the source workstream: Add required MD/SHA-0/RIPEMD and other legacy digest families. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Every inventoried variant has test vectors; obsolete digests remain labelled unsuitable for modern integrity security. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.204.0 implementation stop reached. Run pentest for this exact commit.

## v0.205.0 — SHA-0 analysis

**Status:** planned.

**Setup:** baseline 0.204.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** SHA-0 analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.129.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only sha-0 analysis within the source workstream: Add required MD/SHA-0/RIPEMD and other legacy digest families. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Every inventoried variant has test vectors; obsolete digests remain labelled unsuitable for modern integrity security. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.205.0 implementation stop reached. Run pentest for this exact commit.

## v0.206.0 — RIPEMD variants

**Status:** planned.

**Setup:** baseline 0.205.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** RIPEMD variants.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.129.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only ripemd variants within the source workstream: Add required MD/SHA-0/RIPEMD and other legacy digest families. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Every inventoried variant has test vectors; obsolete digests remain labelled unsuitable for modern integrity security. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.206.0 implementation stop reached. Run pentest for this exact commit.

## v0.207.0 — Residual historical digest closure

**Status:** planned.

**Setup:** baseline 0.206.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Residual historical digest closure.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.129.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only residual historical digest closure within the source workstream: Add required MD/SHA-0/RIPEMD and other legacy digest families. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Every inventoried variant has test vectors; obsolete digests remain labelled unsuitable for modern integrity security. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.207.0 implementation stop reached. Run pentest for this exact commit.

## v0.208.0 — GOST digests

**Status:** planned.

**Setup:** baseline 0.207.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** GOST digests.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.130.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only gost digests within the source workstream: Add inventoried GOST/SM3/Whirlpool/Snefru/HAS-160 and other uncommon digests as applicable. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Provider absence, missing variants and licensing restrictions stay visible until resolved. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.208.0 implementation stop reached. Run pentest for this exact commit.

## v0.209.0 — SM3 digest

**Status:** planned.

**Setup:** baseline 0.208.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** SM3 digest.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.130.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only sm3 digest within the source workstream: Add inventoried GOST/SM3/Whirlpool/Snefru/HAS-160 and other uncommon digests as applicable. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Provider absence, missing variants and licensing restrictions stay visible until resolved. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.209.0 implementation stop reached. Run pentest for this exact commit.

## v0.210.0 — Whirlpool digest

**Status:** planned.

**Setup:** baseline 0.209.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Whirlpool digest.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.130.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only whirlpool digest within the source workstream: Add inventoried GOST/SM3/Whirlpool/Snefru/HAS-160 and other uncommon digests as applicable. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Provider absence, missing variants and licensing restrictions stay visible until resolved. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.210.0 implementation stop reached. Run pentest for this exact commit.

## v0.211.0 — Snefru variants

**Status:** planned.

**Setup:** baseline 0.210.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Snefru variants.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.130.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only snefru variants within the source workstream: Add inventoried GOST/SM3/Whirlpool/Snefru/HAS-160 and other uncommon digests as applicable. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Provider absence, missing variants and licensing restrictions stay visible until resolved. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.211.0 implementation stop reached. Run pentest for this exact commit.

## v0.212.0 — HAS-160 digest

**Status:** planned.

**Setup:** baseline 0.211.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** HAS-160 digest.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.130.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only has-160 digest within the source workstream: Add inventoried GOST/SM3/Whirlpool/Snefru/HAS-160 and other uncommon digests as applicable. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Provider absence, missing variants and licensing restrictions stay visible until resolved. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.212.0 implementation stop reached. Run pentest for this exact commit.

## v0.213.0 — Residual specialist digest closure

**Status:** planned.

**Setup:** baseline 0.212.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Residual specialist digest closure.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.130.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only residual specialist digest closure within the source workstream: Add inventoried GOST/SM3/Whirlpool/Snefru/HAS-160 and other uncommon digests as applicable. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Provider absence, missing variants and licensing restrictions stay visible until resolved. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.213.0 implementation stop reached. Run pentest for this exact commit.

## v0.214.0 — Fuzzy and similarity hashes

**Status:** planned.

**Setup:** baseline 0.213.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Fuzzy and similarity hashes.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add the reference’s fuzzy/context-triggered hashes and comparison utilities. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Similarity scores, block sizes and edge cases match reference behavior; results are not represented as cryptographic proofs. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.214.0 implementation stop reached. Run pentest for this exact commit.

## v0.215.0 — ROT and substitution analysis

**Status:** planned.

**Setup:** baseline 0.214.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** ROT and substitution analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.132.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only rot and substitution analysis within the source workstream: Add ROT families, Vigenere, Morse, Bacon, Affine, Atbash, A1Z26, substitution and related inventory entries. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Alphabet, case, punctuation and non-ASCII policies are explicit and fixture-tested. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.215.0 implementation stop reached. Run pentest for this exact commit.

## v0.216.0 — Vigenere analysis

**Status:** planned.

**Setup:** baseline 0.215.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Vigenere analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.132.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only vigenere analysis within the source workstream: Add ROT families, Vigenere, Morse, Bacon, Affine, Atbash, A1Z26, substitution and related inventory entries. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Alphabet, case, punctuation and non-ASCII policies are explicit and fixture-tested. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.216.0 implementation stop reached. Run pentest for this exact commit.

## v0.217.0 — Morse encoding

**Status:** planned.

**Setup:** baseline 0.216.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Morse encoding.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.132.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only morse encoding within the source workstream: Add ROT families, Vigenere, Morse, Bacon, Affine, Atbash, A1Z26, substitution and related inventory entries. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Alphabet, case, punctuation and non-ASCII policies are explicit and fixture-tested. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.217.0 implementation stop reached. Run pentest for this exact commit.

## v0.218.0 — Bacon encoding

**Status:** planned.

**Setup:** baseline 0.217.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Bacon encoding.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.132.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only bacon encoding within the source workstream: Add ROT families, Vigenere, Morse, Bacon, Affine, Atbash, A1Z26, substitution and related inventory entries. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Alphabet, case, punctuation and non-ASCII policies are explicit and fixture-tested. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.218.0 implementation stop reached. Run pentest for this exact commit.

## v0.219.0 — Affine cipher

**Status:** planned.

**Setup:** baseline 0.218.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Affine cipher.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.132.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only affine cipher within the source workstream: Add ROT families, Vigenere, Morse, Bacon, Affine, Atbash, A1Z26, substitution and related inventory entries. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Alphabet, case, punctuation and non-ASCII policies are explicit and fixture-tested. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.219.0 implementation stop reached. Run pentest for this exact commit.

## v0.220.0 — Atbash cipher

**Status:** planned.

**Setup:** baseline 0.219.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Atbash cipher.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.132.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only atbash cipher within the source workstream: Add ROT families, Vigenere, Morse, Bacon, Affine, Atbash, A1Z26, substitution and related inventory entries. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Alphabet, case, punctuation and non-ASCII policies are explicit and fixture-tested. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.220.0 implementation stop reached. Run pentest for this exact commit.

## v0.221.0 — A1Z26 encoding

**Status:** planned.

**Setup:** baseline 0.220.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** A1Z26 encoding.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.132.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only a1z26 encoding within the source workstream: Add ROT families, Vigenere, Morse, Bacon, Affine, Atbash, A1Z26, substitution and related inventory entries. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Alphabet, case, punctuation and non-ASCII policies are explicit and fixture-tested. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.221.0 implementation stop reached. Run pentest for this exact commit.

## v0.222.0 — Residual classical substitution closure

**Status:** planned.

**Setup:** baseline 0.221.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Residual classical substitution closure.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.132.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only residual classical substitution closure within the source workstream: Add ROT families, Vigenere, Morse, Bacon, Affine, Atbash, A1Z26, substitution and related inventory entries. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Alphabet, case, punctuation and non-ASCII policies are explicit and fixture-tested. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.222.0 implementation stop reached. Run pentest for this exact commit.

## v0.223.0 — Bifid analysis

**Status:** planned.

**Setup:** baseline 0.222.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Bifid analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.133.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only bifid analysis within the source workstream: Add Bifid, Rail Fence, Caesar Box and other inventoried transposition/novel encodings. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Incomplete grids, key validation and reverse transforms preserve the required conventions. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.223.0 implementation stop reached. Run pentest for this exact commit.

## v0.224.0 — Rail Fence analysis

**Status:** planned.

**Setup:** baseline 0.223.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Rail Fence analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.133.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only rail fence analysis within the source workstream: Add Bifid, Rail Fence, Caesar Box and other inventoried transposition/novel encodings. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Incomplete grids, key validation and reverse transforms preserve the required conventions. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.224.0 implementation stop reached. Run pentest for this exact commit.

## v0.225.0 — Caesar Box analysis

**Status:** planned.

**Setup:** baseline 0.224.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Caesar Box analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.133.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only caesar box analysis within the source workstream: Add Bifid, Rail Fence, Caesar Box and other inventoried transposition/novel encodings. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Incomplete grids, key validation and reverse transforms preserve the required conventions. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.225.0 implementation stop reached. Run pentest for this exact commit.

## v0.226.0 — Residual classical transposition closure

**Status:** planned.

**Setup:** baseline 0.225.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Residual classical transposition closure.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.133.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only residual classical transposition closure within the source workstream: Add Bifid, Rail Fence, Caesar Box and other inventoried transposition/novel encodings. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Incomplete grids, key validation and reverse transforms preserve the required conventions. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.226.0 implementation stop reached. Run pentest for this exact commit.

## v0.227.0 — Enigma analysis

**Status:** planned.

**Setup:** baseline 0.226.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Enigma analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.134.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only enigma analysis within the source workstream: Add Enigma/Typex/Lorenz/SIGABA and associated analysis tools such as Bombe/Colossus when inventoried. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Machine settings and known historical/reference fixtures agree; expensive searches have strict work budgets. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.227.0 implementation stop reached. Run pentest for this exact commit.

## v0.228.0 — Typex analysis

**Status:** planned.

**Setup:** baseline 0.227.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Typex analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.134.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only typex analysis within the source workstream: Add Enigma/Typex/Lorenz/SIGABA and associated analysis tools such as Bombe/Colossus when inventoried. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Machine settings and known historical/reference fixtures agree; expensive searches have strict work budgets. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.228.0 implementation stop reached. Run pentest for this exact commit.

## v0.229.0 — Lorenz analysis

**Status:** planned.

**Setup:** baseline 0.228.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Lorenz analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.134.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only lorenz analysis within the source workstream: Add Enigma/Typex/Lorenz/SIGABA and associated analysis tools such as Bombe/Colossus when inventoried. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Machine settings and known historical/reference fixtures agree; expensive searches have strict work budgets. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.229.0 implementation stop reached. Run pentest for this exact commit.

## v0.230.0 — SIGABA analysis

**Status:** planned.

**Setup:** baseline 0.229.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** SIGABA analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.134.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only sigaba analysis within the source workstream: Add Enigma/Typex/Lorenz/SIGABA and associated analysis tools such as Bombe/Colossus when inventoried. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Machine settings and known historical/reference fixtures agree; expensive searches have strict work budgets. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.230.0 implementation stop reached. Run pentest for this exact commit.

## v0.231.0 — Bombe search if inventoried

**Status:** planned.

**Setup:** baseline 0.230.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Bombe search if inventoried.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.134.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only bombe search if inventoried within the source workstream: Add Enigma/Typex/Lorenz/SIGABA and associated analysis tools such as Bombe/Colossus when inventoried. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Machine settings and known historical/reference fixtures agree; expensive searches have strict work budgets. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.231.0 implementation stop reached. Run pentest for this exact commit.

## v0.232.0 — Colossus search if inventoried

**Status:** planned.

**Setup:** baseline 0.231.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Colossus search if inventoried.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.134.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only colossus search if inventoried within the source workstream: Add Enigma/Typex/Lorenz/SIGABA and associated analysis tools such as Bombe/Colossus when inventoried. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Machine settings and known historical/reference fixtures agree; expensive searches have strict work budgets. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.232.0 implementation stop reached. Run pentest for this exact commit.

## v0.233.0 — EVP legacy compatibility

**Status:** planned.

**Setup:** baseline 0.232.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** EVP legacy compatibility.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.135.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only evp legacy compatibility within the source workstream: Deliver remaining EVP/CipherSaber/Citrix/LS47 and other residual legacy entries, splitting releases as necessary. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Generated coverage shows no unowned long-tail algorithm or argument gap; all required browser paths are tested. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.233.0 implementation stop reached. Run pentest for this exact commit.

## v0.234.0 — CipherSaber analysis

**Status:** planned.

**Setup:** baseline 0.233.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** CipherSaber analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.135.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only ciphersaber analysis within the source workstream: Deliver remaining EVP/CipherSaber/Citrix/LS47 and other residual legacy entries, splitting releases as necessary. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Generated coverage shows no unowned long-tail algorithm or argument gap; all required browser paths are tested. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.234.0 implementation stop reached. Run pentest for this exact commit.

## v0.235.0 — Citrix compatibility

**Status:** planned.

**Setup:** baseline 0.234.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Citrix compatibility.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.135.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only citrix compatibility within the source workstream: Deliver remaining EVP/CipherSaber/Citrix/LS47 and other residual legacy entries, splitting releases as necessary. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Generated coverage shows no unowned long-tail algorithm or argument gap; all required browser paths are tested. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.235.0 implementation stop reached. Run pentest for this exact commit.

## v0.236.0 — LS47 analysis

**Status:** planned.

**Setup:** baseline 0.235.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** LS47 analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.135.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only ls47 analysis within the source workstream: Deliver remaining EVP/CipherSaber/Citrix/LS47 and other residual legacy entries, splitting releases as necessary. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Generated coverage shows no unowned long-tail algorithm or argument gap; all required browser paths are tested. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.236.0 implementation stop reached. Run pentest for this exact commit.

## v0.237.0 — Residual legacy acceptance

**Status:** planned.

**Setup:** baseline 0.236.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Residual legacy acceptance.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.135.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only residual legacy acceptance within the source workstream: Deliver remaining EVP/CipherSaber/Citrix/LS47 and other residual legacy entries, splitting releases as necessary. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Generated coverage shows no unowned long-tail algorithm or argument gap; all required browser paths are tested. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.237.0 implementation stop reached. Run pentest for this exact commit.
