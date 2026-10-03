# Version Roadmap — 0.1.0 through 1.0.0

**Planning date:** 2 October 2026. **Starting compiler:** Rust 1.99.0.  
**Status:** proposed engineering work breakdown; none of these releases is represented as implemented.  
**Companions:** `ARCHITECTURE.md`, `PARITY_AND_RISK_REGISTER.md`, `roadmap.json`.

## How to use this roadmap

The 240 numbered minor releases below are an ordered baseline, not a deadline or a promise that each item is equally small. Split a release whenever an operation family, security fix, missing dialect or browser-portability problem deserves a smaller independently testable increment. Insert new 0.x versions and update dependencies instead of squeezing unfinished work into a tag. After the nominal 0.240.0 gate, continue with 0.241.0, 0.242.0 and as many releases as necessary until the complete acceptance contract passes.

The numerical ordering supplies a simple default dependency chain in `roadmap.json`. Independent operation-provider work can proceed in parallel after its kernel, artifact, security and conformance prerequisites exist. No release requires literally waiting for unrelated work purely because a number was reserved. Do not create 240 branches or hundreds of empty crates on day one.

Every operation-family row means **the exact discovered operations, arguments, defaults, data conversions and platform behavior from the pinned reference**, not merely similarly named Rust implementations. Some examples below are separately labelled enhancements; the operation inventory, not these illustrative names, defines mandatory parity. Query dialects, legacy algorithms, OCR, YARA and media support may require many additional minor releases. Native-only implementation does not satisfy a browser-local baseline capability.

## Definition of done for every minor release

A release contains a useful demonstrable increment, its documented API/behavior, positive and negative tests, relevant differential fixtures, applicable chunk-partition tests, resource-limit tests and a change log. Security-sensitive changes receive an explicit threat review and regression tests in the same release. Check no_std/feature matrices, actual browser tests for browser changes, and dependency/unsafe-code deltas. A new operation requires its descriptor, argument schema, help/examples, limits, error semantics, deterministic/cache policy and platform declaration.

Database changes include backend-owned migrations and repository tests. Transport changes include the application-owned contract suite. Releases introducing parsers or providers include hostile-input cases and fuzz targets. Performance claims require recorded measurements; zero-copy, constant-memory, sandboxed and Rust-native are not accepted without qualifying what those terms actually cover.

A patch release `0.N.P` fixes compatible defects in a released increment. Breaking semantic changes receive a new operation revision and recipe migration, even before 1.0 when the package version itself permits more change. Keep old fixtures and imported-recipe behavior observable. The service API, recipe format, operation semantic revision, plugin ABI and application package versions are separate compatibility axes.

## Phase map

| Phase | Releases | Outcome |
|---|---|---|
| A | 0.1.0–0.15.0 | Foundation and useful vertical slice |
| B | 0.16.0–0.30.0 | Bytes, text and foundational encodings |
| C | 0.31.0–0.45.0 | Streaming, artifacts and execution foundations |
| D | 0.46.0–0.60.0 | Modern browser workbench |
| E | 0.61.0–0.75.0 | Remote API, PostgreSQL and secure server execution |
| F | 0.76.0–0.90.0 | Structured formats, queries and utilities |
| G | 0.91.0–0.105.0 | Compression and archives |
| H | 0.106.0–0.120.0 | Modern hashing and cryptographic operations |
| I | 0.121.0–0.135.0 | Legacy cryptography, hashes and classical ciphers |
| J | 0.136.0–0.150.0 | Public keys, certificates and tokens |
| K | 0.151.0–0.165.0 | Network and forensic analysis |
| L | 0.166.0–0.180.0 | Images, media and document presentation |
| M | 0.181.0–0.195.0 | Complete recipe semantics, Magic and compatibility |
| N | 0.196.0–0.210.0 | Extensibility and replacement-adapter proof |
| O | 0.211.0–0.225.0 | Portability, collaboration and operations |
| P | 0.226.0–0.240.0 | Qualification and general-availability readiness |

## Phase A — Foundation and useful vertical slice

Prove the same Rust transformation works in a real browser worker and a native host, then establish the contracts that prevent later rewrites.

| Version | Increment | Deliverable | Release acceptance |
|---|---|---|---|
| **0.1.0** | Executable seed | Pin Rust 1.99.0; create kernel, engine, browser and native host packages; run one hex operation from a real browser worker. | Native and browser fixtures agree; the example needs neither PostgreSQL nor a sibling repository. |
| **0.2.0** | Reference baseline | Resolve the reviewed tag and adopted current-source deltas to immutable commits; inventory operations, arguments, workflow features and licenses, including observed certificate-bundle parsing. | Every discovered operation has a stable tracking record; the reference commit and file hashes are recorded, not guessed. |
| **0.3.0** | Application contracts | Define operation IDs, semantic revisions, structured errors, recipe envelopes, artifact references and local EngineClient commands. | Round-trip tests reject unknown required fields and preserve large offsets without JavaScript number truncation. |
| **0.4.0** | Portable kernel | Separate no_std/no-alloc kernel, alloc-enabled compiler and std hosts; establish feature and target matrices. | Bare-metal-style compile checks catch std leakage; unsafe code is forbidden in first-party portable core by default. |
| **0.5.0** | Bounded buffer contract | Add caller-provided input/output windows, consumed/produced counts, partial progress, cancellation checkpoints and finish states. | Zero-sized windows, short writes, empty inputs and repeated finish calls have defined results without panics. |
| **0.6.0** | Operation descriptors | Define typed arguments, defaults, help, execution class, secret fields and capabilities; generate a minimal catalogue. | One new operation registers once and appears in catalogue, validation, documentation and generated argument controls. |
| **0.7.0** | Linear execution | Compile and run a sequence of hex, text and XOR operations with explicit byte/text conversion. | Chunk partitions do not alter outputs; invalid intermediate types fail before execution where statically knowable. |
| **0.8.0** | Worker protocol | Introduce versioned worker messages, input transfers, job generations, progress and error events. | Processing runs outside the UI thread; stale generations and malformed messages cannot update active results. |
| **0.9.0** | Cancellation lifecycle | Implement cooperative cancellation and browser worker termination/recreation for non-cooperative work. | A cancelled job cannot publish a successful artifact; cancellation leaves the next job usable. |
| **0.10.0** | First browser workbench | Build accessible input, recipe and output panes, operation search and a manual Run button. | Keyboard-only use completes a sample recipe; raw output is never interpreted as trusted HTML. |
| **0.11.0** | Loopback API host | Expose capabilities, catalogue, validate, run, status and cancel through a replaceable HTTP adapter. | Local and HTTP clients pass the same contract suite; the development server binds loopback by default. |
| **0.12.0** | Hard-feature feasibility | Exercise candidate regex, query-language, YARA, crypto, compression, disassembly and OCR strategies in browser and native spikes. | Record dialect, licensing, dependencies, limits and remaining gaps; unsupported candidates do not become assumed dependencies. |
| **0.13.0** | Differential harness | Build a reference runner, fixture provenance rules and partitioned-input comparison harness. | Positive, negative, binary and Unicode cases run reproducibly; upstream bugs are recorded rather than blindly copied. |
| **0.14.0** | First threat review | Review imported recipes, worker boundaries, preview escaping, logging and dependency graph. | No payload telemetry or automatic network side effects; hostile samples produce bounded failures. |
| **0.15.0** | Usable vertical alpha | Package a small offline-capable workbench with recipe save/load, loopback API examples and developer operation guide. | A fresh clone builds and runs without sibling projects or a database; phase A contracts are demonstrated end to end. |

**Phase gate:** Do not expand into dozens of packages until the browser/native slice works and the difficult compatibility risks have explicit owners and evidence.

## Phase B — Bytes, text and foundational encodings

Build common operations on the portable kernel while making text semantics and chunk boundaries explicit.

