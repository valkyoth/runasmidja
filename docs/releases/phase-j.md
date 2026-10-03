# Phase J: Public keys, certificates and tokens

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

## v0.238.0 — BER parsing

**Status:** planned.

**Setup:** baseline 0.237.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** BER parsing.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.136.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only ber parsing within the source workstream: Add bounded BER/DER parsing, ASN.1 display and OID conversions required by inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Excessive lengths, recursion, non-canonical encodings and truncated objects have precise failures. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.238.0 implementation stop reached. Run pentest for this exact commit.

## v0.239.0 — DER canonical parsing

**Status:** planned.

**Setup:** baseline 0.238.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** DER canonical parsing.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.136.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only der canonical parsing within the source workstream: Add bounded BER/DER parsing, ASN.1 display and OID conversions required by inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Excessive lengths, recursion, non-canonical encodings and truncated objects have precise failures. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.239.0 implementation stop reached. Run pentest for this exact commit.

## v0.240.0 — ASN.1 display

**Status:** planned.

**Setup:** baseline 0.239.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** ASN.1 display.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.136.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only asn.1 display within the source workstream: Add bounded BER/DER parsing, ASN.1 display and OID conversions required by inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Excessive lengths, recursion, non-canonical encodings and truncated objects have precise failures. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.240.0 implementation stop reached. Run pentest for this exact commit.

## v0.241.0 — OID conversion

**Status:** planned.

**Setup:** baseline 0.240.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OID conversion.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.136.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only oid conversion within the source workstream: Add bounded BER/DER parsing, ASN.1 display and OID conversions required by inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Excessive lengths, recursion, non-canonical encodings and truncated objects have precise failures. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.241.0 implementation stop reached. Run pentest for this exact commit.

## v0.242.0 — PEM and key representations

**Status:** planned.

**Setup:** baseline 0.241.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** PEM and key representations.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add PEM/hex/JWK conversions and typed private/public key containers. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Key types, curves, leading zeros and private-field redaction survive round trips. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.242.0 implementation stop reached. Run pentest for this exact commit.

## v0.243.0 — X.509 fields and extensions

**Status:** planned.

**Setup:** baseline 0.242.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** X.509 fields and extensions.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.138.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only x.509 fields and extensions within the source workstream: Add certificate fields, extensions, public-key extraction, certificate-bundle parsing and required display forms; pin the adopted current-source delta. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Parsing success is never labelled certificate trust; unknown extensions remain available as data. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.243.0 implementation stop reached. Run pentest for this exact commit.

## v0.244.0 — Certificate-bundle parsing delta

**Status:** planned.

**Setup:** baseline 0.243.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Certificate-bundle parsing delta.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.138.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only certificate-bundle parsing delta within the source workstream: Add certificate fields, extensions, public-key extraction, certificate-bundle parsing and required display forms; pin the adopted current-source delta. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Parsing success is never labelled certificate trust; unknown extensions remain available as data. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.244.0 implementation stop reached. Run pentest for this exact commit.

## v0.245.0 — CRL analysis

**Status:** planned.

**Setup:** baseline 0.244.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** CRL analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.139.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only crl analysis within the source workstream: Add revocation-list and signing-request parsing with explicit signature-verification actions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Invalid signatures and malformed fields are distinguished from mere parsing errors. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.245.0 implementation stop reached. Run pentest for this exact commit.

## v0.246.0 — CSR analysis

**Status:** planned.

**Setup:** baseline 0.245.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** CSR analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.139.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only csr analysis within the source workstream: Add revocation-list and signing-request parsing with explicit signature-verification actions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Invalid signatures and malformed fields are distinguished from mere parsing errors. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.246.0 implementation stop reached. Run pentest for this exact commit.

## v0.247.0 — RSA key generation

**Status:** planned.

**Setup:** baseline 0.246.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** RSA key generation.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.140.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only rsa key generation within the source workstream: Add key generation, encrypt/decrypt and sign/verify with exact padding/hash options. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Entropy, key-size budgets, padding failures and reference compatibility are tested; no raw-secret logging. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.247.0 implementation stop reached. Run pentest for this exact commit.

## v0.248.0 — RSA encryption and decryption

**Status:** planned.

**Setup:** baseline 0.247.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** RSA encryption and decryption.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.140.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only rsa encryption and decryption within the source workstream: Add key generation, encrypt/decrypt and sign/verify with exact padding/hash options. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Entropy, key-size budgets, padding failures and reference compatibility are tested; no raw-secret logging. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.248.0 implementation stop reached. Run pentest for this exact commit.

## v0.249.0 — RSA signing and verification

**Status:** planned.

**Setup:** baseline 0.248.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** RSA signing and verification.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.140.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only rsa signing and verification within the source workstream: Add key generation, encrypt/decrypt and sign/verify with exact padding/hash options. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Entropy, key-size budgets, padding failures and reference compatibility are tested; no raw-secret logging. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.249.0 implementation stop reached. Run pentest for this exact commit.

## v0.250.0 — ECDSA curve and key formats

**Status:** planned.

**Setup:** baseline 0.249.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** ECDSA curve and key formats.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.141.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only ecdsa curve and key formats within the source workstream: Add selected curves, key generation, signing/verification and signature-format conversion. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: DER versus fixed-width forms, low-S policy and invalid curve points are handled explicitly. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.250.0 implementation stop reached. Run pentest for this exact commit.

## v0.251.0 — ECDSA signatures

