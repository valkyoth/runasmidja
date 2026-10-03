# Phase H: Modern hashing and cryptographic operations

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

## v0.160.0 — Crypto provider boundary

**Status:** planned.

**Setup:** baseline 0.159.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Crypto provider boundary.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Define key/nonce/tag types, randomness injection, algorithm identifiers and capability metadata. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Raw keys are redacted and excluded from default persistence/cache; no application transport depends on operation-pack crypto. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.160.0 implementation stop reached. Run pentest for this exact commit.

## v0.161.0 — SHA-2 variants

**Status:** planned.

**Setup:** baseline 0.160.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** SHA-2 variants.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.107.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only sha-2 variants within the source workstream: Add required SHA-2 variants, HMAC parameters and streaming hash operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Known-answer vectors, long inputs and arbitrary partitions agree across targets. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.161.0 implementation stop reached. Run pentest for this exact commit.

## v0.162.0 — HMAC construction

**Status:** planned.

**Setup:** baseline 0.161.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** HMAC construction.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.107.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only hmac construction within the source workstream: Add required SHA-2 variants, HMAC parameters and streaming hash operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Known-answer vectors, long inputs and arbitrary partitions agree across targets. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.162.0 implementation stop reached. Run pentest for this exact commit.

## v0.163.0 — SHA-3 variants

**Status:** planned.

**Setup:** baseline 0.162.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** SHA-3 variants.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.108.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only sha-3 variants within the source workstream: Add distinct SHA-3/Keccak variants and SHAKE-style extendable outputs where in scope. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Domain separation and output length are explicit; similar algorithm names cannot be substituted. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.163.0 implementation stop reached. Run pentest for this exact commit.

## v0.164.0 — Keccak variants

**Status:** planned.

**Setup:** baseline 0.163.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Keccak variants.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.108.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only keccak variants within the source workstream: Add distinct SHA-3/Keccak variants and SHAKE-style extendable outputs where in scope. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Domain separation and output length are explicit; similar algorithm names cannot be substituted. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.164.0 implementation stop reached. Run pentest for this exact commit.

## v0.165.0 — SHAKE output semantics

**Status:** planned.

**Setup:** baseline 0.164.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** SHAKE output semantics.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.108.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only shake output semantics within the source workstream: Add distinct SHA-3/Keccak variants and SHAKE-style extendable outputs where in scope. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Domain separation and output length are explicit; similar algorithm names cannot be substituted. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.165.0 implementation stop reached. Run pentest for this exact commit.

## v0.166.0 — BLAKE variants

**Status:** planned.

**Setup:** baseline 0.165.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** BLAKE variants.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.109.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only blake variants within the source workstream: Add required BLAKE variants and optional BLAKE3 enhancement through narrow provider features. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Keyed/context modes and tree boundaries have vectors; provider upgrades cannot silently alter cache identities. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.166.0 implementation stop reached. Run pentest for this exact commit.

## v0.167.0 — BLAKE3 enhancement assessment

**Status:** planned.

**Setup:** baseline 0.166.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** BLAKE3 enhancement assessment.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.109.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only blake3 enhancement assessment within the source workstream: Add required BLAKE variants and optional BLAKE3 enhancement through narrow provider features. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Keyed/context modes and tree boundaries have vectors; provider upgrades cannot silently alter cache identities. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.167.0 implementation stop reached. Run pentest for this exact commit.

## v0.168.0 — Checksums and CRCs

**Status:** planned.

**Setup:** baseline 0.167.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Checksums and CRCs.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add inventory checksum families and parameterized CRC configurations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Polynomial reflection, initial/final values and output byte order are independently tested. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.168.0 implementation stop reached. Run pentest for this exact commit.

## v0.169.0 — PBKDF2

**Status:** planned.

**Setup:** baseline 0.168.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** PBKDF2.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.111.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only pbkdf2 within the source workstream: Add PBKDF2, HKDF and related modern derivations with parameter ceilings. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Salt/info distinctions, output bounds and excessive iteration requests are tested; secrets remain tainted. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.169.0 implementation stop reached. Run pentest for this exact commit.

## v0.170.0 — HKDF

**Status:** planned.

**Setup:** baseline 0.169.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** HKDF.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.111.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only hkdf within the source workstream: Add PBKDF2, HKDF and related modern derivations with parameter ceilings. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Salt/info distinctions, output bounds and excessive iteration requests are tested; secrets remain tainted. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.170.0 implementation stop reached. Run pentest for this exact commit.

## v0.171.0 — Residual inventoried KDFs

**Status:** planned.

**Setup:** baseline 0.170.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Residual inventoried KDFs.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.111.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only residual inventoried kdfs within the source workstream: Add PBKDF2, HKDF and related modern derivations with parameter ceilings. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Salt/info distinctions, output bounds and excessive iteration requests are tested; secrets remain tainted. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.171.0 implementation stop reached. Run pentest for this exact commit.

