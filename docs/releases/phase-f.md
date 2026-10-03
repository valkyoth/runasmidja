# Phase F: Structured formats, queries and utilities

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

## v0.121.0 — Lossless JSON

**Status:** planned.

**Setup:** baseline 0.120.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Lossless JSON.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.76.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only lossless json within the source workstream: Add strict/lossless JSON, CSV conversion, configurable delimiters, quoting and invalid-input diagnostics. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Large integers, duplicate-key policy, multiline fields and final newline behavior are fixture-tested. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.121.0 implementation stop reached. Run pentest for this exact commit.

## v0.122.0 — CSV semantics

**Status:** planned.

**Setup:** baseline 0.121.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** CSV semantics.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.76.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only csv semantics within the source workstream: Add strict/lossless JSON, CSV conversion, configurable delimiters, quoting and invalid-input diagnostics. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Large integers, duplicate-key policy, multiline fields and final newline behavior are fixture-tested. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.122.0 implementation stop reached. Run pentest for this exact commit.

## v0.123.0 — XML data processing

**Status:** planned.

**Setup:** baseline 0.122.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** XML data processing.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.77.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only xml data processing within the source workstream: Add XML/HTML extraction, formatting and escaping with external entity/network access disabled by default. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Entity expansion, excessive depth and malformed documents fail within budgets; renderers receive inert data. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.123.0 implementation stop reached. Run pentest for this exact commit.

## v0.124.0 — HTML data processing

**Status:** planned.

**Setup:** baseline 0.123.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** HTML data processing.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.77.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only html data processing within the source workstream: Add XML/HTML extraction, formatting and escaping with external entity/network access disabled by default. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Entity expansion, excessive depth and malformed documents fail within budgets; renderers receive inert data. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.124.0 implementation stop reached. Run pentest for this exact commit.

## v0.125.0 — XPath dialect

**Status:** planned.

**Setup:** baseline 0.124.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** XPath dialect.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.78.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only xpath dialect within the source workstream: Implement the selected reference dialects through isolated query providers and result adapters. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Namespaces, selector syntax and output formatting match compatibility fixtures; unsupported syntax is not silently simplified. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.125.0 implementation stop reached. Run pentest for this exact commit.

## v0.126.0 — CSS selector dialect

**Status:** planned.

**Setup:** baseline 0.125.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** CSS selector dialect.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.78.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only css selector dialect within the source workstream: Implement the selected reference dialects through isolated query providers and result adapters. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Namespaces, selector syntax and output formatting match compatibility fixtures; unsupported syntax is not silently simplified. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.126.0 implementation stop reached. Run pentest for this exact commit.

## v0.127.0 — JSONPath dialect

**Status:** planned.

**Setup:** baseline 0.126.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** JSONPath dialect.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.79.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only jsonpath dialect within the source workstream: Deliver the required JSONPath, JMESPath, jq/JSONata-style capabilities actually present in the pinned inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Each discovered language has its own dialect/version tests; equivalent branding is not accepted as compatibility evidence. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.127.0 implementation stop reached. Run pentest for this exact commit.

## v0.128.0 — JMESPath dialect

**Status:** planned.

**Setup:** baseline 0.127.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** JMESPath dialect.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.79.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only jmespath dialect within the source workstream: Deliver the required JSONPath, JMESPath, jq/JSONata-style capabilities actually present in the pinned inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Each discovered language has its own dialect/version tests; equivalent branding is not accepted as compatibility evidence. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.128.0 implementation stop reached. Run pentest for this exact commit.

## v0.129.0 — jq dialect if inventoried

**Status:** planned.

**Setup:** baseline 0.128.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** jq dialect if inventoried.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.79.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only jq dialect if inventoried within the source workstream: Deliver the required JSONPath, JMESPath, jq/JSONata-style capabilities actually present in the pinned inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Each discovered language has its own dialect/version tests; equivalent branding is not accepted as compatibility evidence. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.129.0 implementation stop reached. Run pentest for this exact commit.

## v0.130.0 — JSONata dialect if inventoried

**Status:** planned.

**Setup:** baseline 0.129.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** JSONata dialect if inventoried.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.79.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only jsonata dialect if inventoried within the source workstream: Deliver the required JSONPath, JMESPath, jq/JSONata-style capabilities actually present in the pinned inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Each discovered language has its own dialect/version tests; equivalent branding is not accepted as compatibility evidence. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.130.0 implementation stop reached. Run pentest for this exact commit.

## v0.131.0 — YAML semantics

**Status:** planned.

**Setup:** baseline 0.130.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** YAML semantics.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.80.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only yaml semantics within the source workstream: Add parse/emit and JSON conversions with explicit type inference and alias behavior. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Alias bombs, implicit scalar differences and non-string mapping keys are handled according to documented profiles. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.131.0 implementation stop reached. Run pentest for this exact commit.

## v0.132.0 — Rison semantics

**Status:** planned.

