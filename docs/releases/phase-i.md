# Phase I: Legacy cryptography, hashes and classical ciphers

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

Verification checklists apply only to introduced or retained behavior in the reviewed bounded scope. Record absent later capabilities as pending with numbered owners; contract fixtures never attest their runtime PASS. A prerequisite needed by this pass must be implemented and verified first, rather than deferred. Every future owner still owes its full acceptance before exposure/1.0.

## v0.209.0 — Legacy safety separation

**Status:** planned.

**Setup:** baseline 0.208.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Legacy safety separation.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Package historical algorithms with explicit analysis labels and separate features from application security. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Enabling every operation cannot weaken HTTPS, sessions, storage encryption or identity verification. Enabling legacy analysis cannot change account hashing, TLS, live encryption, provider policy or recommended defaults; dependency/feature graphs prove separation. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.209.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.210.0 — DES analysis

**Status:** planned.

**Setup:** baseline 0.209.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** DES analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.122.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only des analysis within the source workstream: Add modes, padding and historical key conventions required by reference fixtures. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Weak-key and parity-bit handling is documented; outputs match independent known-answer tests. DES/Triple DES variants test key parity/weak-key policy, modes/padding and independent historical vectors under analysis-only descriptors. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.210.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.211.0 — Triple DES analysis

**Status:** planned.

**Setup:** baseline 0.210.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Triple DES analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.122.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only triple des analysis within the source workstream: Add modes, padding and historical key conventions required by reference fixtures. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Weak-key and parity-bit handling is documented; outputs match independent known-answer tests. DES/Triple DES variants test key parity/weak-key policy, modes/padding and independent historical vectors under analysis-only descriptors. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.211.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.212.0 — Blowfish analysis

**Status:** planned.

**Setup:** baseline 0.211.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Blowfish analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.123.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only blowfish analysis within the source workstream: Deliver required modes and parameter variants through reviewed implementations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Key expansion limits, effective key bits and legacy padding have positive and negative fixtures. Blowfish/RC2 variants independently qualify key/round/effective-key/mode defaults and malformed inputs; maintained provider admission is documented. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.212.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.213.0 — RC2 analysis

**Status:** planned.

**Setup:** baseline 0.212.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** RC2 analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.123.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only rc2 analysis within the source workstream: Deliver required modes and parameter variants through reviewed implementations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Key expansion limits, effective key bits and legacy padding have positive and negative fixtures. Blowfish/RC2 variants independently qualify key/round/effective-key/mode defaults and malformed inputs; maintained provider admission is documented. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.213.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.214.0 — RC4 and drop analysis

**Status:** planned.

**Setup:** baseline 0.213.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** RC4 and drop analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.124.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only rc4 and drop analysis within the source workstream: Add stream variants, RC4-drop controls and exact byte semantics. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: State persists across chunks; skip/drop parameters cannot cause uncontrolled work. RC4/drop/Rabbit variants pass independent key/IV/state vectors across partitions; analysis warnings/defaults and counter/resource policy are explicit. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.214.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.215.0 — Rabbit analysis

**Status:** planned.

**Setup:** baseline 0.214.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Rabbit analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.124.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only rabbit analysis within the source workstream: Add stream variants, RC4-drop controls and exact byte semantics. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: State persists across chunks; skip/drop parameters cannot cause uncontrolled work. RC4/drop/Rabbit variants pass independent key/IV/state vectors across partitions; analysis warnings/defaults and counter/resource policy are explicit. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.215.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.216.0 — TEA analysis

**Status:** planned.

**Setup:** baseline 0.215.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** TEA analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.125.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only tea analysis within the source workstream: Add TEA, XTEA and XXTEA with explicit word order and length conventions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Short messages, padding and unusual variants have independently sourced compatibility cases. TEA/XTEA/XXTEA separately freeze endian/round/padding/block variants with independent vectors; ambiguous names never conceal different algorithms. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.216.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.217.0 — XTEA analysis

**Status:** planned.

**Setup:** baseline 0.216.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** XTEA analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.125.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only xtea analysis within the source workstream: Add TEA, XTEA and XXTEA with explicit word order and length conventions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Short messages, padding and unusual variants have independently sourced compatibility cases. TEA/XTEA/XXTEA separately freeze endian/round/padding/block variants with independent vectors; ambiguous names never conceal different algorithms. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.217.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.218.0 — XXTEA analysis