**Status:** planned.

**Setup:** baseline 0.250.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** ECDSA signatures.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.141.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only ecdsa signatures within the source workstream: Add selected curves, key generation, signing/verification and signature-format conversion. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: DER versus fixed-width forms, low-S policy and invalid curve points are handled explicitly. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.251.0 implementation stop reached. Run pentest for this exact commit.

## v0.252.0 — SM2 identity and signatures

**Status:** planned.

**Setup:** baseline 0.251.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** SM2 identity and signatures.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.142.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only sm2 identity and signatures within the source workstream: Add inventoried public-key operations, identity parameters and GOST wrap/sign variants. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Parameter sets and user-identity fields have vectors; missing provider variants remain blocking gaps. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.252.0 implementation stop reached. Run pentest for this exact commit.

## v0.253.0 — GOST signature and wrap variants

**Status:** planned.

**Setup:** baseline 0.252.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** GOST signature and wrap variants.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.142.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only gost signature and wrap variants within the source workstream: Add inventoried public-key operations, identity parameters and GOST wrap/sign variants. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Parameter sets and user-identity fields have vectors; missing provider variants remain blocking gaps. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.253.0 implementation stop reached. Run pentest for this exact commit.

## v0.254.0 — OpenPGP packet inspection

**Status:** planned.

**Setup:** baseline 0.253.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OpenPGP packet inspection.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.143.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only openpgp packet inspection within the source workstream: Add packet/key inspection and generation with the pinned reference’s capability matrix. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Unsupported packets or algorithms are reported precisely; packet lengths and recursion are bounded. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.254.0 implementation stop reached. Run pentest for this exact commit.

## v0.255.0 — OpenPGP key inspection

**Status:** planned.

**Setup:** baseline 0.254.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OpenPGP key inspection.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.143.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only openpgp key inspection within the source workstream: Add packet/key inspection and generation with the pinned reference’s capability matrix. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Unsupported packets or algorithms are reported precisely; packet lengths and recursion are bounded. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.255.0 implementation stop reached. Run pentest for this exact commit.

## v0.256.0 — OpenPGP key generation

**Status:** planned.

**Setup:** baseline 0.255.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OpenPGP key generation.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.143.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only openpgp key generation within the source workstream: Add packet/key inspection and generation with the pinned reference’s capability matrix. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Unsupported packets or algorithms are reported precisely; packet lengths and recursion are bounded. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.256.0 implementation stop reached. Run pentest for this exact commit.

## v0.257.0 — OpenPGP encryption

**Status:** planned.

**Setup:** baseline 0.256.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OpenPGP encryption.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add encrypt/decrypt and key-selection behavior for required OpenPGP formats. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Integrity-protected output stays staged until verified; legacy insecure forms are clearly identified. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.257.0 implementation stop reached. Run pentest for this exact commit.

## v0.258.0 — OpenPGP signing and verification

**Status:** planned.

**Setup:** baseline 0.257.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OpenPGP signing and verification.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.145.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only openpgp signing and verification within the source workstream: Add sign/verify and combined encrypt/sign workflows with separate validity and trust reports. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Detached/embedded signatures, canonical text and multi-signature cases match fixtures. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.258.0 implementation stop reached. Run pentest for this exact commit.

## v0.259.0 — OpenPGP combined encrypt and sign

**Status:** planned.

**Setup:** baseline 0.258.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** OpenPGP combined encrypt and sign.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.145.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only openpgp combined encrypt and sign within the source workstream: Add sign/verify and combined encrypt/sign workflows with separate validity and trust reports. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Detached/embedded signatures, canonical text and multi-signature cases match fixtures. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.259.0 implementation stop reached. Run pentest for this exact commit.

## v0.260.0 — SSH key analysis

**Status:** planned.

**Setup:** baseline 0.259.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** SSH key analysis.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add host-key parsing, fingerprints and inventoried conversions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Algorithm distinctions and malformed length fields are bounded; no SSH connection is implied by parsing a key. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.260.0 implementation stop reached. Run pentest for this exact commit.

## v0.261.0 — JWT and token inspection

**Status:** planned.

**Setup:** baseline 0.260.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** JWT and token inspection.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add decode/sign/verify with explicit permitted algorithms and key types. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Decode never implies validation; algorithm confusion, missing signatures and key-type mismatch tests fail closed. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.261.0 implementation stop reached. Run pentest for this exact commit.

## v0.262.0 — Signed session formats

**Status:** planned.

**Setup:** baseline 0.261.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Signed session formats.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add Flask-session and other inventoried signed-container workflows. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Timestamp, compression, secret encoding and serializer variants are fixture-tested without persisting signing secrets. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.262.0 implementation stop reached. Run pentest for this exact commit.

## v0.263.0 — Key and secret UX

**Status:** planned.

**Setup:** baseline 0.262.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Key and secret UX.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add ephemeral secret slots, import warnings, copy/export confirmation and reproducibility redaction. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Recipe sharing cannot accidentally include private keys; browser/OS memory erasure limitations are documented honestly. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.263.0 implementation stop reached. Run pentest for this exact commit.

## v0.264.0 — Public-key qualification

**Status:** planned.

**Setup:** baseline 0.263.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Public-key qualification.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Run independent vectors, malformed corpora, interoperability and browser/native conformance. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Every advertised algorithm/format is tested; a successful parse, a valid signature and a trusted identity remain distinct states. Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.264.0 implementation stop reached. Run pentest for this exact commit.
