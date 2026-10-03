# Phase J: Public keys, certificates and tokens

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

Verification checklists apply only to introduced or retained behavior in the reviewed bounded scope. Record absent later capabilities as pending with numbered owners; contract fixtures never attest their runtime PASS. A prerequisite needed by this pass must be implemented and verified first, rather than deferred. Every future owner still owes its full acceptance before exposure/1.0.

## v0.260.0 — BER parsing

**Status:** planned.

**Setup:** baseline 0.259.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** BER parsing.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.136.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only ber parsing within the source workstream: Add bounded BER/DER parsing, ASN.1 display and OID conversions required by inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Excessive lengths, recursion, non-canonical encodings and truncated objects have precise failures. BER/DER/ASN.1/OID scopes separately test canonicality, indefinite lengths, nesting, malformed tags and checked length/output budgets. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.260.0 implementation stop reached. Run pentest for this exact commit.

## v0.261.0 — DER canonical parsing

**Status:** planned.

**Setup:** baseline 0.260.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** DER canonical parsing.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.136.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only der canonical parsing within the source workstream: Add bounded BER/DER parsing, ASN.1 display and OID conversions required by inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Excessive lengths, recursion, non-canonical encodings and truncated objects have precise failures. BER/DER/ASN.1/OID scopes separately test canonicality, indefinite lengths, nesting, malformed tags and checked length/output budgets. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.261.0 implementation stop reached. Run pentest for this exact commit.

## v0.262.0 — ASN.1 display

**Status:** planned.

**Setup:** baseline 0.261.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** ASN.1 display.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.136.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only asn.1 display within the source workstream: Add bounded BER/DER parsing, ASN.1 display and OID conversions required by inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Excessive lengths, recursion, non-canonical encodings and truncated objects have precise failures. BER/DER/ASN.1/OID scopes separately test canonicality, indefinite lengths, nesting, malformed tags and checked length/output budgets. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.262.0 implementation stop reached. Run pentest for this exact commit.

## v0.263.0 — OID conversion

**Status:** planned.

**Setup:** baseline 0.262.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OID conversion.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.136.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only oid conversion within the source workstream: Add bounded BER/DER parsing, ASN.1 display and OID conversions required by inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Excessive lengths, recursion, non-canonical encodings and truncated objects have precise failures. BER/DER/ASN.1/OID scopes separately test canonicality, indefinite lengths, nesting, malformed tags and checked length/output budgets. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.263.0 implementation stop reached. Run pentest for this exact commit.

## v0.264.0 — PEM and key representations

**Status:** planned.

**Setup:** baseline 0.263.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** PEM and key representations.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add PEM/hex/JWK conversions and typed private/public key containers. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Key types, curves, leading zeros and private-field redaction survive round trips. PEM/key representations preserve format/type/algorithm distinctions; malformed armor and wrong labels reject, and private values keep secret sensitivity. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.264.0 implementation stop reached. Run pentest for this exact commit.

## v0.265.0 — X.509 fields and extensions

**Status:** planned.

**Setup:** baseline 0.264.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** X.509 fields and extensions.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.138.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only x.509 fields and extensions within the source workstream: Add certificate fields, extensions, public-key extraction, certificate-bundle parsing and required display forms; pin the adopted current-source delta. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Parsing success is never labelled certificate trust; unknown extensions remain available as data. X.509 fields/extensions/bundles parse with bounded lossless diagnostics; malformed/unknown extensions and algorithms remain data. Parsing never claims trust. Any separately inventoried validation action requires explicit roots/time/name/policy and its own negative trust fixtures. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.265.0 implementation stop reached. Run pentest for this exact commit.

## v0.266.0 — Certificate-bundle parsing delta

**Status:** planned.

**Setup:** baseline 0.265.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Certificate-bundle parsing delta.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.138.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only certificate-bundle parsing delta within the source workstream: Add certificate fields, extensions, public-key extraction, certificate-bundle parsing and required display forms; pin the adopted current-source delta. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Parsing success is never labelled certificate trust; unknown extensions remain available as data. X.509 fields/extensions/bundles parse with bounded lossless diagnostics; malformed/unknown extensions and algorithms remain data. Parsing never claims trust. Any separately inventoried validation action requires explicit roots/time/name/policy and its own negative trust fixtures. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.266.0 implementation stop reached. Run pentest for this exact commit.

## v0.267.0 — CRL analysis

**Status:** planned.

**Setup:** baseline 0.266.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** CRL analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.139.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only crl analysis within the source workstream: Add revocation-list and signing-request parsing with explicit signature-verification actions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Invalid signatures and malformed fields are distinguished from mere parsing errors. CRL/CSR parsing and explicit signature-verification actions have separate states and bounded independent fixtures. A valid signature alone cannot claim issuer trust, revocation completeness or certificate validity; those need separately scoped evidence. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.267.0 implementation stop reached. Run pentest for this exact commit.

## v0.268.0 — CSR analysis

**Status:** planned.