| Version | Increment | Deliverable | Release acceptance |
|---|---|---|---|
| **0.16.0** | Byte inspection | Add hex dumps, binary, octal, decimal byte views and reversible dump parsing. | Offsets, delimiters, malformed rows and partial final lines match the selected compatibility profile. |
| **0.17.0** | Integer and float formats | Add charcode, text-integer, arbitrary-width numeric conversion, BCD, float bit views and endianness controls. | Signedness, precision, overflow, NaN payloads and byte-order behavior have explicit tests. |
| **0.18.0** | Base64 family | Add configured alphabets, padding policies, URL-safe forms and source/output offset mapping. | RFC vectors and reference arguments pass across every short-input chunk partition; padding is accepted only in valid positions. |
| **0.19.0** | Base32 and Base45 | Add available alphabet variants, whitespace policies and precise invalid-symbol diagnostics. | Case handling, trailing bits and incomplete blocks have separate strict and compatibility fixtures. |
| **0.20.0** | Base58 and Bech32 | Add leading-zero handling, checksummed forms and selected alphabet variants. | Checksums, mixed-case policy, network prefixes and maximum-length limits are enforced without ambiguous repair. |
| **0.21.0** | Other base encodings | Add Base62, Base85, Base92 and generic-base operations from the inventory. | Exact alphabets, escaping and output lengths match fixtures; base conversion cannot request unbounded integer storage. |
| **0.22.0** | URL and entities | Implement percent encoding/decoding, HTML entities and quoted-printable with explicit byte/text boundaries. | Reserved characters, malformed escapes and newline handling match documented profiles; results remain inert data. |
| **0.23.0** | Unicode escapes and normalization | Add Unicode escapes, smart-character handling, normalization and versioned Unicode data. | Surrogate and invalid-sequence policy is explicit; normalization is tested at chunk boundaries and against table versions. |
| **0.24.0** | Character encodings | Add an initial encoding-table pack, encode/decode operations and a complete remaining-encoding checklist. | Every enabled encoding has round-trip and lossy-mode tests; unimplemented table variants remain visible gaps. |
| **0.25.0** | Text transformations | Add case transforms, trimming, diacritic removal, reverse, padding and character/word/line selection. | Byte, Unicode scalar, grapheme and legacy UTF-16 behaviors are not silently interchanged. |
| **0.26.0** | Lines and collections | Add split/join, line filtering, numbering, deduplication and stable sorting. | Long lines and whole-input sorting obey budgets; ordering and empty-record semantics match fixtures. |
| **0.27.0** | Search and replace core | Add literal search, bounded safe-regex mode, captures, replacement and highlighting as structured spans. | Safe-mode syntax is labelled distinctly from full compatibility regex; all highlighting is escaped by renderers. |
| **0.28.0** | Bitwise and byte arithmetic | Add AND, OR, NOT, XOR, shifts, rotates, add/subtract and bounded brute-force primitives. | Key repetition, carry, signedness and integer overflow rules are deterministic across targets. |
| **0.29.0** | Additional text encodings | Deliver Braille, Punycode, Modhex, COBS, caret/control encodings and MIME decoding from inventory. | Embedded zeroes, invalid framing, malformed labels and nested MIME limits have adversarial fixtures. |
| **0.30.0** | Encoding completeness gate | Reconcile every basic encoding and text inventory row, including missing variants discovered during implementation. | A generated report separates complete operations, argument gaps and intentionally different safe defaults; no hidden omissions. |

**Phase gate:** Common recipes work correctly, but the overall product is not advertised as CyberChef-complete. Full regex dialect compatibility is a tracked later gate.

## Phase C — Streaming, artifacts and execution foundations

Make large inputs, multi-input operations and resource limits real before adding heavyweight operation families.

| Version | Increment | Deliverable | Release acceptance |
|---|---|---|---|
| **0.31.0** | Resource ledger | Account for input windows, queued bytes, operation state, output, cache, artifacts and provider allocations. | A deliberately expanding operation hits the declared budget; reported totals do not omit retained branch buffers. |
| **0.32.0** | Backpressure scheduler | Add deterministic ready queues, bounded channels or equivalent credits and partial-output resumption. | Slow consumers cannot grow memory indefinitely; synchronous CPU work does not depend on an async task per node. |
| **0.33.0** | Stream state machines | Standardize EOF, truncation, cancellation, errors, logical record boundaries and output completion. | Every state transition is tested; EOF is neither duplicated nor inferred from an arbitrary chunk boundary. |
| **0.34.0** | Multi-input ports | Add constant parameters, immutable keys and synchronized data inputs with explicit joining policies. | Arrival order cannot change XOR/key semantics; unresolved inputs block safely and never grow unbounded buffers. |
| **0.35.0** | Branches and joins | Implement graph regions, ordered fork/join, fan-out reference sharing and explicit merge policies. | Reconverging branches, slow consumers and early exits do not deadlock or lose output. |
| **0.36.0** | Whole-input and seekable adapters | Support bounded accumulation, two-pass operations and seekable artifact readers. | Non-streaming operations declare their class and reject oversized jobs before uncontrolled allocation. |
| **0.37.0** | Native artifact storage | Introduce staged artifacts, immutable manifests, range reads, leases and verified finalization on local disk. | Crash simulation cannot expose a partial artifact as complete; offsets and lengths are checked. |
| **0.38.0** | Browser artifact storage | Implement IndexedDB metadata and optional OPFS chunk storage with memory/file fallbacks. | Firefox and other supported browsers work without optional APIs; quota failures never trigger silent upload. |
| **0.39.0** | Storage transaction discipline | Add transaction-completion waits, chunk manifests, orphan cleanup and storage schema migrations. | Aborted transactions and interrupted writes are reported; no successful-write result precedes commit confirmation. |
| **0.40.0** | Semantic content identities | Define canonical typed parameters, ordered ports, operation revision and chunk-independent input digests. | Repartitioning input leaves identity unchanged; different parameters or operation semantics never reuse an entry accidentally. |
| **0.41.0** | Selective computation cache | Cache only deterministic, completed, permitted jobs using immutable input identities or completed spool hashes. | Unknown streams are not fully buffered merely to attempt an early hit; secrets and failed jobs are excluded by default. |
| **0.42.0** | Cache lifecycle | Add per-workspace quotas, reference pinning, eviction, cancellation cleanup and encrypted-at-rest hooks where configured. | Eviction cannot delete a live artifact; cache misses and storage failures do not corrupt authoritative recipes. |
| **0.43.0** | Bounded control-flow IR | Represent labels, conditional branches, bounded repeats, registers and subrecipes separately from DAG regions. | Graph-cycle rejection does not mistakenly eliminate required recipe loops; iteration/work budgets are enforced. |
| **0.44.0** | Execution provenance | Record operation revisions, argument redactions, input references, diagnostics and exact reproducibility conditions. | Sensitive arguments stay out of logs; nondeterministic jobs cannot masquerade as reproducible cached results. |
| **0.45.0** | Engine stress qualification | Exercise huge streams, joins, cancellation, expansion bombs, temporary storage exhaustion and corrupt artifacts. | Measured memory stays within each declared profile and errors remain recoverable; no universal constant-memory claim. |

**Phase gate:** The engine can distinguish streaming from whole-input work, maintain bounded resources and publish only complete artifacts. This gate precedes broad archive and crypto expansion.

## Phase D — Modern browser workbench

Build the daily-use experience without making a complex graph or GPU a prerequisite.