**Setup:** baseline 0.131.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Rison semantics.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.80.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only rison semantics within the source workstream: Add parse/emit and JSON conversions with explicit type inference and alias behavior. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Alias bombs, implicit scalar differences and non-string mapping keys are handled according to documented profiles. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.132.0 implementation stop reached. Run pentest for this exact commit.

## v0.133.0 — MessagePack semantics

**Status:** planned.

**Setup:** baseline 0.132.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** MessagePack semantics.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.81.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only messagepack semantics within the source workstream: Add lossless tagged/binary/numeric mappings and round-trip conversions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Indefinite lengths, nesting, duplicate keys and extension types are bounded and represented without accidental loss. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.133.0 implementation stop reached. Run pentest for this exact commit.

## v0.134.0 — CBOR semantics

**Status:** planned.

**Setup:** baseline 0.133.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** CBOR semantics.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.81.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only cbor semantics within the source workstream: Add lossless tagged/binary/numeric mappings and round-trip conversions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Indefinite lengths, nesting, duplicate keys and extension types are bounded and represented without accidental loss. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.134.0 implementation stop reached. Run pentest for this exact commit.

## v0.135.0 — AMF variants

**Status:** planned.

**Setup:** baseline 0.134.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** AMF variants.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.82.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only amf variants within the source workstream: Add the pinned AMF variants and Avro-to-JSON requirements behind separate provider modules. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Unsupported schema features become tracked gaps; hostile references and lengths cannot escape limits. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.135.0 implementation stop reached. Run pentest for this exact commit.

## v0.136.0 — Avro schemas

**Status:** planned.

**Setup:** baseline 0.135.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Avro schemas.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.82.0; implement only the named topic, preserving the other topics for their mapped passes.

**Deliverables:** Deliver only avro schemas within the source workstream: Add the pinned AMF variants and Avro-to-JSON requirements behind separate provider modules. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Unsupported schema features become tracked gaps; hostile references and lengths cannot escape limits. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.136.0 implementation stop reached. Run pentest for this exact commit.

## v0.137.0 — TLV and binary structures

**Status:** planned.

**Setup:** baseline 0.136.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** TLV and binary structures.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add configurable TLV parsing, field bounds and related binary-to-structured helpers from inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Truncation, overlapping lengths, large tags and signed/unsigned decoding have negative tests. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.137.0 implementation stop reached. Run pentest for this exact commit.

## v0.138.0 — Code formatting and minification

**Status:** planned.

**Setup:** baseline 0.137.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Code formatting and minification.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add the inventoried language beautifiers/minifiers using syntax-aware providers where semantics require them. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Strings, comments, regex literals and template syntax survive correctly; substitutions are not advertised as parsers. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.138.0 implementation stop reached. Run pentest for this exact commit.

## v0.139.0 — Mathematics and statistics

**Status:** planned.

**Setup:** baseline 0.138.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Mathematics and statistics.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add bounded integer arithmetic, modular functions, aggregates and statistical operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Precision, divide-by-zero, overflow and ordering are explicit and consistent across browser/native targets. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.139.0 implementation stop reached. Run pentest for this exact commit.

## v0.140.0 — Set and combinatorial operations

**Status:** planned.

**Setup:** baseline 0.139.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Set and combinatorial operations.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add unions, intersections, differences, Cartesian products, power sets and permutation-style utilities. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Output cardinality is estimated and capped before exponential expansion; ordering matches fixtures. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.140.0 implementation stop reached. Run pentest for this exact commit.

## v0.141.0 — Time and identifiers

**Status:** planned.

**Setup:** baseline 0.140.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Time and identifiers.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add timestamp formats, duration helpers, UUID/object-ID interpretation and versioned time-zone data where required. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Invalid dates, offset transitions, precision and deterministic clock injection have tests. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.141.0 implementation stop reached. Run pentest for this exact commit.

## v0.142.0 — Distances and miscellaneous utilities

**Status:** planned.

**Setup:** baseline 0.141.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Distances and miscellaneous utilities.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add unit conversions, geographical calculations, formatting and remaining small utility operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Numeric units, coordinate ranges and rounding are explicit; map/network resources require declared capability or offline assets. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.142.0 implementation stop reached. Run pentest for this exact commit.

## v0.143.0 — Remaining text and encoding tables

**Status:** planned.

**Setup:** baseline 0.142.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Remaining text and encoding tables.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Close missing code pages, language data, tokenization and utility variants discovered by the inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Every claimed encoding/dialect identifies its data-table version and has native/browser fixtures. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.143.0 implementation stop reached. Run pentest for this exact commit.

## v0.144.0 — Structured-format gate

**Status:** planned.

**Setup:** baseline 0.143.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Structured-format gate.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Run the full query/format corpus and publish per-argument, per-platform parity results. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Unsupported syntax remains a release blocker for 1.0; the plan extends rather than hiding difficult languages. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.144.0 implementation stop reached. Run pentest for this exact commit.
