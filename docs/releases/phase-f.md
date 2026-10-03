# Phase F: Structured formats, queries and utilities

Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).

Verification checklists apply only to introduced or retained behavior in the reviewed bounded scope. Record absent later capabilities as pending with numbered owners; contract fixtures never attest their runtime PASS. A prerequisite needed by this pass must be implemented and verified first, rather than deferred. Every future owner still owes its full acceptance before exposure/1.0.

## v0.134.0 — Lossless JSON

**Status:** planned.

**Setup:** baseline 0.133.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Lossless JSON.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.76.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only lossless json within the source workstream: Add strict/lossless JSON, CSV conversion, configurable delimiters, quoting and invalid-input diagnostics. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Large integers, duplicate-key policy, multiline fields and final newline behavior are fixture-tested. JSON and CSV independently preserve declared numeric/null/duplicate/order/quoting semantics; depth/record limits and malformed fixtures pass both targets. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.134.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.135.0 — CSV semantics

**Status:** planned.

**Setup:** baseline 0.134.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** CSV semantics.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.76.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only csv semantics within the source workstream: Add strict/lossless JSON, CSV conversion, configurable delimiters, quoting and invalid-input diagnostics. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Large integers, duplicate-key policy, multiline fields and final newline behavior are fixture-tested. JSON and CSV independently preserve declared numeric/null/duplicate/order/quoting semantics; depth/record limits and malformed fixtures pass both targets. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.135.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.136.0 — XML data processing

**Status:** planned.

**Setup:** baseline 0.135.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** XML data processing.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.77.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only xml data processing within the source workstream: Add XML/HTML extraction, formatting and escaping with external entity/network access disabled by default. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Entity expansion, excessive depth and malformed documents fail within budgets; renderers receive inert data. XML/HTML parsers reject external entity/network effects and expansion excess; hostile markup stays data and byte/text conversion is explicit. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.136.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.137.0 — HTML data processing

**Status:** planned.

**Setup:** baseline 0.136.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** HTML data processing.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.77.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only html data processing within the source workstream: Add XML/HTML extraction, formatting and escaping with external entity/network access disabled by default. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Entity expansion, excessive depth and malformed documents fail within budgets; renderers receive inert data. XML/HTML parsers reject external entity/network effects and expansion excess; hostile markup stays data and byte/text conversion is explicit. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.137.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.138.0 — XPath dialect

**Status:** planned.

**Setup:** baseline 0.137.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** XPath dialect.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.78.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only xpath dialect within the source workstream: Implement the selected reference dialects through isolated query providers and result adapters. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Namespaces, selector syntax and output formatting match compatibility fixtures; unsupported syntax is not silently simplified. Each XPath/CSS dialect and namespace/default is frozen; result/depth/work ceilings and hostile expressions terminate with precise diagnostics. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.138.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.139.0 — CSS selector dialect

**Status:** planned.

**Setup:** baseline 0.138.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** CSS selector dialect.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.78.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only css selector dialect within the source workstream: Implement the selected reference dialects through isolated query providers and result adapters. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Namespaces, selector syntax and output formatting match compatibility fixtures; unsupported syntax is not silently simplified. Each XPath/CSS dialect and namespace/default is frozen; result/depth/work ceilings and hostile expressions terminate with precise diagnostics. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.139.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.140.0 — JSONPath dialect

**Status:** planned.

**Setup:** baseline 0.139.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** JSONPath dialect.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.79.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only jsonpath dialect within the source workstream: Deliver the required JSONPath, JMESPath, jq/JSONata-style capabilities actually present in the pinned inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Each discovered language has its own dialect/version tests; equivalent branding is not accepted as compatibility evidence. Each inventoried JSONPath/JMESPath/jq/JSONata dialect has separate semantic vectors; unsupported syntax, recursion and explosive queries are bounded. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.140.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.141.0 — JMESPath dialect

**Status:** planned.