**Setup:** baseline 0.267.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** CSR analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.139.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only csr analysis within the source workstream: Add revocation-list and signing-request parsing with explicit signature-verification actions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Invalid signatures and malformed fields are distinguished from mere parsing errors. CRL/CSR parsing and explicit signature-verification actions have separate states and bounded independent fixtures. A valid signature alone cannot claim issuer trust, revocation completeness or certificate validity; those need separately scoped evidence. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.268.0 implementation stop reached. Run pentest for this exact commit.

## v0.269.0 — RSA key generation

**Status:** planned.

**Setup:** baseline 0.268.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** RSA key generation.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.140.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only rsa key generation within the source workstream: Add key generation, encrypt/decrypt and sign/verify with exact padding/hash options. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Entropy, key-size budgets, padding failures and reference compatibility are tested; no raw-secret logging. RSA generation/encryption/signature variants independently test padding/hash/length/key policy; secure entropy, malformed keys and relevant side-channel review pass. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.269.0 implementation stop reached. Run pentest for this exact commit.

## v0.270.0 — RSA encryption and decryption

**Status:** planned.

**Setup:** baseline 0.269.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** RSA encryption and decryption.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.140.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only rsa encryption and decryption within the source workstream: Add key generation, encrypt/decrypt and sign/verify with exact padding/hash options. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Entropy, key-size budgets, padding failures and reference compatibility are tested; no raw-secret logging. RSA generation/encryption/signature variants independently test padding/hash/length/key policy; secure entropy, malformed keys and relevant side-channel review pass. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.270.0 implementation stop reached. Run pentest for this exact commit.

## v0.271.0 — RSA signing and verification

**Status:** planned.

**Setup:** baseline 0.270.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** RSA signing and verification.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.140.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only rsa signing and verification within the source workstream: Add key generation, encrypt/decrypt and sign/verify with exact padding/hash options. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Entropy, key-size budgets, padding failures and reference compatibility are tested; no raw-secret logging. RSA generation/encryption/signature variants independently test padding/hash/length/key policy; secure entropy, malformed keys and relevant side-channel review pass. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.271.0 implementation stop reached. Run pentest for this exact commit.

## v0.272.0 — ECDSA curve and key formats

**Status:** planned.

**Setup:** baseline 0.271.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** ECDSA curve and key formats.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.141.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only ecdsa curve and key formats within the source workstream: Add selected curves, key generation, signing/verification and signature-format conversion. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: DER versus fixed-width forms, low-S policy and invalid curve points are handled explicitly. Each ECDSA curve/key/signature encoding gets independent vectors; malformed points/scalars, nonce policy, malleability rules and trust separation are explicit. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.272.0 implementation stop reached. Run pentest for this exact commit.

## v0.273.0 — ECDSA signatures

**Status:** planned.

**Setup:** baseline 0.272.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** ECDSA signatures.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.141.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only ecdsa signatures within the source workstream: Add selected curves, key generation, signing/verification and signature-format conversion. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: DER versus fixed-width forms, low-S policy and invalid curve points are handled explicitly. Each ECDSA curve/key/signature encoding gets independent vectors; malformed points/scalars, nonce policy, malleability rules and trust separation are explicit. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.273.0 implementation stop reached. Run pentest for this exact commit.

## v0.274.0 — SM2 identity and signatures

**Status:** planned.

**Setup:** baseline 0.273.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** SM2 identity and signatures.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.142.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only sm2 identity and signatures within the source workstream: Add inventoried public-key operations, identity parameters and GOST wrap/sign variants. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Parameter sets and user-identity fields have vectors; missing provider variants remain blocking gaps. SM2 identity and GOST parameter/signature/wrap variants pass independent vectors; wrong identity/curve/format inputs fail with no secret disclosure. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.274.0 implementation stop reached. Run pentest for this exact commit.

## v0.275.0 — GOST signature and wrap variants

**Status:** planned.

**Setup:** baseline 0.274.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** GOST signature and wrap variants.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.142.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only gost signature and wrap variants within the source workstream: Add inventoried public-key operations, identity parameters and GOST wrap/sign variants. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Parameter sets and user-identity fields have vectors; missing provider variants remain blocking gaps. SM2 identity and GOST parameter/signature/wrap variants pass independent vectors; wrong identity/curve/format inputs fail with no secret disclosure. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.275.0 implementation stop reached. Run pentest for this exact commit.

## v0.276.0 — OpenPGP packet inspection

**Status:** planned.

**Setup:** baseline 0.275.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OpenPGP packet inspection.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.143.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only openpgp packet inspection within the source workstream: Add packet/key inspection and generation with the pinned reference’s capability matrix. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Unsupported packets or algorithms are reported precisely; packet lengths and recursion are bounded. OpenPGP packet/key/generation variants pass independent corpora; legacy algorithm/packet gaps, nesting/compression limits, entropy and browser backend risks are explicit. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.276.0 implementation stop reached. Run pentest for this exact commit.

## v0.277.0 — OpenPGP key inspection

**Status:** planned.