**Status:** planned.

**Setup:** baseline 0.217.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** XXTEA analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.125.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only xxtea analysis within the source workstream: Add TEA, XTEA and XXTEA with explicit word order and length conventions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Short messages, padding and unusual variants have independently sourced compatibility cases. TEA/XTEA/XXTEA separately freeze endian/round/padding/block variants with independent vectors; ambiguous names never conceal different algorithms. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.218.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.219.0 — RC6 analysis

**Status:** planned.

**Setup:** baseline 0.218.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** RC6 analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.126.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only rc6 analysis within the source workstream: Add required RC6, Twofish, PRESENT and other inventoried block families. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Each algorithm/variant is separately tracked; an unavailable provider causes more 0.x work, not an unlabelled replacement. Each inventoried RC6/Twofish/PRESENT/other block cipher gets a separate bounded provider pass and vector set; absence of a provider stays a gap. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.219.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.220.0 — Twofish analysis

**Status:** planned.

**Setup:** baseline 0.219.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Twofish analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.126.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only twofish analysis within the source workstream: Add required RC6, Twofish, PRESENT and other inventoried block families. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Each algorithm/variant is separately tracked; an unavailable provider causes more 0.x work, not an unlabelled replacement. Each inventoried RC6/Twofish/PRESENT/other block cipher gets a separate bounded provider pass and vector set; absence of a provider stays a gap. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.220.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.221.0 — PRESENT analysis

**Status:** planned.

**Setup:** baseline 0.220.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** PRESENT analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.126.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only present analysis within the source workstream: Add required RC6, Twofish, PRESENT and other inventoried block families. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Each algorithm/variant is separately tracked; an unavailable provider causes more 0.x work, not an unlabelled replacement. Each inventoried RC6/Twofish/PRESENT/other block cipher gets a separate bounded provider pass and vector set; absence of a provider stays a gap. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.221.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.222.0 — Residual block-cipher inventory closure

**Status:** planned.

**Setup:** baseline 0.221.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Residual block-cipher inventory closure.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.126.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only residual block-cipher inventory closure within the source workstream: Add required RC6, Twofish, PRESENT and other inventoried block families. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Each algorithm/variant is separately tracked; an unavailable provider causes more 0.x work, not an unlabelled replacement. Each inventoried RC6/Twofish/PRESENT/other block cipher gets a separate bounded provider pass and vector set; absence of a provider stays a gap. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.222.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.223.0 — SM4 analysis

**Status:** planned.

**Setup:** baseline 0.222.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** SM4 analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.127.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only sm4 analysis within the source workstream: Add required modes and parameter sets with explicit identifiers. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Parameter-set selection is reproducible; names alone cannot choose an incompatible implementation. SM4 and each GOST parameter/S-box/mode variant have exact independent vectors and policy separation from transport/account security. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.223.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.224.0 — GOST encryption parameter sets

**Status:** planned.

**Setup:** baseline 0.223.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** GOST encryption parameter sets.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.127.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only gost encryption parameter sets within the source workstream: Add required modes and parameter sets with explicit identifiers. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Parameter-set selection is reproducible; names alone cannot choose an incompatible implementation. SM4 and each GOST parameter/S-box/mode variant have exact independent vectors and policy separation from transport/account security. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.224.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.225.0 — Ascon variants

**Status:** planned.

**Setup:** baseline 0.224.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Ascon variants.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add the exact Ascon versions exposed by the pinned reference and separately identify newer variants. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Algorithm revision, nonce/tag lengths and byte-order differences are verified rather than conflated. Ascon variants distinguish historical versus standardized revisions, nonce/tag/output semantics, mutation failures and secret staging. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.225.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.226.0 — MD-family historical digests

**Status:** planned.

**Setup:** baseline 0.225.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** MD-family historical digests.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.129.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only md-family historical digests within the source workstream: Add required MD/SHA-0/RIPEMD and other legacy digest families. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Every inventoried variant has test vectors; obsolete digests remain labelled unsuitable for modern integrity security. Each historical digest has independently verified exact revision/padding/encoding semantics; no insecure digest becomes an authentication default. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.226.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.227.0 — SHA-0 analysis