| Version | Increment | Deliverable | Release acceptance |
|---|---|---|---|
| **0.46.0** | Workspace shell | Add responsive resizable panes, themes, remembered non-sensitive preferences and command navigation. | Layout remains usable at narrow widths and high zoom; theme preference does not capture input content. |
| **0.47.0** | Recipe editing | Add drag/drop with keyboard alternatives, undo/redo, duplicate, disable, reorder and parameter validation. | Editing preserves stable node identities and annotations; purely visual movement does not rerun processing. |
| **0.48.0** | Generated operation inspector | Render argument forms, examples, defaults, capability warnings and semantic-version details from descriptors. | New descriptors require no handwritten duplicate API schema or form definition for supported field types. |
| **0.49.0** | Safe automatic preview | Add debounced, bounded previews for permitted pure operations and an explicit full-run action. | Imported recipes and effectful/expensive operations never start merely because they were pasted or opened. |
| **0.50.0** | Paged text viewer | Add incremental decoding, line indexing, search, selection and bounded text previews. | Large single lines and invalid UTF sequences do not force a full document string allocation. |
| **0.51.0** | Virtual hex viewer | Add range-backed hex/ASCII viewing, exact offset navigation, selection and export. | Offsets above 32-bit ranges remain correct; UI memory is measured separately from underlying artifact storage. |
| **0.52.0** | Structured and table viewers | Add lossless tree/table views, typed cell rendering, pagination and safe copy/export. | Large integers and binary values remain exact; untrusted strings cannot inject markup or spreadsheet formulas without warning. |
| **0.53.0** | Graph editor | Add an optional visual graph for typed ports, branches, joins and structured control regions. | Invalid edges are rejected by the engine compiler, not only by visual UI rules; keyboard editing remains possible. |
| **0.54.0** | Debugging controls | Add breakpoints, single-step, node diagnostics, intermediate inspection and cancellation status. | Viewing a preview does not prematurely terminate a full output stream or leak a secret artifact into history. |
| **0.55.0** | Offset provenance UI | Show source/output correspondences where transformations provide them, including encoded-byte relationships. | Non-local or lossy transforms say unmappable/approximate explicitly rather than invent exact positions. |
| **0.56.0** | Multiple inputs and batches | Add named inputs, file sets, deterministic batch ordering and per-item error policy. | A failed batch item cannot silently discard other results; files are not duplicated into UI state. |
| **0.57.0** | Local recipe library | Add folders/tags, favourites, search, revision history and exportable local workspaces. | Persistence is opt-in for sensitive data; recipe export omits secrets and bulk inputs by default. |
| **0.58.0** | Sharing and imports | Support recipe-only links/files, explicit input inclusion, compatibility links and import previews. | Users see capabilities and embedded data before running; history and URL exposure are clearly distinguished. |
| **0.59.0** | Offline packaging | Cache versioned app assets and selected operation packs; provide a complete offline distribution option. | Offline operation availability is visible; service-worker upgrades cannot mix incompatible engine and pack revisions. |
| **0.60.0** | Browser accessibility gate | Test keyboard, screen reader, focus, reduced motion, high contrast and touch-friendly responsive layouts. | Core tasks work without canvas-only controls, GPU acceleration, shared memory or a mouse. |

**Phase gate:** The web application is useful as a self-contained tool. Native desktop/mobile packaging is still out of scope until after 1.0.0.

## Phase E — Remote API, PostgreSQL and secure server execution

Add optional persistence and explicitly selected remote execution without changing local behavior.

| Version | Increment | Deliverable | Release acceptance |
|---|---|---|---|
| **0.61.0** | Public API specification | Stabilize pre-1.0 JSON envelopes, binary artifact routes, pagination, errors and capability negotiation. | Local and HTTP transports pass shared use-case tests; framework request types never enter the application layer. |
| **0.62.0** | Job lifecycle API | Add queued/running/succeeded/failed/cancelled/expired states, progress events and resumable observation. | Reconnection and duplicated requests cannot create ambiguous terminal states or leak another principal’s job. |
| **0.63.0** | Artifact transfer API | Add bounded uploads, integrity checks, range downloads, retention and explicit remote-consent UX. | Incomplete uploads remain staged; large files do not travel as JSON Base64 payloads by default. |
| **0.64.0** | Repository contracts | Define atomic recipe revision saves, job leases, permissions, metadata search and transaction boundaries. | Contracts describe domain semantics instead of generic execute-SQL methods; an in-memory adapter passes the suite. |
| **0.65.0** | PostgreSQL adapter | Implement parameterized queries, pool configuration and migrations outside core domain packages. | Recipes and jobs pass repository tests on an actual PostgreSQL instance; driver row types stay in the adapter. |
| **0.66.0** | Database TLS seam | Wire tokio-postgres through a replaceable TLS connector and explicit identity/trust configuration. | Certificate validation failures are fatal; a mock provider proves database TLS is not permanently tied to rustls. |
| **0.67.0** | Identity and sessions | Add server authentication, bounded sessions, token expiry, CSRF defenses and optional identity-provider integration. | Authorization is enforced server-side for every object; browser-local use remains anonymous and database-free. |
| **0.68.0** | Workspace authorization | Add owner/editor/viewer roles, tenant scoping and explicit service-account permissions. | Cross-workspace and confused-deputy tests fail closed even without database-specific row-security features. |
| **0.69.0** | Isolated execution workers | Move remotely submitted CPU work into restricted processes with memory, CPU, disk and egress policies. | A parser crash or non-cooperative job can be killed without taking down API or other tenants. |
| **0.70.0** | Admission and quotas | Add principal/workspace job quotas, maximum artifacts, rate limits and queue backpressure. | Repeated tiny requests and large expanding jobs cannot bypass aggregate resource accounting. |
| **0.71.0** | Durable jobs and leases | Add job leases, fencing tokens, worker heartbeat, retry eligibility and idempotency records. | Expired workers cannot finalize duplicate results; retry is prohibited for unsafe external side effects. |
| **0.72.0** | Server networking policy | Centralize outbound connections, redirects, destination restrictions, credentials and HTTP limits. | SSRF, rebinding, private/metadata destinations and mapped-address cases are covered before user HTTP operations are public. |
| **0.73.0** | Metadata-only observability | Add health, readiness, redacted audit events, bounded metrics and structured operational errors. | Default logs contain no raw inputs, outputs, secrets or high-cardinality user payload labels. |
| **0.74.0** | Server deployment profile | Ship a hardened single-node deployment with reverse-proxy and direct-TLS options, backups and cleanup jobs. | Restart and restore drills preserve metadata/artifact consistency; insecure development defaults cannot silently become public. |
| **0.75.0** | Server security gate | Test authentication, object authorization, uploads, worker isolation, cancellation and resource abuse. | Public remote execution stays disabled until isolation and quota tests pass; local web mode remains independently releasable. |

**Phase gate:** A server may be deployed safely with PostgreSQL, but local processing remains the default. Database replacement contracts exist before a second SQL backend is implemented.

## Phase F — Structured formats, queries and utilities

Deliver data transformation breadth while preserving dialect and numeric semantics.