## v0.172.0 — bcrypt variants

**Status:** planned.

**Setup:** baseline 0.171.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** bcrypt variants.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.112.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only bcrypt variants within the source workstream: Add bcrypt/scrypt and a separately labelled Argon2 enhancement when provider review permits. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: CPU/memory costs are validated before scheduling; compatibility variants and truncation rules are explicit. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.172.0 implementation stop reached. Run pentest for this exact commit.

## v0.173.0 — scrypt variants

**Status:** planned.

**Setup:** baseline 0.172.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** scrypt variants.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.112.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only scrypt variants within the source workstream: Add bcrypt/scrypt and a separately labelled Argon2 enhancement when provider review permits. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: CPU/memory costs are validated before scheduling; compatibility variants and truncation rules are explicit. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.173.0 implementation stop reached. Run pentest for this exact commit.

## v0.174.0 — Argon2 enhancement assessment

**Status:** planned.

**Setup:** baseline 0.173.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Argon2 enhancement assessment.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.112.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only argon2 enhancement assessment within the source workstream: Add bcrypt/scrypt and a separately labelled Argon2 enhancement when provider review permits. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: CPU/memory costs are validated before scheduling; compatibility variants and truncation rules are explicit. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.174.0 implementation stop reached. Run pentest for this exact commit.

## v0.175.0 — AES block-mode inventory and provider qualification

**Status:** planned.

**Setup:** baseline 0.174.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** AES block-mode inventory and provider qualification.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.113.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only aes block-mode inventory and provider qualification within the source workstream: Add inventoried AES modes, key lengths, padding and byte-format mappings. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Standard vectors and negative padding cases pass; insecure modes are analysis tools, never default application encryption. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.175.0 implementation stop reached. Run pentest for this exact commit.

## v0.176.0 — AES ECB analysis

**Status:** planned.

**Setup:** baseline 0.175.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** AES ECB analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.113.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only aes ecb analysis within the source workstream: Add inventoried AES modes, key lengths, padding and byte-format mappings. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Standard vectors and negative padding cases pass; insecure modes are analysis tools, never default application encryption. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.176.0 implementation stop reached. Run pentest for this exact commit.

## v0.177.0 — AES CBC analysis

**Status:** planned.

**Setup:** baseline 0.176.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** AES CBC analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.113.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only aes cbc analysis within the source workstream: Add inventoried AES modes, key lengths, padding and byte-format mappings. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Standard vectors and negative padding cases pass; insecure modes are analysis tools, never default application encryption. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.177.0 implementation stop reached. Run pentest for this exact commit.

## v0.178.0 — AES CFB analysis

**Status:** planned.

**Setup:** baseline 0.177.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** AES CFB analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.113.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only aes cfb analysis within the source workstream: Add inventoried AES modes, key lengths, padding and byte-format mappings. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Standard vectors and negative padding cases pass; insecure modes are analysis tools, never default application encryption. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.178.0 implementation stop reached. Run pentest for this exact commit.

## v0.179.0 — AES OFB analysis

**Status:** planned.

**Setup:** baseline 0.178.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** AES OFB analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.113.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only aes ofb analysis within the source workstream: Add inventoried AES modes, key lengths, padding and byte-format mappings. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Standard vectors and negative padding cases pass; insecure modes are analysis tools, never default application encryption. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.179.0 implementation stop reached. Run pentest for this exact commit.

## v0.180.0 — AES CTR analysis

**Status:** planned.

**Setup:** baseline 0.179.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** AES CTR analysis.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.113.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only aes ctr analysis within the source workstream: Add inventoried AES modes, key lengths, padding and byte-format mappings. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Standard vectors and negative padding cases pass; insecure modes are analysis tools, never default application encryption. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.180.0 implementation stop reached. Run pentest for this exact commit.

## v0.181.0 — Residual inventoried AES modes

**Status:** planned.

**Setup:** baseline 0.180.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Residual inventoried AES modes.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.113.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only residual inventoried aes modes within the source workstream: Add inventoried AES modes, key lengths, padding and byte-format mappings. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Standard vectors and negative padding cases pass; insecure modes are analysis tools, never default application encryption. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.181.0 implementation stop reached. Run pentest for this exact commit.

## v0.182.0 — AEAD parameter contracts

**Status:** planned.

**Setup:** baseline 0.181.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** AEAD parameter contracts.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.114.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only aead parameter contracts within the source workstream: Add required AEAD forms with staged decryption output and explicit tag verification. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: A failed tag releases no plaintext artifact; all input/tag/nonce changes have negative vectors. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.182.0 implementation stop reached. Run pentest for this exact commit.

## v0.183.0 — AEAD authenticated encryption

**Status:** planned.

**Setup:** baseline 0.182.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** AEAD authenticated encryption.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.114.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only aead authenticated encryption within the source workstream: Add required AEAD forms with staged decryption output and explicit tag verification. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: A failed tag releases no plaintext artifact; all input/tag/nonce changes have negative vectors. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.183.0 implementation stop reached. Run pentest for this exact commit.