**Status:** planned.

**Setup:** baseline 0.226.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** SHA-0 analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.129.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only sha-0 analysis within the source workstream: Add required MD/SHA-0/RIPEMD and other legacy digest families. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Every inventoried variant has test vectors; obsolete digests remain labelled unsuitable for modern integrity security. Each historical digest has independently verified exact revision/padding/encoding semantics; no insecure digest becomes an authentication default. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.227.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.228.0 — RIPEMD variants

**Status:** planned.

**Setup:** baseline 0.227.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** RIPEMD variants.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.129.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only ripemd variants within the source workstream: Add required MD/SHA-0/RIPEMD and other legacy digest families. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Every inventoried variant has test vectors; obsolete digests remain labelled unsuitable for modern integrity security. Each historical digest has independently verified exact revision/padding/encoding semantics; no insecure digest becomes an authentication default. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.228.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.229.0 — Residual historical digest closure

**Status:** planned.

**Setup:** baseline 0.228.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Residual historical digest closure.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.129.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only residual historical digest closure within the source workstream: Add required MD/SHA-0/RIPEMD and other legacy digest families. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Every inventoried variant has test vectors; obsolete digests remain labelled unsuitable for modern integrity security. Each historical digest has independently verified exact revision/padding/encoding semantics; no insecure digest becomes an authentication default. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.229.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.230.0 — GOST digests

**Status:** planned.

**Setup:** baseline 0.229.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** GOST digests.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.130.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only gost digests within the source workstream: Add inventoried GOST/SM3/Whirlpool/Snefru/HAS-160 and other uncommon digests as applicable. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Provider absence, missing variants and licensing restrictions stay visible until resolved. GOST/SM3/Whirlpool/Snefru/HAS-160 and residual variants require separately scoped known answers, endian/parameter sets and bounded streaming state. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.230.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.231.0 — SM3 digest

**Status:** planned.

**Setup:** baseline 0.230.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** SM3 digest.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.130.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only sm3 digest within the source workstream: Add inventoried GOST/SM3/Whirlpool/Snefru/HAS-160 and other uncommon digests as applicable. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Provider absence, missing variants and licensing restrictions stay visible until resolved. GOST/SM3/Whirlpool/Snefru/HAS-160 and residual variants require separately scoped known answers, endian/parameter sets and bounded streaming state. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.231.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.232.0 — Whirlpool digest

**Status:** planned.

**Setup:** baseline 0.231.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Whirlpool digest.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.130.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only whirlpool digest within the source workstream: Add inventoried GOST/SM3/Whirlpool/Snefru/HAS-160 and other uncommon digests as applicable. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Provider absence, missing variants and licensing restrictions stay visible until resolved. GOST/SM3/Whirlpool/Snefru/HAS-160 and residual variants require separately scoped known answers, endian/parameter sets and bounded streaming state. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.232.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.233.0 — Snefru variants

**Status:** planned.

**Setup:** baseline 0.232.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Snefru variants.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.130.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only snefru variants within the source workstream: Add inventoried GOST/SM3/Whirlpool/Snefru/HAS-160 and other uncommon digests as applicable. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Provider absence, missing variants and licensing restrictions stay visible until resolved. GOST/SM3/Whirlpool/Snefru/HAS-160 and residual variants require separately scoped known answers, endian/parameter sets and bounded streaming state. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.233.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.234.0 — HAS-160 digest

**Status:** planned.

**Setup:** baseline 0.233.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** HAS-160 digest.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.130.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only has-160 digest within the source workstream: Add inventoried GOST/SM3/Whirlpool/Snefru/HAS-160 and other uncommon digests as applicable. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Provider absence, missing variants and licensing restrictions stay visible until resolved. GOST/SM3/Whirlpool/Snefru/HAS-160 and residual variants require separately scoped known answers, endian/parameter sets and bounded streaming state. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.234.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.235.0 — Residual specialist digest closure

**Status:** planned.

**Setup:** baseline 0.234.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Residual specialist digest closure.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.130.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only residual specialist digest closure within the source workstream: Add inventoried GOST/SM3/Whirlpool/Snefru/HAS-160 and other uncommon digests as applicable. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Provider absence, missing variants and licensing restrictions stay visible until resolved. GOST/SM3/Whirlpool/Snefru/HAS-160 and residual variants require separately scoped known answers, endian/parameter sets and bounded streaming state. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.235.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.236.0 — Fuzzy and similarity hashes