| Version | Increment | Deliverable | Release acceptance |
|---|---|---|---|
| **0.76.0** | JSON and CSV foundations | Add strict/lossless JSON, CSV conversion, configurable delimiters, quoting and invalid-input diagnostics. | Large integers, duplicate-key policy, multiline fields and final newline behavior are fixture-tested. |
| **0.77.0** | XML and HTML data | Add XML/HTML extraction, formatting and escaping with external entity/network access disabled by default. | Entity expansion, excessive depth and malformed documents fail within budgets; renderers receive inert data. |
| **0.78.0** | XPath and CSS selectors | Implement the selected reference dialects through isolated query providers and result adapters. | Namespaces, selector syntax and output formatting match compatibility fixtures; unsupported syntax is not silently simplified. |
| **0.79.0** | JSON query dialects | Deliver the required JSONPath, JMESPath, jq/JSONata-style capabilities actually present in the pinned inventory. | Each discovered language has its own dialect/version tests; equivalent branding is not accepted as compatibility evidence. |
| **0.80.0** | YAML and Rison | Add parse/emit and JSON conversions with explicit type inference and alias behavior. | Alias bombs, implicit scalar differences and non-string mapping keys are handled according to documented profiles. |
| **0.81.0** | MessagePack and CBOR | Add lossless tagged/binary/numeric mappings and round-trip conversions. | Indefinite lengths, nesting, duplicate keys and extension types are bounded and represented without accidental loss. |
| **0.82.0** | AMF and Avro | Add the pinned AMF variants and Avro-to-JSON requirements behind separate provider modules. | Unsupported schema features become tracked gaps; hostile references and lengths cannot escape limits. |
| **0.83.0** | TLV and binary structures | Add configurable TLV parsing, field bounds and related binary-to-structured helpers from inventory. | Truncation, overlapping lengths, large tags and signed/unsigned decoding have negative tests. |
| **0.84.0** | Code formatting and minification | Add the inventoried language beautifiers/minifiers using syntax-aware providers where semantics require them. | Strings, comments, regex literals and template syntax survive correctly; substitutions are not advertised as parsers. |
| **0.85.0** | Mathematics and statistics | Add bounded integer arithmetic, modular functions, aggregates and statistical operations. | Precision, divide-by-zero, overflow and ordering are explicit and consistent across browser/native targets. |
| **0.86.0** | Set and combinatorial operations | Add unions, intersections, differences, Cartesian products, power sets and permutation-style utilities. | Output cardinality is estimated and capped before exponential expansion; ordering matches fixtures. |
| **0.87.0** | Time and identifiers | Add timestamp formats, duration helpers, UUID/object-ID interpretation and versioned time-zone data where required. | Invalid dates, offset transitions, precision and deterministic clock injection have tests. |
| **0.88.0** | Distances and miscellaneous utilities | Add unit conversions, geographical calculations, formatting and remaining small utility operations. | Numeric units, coordinate ranges and rounding are explicit; map/network resources require declared capability or offline assets. |
| **0.89.0** | Remaining text and encoding tables | Close missing code pages, language data, tokenization and utility variants discovered by the inventory. | Every claimed encoding/dialect identifies its data-table version and has native/browser fixtures. |
| **0.90.0** | Structured-format gate | Run the full query/format corpus and publish per-argument, per-platform parity results. | Unsupported syntax remains a release blocker for 1.0; the plan extends rather than hiding difficult languages. |

**Phase gate:** Language interpreters and structured parsers are treated as high-risk providers with limits, not assumed interchangeable Rust crates.

## Phase G — Compression and archives

Provide full compression/archive operation parity with explicit expansion, memory and file-system boundaries.

| Version | Increment | Deliverable | Release acceptance |
|---|---|---|---|
| **0.91.0** | Compression provider contract | Standardize streaming encoder/decoder state, trailing-data policy, dictionary limits and byte counters. | Truncated streams and short output buffers resume or fail deterministically without hiding retained state. |
| **0.92.0** | Deflate | Add raw Deflate compression/decompression and reference parameter mapping. | Stored, fixed and dynamic blocks pass reference fixtures across all tested chunk boundaries. |
| **0.93.0** | Zlib | Add wrappers, dictionary handling and checksums with strict and compatibility framing policies. | Header, dictionary-ID and checksum failures are distinguished; limits include dictionary memory. |
| **0.94.0** | Gzip | Add gzip metadata, concatenated members, checksums and deterministic-output options. | Member boundaries and trailing garbage follow documented semantics; preview cannot skip final integrity validation. |
| **0.95.0** | Bzip2 | Deliver required compression/decompression variants through a reviewed provider. | Block limits, corrupt indexes and expansion attacks are tested in browser and native builds. |
| **0.96.0** | LZMA and containers | Add the inventory’s LZMA/container variants with configurable but bounded dictionaries. | Dictionary size is validated before allocation; unsupported container variants remain named gaps. |
| **0.97.0** | LZ4 | Add required block/frame operations, checksums and content-size handling. | Frame flags, dictionaries, short blocks and independent/dependent block behavior match fixtures. |
| **0.98.0** | LZ string encodings | Add LZ-based string and transport variants present in the reference. | UTF-16/code-unit behavior is reproduced explicitly rather than replaced with a superficially similar byte codec. |
| **0.99.0** | Platform compression families | Add NT/XPRESS and other inventoried platform-specific formats without calling local shell utilities. | Published/reference samples and malformed streams work identically in the browser and native engine. |
| **0.100.0** | ZIP listing and extraction | Add multi-entry archives, data descriptors, name encodings and password variants required by inventory. | Entry count, expansion, encryption errors and path normalization are bounded; extraction never writes arbitrary host paths. |
| **0.101.0** | ZIP creation | Add selected compression methods, metadata mapping and deterministic archive options. | Round trips preserve required names and bytes; archives larger than basic format limits use supported extensions or fail clearly. |
| **0.102.0** | TAR operations | Add listing, extraction and creation for required header variants and links. | Traversal, absolute paths, devices, symlinks and hardlinks cannot bypass the artifact namespace. |
| **0.103.0** | Nested archive workflows | Connect archive outputs to file collections and bounded recursive processing. | Total nesting, members, bytes and work are capped across the whole job, not reset per nested archive. |
| **0.104.0** | Archive UX and integrity | Add per-member inspection, safe selection, artifact exports and verification status. | Incomplete or checksum-failed outputs never appear as verified; selected member export preserves authorization. |
| **0.105.0** | Compression qualification | Close all compression inventory gaps and run corpus-based fuzzing and expansion stress tests. | Every provider declares measured memory profiles; unsupported methods cannot be omitted from the parity denominator. |

**Phase gate:** All selected formats are available locally where the reference supports local execution. Native-only decompression is a parity gap, not a substitute.

## Phase H — Modern hashing and cryptographic operations

Use reviewed providers and typed key material; do not confuse forensic capability with application security policy.

| Version | Increment | Deliverable | Release acceptance |
|---|---|---|---|
| **0.106.0** | Crypto provider boundary | Define key/nonce/tag types, randomness injection, algorithm identifiers and capability metadata. | Raw keys are redacted and excluded from default persistence/cache; no application transport depends on operation-pack crypto. |
| **0.107.0** | SHA-2 and HMAC | Add required SHA-2 variants, HMAC parameters and streaming hash operations. | Known-answer vectors, long inputs and arbitrary partitions agree across targets. |
| **0.108.0** | SHA-3 and Keccak | Add distinct SHA-3/Keccak variants and SHAKE-style extendable outputs where in scope. | Domain separation and output length are explicit; similar algorithm names cannot be substituted. |
| **0.109.0** | BLAKE families | Add required BLAKE variants and optional BLAKE3 enhancement through narrow provider features. | Keyed/context modes and tree boundaries have vectors; provider upgrades cannot silently alter cache identities. |
| **0.110.0** | Checksums and CRCs | Add inventory checksum families and parameterized CRC configurations. | Polynomial reflection, initial/final values and output byte order are independently tested. |
| **0.111.0** | KDF primitives | Add PBKDF2, HKDF and related modern derivations with parameter ceilings. | Salt/info distinctions, output bounds and excessive iteration requests are tested; secrets remain tainted. |
| **0.112.0** | Password derivation | Add bcrypt/scrypt and a separately labelled Argon2 enhancement when provider review permits. | CPU/memory costs are validated before scheduling; compatibility variants and truncation rules are explicit. |
| **0.113.0** | AES block modes | Add inventoried AES modes, key lengths, padding and byte-format mappings. | Standard vectors and negative padding cases pass; insecure modes are analysis tools, never default application encryption. |
| **0.114.0** | Authenticated encryption | Add required AEAD forms with staged decryption output and explicit tag verification. | A failed tag releases no plaintext artifact; all input/tag/nonce changes have negative vectors. |
| **0.115.0** | AES key wrap | Add wrap/unwrap variants and integrity checks required by the reference. | Invalid key lengths, padding and integrity failures do not expose partially unwrapped material. |
| **0.116.0** | ChaCha and Poly1305 | Add exact ChaCha variants, counters and authenticated combinations when in scope. | Counter overflow and nonce construction are checked; variant differences remain visible in descriptors. |
| **0.117.0** | Salsa family | Add Salsa20/XSalsa20 operations with exact key, nonce and counter semantics. | Known vectors and boundary conditions work in streaming and one-shot paths. |
| **0.118.0** | Fernet and authenticated wrappers | Add Fernet and related required wrappers with timestamp and token-format handling. | Authentication precedes plaintext publication; injected clock and expiry policy are testable. |
| **0.119.0** | Random and prime generation | Add explicit deterministic PRNG operations and secure random/prime generation through distinct providers. | Seeded analysis tools are not mistaken for CSPRNG; entropy failure is fatal where secure randomness is required. |
| **0.120.0** | Modern crypto qualification | Run independent vectors, malformed inputs, cross-provider comparisons and secret-lifecycle checks. | No known high-severity provider issue remains; side-channel claims are limited to evidence and platform capabilities. |

