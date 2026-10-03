# Phase K: Network and forensic analysis

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

## v0.274.0 — IP and network primitives

**Status:** planned.

**Setup:** baseline 0.273.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** IP and network primitives.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add IP-format conversion, subnets, CIDR calculations and related byte/address operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** IPv4/IPv6, mapped addresses and boundary masks have fixtures without accidental outbound traffic. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.274.0 implementation stop reached. Run pentest for this exact commit.

## v0.275.0 — URL and domain analysis

**Status:** planned.

**Setup:** baseline 0.274.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** URL and domain analysis.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add URL parsing, extraction, defang/refang and domain helpers from inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Decoding order and Unicode display cannot silently change a network destination. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.275.0 implementation stop reached. Run pentest for this exact commit.

## v0.276.0 — HTTP data parsing

**Status:** planned.

**Setup:** baseline 0.275.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** HTTP data parsing.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add request/response, headers, cookies, content metadata and related format operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Ambiguous framing is reported; parsing hostile HTTP never routes it through the live service parser as a trusted request. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.276.0 implementation stop reached. Run pentest for this exact commit.

## v0.277.0 — User HTTP request operation

**Status:** planned.

**Setup:** baseline 0.276.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** User HTTP request operation.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Expose explicit browser-fetch and controlled native-gateway modes with credential/redirection policy. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Browser CORS limitations are visible; remote mode passes SSRF and egress tests and never runs automatically on import. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.277.0 implementation stop reached. Run pentest for this exact commit.

## v0.278.0 — DNS data and queries

**Status:** planned.

**Setup:** baseline 0.277.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** DNS data and queries.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add required DNS parsing/lookup capabilities with separate local-data and network modes. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Network use requires consent/capability; responses, name compression and timeout/work limits are bounded. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.278.0 implementation stop reached. Run pentest for this exact commit.

## v0.279.0 — TLS and SSH fingerprints

**Status:** planned.

**Setup:** baseline 0.278.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** TLS and SSH fingerprints.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add inventoried JA3/JA4/HASSH and related passive fingerprint operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Fingerprint versions and normalization rules are explicit; analysis of legacy handshakes does not enable legacy TLS transport. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.279.0 implementation stop reached. Run pentest for this exact commit.

## v0.280.0 — Packet and protocol extraction

**Status:** planned.

**Setup:** baseline 0.279.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Packet and protocol extraction.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add required packet/protocol field parsers, protobuf/varint helpers and payload extraction. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Truncation, nested lengths and reassembly limits are tested; unsupported protocol revisions are reported. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.280.0 implementation stop reached. Run pentest for this exact commit.

## v0.281.0 — File identification

**Status:** planned.

**Setup:** baseline 0.280.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** File identification.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add versioned signatures, confidence explanations, strings and binary structure probes. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Detection is labelled heuristic where appropriate; input-controlled paths or extensions do not override byte evidence. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.281.0 implementation stop reached. Run pentest for this exact commit.

## v0.282.0 — Executable analysis

**Status:** planned.

**Setup:** baseline 0.281.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Executable analysis.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add the inventoried executable formats and section/header extraction with bounded reads. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Corrupt offsets and huge section counts fail safely; extracted code is never executed. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.282.0 implementation stop reached. Run pentest for this exact commit.

## v0.283.0 — Disassembly

**Status:** planned.

**Setup:** baseline 0.282.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Disassembly.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Integrate the required architectures/modes through isolated providers and structured instruction results. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Native/browser outputs and syntax options match the selected reference; architecture support is enumerated, not implied. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.283.0 implementation stop reached. Run pentest for this exact commit.

## v0.284.0 — YARA language support

**Status:** planned.

**Setup:** baseline 0.283.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** YARA language support.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Deliver the exact required YARA syntax/module behavior and compiler diagnostics. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Rule corpus covers modules, strings, conditions and language variants; a subset implementation cannot claim full parity. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.284.0 implementation stop reached. Run pentest for this exact commit.

## v0.285.0 — YARA execution controls

**Status:** planned.

**Setup:** baseline 0.284.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** YARA execution controls.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add match offsets, metadata, warnings, cost limits and killable worker execution. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Hostile rules and many matches respect budgets; scanning requires no filesystem/network privileges. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.285.0 implementation stop reached. Run pentest for this exact commit.

## v0.286.0 — Carving and extraction

**Status:** planned.

**Setup:** baseline 0.285.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Carving and extraction.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add byte signatures, embedded artifact carving and bounded output collections. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Overlapping candidates, nested files and excessive matches cannot exceed job-wide quotas. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.286.0 implementation stop reached. Run pentest for this exact commit.

## v0.287.0 — Forensic analysis views

**Status:** planned.

**Setup:** baseline 0.286.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Forensic analysis views.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add entropy maps, byte frequency, comparisons and inventoried statistical/search helpers. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Sampling versus full analysis is labelled; results are deterministic for a fixed input and algorithm revision. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.287.0 implementation stop reached. Run pentest for this exact commit.

## v0.288.0 — Forensic completeness gate

**Status:** planned.

**Setup:** baseline 0.287.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Forensic completeness gate.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Reconcile network/forensic inventory, capabilities, passive/active distinctions and offline availability. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** No browser-local reference capability is silently replaced by a server-only implementation. Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.288.0 implementation stop reached. Run pentest for this exact commit.