**Status:** planned.

**Setup:** baseline 0.235.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Fuzzy and similarity hashes.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add the reference’s fuzzy/context-triggered hashes and comparison utilities. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Similarity scores, block sizes and edge cases match reference behavior; results are not represented as cryptographic proofs. Fuzzy hashes pin algorithm/data/revision and test similarity edge cases against an independent implementation; matches are explained as evidence, not identity proof. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.236.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.237.0 — ROT and substitution analysis

**Status:** planned.

**Setup:** baseline 0.236.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** ROT and substitution analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.132.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only rot and substitution analysis within the source workstream: Add ROT families, Vigenere, Morse, Bacon, Affine, Atbash, A1Z26, substitution and related inventory entries. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Alphabet, case, punctuation and non-ASCII policies are explicit and fixture-tested. Each substitution/ROT/Vigenere/Morse/Bacon/Affine/Atbash/A1Z26 variant freezes alphabet/case/nonalphabet handling with independent reference vectors. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.237.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.238.0 — Vigenere analysis

**Status:** planned.

**Setup:** baseline 0.237.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Vigenere analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.132.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only vigenere analysis within the source workstream: Add ROT families, Vigenere, Morse, Bacon, Affine, Atbash, A1Z26, substitution and related inventory entries. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Alphabet, case, punctuation and non-ASCII policies are explicit and fixture-tested. Each substitution/ROT/Vigenere/Morse/Bacon/Affine/Atbash/A1Z26 variant freezes alphabet/case/nonalphabet handling with independent reference vectors. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.238.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.239.0 — Morse encoding

**Status:** planned.

**Setup:** baseline 0.238.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Morse encoding.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.132.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only morse encoding within the source workstream: Add ROT families, Vigenere, Morse, Bacon, Affine, Atbash, A1Z26, substitution and related inventory entries. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Alphabet, case, punctuation and non-ASCII policies are explicit and fixture-tested. Each substitution/ROT/Vigenere/Morse/Bacon/Affine/Atbash/A1Z26 variant freezes alphabet/case/nonalphabet handling with independent reference vectors. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.239.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.240.0 — Bacon encoding

**Status:** planned.

**Setup:** baseline 0.239.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Bacon encoding.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.132.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only bacon encoding within the source workstream: Add ROT families, Vigenere, Morse, Bacon, Affine, Atbash, A1Z26, substitution and related inventory entries. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Alphabet, case, punctuation and non-ASCII policies are explicit and fixture-tested. Each substitution/ROT/Vigenere/Morse/Bacon/Affine/Atbash/A1Z26 variant freezes alphabet/case/nonalphabet handling with independent reference vectors. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.240.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.241.0 — Affine cipher

**Status:** planned.

**Setup:** baseline 0.240.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Affine cipher.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.132.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only affine cipher within the source workstream: Add ROT families, Vigenere, Morse, Bacon, Affine, Atbash, A1Z26, substitution and related inventory entries. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Alphabet, case, punctuation and non-ASCII policies are explicit and fixture-tested. Each substitution/ROT/Vigenere/Morse/Bacon/Affine/Atbash/A1Z26 variant freezes alphabet/case/nonalphabet handling with independent reference vectors. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.241.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.242.0 — Atbash cipher

**Status:** planned.

**Setup:** baseline 0.241.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Atbash cipher.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.132.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only atbash cipher within the source workstream: Add ROT families, Vigenere, Morse, Bacon, Affine, Atbash, A1Z26, substitution and related inventory entries. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Alphabet, case, punctuation and non-ASCII policies are explicit and fixture-tested. Each substitution/ROT/Vigenere/Morse/Bacon/Affine/Atbash/A1Z26 variant freezes alphabet/case/nonalphabet handling with independent reference vectors. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.242.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.243.0 — A1Z26 encoding

**Status:** planned.