**Phase gate:** Production cryptography is not written from scratch solely to reduce crate counts. Analysis operations and service TLS remain separate security domains.

## Phase I — Legacy cryptography, hashes and classical ciphers

Close the long-tail compatibility scope without enabling obsolete security in the service.

| Version | Increment | Deliverable | Release acceptance |
|---|---|---|---|
| **0.121.0** | Legacy safety separation | Package historical algorithms with explicit analysis labels and separate features from application security. | Enabling every operation cannot weaken HTTPS, sessions, storage encryption or identity verification. |
| **0.122.0** | DES and Triple DES | Add modes, padding and historical key conventions required by reference fixtures. | Weak-key and parity-bit handling is documented; outputs match independent known-answer tests. |
| **0.123.0** | Blowfish and RC2 | Deliver required modes and parameter variants through reviewed implementations. | Key expansion limits, effective key bits and legacy padding have positive and negative fixtures. |
| **0.124.0** | RC4 and Rabbit | Add stream variants, RC4-drop controls and exact byte semantics. | State persists across chunks; skip/drop parameters cannot cause uncontrolled work. |
| **0.125.0** | TEA family | Add TEA, XTEA and XXTEA with explicit word order and length conventions. | Short messages, padding and unusual variants have independently sourced compatibility cases. |
| **0.126.0** | Additional block ciphers | Add required RC6, Twofish, PRESENT and other inventoried block families. | Each algorithm/variant is separately tracked; an unavailable provider causes more 0.x work, not an unlabelled replacement. |
| **0.127.0** | SM4 and GOST encryption | Add required modes and parameter sets with explicit identifiers. | Parameter-set selection is reproducible; names alone cannot choose an incompatible implementation. |
| **0.128.0** | Ascon variants | Add the exact Ascon versions exposed by the pinned reference and separately identify newer variants. | Algorithm revision, nonce/tag lengths and byte-order differences are verified rather than conflated. |
| **0.129.0** | Historical hashes | Add required MD/SHA-0/RIPEMD and other legacy digest families. | Every inventoried variant has test vectors; obsolete digests remain labelled unsuitable for modern integrity security. |
| **0.130.0** | Specialist hashes | Add inventoried GOST/SM3/Whirlpool/Snefru/HAS-160 and other uncommon digests as applicable. | Provider absence, missing variants and licensing restrictions stay visible until resolved. |
| **0.131.0** | Fuzzy and similarity hashes | Add the reference’s fuzzy/context-triggered hashes and comparison utilities. | Similarity scores, block sizes and edge cases match reference behavior; results are not represented as cryptographic proofs. |
| **0.132.0** | Classical substitution | Add ROT families, Vigenere, Morse, Bacon, Affine, Atbash, A1Z26, substitution and related inventory entries. | Alphabet, case, punctuation and non-ASCII policies are explicit and fixture-tested. |
| **0.133.0** | Classical transposition | Add Bifid, Rail Fence, Caesar Box and other inventoried transposition/novel encodings. | Incomplete grids, key validation and reverse transforms preserve the required conventions. |
| **0.134.0** | Historical machines | Add Enigma/Typex/Lorenz/SIGABA and associated analysis tools such as Bombe/Colossus when inventoried. | Machine settings and known historical/reference fixtures agree; expensive searches have strict work budgets. |
| **0.135.0** | Legacy completeness gate | Deliver remaining EVP/CipherSaber/Citrix/LS47 and other residual legacy entries, splitting releases as necessary. | Generated coverage shows no unowned long-tail algorithm or argument gap; all required browser paths are tested. |

**Phase gate:** This phase may require substantial extra releases. A cipher name in a list is not evidence of compatible implementation or validated security.

## Phase J — Public keys, certificates and tokens

Deliver parsing and cryptographic workflows without conflating parse, verify and trust decisions.

| Version | Increment | Deliverable | Release acceptance |
|---|---|---|---|
| **0.136.0** | ASN.1 and OIDs | Add bounded BER/DER parsing, ASN.1 display and OID conversions required by inventory. | Excessive lengths, recursion, non-canonical encodings and truncated objects have precise failures. |
| **0.137.0** | PEM and key representations | Add PEM/hex/JWK conversions and typed private/public key containers. | Key types, curves, leading zeros and private-field redaction survive round trips. |
| **0.138.0** | X.509 parsing | Add certificate fields, extensions, public-key extraction, certificate-bundle parsing and required display forms; pin the adopted current-source delta. | Parsing success is never labelled certificate trust; unknown extensions remain available as data. |
| **0.139.0** | CRLs and CSRs | Add revocation-list and signing-request parsing with explicit signature-verification actions. | Invalid signatures and malformed fields are distinguished from mere parsing errors. |
| **0.140.0** | RSA operations | Add key generation, encrypt/decrypt and sign/verify with exact padding/hash options. | Entropy, key-size budgets, padding failures and reference compatibility are tested; no raw-secret logging. |
| **0.141.0** | ECDSA operations | Add selected curves, key generation, signing/verification and signature-format conversion. | DER versus fixed-width forms, low-S policy and invalid curve points are handled explicitly. |
| **0.142.0** | SM2 and GOST signatures | Add inventoried public-key operations, identity parameters and GOST wrap/sign variants. | Parameter sets and user-identity fields have vectors; missing provider variants remain blocking gaps. |
| **0.143.0** | OpenPGP parsing and keys | Add packet/key inspection and generation with the pinned reference’s capability matrix. | Unsupported packets or algorithms are reported precisely; packet lengths and recursion are bounded. |
| **0.144.0** | OpenPGP encryption | Add encrypt/decrypt and key-selection behavior for required OpenPGP formats. | Integrity-protected output stays staged until verified; legacy insecure forms are clearly identified. |
| **0.145.0** | OpenPGP signatures | Add sign/verify and combined encrypt/sign workflows with separate validity and trust reports. | Detached/embedded signatures, canonical text and multi-signature cases match fixtures. |
| **0.146.0** | SSH key analysis | Add host-key parsing, fingerprints and inventoried conversions. | Algorithm distinctions and malformed length fields are bounded; no SSH connection is implied by parsing a key. |
| **0.147.0** | JWT and token inspection | Add decode/sign/verify with explicit permitted algorithms and key types. | Decode never implies validation; algorithm confusion, missing signatures and key-type mismatch tests fail closed. |
| **0.148.0** | Signed session formats | Add Flask-session and other inventoried signed-container workflows. | Timestamp, compression, secret encoding and serializer variants are fixture-tested without persisting signing secrets. |
| **0.149.0** | Key and secret UX | Add ephemeral secret slots, import warnings, copy/export confirmation and reproducibility redaction. | Recipe sharing cannot accidentally include private keys; browser/OS memory erasure limitations are documented honestly. |
| **0.150.0** | Public-key qualification | Run independent vectors, malformed corpora, interoperability and browser/native conformance. | Every advertised algorithm/format is tested; a successful parse, a valid signature and a trusted identity remain distinct states. |