**Setup:** baseline 0.276.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OpenPGP key inspection.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.143.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only openpgp key inspection within the source workstream: Add packet/key inspection and generation with the pinned reference’s capability matrix. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Unsupported packets or algorithms are reported precisely; packet lengths and recursion are bounded. OpenPGP packet/key/generation variants pass independent corpora; legacy algorithm/packet gaps, nesting/compression limits, entropy and browser backend risks are explicit. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.277.0 implementation stop reached. Run pentest for this exact commit.

## v0.278.0 — OpenPGP key generation

**Status:** planned.

**Setup:** baseline 0.277.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OpenPGP key generation.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.143.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only openpgp key generation within the source workstream: Add packet/key inspection and generation with the pinned reference’s capability matrix. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Unsupported packets or algorithms are reported precisely; packet lengths and recursion are bounded. OpenPGP packet/key/generation variants pass independent corpora; legacy algorithm/packet gaps, nesting/compression limits, entropy and browser backend risks are explicit. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.278.0 implementation stop reached. Run pentest for this exact commit.

## v0.279.0 — OpenPGP encryption

**Status:** planned.

**Setup:** baseline 0.278.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OpenPGP encryption.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add encrypt/decrypt and key-selection behavior for required OpenPGP formats. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Integrity-protected output stays staged until verified; legacy insecure forms are clearly identified. OpenPGP encrypted formats/recipient variants interoperate with independent tooling; wrong key/tag/MDC/truncation cannot expose plaintext before authentication. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.279.0 implementation stop reached. Run pentest for this exact commit.

## v0.280.0 — OpenPGP signing and verification

**Status:** planned.

**Setup:** baseline 0.279.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OpenPGP signing and verification.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.145.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only openpgp signing and verification within the source workstream: Add sign/verify and combined encrypt/sign workflows with separate validity and trust reports. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Detached/embedded signatures, canonical text and multi-signature cases match fixtures. OpenPGP signing/verification/combined variants freeze canonicalization and result states; cryptographic validity never implies identity trust by default. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.280.0 implementation stop reached. Run pentest for this exact commit.

## v0.281.0 — OpenPGP combined encrypt and sign

**Status:** planned.

**Setup:** baseline 0.280.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OpenPGP combined encrypt and sign.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.145.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only openpgp combined encrypt and sign within the source workstream: Add sign/verify and combined encrypt/sign workflows with separate validity and trust reports. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Detached/embedded signatures, canonical text and multi-signature cases match fixtures. OpenPGP signing/verification/combined variants freeze canonicalization and result states; cryptographic validity never implies identity trust by default. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.281.0 implementation stop reached. Run pentest for this exact commit.

## v0.282.0 — SSH key analysis

**Status:** planned.

**Setup:** baseline 0.281.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** SSH key analysis.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add host-key parsing, fingerprints and inventoried conversions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Algorithm distinctions and malformed length fields are bounded; no SSH connection is implied by parsing a key. SSH key/authorized-key formats and fingerprints have independent vectors; malformed keys/options and private-key display are bounded/redacted. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.282.0 implementation stop reached. Run pentest for this exact commit.

## v0.283.0 — JWT and token inspection

**Status:** planned.

**Setup:** baseline 0.282.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** JWT and token inspection.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add decode/sign/verify with explicit permitted algorithms and key types. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Decode never implies validation; algorithm confusion, missing signatures and key-type mismatch tests fail closed. Decode treats claims as untrusted data and never implies validation. Explicit verification modes test algorithm/key/signature confusion and configured issuer/audience/time policy; inspection preserves malformed/historical data according to its declared analysis profile without weakening live session validation. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.283.0 implementation stop reached. Run pentest for this exact commit.

## v0.284.0 — Signed session formats

**Status:** planned.

**Setup:** baseline 0.283.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Signed session formats.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add Flask-session and other inventoried signed-container workflows. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Timestamp, compression, secret encoding and serializer variants are fixture-tested without persisting signing secrets. Each signed-session format passes independent framing/MAC/signature vectors; decoded claims remain untrusted until explicitly verified and authorized. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.284.0 implementation stop reached. Run pentest for this exact commit.

## v0.285.0 — Key and secret UX

**Status:** planned.

**Setup:** baseline 0.284.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Key and secret UX.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add ephemeral secret slots, import warnings, copy/export confirmation and reproducibility redaction. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Recipe sharing cannot accidentally include private keys; browser/OS memory erasure limitations are documented honestly. Key entry/reveal/export/clipboard actions need scoped grants; sentinel keys never enter history, logs, links, cache, search or default persistence. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.285.0 implementation stop reached. Run pentest for this exact commit.

## v0.286.0 — Public-key qualification

**Status:** planned.

**Setup:** baseline 0.285.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Public-key qualification.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Run independent vectors, malformed corpora, interoperability and browser/native conformance. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Every advertised algorithm/format is tested; a successful parse, a valid signature and a trusted identity remain distinct states. All public-key/format/argument/target rows and trust-negative suites pass; browser backend limitations and relevant timing risks have qualified dispositions. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.286.0 implementation stop reached. Run pentest for this exact commit.