**Setup:** baseline 0.140.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** JMESPath dialect.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.79.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only jmespath dialect within the source workstream: Deliver the required JSONPath, JMESPath, jq/JSONata-style capabilities actually present in the pinned inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Each discovered language has its own dialect/version tests; equivalent branding is not accepted as compatibility evidence. Each inventoried JSONPath/JMESPath/jq/JSONata dialect has separate semantic vectors; unsupported syntax, recursion and explosive queries are bounded. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.141.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.142.0 — jq dialect if inventoried

**Status:** planned.

**Setup:** baseline 0.141.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** jq dialect if inventoried.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.79.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only jq dialect if inventoried within the source workstream: Deliver the required JSONPath, JMESPath, jq/JSONata-style capabilities actually present in the pinned inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Each discovered language has its own dialect/version tests; equivalent branding is not accepted as compatibility evidence. Each inventoried JSONPath/JMESPath/jq/JSONata dialect has separate semantic vectors; unsupported syntax, recursion and explosive queries are bounded. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.142.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.143.0 — JSONata dialect if inventoried

**Status:** planned.

**Setup:** baseline 0.142.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** JSONata dialect if inventoried.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.79.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only jsonata dialect if inventoried within the source workstream: Deliver the required JSONPath, JMESPath, jq/JSONata-style capabilities actually present in the pinned inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Each discovered language has its own dialect/version tests; equivalent branding is not accepted as compatibility evidence. Each inventoried JSONPath/JMESPath/jq/JSONata dialect has separate semantic vectors; unsupported syntax, recursion and explosive queries are bounded. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.143.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.144.0 — YAML semantics

**Status:** planned.

**Setup:** baseline 0.143.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** YAML semantics.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.80.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only yaml semantics within the source workstream: Add parse/emit and JSON conversions with explicit type inference and alias behavior. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Alias bombs, implicit scalar differences and non-string mapping keys are handled according to documented profiles. YAML/Rison independently define tags/aliases/merge/numbers; alias bombs, deep input, unsafe tags and malformed documents fail within ceilings. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.144.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.145.0 — Rison semantics

**Status:** planned.

**Setup:** baseline 0.144.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Rison semantics.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.80.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only rison semantics within the source workstream: Add parse/emit and JSON conversions with explicit type inference and alias behavior. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Alias bombs, implicit scalar differences and non-string mapping keys are handled according to documented profiles. YAML/Rison independently define tags/aliases/merge/numbers; alias bombs, deep input, unsafe tags and malformed documents fail within ceilings. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.145.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.146.0 — MessagePack semantics

**Status:** planned.

**Setup:** baseline 0.145.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** MessagePack semantics.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.81.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only messagepack semantics within the source workstream: Add lossless tagged/binary/numeric mappings and round-trip conversions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Indefinite lengths, nesting, duplicate keys and extension types are bounded and represented without accidental loss. MessagePack/CBOR independently test integers, binary/text, tags, map semantics, noncanonical encodings and truncation without lossy JSON conversion. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.146.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.147.0 — CBOR semantics

**Status:** planned.

**Setup:** baseline 0.146.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** CBOR semantics.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.81.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only cbor semantics within the source workstream: Add lossless tagged/binary/numeric mappings and round-trip conversions. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Indefinite lengths, nesting, duplicate keys and extension types are bounded and represented without accidental loss. MessagePack/CBOR independently test integers, binary/text, tags, map semantics, noncanonical encodings and truncation without lossy JSON conversion. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.147.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.148.0 — AMF variants

**Status:** planned.

**Setup:** baseline 0.147.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** AMF variants.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.82.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only amf variants within the source workstream: Add the pinned AMF variants and Avro-to-JSON requirements behind separate provider modules. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Unsupported schema features become tracked gaps; hostile references and lengths cannot escape limits. Each AMF variant/Avro schema feature has independent vectors; cyclic schemas, reference growth, incompatible schemas and records hit declared limits. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.148.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.149.0 — Avro schemas

**Status:** planned.

**Setup:** baseline 0.148.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Avro schemas.

**Scope:** one reviewable pass in this workstream. Source bundle owner 0.82.0; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.