**Phase gate:** No user analysis certificate or imported root is allowed to alter the application’s HTTPS/identity trust configuration.

## Phase K — Network and forensic analysis

Cover network and forensic operations while separating passive parsing from controlled network effects.

| Version | Increment | Deliverable | Release acceptance |
|---|---|---|---|
| **0.151.0** | IP and network primitives | Add IP-format conversion, subnets, CIDR calculations and related byte/address operations. | IPv4/IPv6, mapped addresses and boundary masks have fixtures without accidental outbound traffic. |
| **0.152.0** | URL and domain analysis | Add URL parsing, extraction, defang/refang and domain helpers from inventory. | Decoding order and Unicode display cannot silently change a network destination. |
| **0.153.0** | HTTP data parsing | Add request/response, headers, cookies, content metadata and related format operations. | Ambiguous framing is reported; parsing hostile HTTP never routes it through the live service parser as a trusted request. |
| **0.154.0** | User HTTP request operation | Expose explicit browser-fetch and controlled native-gateway modes with credential/redirection policy. | Browser CORS limitations are visible; remote mode passes SSRF and egress tests and never runs automatically on import. |
| **0.155.0** | DNS data and queries | Add required DNS parsing/lookup capabilities with separate local-data and network modes. | Network use requires consent/capability; responses, name compression and timeout/work limits are bounded. |
| **0.156.0** | TLS and SSH fingerprints | Add inventoried JA3/JA4/HASSH and related passive fingerprint operations. | Fingerprint versions and normalization rules are explicit; analysis of legacy handshakes does not enable legacy TLS transport. |
| **0.157.0** | Packet and protocol extraction | Add required packet/protocol field parsers, protobuf/varint helpers and payload extraction. | Truncation, nested lengths and reassembly limits are tested; unsupported protocol revisions are reported. |
| **0.158.0** | File identification | Add versioned signatures, confidence explanations, strings and binary structure probes. | Detection is labelled heuristic where appropriate; input-controlled paths or extensions do not override byte evidence. |
| **0.159.0** | Executable analysis | Add the inventoried executable formats and section/header extraction with bounded reads. | Corrupt offsets and huge section counts fail safely; extracted code is never executed. |
| **0.160.0** | Disassembly | Integrate the required architectures/modes through isolated providers and structured instruction results. | Native/browser outputs and syntax options match the selected reference; architecture support is enumerated, not implied. |
| **0.161.0** | YARA language support | Deliver the exact required YARA syntax/module behavior and compiler diagnostics. | Rule corpus covers modules, strings, conditions and language variants; a subset implementation cannot claim full parity. |
| **0.162.0** | YARA execution controls | Add match offsets, metadata, warnings, cost limits and killable worker execution. | Hostile rules and many matches respect budgets; scanning requires no filesystem/network privileges. |
| **0.163.0** | Carving and extraction | Add byte signatures, embedded artifact carving and bounded output collections. | Overlapping candidates, nested files and excessive matches cannot exceed job-wide quotas. |
| **0.164.0** | Forensic analysis views | Add entropy maps, byte frequency, comparisons and inventoried statistical/search helpers. | Sampling versus full analysis is labelled; results are deterministic for a fixed input and algorithm revision. |
| **0.165.0** | Forensic completeness gate | Reconcile network/forensic inventory, capabilities, passive/active distinctions and offline availability. | No browser-local reference capability is silently replaced by a server-only implementation. |

**Phase gate:** Native networking uses the central gateway and TLS seam. Passive protocol analysis uses independent parsers and cannot change application security settings.

## Phase L — Images, media and document presentation

Deliver the complete relevant media catalogue without making GPU or cloud services mandatory.

| Version | Increment | Deliverable | Release acceptance |
|---|---|---|---|
| **0.166.0** | Media provider boundary | Define bounded image/frame/audio artifacts, metadata, dimensions and deterministic decode policy. | Pixel/frame/duration limits are checked before allocation; corrupted metadata cannot request unbounded buffers. |
| **0.167.0** | Image decoding | Add every required input image format and animated variant via reviewed feature-selected providers. | Browser/native decode fixtures record color, alpha and frame semantics; unavailable codecs remain explicit gaps. |
| **0.168.0** | Image encoding | Add reference output formats, metadata policy and deterministic options where possible. | Quality settings and byte-level nondeterminism are documented; exact output comparisons use the right compatibility criteria. |
| **0.169.0** | Geometry transforms | Add resize, crop, rotate, flip and related inventoried image operations. | Coordinate bounds, interpolation options, orientation and very large dimensions are fixture-tested. |
| **0.170.0** | Color transforms | Add channels, grayscale, inversion, brightness/contrast and required color operations. | Color space, alpha premultiplication and clamping rules are explicit and reproducible. |
| **0.171.0** | Filters and effects | Add required blur/sharpen/convolution and other image effects from inventory. | Kernel costs and edge behavior are bounded; arbitrary filter input cannot cause uncontrolled GPU/CPU allocation. |
| **0.172.0** | Image composition | Add layering, text/annotation and inventoried composition helpers. | Fonts/assets are local and versioned; untrusted text remains inert and export respects declared dimensions. |
| **0.173.0** | Steganography and bit planes | Add required image byte/bit extraction and embedding operations. | Capacity limits, channel order and malformed payloads have round-trip and negative tests. |
| **0.174.0** | QR and barcode generation | Add required symbologies and rendering options. | Payload capacity, error correction and invalid character sets are checked against reference fixtures. |
| **0.175.0** | QR and barcode recognition | Add local recognition for inventoried formats with deterministic input preprocessing. | Recognition failure is explicit; no image is uploaded to a third-party recognition service. |
| **0.176.0** | OCR | Add a local OCR provider and required language/model pack handling with bounded worker execution. | Model availability, accuracy corpus, memory costs and browser support are measured; absent languages are tracked gaps. |
| **0.177.0** | Image and audio metadata | Add EXIF/ID3 and required metadata extraction/editing or display operations. | Nested metadata, thumbnails and encoding variants are bounded; metadata is not interpreted as trusted markup. |
| **0.178.0** | Audio and other media operations | Deliver inventoried playback/visualization/transforms using provider or browser presentation adapters. | User activation requirements and codec support are visible; playback is never automatic for imported recipes. |
| **0.179.0** | PDF/HTML/media preview | Add the presentation behaviors actually required by the reference, with isolated preview surfaces and download fallback. | Active content cannot access app origin, secrets or APIs; no unsupported claim of a full Rust PDF renderer. |
| **0.180.0** | Media qualification | Close format/argument gaps, compare outputs using declared tolerances and test malicious media corpora. | Baseline use works without WebGPU; optional acceleration produces equivalent results within documented tolerances. |

**Phase gate:** Media is a required parity workstream, not a reason to silently introduce cloud processing. Heavy packs may load on demand and must be available in offline bundles.

## Phase M — Complete recipe semantics, Magic and compatibility

Finish behavioral compatibility at the workflow level, not just the operation list.

