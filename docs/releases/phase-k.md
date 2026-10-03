# Phase K: Network and forensic analysis

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

Verification checklists apply only to introduced or retained behavior in the reviewed bounded scope. Record absent later capabilities as pending with numbered owners; contract fixtures never attest their runtime PASS. A prerequisite needed by this pass must be implemented and verified first, rather than deferred. Every future owner still owes its full acceptance before exposure/1.0.

## v0.287.0 — IP and network primitives

**Status:** planned.

**Setup:** baseline 0.286.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** IP and network primitives.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add IP-format conversion, subnets, CIDR calculations and related byte/address operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** IPv4/IPv6, mapped addresses and boundary masks have fixtures without accidental outbound traffic. IP/CIDR/endian/network representations cover IPv4/IPv6 edge vectors without I/O; overflowing masks, ambiguous forms and malformed addresses reject. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.287.0 implementation stop reached. Run pentest for this exact commit.

## v0.288.0 — URL and domain analysis

**Status:** planned.

**Setup:** baseline 0.287.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** URL and domain analysis.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add URL parsing, extraction, defang/refang and domain helpers from inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Decoding order and Unicode display cannot silently change a network destination. URL/domain/punycode/public-suffix semantics pin datasets and parser rules; confusable/ambiguous/untrusted links remain inert and do not resolve automatically. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.288.0 implementation stop reached. Run pentest for this exact commit.

## v0.289.0 — HTTP data parsing

**Status:** planned.

**Setup:** baseline 0.288.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** HTTP data parsing.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add request/response, headers, cookies, content metadata and related format operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Ambiguous framing is reported; parsing hostile HTTP never routes it through the live service parser as a trusted request. HTTP artifact parsing is passive and distinct from serving; malformed framing/headers/binary bodies have bounded diagnostic output and no network effects. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.289.0 implementation stop reached. Run pentest for this exact commit.

## v0.290.0 — User HTTP request operation

**Status:** planned.

**Setup:** baseline 0.289.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** User HTTP request operation.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Expose explicit browser-fetch and controlled native-gateway modes with credential/redirection policy. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Browser CORS limitations are visible; remote mode passes SSRF and egress tests and never runs automatically on import. Explicit network grants plus broker SSRF policy cover every redirect/retry/connect; missing grants, private destinations and browser restrictions never cause silent remote fallback. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.290.0 implementation stop reached. Run pentest for this exact commit.

## v0.291.0 — DNS data and queries

**Status:** planned.

**Setup:** baseline 0.290.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** DNS data and queries.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add required DNS parsing/lookup capabilities with separate local-data and network modes. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Network use requires consent/capability; responses, name compression and timeout/work limits are bounded. DNS packet/query variants bound compression-pointer cycles, records and names; actual queries require grants and resolver/destination policy. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.291.0 implementation stop reached. Run pentest for this exact commit.

## v0.292.0 — TLS and SSH fingerprints

**Status:** planned.

**Setup:** baseline 0.291.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** TLS and SSH fingerprints.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add inventoried JA3/JA4/HASSH and related passive fingerprint operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Fingerprint versions and normalization rules are explicit; analysis of legacy handshakes does not enable legacy TLS transport. TLS/SSH fingerprint formats freeze exact revisions and input normalization with independent vectors; historical parsing cannot weaken live TLS policy. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.292.0 implementation stop reached. Run pentest for this exact commit.

## v0.293.0 — Packet and protocol extraction

**Status:** planned.

**Setup:** baseline 0.292.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Packet and protocol extraction.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add required packet/protocol field parsers, protobuf/varint helpers and payload extraction. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Truncation, nested lengths and reassembly limits are tested; unsupported protocol revisions are reported. Packet/protocol parsers reject malformed lengths/fragmentation/reassembly excess; passive offline input remains local and ordered outputs are reproducible. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.293.0 implementation stop reached. Run pentest for this exact commit.

## v0.294.0 — File identification

**Status:** planned.

**Setup:** baseline 0.293.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** File identification.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add versioned signatures, confidence explanations, strings and binary structure probes. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Detection is labelled heuristic where appropriate; input-controlled paths or extensions do not override byte evidence. File signatures/datasets are pinned and licensed; ambiguous/truncated/polyglot fixtures explain evidence and scanning remains bounded. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.294.0 implementation stop reached. Run pentest for this exact commit.

## v0.295.0 — Executable analysis

**Status:** planned.

**Setup:** baseline 0.294.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Executable analysis.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add the inventoried executable formats and section/header extraction with bounded reads. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Corrupt offsets and huge section counts fail safely; extracted code is never executed. Each executable format checks tables/offsets/overlap/depth with independent fixtures; analysis never loads/runs sample code or follows external resources. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.295.0 implementation stop reached. Run pentest for this exact commit.

## v0.296.0 — Disassembly

**Status:** planned.

**Setup:** baseline 0.295.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Disassembly.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Integrate the required architectures/modes through isolated providers and structured instruction results. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Native/browser outputs and syntax options match the selected reference; architecture support is enumerated, not implied. Each disassembly architecture/mode/endian has independent instruction vectors, truncation policy and bounded output; actual browser implementation is required. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.296.0 implementation stop reached. Run pentest for this exact commit.

## v0.297.0 — YARA language support

**Status:** planned.

**Setup:** baseline 0.296.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** YARA language support.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Deliver the exact required YARA syntax/module behavior and compiler diagnostics. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Rule corpus covers modules, strings, conditions and language variants; a subset implementation cannot claim full parity. Freeze YARA rule/compiler/module dialect, include policy and actual target support; unsupported syntax/modules reject instead of silently weakening rules. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.297.0 implementation stop reached. Run pentest for this exact commit.

## v0.298.0 — YARA execution controls

**Status:** planned.

**Setup:** baseline 0.297.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** YARA execution controls.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add match offsets, metadata, warnings, cost limits and killable worker execution. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Hostile rules and many matches respect budgets; scanning requires no filesystem/network privileges. Pathological patterns/loops/modules hit work/memory/output caps; rule compilation and scanning are killable and have no ambient filesystem/process/network access. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.298.0 implementation stop reached. Run pentest for this exact commit.

## v0.299.0 — Carving and extraction

**Status:** planned.

**Setup:** baseline 0.298.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Carving and extraction.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add byte signatures, embedded artifact carving and bounded output collections. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Overlapping candidates, nested files and excessive matches cannot exceed job-wide quotas. Carving/extraction bounds candidate count, overlap, total artifacts/bytes and file names; malicious patterns cannot create unlimited retained outputs. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.299.0 implementation stop reached. Run pentest for this exact commit.

## v0.300.0 — Forensic analysis views

**Status:** planned.

**Setup:** baseline 0.299.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Forensic analysis views.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add entropy maps, byte frequency, comparisons and inventoried statistical/search helpers. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Sampling versus full analysis is labelled; results are deterministic for a fixed input and algorithm revision. Forensic tables/bytes/provenance are paged and inert; payloads/sample identifiers do not leak through caches/logs or external lookups. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.300.0 implementation stop reached. Run pentest for this exact commit.

## v0.301.0 — Forensic completeness gate

**Status:** planned.

**Setup:** baseline 0.300.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Forensic completeness gate.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Reconcile network/forensic inventory, capabilities, passive/active distinctions and offline availability. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** No browser-local reference capability is silently replaced by a server-only implementation. All forensic/network operation/argument/target rows close with passive and explicit-capability tests; native-only YARA/disassembly remains a browser gap. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.301.0 implementation stop reached. Run pentest for this exact commit.