**Deliverables:** Deliver only avro schemas within the source workstream: Add the pinned AMF variants and Avro-to-JSON requirements behind separate provider modules. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** For this scoped topic: Unsupported schema features become tracked gaps; hostile references and lengths cannot escape limits. Each AMF variant/Avro schema feature has independent vectors; cyclic schemas, reference growth, incompatible schemas and records hit declared limits. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.149.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.150.0 — TLV and binary structures

**Status:** planned.

**Setup:** baseline 0.149.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** TLV and binary structures.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add configurable TLV parsing, field bounds and related binary-to-structured helpers from inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Truncation, overlapping lengths, large tags and signed/unsigned decoding have negative tests. Length/count/offset arithmetic in TLV/binary structures is checked; truncated/overlapping/cyclic fields reject without oversized allocations. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.150.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.151.0 — Code formatting and minification

**Status:** planned.

**Setup:** baseline 0.150.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Code formatting and minification.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add the inventoried language beautifiers/minifiers using syntax-aware providers where semantics require them. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Strings, comments, regex literals and template syntax survive correctly; substitutions are not advertised as parsers. Each language formatter/minifier has frozen dialect and literal-preservation fixtures; malformed or pathological code cannot execute or exceed work limits. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.151.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.152.0 — Mathematics and statistics

**Status:** planned.

**Setup:** baseline 0.151.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Mathematics and statistics.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add bounded integer arithmetic, modular functions, aggregates and statistical operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Precision, divide-by-zero, overflow and ordering are explicit and consistent across browser/native targets. Math/statistics freeze domain errors, precision/rounding, NaN/overflow and deterministic reduction order; limits apply to expensive computations. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.152.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.153.0 — Set and combinatorial operations

**Status:** planned.

**Setup:** baseline 0.152.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Set and combinatorial operations.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add unions, intersections, differences, Cartesian products, power sets and permutation-style utilities. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Output cardinality is estimated and capped before exponential expansion; ordering matches fixtures. Cardinality/product growth is preflighted and charged; huge Cartesian/permutation outputs reject before memory/disk exhaustion. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.153.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.154.0 — Time and identifiers

**Status:** planned.

**Setup:** baseline 0.153.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Time and identifiers.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add timestamp formats, duration helpers, UUID/object-ID interpretation and versioned time-zone data where required. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Invalid dates, offset transitions, precision and deterministic clock injection have tests. Time/ID formats define zone/calendar/precision/version behavior; datasets are pinned and invalid/ambiguous/overflow cases have fixed outcomes. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.154.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.155.0 — Distances and miscellaneous utilities

**Status:** planned.

**Setup:** baseline 0.154.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Distances and miscellaneous utilities.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Add unit conversions, geographical calculations, formatting and remaining small utility operations. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Numeric units, coordinate ranges and rounding are explicit; map/network resources require declared capability or offline assets. Each distance/utility has independent edge vectors and complexity ceilings; quadratic work uses explicit admission rather than hidden interactive scans. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.155.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.156.0 — Remaining text and encoding tables

**Status:** planned.

**Setup:** baseline 0.155.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Remaining text and encoding tables.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Close missing code pages, language data, tokenization and utility variants discovered by the inventory. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Every claimed encoding/dialect identifies its data-table version and has native/browser fixtures. Remaining tables/dialects close inventoried variants with source/license hashes; unsupported characters and Unicode-version differences are recorded. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.156.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## v0.157.0 — Structured-format gate

**Status:** planned.

**Setup:** baseline 0.156.0; verify current upstream sources and record a bounded scope manifest before coding.

**Goal:** Structured-format gate.

**Scope:** one reviewable pass in this workstream. Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.

**Deliverables:** Run the full query/format corpus and publish per-argument, per-platform parity results. Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.

**Verification:** Unsupported syntax remains a release blocker for 1.0; the plan extends rather than hiding difficult languages. All format/query argument and target rows close with actual browser/native results; family names or a parser subset do not count as dialect parity. Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons. Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.

**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v0.157.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.