| Version | Increment | Deliverable | Release acceptance |
|---|---|---|---|
| **0.181.0** | Compatibility interpreter | Complete execution of imported reference recipe sequences using the bounded control-flow IR. | Recipes with disabled operations, defaults and mixed data types preserve documented semantics. |
| **0.182.0** | Fork and Merge compatibility | Map reference branch/delimiter behavior to typed graph regions and ordered joins. | Empty branches, delimiters and nested forks match fixtures independently of runtime chunking. |
| **0.183.0** | Subsection processing | Add bounded subsequence selection and reinsertion with exact offset/text semantics. | Boundary, Unicode and changing-output-length cases preserve the required surrounding data. |
| **0.184.0** | Registers and variables | Implement reference register capture/substitution plus typed native variables and secret references. | Scope, escaping, missing registers and lifetime rules are deterministic; secrets do not leak into recipe serialization. |
| **0.185.0** | Labels and jumps | Deliver forward/backward and conditional jumps with explicit iteration and total-work limits. | Looping reference fixtures pass; exhausted limits return a precise diagnostic rather than hang. |
| **0.186.0** | Return and nested recipes | Add early return, comments, subrecipe calls and reusable parameterized recipe blocks. | Return scopes and nested budget inheritance are tested; recursion is bounded or rejected by the declared profile. |
| **0.187.0** | Compatibility recipe importer | Import supported JSON and URL recipe encodings into the canonical model with a diagnostic report. | Unknown operations/arguments are preserved for review or rejected, never silently dropped. |
| **0.188.0** | Compatibility exporter | Export representable recipes to the reference format and native full-fidelity format. | Unrepresentable graph features produce an explicit report; no misleading successful export loses behavior. |
| **0.189.0** | Detection primitives | Add versioned signature, alphabet, entropy and structure detectors with bounded sampling. | Detectors explain evidence and uncertainty; a score is not advertised as a calibrated probability without validation. |
| **0.190.0** | Magic one-step suggestions | Suggest candidate reversible transforms and display previews without changing the active recipe. | Suggestions require user acceptance; network, secret-revealing or expensive actions are excluded by default. |
| **0.191.0** | Magic bounded search | Add multi-layer transform search with deduplication, depth/work budgets and reproducible ranking. | Adversarial recursive inputs terminate; repeated runs on the same data/revision produce stable candidate ordering. |
| **0.192.0** | Brute-force analysis | Complete required XOR/rotation/encoding/language-scoring searches and ranked result presentation. | Work estimates, candidate limits and cancellation are effective; heavy searches are never automatic by default. |
| **0.193.0** | Full regex compatibility | Close remaining XRegExp/JavaScript syntax, Unicode, capture, replacement and formatting gaps through the approved strategy. | Reference dialect corpus passes locally and natively; safe-regex mode remains separately identified. |
| **0.194.0** | End-to-end reference recipes | Run a broad versioned corpus combining formats, crypto, loops, archives, media and forensic operations. | Equality criteria cover bytes, structure, diagnostics and allowed nondeterminism; every mismatch has a tracked disposition. |
| **0.195.0** | Feature-complete parity candidate | Reconcile operation, argument, recipe, UI and browser/native matrices against the frozen reference. | No required capability is missing; any open gap creates additional 0.x releases before qualification. |

**Phase gate:** This is the first feature-complete candidate, not general availability. Full functional parity cannot be established by counting operation names alone.

## Phase N — Extensibility and replacement-adapter proof

Prove additions and infrastructure changes do not force edits throughout the engine or UI.

| Version | Increment | Deliverable | Release acceptance |
|---|---|---|---|
| **0.196.0** | Operation SDK | Publish first-party operation scaffolding, descriptor validators, fixture templates and threat-review guidance. | A sample operation is added without modifying scheduler, HTTP routes, database schema or handwritten UI forms. |
| **0.197.0** | Operation pack manifests | Group operation implementations by capability, version, dependency footprint and platform support. | Required dependencies are explicit; removing a pack cannot produce silently incomplete loaded recipes. |
| **0.198.0** | Lazy browser packs | Add on-demand loading and an explicit complete offline-pack catalogue. | App, engine and pack versions are verified before activation; failed downloads leave a usable previous state. |
| **0.199.0** | Provider replacement tests | Run selected operations against alternate providers behind stable semantic descriptors. | Replacement requires byte/behavior conformance and security review; provider identity participates where it affects reproducibility. |
| **0.200.0** | Core-Wasm plugin ABI | Specify a narrow versioned ABI for memory, metadata, bounded I/O, errors and capability requests. | The ABI contains no host pointers, unrestricted syscalls or implicit network/file access. |
| **0.201.0** | Browser plugin sandbox | Load plugins in a separate worker/instance with allowlisted imports, resource limits and explicit grants. | An infinite loop, memory growth or hostile output can be terminated without accessing app state or persistent secrets. |
| **0.202.0** | Native plugin sandbox | Add a reviewed Wasm runtime adapter with fuel/epoch or equivalent limits and constrained host calls. | Resource and capability tests cover malicious modules; signatures are not treated as proof of safety. |
| **0.203.0** | Plugin package integrity | Add manifests, hashes, optional signatures, provenance, revocation and administrator policy. | Unknown publishers are not automatically trusted; rollback protection and offline integrity checks have tests. |
| **0.204.0** | Plugin conformance kit | Publish ABI vectors, boundary fuzzing, malformed-module tests and example portable operations. | Plugin authors can validate behavior without depending on the web framework or database. |
| **0.205.0** | Component-model evaluation | Evaluate a WIT/component adapter using the required JavaScript shims/transpilation where needed. | Keep it optional unless browser/native portability and resource enforcement match the established plugin contract. |
| **0.206.0** | HTTP server replacement seam | Implement a second minimal/mock HTTP adapter and route conformance suite for a future Vef provider. | All application endpoints run without importing the original framework outside its adapter package. |
| **0.207.0** | Outbound HTTP replacement seam | Centralize identity, user HTTP, object-storage and other outbound clients behind application-owned gateway policy. | No native subsystem opens an unreviewed HTTP/TLS path; destination and trust policies survive provider substitution. |
| **0.208.0** | TLS replacement seam | Test inbound/outbound TLS and database TLS connectors with alternate/mock providers for future Brynja integration. | Trust, hostname verification, ALPN, timeouts and errors remain explicit; browser-owned TLS is documented as outside this seam. |
| **0.209.0** | Conditional sibling integrations | Add real Vef/Brynja adapter packages only when their APIs and security properties are usable; otherwise ship contract harnesses. | The default build works without sibling paths; integration is not claimed complete when only a placeholder exists. |
| **0.210.0** | Extensibility qualification | Demonstrate a new operation, new pack, provider swap and transport replacement through the public contracts. | No domain/database/UI rewrite is needed; every accepted extra dependency has a documented purpose and feature budget. |

**Phase gate:** Third-party plugins may be disabled by policy. First-party extensibility is mandatory. Future sibling readiness is not a blocker for 1.0 if the replacement boundaries are proven.

## Phase O — Portability, collaboration and operations

Prove SQL portability and deployability while keeping optional server features separate from local processing.