**Setup:** baseline 0.242.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** A1Z26 encoding.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.132.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only a1z26 encoding within the source workstream: Add ROT families, Vigenere, Morse, Bacon, Affine, Atbash, A1Z26, substitution and related inventory entries. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Alphabet, case, punctuation and non-ASCII policies are explicit and fixture-tested. Each substitution/ROT/Vigenere/Morse/Bacon/Affine/Atbash/A1Z26 variant freezes alphabet/case/nonalphabet handling with independent reference vectors. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.243.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.244.0 — Residual classical substitution closure

**Status:** planned.

**Setup:** baseline 0.243.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Residual classical substitution closure.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.132.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only residual classical substitution closure within the source workstream: Add ROT families, Vigenere, Morse, Bacon, Affine, Atbash, A1Z26, substitution and related inventory entries. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Alphabet, case, punctuation and non-ASCII policies are explicit and fixture-tested. Each substitution/ROT/Vigenere/Morse/Bacon/Affine/Atbash/A1Z26 variant freezes alphabet/case/nonalphabet handling with independent reference vectors. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.244.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.245.0 — Bifid analysis

**Status:** planned.

**Setup:** baseline 0.244.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Bifid analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.133.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only bifid analysis within the source workstream: Add Bifid, Rail Fence, Caesar Box and other inventoried transposition/novel encodings. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Incomplete grids, key validation and reverse transforms preserve the required conventions. Each Bifid/Rail Fence/Caesar Box/transposition variant defines dimensions, padding and global-input bounds; inverse/reference and malformed cases pass. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.245.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.246.0 — Rail Fence analysis

**Status:** planned.

**Setup:** baseline 0.245.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Rail Fence analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.133.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only rail fence analysis within the source workstream: Add Bifid, Rail Fence, Caesar Box and other inventoried transposition/novel encodings. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Incomplete grids, key validation and reverse transforms preserve the required conventions. Each Bifid/Rail Fence/Caesar Box/transposition variant defines dimensions, padding and global-input bounds; inverse/reference and malformed cases pass. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.246.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.247.0 — Caesar Box analysis

**Status:** planned.

**Setup:** baseline 0.246.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Caesar Box analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.133.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only caesar box analysis within the source workstream: Add Bifid, Rail Fence, Caesar Box and other inventoried transposition/novel encodings. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Incomplete grids, key validation and reverse transforms preserve the required conventions. Each Bifid/Rail Fence/Caesar Box/transposition variant defines dimensions, padding and global-input bounds; inverse/reference and malformed cases pass. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.247.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.248.0 — Residual classical transposition closure

**Status:** planned.

**Setup:** baseline 0.247.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Residual classical transposition closure.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.133.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only residual classical transposition closure within the source workstream: Add Bifid, Rail Fence, Caesar Box and other inventoried transposition/novel encodings. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Incomplete grids, key validation and reverse transforms preserve the required conventions. Each Bifid/Rail Fence/Caesar Box/transposition variant defines dimensions, padding and global-input bounds; inverse/reference and malformed cases pass. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.248.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.249.0 — Enigma analysis

**Status:** planned.

**Setup:** baseline 0.248.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Enigma analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.134.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only enigma analysis within the source workstream: Add Enigma/Typex/Lorenz/SIGABA and associated analysis tools such as Bombe/Colossus when inventoried. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Machine settings and known historical/reference fixtures agree; expensive searches have strict work budgets. Enigma/Typex/Lorenz/SIGABA and inventoried search tools have exact machine settings/vectors; key search has global fuel and deterministic cancellation. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.249.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.250.0 — Typex analysis

**Status:** planned.

**Setup:** baseline 0.249.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Typex analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.134.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only typex analysis within the source workstream: Add Enigma/Typex/Lorenz/SIGABA and associated analysis tools such as Bombe/Colossus when inventoried. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Machine settings and known historical/reference fixtures agree; expensive searches have strict work budgets. Enigma/Typex/Lorenz/SIGABA and inventoried search tools have exact machine settings/vectors; key search has global fuel and deterministic cancellation. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.250.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.251.0 — Lorenz analysis

**Status:** planned.

**Setup:** baseline 0.250.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Lorenz analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.134.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only lorenz analysis within the source workstream: Add Enigma/Typex/Lorenz/SIGABA and associated analysis tools such as Bombe/Colossus when inventoried. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Machine settings and known historical/reference fixtures agree; expensive searches have strict work budgets. Enigma/Typex/Lorenz/SIGABA and inventoried search tools have exact machine settings/vectors; key search has global fuel and deterministic cancellation. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.251.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.252.0 — SIGABA analysis