## v0.184.0 — AEAD staged decryption publication

**Status:** planned.

**Setup:** baseline 0.183.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** AEAD staged decryption publication.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.114.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only aead staged decryption publication within the source workstream: Add required AEAD forms with staged decryption output and explicit tag verification. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: A failed tag releases no plaintext artifact; all input/tag/nonce changes have negative vectors. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.184.0 implementation stop reached. Run pentest for this exact commit.

## v0.185.0 — AES key wrap

**Status:** planned.

**Setup:** baseline 0.184.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** AES key wrap.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add wrap/unwrap variants and integrity checks required by the reference. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Invalid key lengths, padding and integrity failures do not expose partially unwrapped material. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.185.0 implementation stop reached. Run pentest for this exact commit.

## v0.186.0 — ChaCha stream variants

**Status:** planned.

**Setup:** baseline 0.185.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** ChaCha stream variants.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.116.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only chacha stream variants within the source workstream: Add exact ChaCha variants, counters and authenticated combinations when in scope. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Counter overflow and nonce construction are checked; variant differences remain visible in descriptors. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.186.0 implementation stop reached. Run pentest for this exact commit.

## v0.187.0 — Poly1305 authentication

**Status:** planned.

**Setup:** baseline 0.186.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Poly1305 authentication.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.116.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only poly1305 authentication within the source workstream: Add exact ChaCha variants, counters and authenticated combinations when in scope. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Counter overflow and nonce construction are checked; variant differences remain visible in descriptors. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.187.0 implementation stop reached. Run pentest for this exact commit.

## v0.188.0 — ChaCha authenticated combinations

**Status:** planned.

**Setup:** baseline 0.187.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** ChaCha authenticated combinations.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.116.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only chacha authenticated combinations within the source workstream: Add exact ChaCha variants, counters and authenticated combinations when in scope. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Counter overflow and nonce construction are checked; variant differences remain visible in descriptors. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.188.0 implementation stop reached. Run pentest for this exact commit.

## v0.189.0 — Salsa20

**Status:** planned.

**Setup:** baseline 0.188.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Salsa20.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.117.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only salsa20 within the source workstream: Add Salsa20/XSalsa20 operations with exact key, nonce and counter semantics. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Known vectors and boundary conditions work in streaming and one-shot paths. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.189.0 implementation stop reached. Run pentest for this exact commit.

## v0.190.0 — XSalsa20

**Status:** planned.

**Setup:** baseline 0.189.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** XSalsa20.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.117.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only xsalsa20 within the source workstream: Add Salsa20/XSalsa20 operations with exact key, nonce and counter semantics. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Known vectors and boundary conditions work in streaming and one-shot paths. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.190.0 implementation stop reached. Run pentest for this exact commit.

## v0.191.0 — Fernet and authenticated wrappers

**Status:** planned.

**Setup:** baseline 0.190.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Fernet and authenticated wrappers.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add Fernet and related required wrappers with timestamp and token-format handling. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Authentication precedes plaintext publication; injected clock and expiry policy are testable. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.191.0 implementation stop reached. Run pentest for this exact commit.

## v0.192.0 — Deterministic analysis PRNGs

**Status:** planned.

**Setup:** baseline 0.191.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Deterministic analysis PRNGs.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.119.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only deterministic analysis prngs within the source workstream: Add explicit deterministic PRNG operations and secure random/prime generation through distinct providers. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Seeded analysis tools are not mistaken for CSPRNG; entropy failure is fatal where secure randomness is required. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.192.0 implementation stop reached. Run pentest for this exact commit.

## v0.193.0 — Secure random generation

**Status:** planned.

**Setup:** baseline 0.192.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Secure random generation.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.119.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only secure random generation within the source workstream: Add explicit deterministic PRNG operations and secure random/prime generation through distinct providers. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Seeded analysis tools are not mistaken for CSPRNG; entropy failure is fatal where secure randomness is required. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.193.0 implementation stop reached. Run pentest for this exact commit.

## v0.194.0 — Bounded prime generation

**Status:** planned.

**Setup:** baseline 0.193.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Bounded prime generation.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.119.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only bounded prime generation within the source workstream: Add explicit deterministic PRNG operations and secure random/prime generation through distinct providers. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Seeded analysis tools are not mistaken for CSPRNG; entropy failure is fatal where secure randomness is required. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.194.0 implementation stop reached. Run pentest for this exact commit.

## v0.195.0 — Modern crypto qualification

**Status:** planned.

**Setup:** baseline 0.194.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Modern crypto qualification.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Run independent vectors, malformed inputs, cross-provider comparisons and secret-lifecycle checks. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** No known high-severity provider issue remains; side-channel claims are limited to evidence and platform capabilities. Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.195.0 implementation stop reached. Run pentest for this exact commit.