| Version | Increment | Deliverable | Release acceptance |
|---|---|---|---|
| **0.211.0** | Shared recipe collections | Add server-backed folders/tags and permission-aware recipe sharing without default input sharing. | Revoking access prevents future reads; links and searches cannot enumerate another workspace. |
| **0.212.0** | Recipe revisions and conflicts | Add optimistic revision checks, compare/restore and explicit multi-client conflict handling. | Two clients cannot silently overwrite each other; no real-time collaboration framework is required. |
| **0.213.0** | Administrative policy | Add operation/pack allowlists, egress policy, resource profiles and retention settings. | Policy is enforced server-side and reported through capabilities; clients cannot self-authorize forbidden operations. |
| **0.214.0** | Audit and retention lifecycle | Add bounded audit export, retention jobs, object deletion and backup-retention documentation. | Payloads are absent by default; deleted live records and retained backups are not misleadingly described as immediate erasure everywhere. |
| **0.215.0** | Logical storage export | Export portable recipe, identity-reference, job and artifact manifests using versioned logical records. | Export is independent of PostgreSQL SQL syntax and contains explicit integrity/referential checks. |
| **0.216.0** | MySQL portability prototype | Implement actual MySQL repository methods and backend-specific migrations in a separate adapter. | Shared contracts run against a real MySQL instance; merely compiling a generic driver is insufficient. |
| **0.217.0** | SQL semantic parity | Exercise collation, uniqueness, JSON values, booleans, timestamps, pagination and transaction behavior on both databases. | Results and conflict semantics agree despite different SQL dialects; deviations stay inside adapters. |
| **0.218.0** | PostgreSQL-to-MySQL migration drill | Import a logical export into MySQL, verify hashes/counts/references, rehearse cutover and rollback. | Application use cases work without domain or API changes; failures leave the original deployment recoverable. |
| **0.219.0** | MySQL-to-PostgreSQL reverse drill | Reimport the same logical model and repeat repository and authorization tests. | Round trips retain identifiers/revisions; the project makes no unsupported zero-downtime migration guarantee. |
| **0.220.0** | Artifact backend portability | Exercise local-disk and an optional object-storage adapter against the same artifact contracts. | Range reads, integrity, leases and orphan cleanup work without tying metadata schema to one cloud provider. |
| **0.221.0** | Backup and disaster recovery | Document and test coordinated metadata/artifact backups, schema recovery and corruption detection. | Restore drills actually read and execute restored recipes/artifacts instead of only checking backup file existence. |
| **0.222.0** | Release packaging | Produce versioned static offline bundles, native API binaries and container images with manifests and notices. | Builds identify exact dependency and operation-pack revisions; no desktop/mobile application is shipped yet. |
| **0.223.0** | Upgrade and rollback | Add compatible server/browser/pack upgrade rules, migration prechecks and rollback guidance. | An interrupted upgrade cannot mix incompatible schema/engine assets or corrupt saved recipes. |
| **0.224.0** | Operational load qualification | Exercise realistic multi-user mixes, expensive-job fairness, disk pressure and process failure. | Published limits come from measurements; API responsiveness survives isolated worker exhaustion. |
| **0.225.0** | Portability and operations gate | Close deployment docs, actual second-database contract tests and Vef/Brynja replacement rehearsals. | PostgreSQL is the initial production-supported backend; MySQL support level is stated separately from the proven portability contract. |

**Phase gate:** Supporting another database still requires its adapter, migrations and qualification. Independence means no core rewrite, not a promise that database switches are free.

## Phase P — Qualification and general-availability readiness

Convert a feature-complete candidate into a defensible full release.

| Version | Increment | Deliverable | Release acceptance |
|---|---|---|---|
| **0.226.0** | Scope freeze | Freeze the 1.0 reference commit, operation revisions, recipe schema, API and required browser profiles. | Later upstream additions enter a separate backlog; security fixes remain eligible for inclusion. |
| **0.227.0** | Catalogue audit | Independently reconcile every operation and argument against the pinned baseline and category/source inventories. | No unexplained omissions, duplicate counting or native-only substitutions inflate the compatibility claim. |
| **0.228.0** | Workflow and UI audit | Verify save/load, links, multiple inputs, breakpoints, offsets, Magic and complete control flow. | Workbench parity is demonstrated beyond unit tests; safety differences are documented prominently. |
| **0.229.0** | Cross-target conformance | Run native and actual Chromium, Firefox and WebKit suites with and without optional browser features. | Required capabilities work on the published baseline; simulated wasm compilation alone is not sufficient. |
| **0.230.0** | Resource and denial-of-service audit | Fuzz parsers, recipe compilation, regex, queries, archives, images and plugin host interfaces. | Memory/work/depth/output limits hold; discovered crashes and hangs are triaged and fixed before release. |
| **0.231.0** | Unsafe and dependency audit | Review unsafe islands, crypto providers, build scripts, generated tables and transitive dependency changes. | No unreviewed dependency exception or known unmitigated high-severity issue remains in the release profile. |
| **0.232.0** | API and authorization assessment | Exercise adversarial authentication, sessions, object permissions, uploads, egress and worker isolation. | Confirmed critical/high findings are fixed and regression-tested; accepted lower risks have owners and rationale. |
| **0.233.0** | Data and cache assessment | Verify secret handling, cache isolation, completed-artifact publication, deletion and backup behavior. | Cross-tenant cache probing and partial-result disclosure tests fail closed; documentation matches actual retention. |
| **0.234.0** | Accessibility and usability assessment | Test realistic tasks with keyboard, screen readers, high zoom, narrow layouts and error recovery. | Essential tasks have non-canvas alternatives; accessibility failures are fixed rather than deferred to native apps. |
| **0.235.0** | Performance characterization | Publish reference hardware/browser measurements for startup, interaction, throughput, memory and cancellation. | Claims distinguish streaming from whole-input operations and cold from warm caches; no invented speedup multipliers. |
| **0.236.0** | Supply-chain release proof | Produce dependency/asset manifests, license notices, signed checksums and reproducibility evidence for distributed artifacts. | Independent clean builds can verify the release process; supplied models/fonts/data are licensed for redistribution. |
| **0.237.0** | Migration and disaster drill | Re-run PostgreSQL/MySQL portability, schema upgrade/rollback and metadata/artifact restore on release candidates. | Recovery preserves recipe revision and authorization invariants; operational instructions are executable. |
| **0.238.0** | Documentation and SDK freeze | Finalize API reference, operation docs, extension guide, offline setup, threat model and migration contracts. | Examples are exercised in CI; docs disclose compatibility limits and browser-owned TLS boundaries. |
| **0.239.0** | Release-candidate rehearsal | Produce a feature-frozen candidate build and run the full acceptance checklist with representative users. | Blocking issues produce further 0.x releases; the version number cannot waive missing functionality or security gates. |
| **0.240.0** | GA acceptance decision | Assemble evidence for all mandatory capabilities, parity matrices, security, accessibility, recovery and provider boundaries. | Advance to 1.0.0-rc only when every mandatory gate passes; otherwise continue 0.241.0 and beyond with concrete gap releases. |

**Phase gate:** After a passing 0.240.0-equivalent gate, publish 1.0.0-rc.1 and further candidates as required, then 1.0.0. The date and number of additional releases are intentionally not promised.

## Release candidates and 1.0.0

**1.0.0-rc.1:** publish only after the feature-complete and qualification gates pass. Freeze the public API v1 contract, recipe schema compatibility policy, operation revision registry and supported browser matrix. Run clean-install, offline, migration, upgrade, restore and adversarial test suites on the exact signed candidate artifacts.

**Further release candidates:** fix defects, update evidence and repeat affected qualification. A missing required operation or substantial semantic gap returns to additional 0.x feature work rather than being quietly relabelled a post-1.0 enhancement.

**1.0.0:** the complete website, shared Rust engine, documented API, PostgreSQL production profile, full declared CyberChef-baseline functionality, operational documentation and proven replacement boundaries. Local browser processing must remain usable without accounts or a server. Native desktop and mobile applications are not part of this release.

## Desktop and mobile after 1.0.0

These are proposed subsequent product milestones, not fixed API-breaking version requirements. Client applications may use independent version numbers while continuing to speak API v1.

| Proposed product milestone | Scope | Required architecture reuse |
|---|---|---|
| 1.1 — Desktop preview | Package a desktop client using the same application contract; start with remote execution and the existing local engine where practical. | Existing EngineClient, recipes, operation registry and artifact interfaces; no duplicate transformations. |
| 1.2 — Desktop stable | Add explicit filesystem grants, secure credential storage, signed updates and qualified native offline execution. | Native host/provider adapters; database remains on the server when using a server profile. |
| 1.3 — Mobile preview | Introduce touch-oriented inspection, recipe editing, API jobs and bounded on-device operations. | API capability negotiation; smaller device budgets rather than altered operation semantics. |
| 1.4 — Mobile stable | Add platform share/file integration, app lifecycle recovery and vetted secure storage/update handling. | The same recipe/error/job contracts and per-platform conformance suite. |
| 1.5+ — Further capabilities | Expand on-device packs, collaboration or additional production-supported databases based on demand. | No coupling of client release numbering to operation revisions or database schema. |

Native-shell selection is deliberately deferred until implementation. The pre-1.0 deliverable is tested reusable contracts, not speculative mobile framework scaffolding. Vef and Brynja can be adopted before or after 1.0 only when their adapters satisfy protocol, interoperability, resource and security requirements; readiness is never assumed from a sibling directory name.