**Status:** planned.

**Setup:** baseline 0.251.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** SIGABA analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.134.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only sigaba analysis within the source workstream: Add Enigma/Typex/Lorenz/SIGABA and associated analysis tools such as Bombe/Colossus when inventoried. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Machine settings and known historical/reference fixtures agree; expensive searches have strict work budgets. Enigma/Typex/Lorenz/SIGABA and inventoried search tools have exact machine settings/vectors; key search has global fuel and deterministic cancellation. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.252.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.253.0 — Bombe search if inventoried

**Status:** planned.

**Setup:** baseline 0.252.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Bombe search if inventoried.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.134.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only bombe search if inventoried within the source workstream: Add Enigma/Typex/Lorenz/SIGABA and associated analysis tools such as Bombe/Colossus when inventoried. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Machine settings and known historical/reference fixtures agree; expensive searches have strict work budgets. Enigma/Typex/Lorenz/SIGABA and inventoried search tools have exact machine settings/vectors; key search has global fuel and deterministic cancellation. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.253.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.254.0 — Colossus search if inventoried

**Status:** planned.

**Setup:** baseline 0.253.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Colossus search if inventoried.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.134.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only colossus search if inventoried within the source workstream: Add Enigma/Typex/Lorenz/SIGABA and associated analysis tools such as Bombe/Colossus when inventoried. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Machine settings and known historical/reference fixtures agree; expensive searches have strict work budgets. Enigma/Typex/Lorenz/SIGABA and inventoried search tools have exact machine settings/vectors; key search has global fuel and deterministic cancellation. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.254.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.255.0 — EVP legacy compatibility

**Status:** planned.

**Setup:** baseline 0.254.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** EVP legacy compatibility.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.135.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only evp legacy compatibility within the source workstream: Deliver remaining EVP/CipherSaber/Citrix/LS47 and other residual legacy entries, splitting releases as necessary. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Generated coverage shows no unowned long-tail algorithm or argument gap; all required browser paths are tested. Every legacy workstream/argument/target closes independently; unsupported historical functionality remains explicit rather than hidden by modern providers. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.255.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.256.0 — CipherSaber analysis

**Status:** planned.

**Setup:** baseline 0.255.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** CipherSaber analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.135.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only ciphersaber analysis within the source workstream: Deliver remaining EVP/CipherSaber/Citrix/LS47 and other residual legacy entries, splitting releases as necessary. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Generated coverage shows no unowned long-tail algorithm or argument gap; all required browser paths are tested. Every legacy workstream/argument/target closes independently; unsupported historical functionality remains explicit rather than hidden by modern providers. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.256.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.257.0 — Citrix compatibility

**Status:** planned.

**Setup:** baseline 0.256.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Citrix compatibility.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.135.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only citrix compatibility within the source workstream: Deliver remaining EVP/CipherSaber/Citrix/LS47 and other residual legacy entries, splitting releases as necessary. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Generated coverage shows no unowned long-tail algorithm or argument gap; all required browser paths are tested. Every legacy workstream/argument/target closes independently; unsupported historical functionality remains explicit rather than hidden by modern providers. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.257.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.258.0 — LS47 analysis

**Status:** planned.

**Setup:** baseline 0.257.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** LS47 analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.135.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only ls47 analysis within the source workstream: Deliver remaining EVP/CipherSaber/Citrix/LS47 and other residual legacy entries, splitting releases as necessary. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Generated coverage shows no unowned long-tail algorithm or argument gap; all required browser paths are tested. Every legacy workstream/argument/target closes independently; unsupported historical functionality remains explicit rather than hidden by modern providers. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.258.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.259.0 — Residual legacy acceptance

**Status:** planned.

**Setup:** baseline 0.258.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Residual legacy acceptance.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.135.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only residual legacy acceptance within the source workstream: Deliver remaining EVP/CipherSaber/Citrix/LS47 and other residual legacy entries, splitting releases as necessary. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Generated coverage shows no unowned long-tail algorithm or argument gap; all required browser paths are tested. Every legacy workstream/argument/target closes independently; unsupported historical functionality remains explicit rather than hidden by modern providers. Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.259.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.
