# Rust Data-Transformation Workbench — Architecture and Release Contract

**Planning date:** 2 October 2026  
**Project name:** not selected; `workbench-*` below is a placeholder namespace.  
**Requested starting toolchain:** Rust 1.99.0, stable, Rust 2024 edition.  
**Product boundary:** a complete browser workbench and public API at 1.0.0; desktop and mobile applications only after 1.0.0.  
**Companion documents:** `ROADMAP.md`, `PARITY_AND_RISK_REGISTER.md`, and the machine-readable `roadmap.json`.

## 1. Executive decision

Build a **local-first, API-driven, typed data-transformation engine**, not a server-bound clone and not a new general-purpose distributed workflow platform. Compile the same Rust operation implementations for browser WebAssembly and native execution. Put the website, server transport, database, TLS provider, and later native applications outside the engine.

The default browser workflow must work without an account, PostgreSQL, or remote execution. Server storage and execution are optional, explicitly selected capabilities. The API is a durable application contract, not a requirement to upload every input or send every processing chunk through HTTP.

Use the Gemini material as concept input, not starter production code. Keep bounded streaming, optional graph editing, paged viewers, operation packs, explicit capabilities, and selective caching. Replace the demonstrated scheduler, caching, browser integration, and persistence designs with contracts that can actually be tested.

Rust 1.99.0 was announced on 1 October 2026 [S01]. Pin that toolchain initially rather than a moving `stable` channel. A later compiler upgrade is a reviewed maintenance change, not a reason to redesign the product.

```toml
# rust-toolchain.toml
[toolchain]
channel = "1.99.0"
profile = "minimal"
components = ["rustfmt", "clippy"]
targets = ["wasm32-unknown-unknown"]
```

Use `edition = "2024"` and `rust-version = "1.99"` for project packages. Check in the application lockfile. Test the pinned toolchain and, separately, the newest stable compiler when maintaining the project. Nightly-only tools may run in separate analysis jobs; no production feature requires a nightly compiler.

**1.0.0 is a set of satisfied requirements, not the inevitable next tag after 0.240.0.** Add more minor releases when a capability, security gate, or portability test remains incomplete. The supplied 240-release sequence is an ordered work breakdown, not a claim that difficult compatibility projects are uniformly small.

## 2. Evidence, assumptions, and corrections to the supplied draft

External facts in this plan are tied to the source register. The architecture and numerical acceptance targets are recommendations, not existing implementation measurements. The requested future mapping is Vef for HTTP/web protocols and Brynja for TLS. No APIs, current implementation completeness, or release dates for the sibling repositories are assumed.

The reviewed CyberChef reference is the `v11.5.0` tag, whose package file reports 11.5.0 [S02]. Use that as a finite initial compatibility target, then resolve and record its immutable Git commit, source hashes, operation configuration, and fixtures at project kickoff. The inspected moving branch has already illustrated why tag and commit matter: its category list includes a certificate-bundle operation absent from the reviewed tag. Track upstream changes as a separate delta queue rather than quietly changing the definition of done [S03, S04].

| Draft claim or implementation | Assessment | Replacement requirement |
|---|---|---|
| CyberChef is essentially a single-threaded tool with no modern processing separation. | Its source explicitly configures input, chef, and background worker integration [S06]. Do not justify the project using an inaccurate comparison. | Benchmark actual workloads and identify measured improvements. |
| `spawn_local` isolates computation from rendering. | It schedules on the current thread, not a new worker [S07]. | Instantiate the processing engine inside a real Dedicated Worker. |
| Streaming APIs and `Bytes` make all transformations zero-copy. | The attached XOR example calls `to_vec`; the bridge also copies input and output. Ownership-sharing and transformation allocations are different issues. | Promise copy-aware, allocation-bounded execution; measure copies per operation. |
| A DAG can directly replace all recipe flow control. | CyberChef Jump can jump backwards [S05]. A strictly acyclic graph alone cannot preserve that behavior. | A workflow IR with DAG regions plus bounded control-flow regions and a compatibility interpreter. |
| Global entropy requires materializing all input. | Byte-frequency counters and a running length are sufficient for a reduction. Conversely, arbitrary global operations may require storage. | Describe stream, reduction, bounded window, seekable, and whole-input execution requirements separately. |
| A fixed number of channel messages guarantees bounded memory. | Messages can have variable size; retained references, state, previews, and cache records also consume memory. | Byte credits, bounded chunk size, bounded operation state, and a job-wide budget. |
| The shown graph wiring is production-ready. | In the attachment, input receivers are removed without insertion into `node_inputs`; draining the output map for each node loses later nodes' outputs. | Compile and validate an immutable plan; test every edge and terminal state. |
| The cache decorator remains streaming. | It first accumulates all input in `buffered_inbound`; it also handles only one input/output port. | Known-artifact identities before execution, or bounded spool-and-hash; never buffer an unbounded stream to find a cache key. |
| Cancelling the coordinator necessarily stops all spawned work. | Independently spawned work requires explicit supervision and termination. | Structured ownership of runs, child tasks, buffers, and cleanup; hard host cancellation for non-cooperative work. |
| IndexedDB request success means a durable operation has committed. | Transactions have their own completion/abort lifecycle [S08]. The draft also treats cursor continuation as a new request and later uses a timestamp field absent from the shown record. | Adapter tests for transaction completion, abort, schema upgrades, callback lifetime, and worker contexts. |
| Browser components can be passed directly to the standard Wasm API as ordinary modules. | Component execution in JavaScript uses tooling/bridging such as Jco [S09]. | Begin with a narrow core-Wasm plugin ABI; add component adapters after browser/native conformance tests. |
| A virtualized canvas makes a 64 GB viewer consume roughly 640 bytes. | That only approximates one visible byte window, not decoded data, canvas pixels, indexes, caches, source buffers, and runtime overhead. | Separately measure viewer, engine, source, and browser/host memory. |

The examples above are a design review, not an exhaustive compiler or security audit of the attached code. Relevant attachment locations include lines 206–215, 744–759, 967–1005, 1283–1292, 1557–1560, 1590–1592, 2040–2044, and 2850–2856.

## 3. Product modes and privacy contract

| Mode | Execution | Persistence | Network behavior |
|---|---|---|---|
| Ephemeral local, default | Browser worker | Memory only | App assets may load; input/recipes/results are not uploaded. |
| Persistent local, opt-in | Browser worker | Local recipe metadata; explicitly permitted artifact storage | No payload upload; clear storage and retention controls are visible. |
| Remote run, explicit | Isolated native/server worker | According to a displayed retention policy | UI shows destination, affected inputs, and permission before upload. |
| Self-hosted team | Either local or remote, per run | PostgreSQL metadata and separate artifact store | Operator policy and access controls govern sharing and execution. |
| Offline bundle | Browser worker from trusted local hosting | Local storage as permitted | Complete selected operation packs available without external services. |

A local processing failure must **never** silently fall back to remote execution. This includes out-of-memory, an unavailable operation pack, browser API limitations, and network restrictions. A user can deliberately choose a new execution plan and approve its data movement.

Do not require a database to decode Base64. Do not automatically persist cryptographic keys, decoded tokens, private files, intermediate results, clipboard content, or browsing sessions. Saved recipes contain secret references or redacted placeholders unless the user explicitly chooses an encrypted export.

The UI must distinguish **local computation**, **local disk persistence**, **remote upload**, and **external network access**. These are different permissions. An operation that makes an HTTP request is a side effect even when the engine itself runs locally. CyberChef's HTTP operation is explicitly manual-bake and uses browser fetch; browser origin restrictions are part of that behavior [S10].

Downloaded/offline bundles should be self-contained and versioned, including models and tables needed by selected packs. Do not fetch fonts, analytics, OCR models, magic databases, or plugin code from third-party CDNs without an explicit product decision and a visible installation step.

## 4. What complete CyberChef functionality means

Feature parity is not a list of familiar operation names. Maintain an executable inventory covering operation IDs, aliases, parameter names/types/defaults, alphabet variants, text and byte conversions, invalid-input behavior, record handling, register substitution, rendering, recipe import/export, browser availability, and test evidence.

The reference catalogue includes much more than encoding and hashes: flow control, structured queries, networking, archives, public keys, image/media operations, OCR, YARA, and disassembly [S03]. The operation-family schedule is therefore deliberately broad. The exact inventory discovered at kickoff is authoritative over the illustrative names used in the roadmap.

The reviewed v11.5.0 tag is a planning anchor, not a claim that a moving branch has no newer functionality. The separately reviewed current catalogue includes a certificate-bundle parsing entry [S04]; include that observed delta in the initial scope reconciliation and the X.509 workstream. At 0.2.0, resolve both the baseline and any adopted current-source deltas to immutable commits, and ensure the chosen initial scope captures the current functionality requested. Later upstream changes follow a documented update policy.

For every inventory item record:

```text
upstream_reference: repository, tag, resolved_commit, source_path
upstream_name / aliases / category memberships
argument_schema / defaults / upstream input and output types
our_operation_id / semantic_revision / parameter_schema_revision
execution_support: browser, native, remote, offline
implementation: Rust core, Rust provider, renderer/host capability
semantic_test_cases / negative_cases / differential_cases
status: not_assessed, specified, implemented, verified
parity: exact, equivalent_representation, documented_safe_difference, gap
security_class / required_capabilities / declared_limits
provider_identity / data_table_versions / license_review
```

Operation categories may duplicate the same operation; count distinct operations separately from category placements. Scan both catalogue/configuration and implementation files. Flag unlisted operations, deprecated aliases, and internal diagnostic operations for an explicit scope decision. Do not silently discard inconvenient cases.

**Three compatibility promises:**

1. Byte-transform operations reproduce the selected reference behavior for supported inputs, options, and encodings, unless an explicit safety difference is documented.
2. Analysis and rendering operations preserve the useful result and controls; HTML markup or a canvas layout need not be byte-identical. Machine-readable results are primary, and a separate formatter supplies legacy text where meaningful.
3. Recipe interchange preserves control flow and arguments. Export a supported subset only when it is semantically representable in CyberChef; otherwise return a precise export error. Import must never silently replace unknown operations with identity transforms.

Test deterministic results exactly. Test randomness with controlled test entropy and separate validity/distribution properties, not byte equality against unrelated random output. Test network operations against recorded or local fixtures. Version Unicode, time-zone, signature, language, and model datasets. For floating-point visualizations, define tolerances and explain them.

A security restriction is not permission to delete functionality. Keep forensic/legacy operations available in an explicitly chosen compatibility profile, with warnings and resource limits. Their availability does not enable obsolete algorithms for account storage, TLS, authentication, cache protection, or server secrets.

For browser-local reference capabilities, a server-only implementation is a parity gap. Large packs may be installed on demand and included in the offline distribution, but cannot require uploading private input simply because their implementation is inconvenient.

## 5. Architecture: dependencies point inward

Use a modular monolith with a separable worker executable. Do not start with microservices, a broker cluster, a plugin marketplace, a custom database, or a general distributed execution engine.

```text
                   Browser website — Rust UI + minimal JS bindings
                                   |
                           EngineClient contract
                     +-------------+-------------+
                     |                           |
              Worker/LocalClient             RemoteClient
                     |                           |
             Browser Wasm host               HTTP API adapter
                     |                           |
                     +------ Application services ------+
                                         |
                             Recipe compiler / runner
                                         |
                   Operation contracts + typed values + budgets
                                         |
                         Rust operations / provider ports

       Native host / browser host / artifact store / repositories
       HTTP client & server / TLS / clock / randomness / diagnostics
                         are replaceable outer adapters.
```

`EngineClient` is a conceptual client contract, not an instruction to serialize every local call. In-process/native use may pass borrowed values. Browser workers use a bounded, versioned message protocol and transferable buffers. Remote clients use the documented HTTP protocol. Business semantics are shared; transport mechanics are not forced into one lowest-common-denominator implementation.

Suggested **logical** workspace boundaries, extracted into crates when needed:

```text
crates/
  workbench-types/             # IDs, lengths, limits, errors; core-only
  workbench-operation/         # descriptors and transform contracts
  workbench-recipe/            # IR, validation, compilation; alloc
  workbench-engine/            # deterministic scheduling and run state
  workbench-application/       # use cases and service contracts
  workbench-api-model/         # wire DTOs and schema mappings
  workbench-ops-encoding/      # operation families, not one crate per op
  workbench-ops-text/
  workbench-ops-format/
  workbench-ops-crypto/
  workbench-ops-archive/
  workbench-ops-forensics/
  workbench-ops-media/
  workbench-compat-cyberchef/   # importer, formatter, compatibility VM
adapters/
  browser/  native/  http-current/  tls-rustls/
  postgres/  artifact-fs/  memory/  indexeddb/  opfs/
apps/
  web/  server/  worker/  cli/
tests/
  conformance/  parity/  adversarial/  browser/  migrations/
docs/
  adr/  threat-model/  operations/  api/  support-matrix/
```

These names describe ownership, not a requirement to create dozens of empty packages on day one. Start with the minimum core, engine, browser host, and API boundaries; split operation families as their build size and dependency requirements justify it.

Public core types may not expose `axum`, `hyper`, `tokio`, `sqlx`, `tokio_postgres`, `rustls`, Leptos signals, browser handles, or provider-specific buffers. Check this with dependency and public-API tests. Keep service contracts and adapters separate enough that a backend replacement does not change recipes, operations, authorization rules, or API payloads.

## 6. Practical no_std and dependency policy

`no_std` removes the standard-library dependency; allocation is a separate decision [S11]. Use three explicit levels rather than advertising the entire website as no_std.

| Layer | Target | Constraint |
|---|---|---|
| Fundamental types, limits, fixed-buffer transforms | `no_std`, no allocation | No third-party runtime dependencies where practical. |
| Recipe IR, planning, larger operation state | `no_std + alloc` where practical | Fallible/budgeted allocation; no OS, database, TLS, or runtime assumptions. |
| UI, browser adapters, server, persistence, heavyweight providers | Host-dependent, generally `std` or browser APIs | Dependencies allowed only within their boundary and selected feature set. |

A Wasm build alone does not prove no_std. Compile the core in a genuine no_std target job, test feature combinations, and inspect feature unification. Keep allocation-free kernels usable without enabling operation packs that require heap allocation.

Own small, reviewable transformations, recipe semantics, boundary validation, limits, and schema metadata. Prefer maintained Rust libraries for cryptography, protocol engines, complex decompression, regex engines, and image/document parsing when that reduces risk. Do not replace a mature security primitive with a new in-house primitive simply to reduce the crate count.

Start with a narrowly configured, replaceable stack: Leptos for a Rust DOM UI; wasm-bindgen/web-sys for browser integration; Tokio and an Axum/Hyper adapter for the server; Rustls for native TLS; `tokio-postgres` for the initial database adapter; selected Rust cryptographic and format providers. Exact dependency versions are chosen and locked during implementation after testing Rust 1.99.0 and the target matrix. This plan does not invent unverified latest versions [S12–S15].

Track direct and transitive production dependencies, build dependencies, proc macros, unsafe code exposure, licenses, vulnerabilities, maintainer health, browser size, and feature expansion. Avoid `full` feature bundles. Test tools may have a broader dependency allowance than shipped binaries. A first-party dependency also needs review; ownership is not evidence of correctness.

No global runtime requirement belongs in operation traits. Do not require `Send + Sync` from all browser-local objects. The native host can impose those bounds where it actually moves a job between threads. Keep browser-local futures/handles outside portable types.

## 7. Operation contract and data model

Use stable operation identifiers, for example `encoding.base64.decode`, independent of display name and crate version. Give each operation a semantic revision: changing defaults, malformed-input behavior, output formatting, or algorithm/data-table behavior is a recipe compatibility event even when Rust signatures do not change.

Each descriptor contains parameter and port schemas; defaults; constraints; input/output kinds; execution class; determinism; capability requirements; sensitivity behavior; side effects; approximate cost indicators; implementation digest; supported targets; documentation; and test identifiers. Generate the operation picker, forms, API catalogue, help pages, CLI help, and conformance scaffolding from the same metadata. Do not independently hand-maintain four parameter definitions.

Core payload kinds should cover raw byte streams, explicitly encoded text, record streams, lossless structured values, tables, file collections, image/frame descriptors, and artifact references. Renderers consume typed results; operations do not generate trusted application HTML.

Important invariants:

- Raw bytes never become text implicitly. Invalid UTF-8 can be inspected as bytes; lossy decoding is a named operation or explicit presentation mode.
- Integers, byte offsets, and lengths have defined ranges. Represent 64-bit offsets as decimal strings in JSON where a JavaScript number would lose precision. Checked conversions are mandatory at Wasm/host and database boundaries.
- Preserve structured number lexemes when ordinary floating-point JSON parsing would destroy precision. Define duplicate-key behavior and object-order semantics.
- A `SecretRef` is a capability-bound handle, not an inline password included in logs or recipes. Secret-marked inputs taint derived outputs unless a reviewed declassification rule says otherwise.
- Artifact IDs are opaque, scoped references. Possession of a digest or ID is not authorization to fetch an artifact.
- A multi-file result consists of entries with sanitized display names and separate payload handles, not paths automatically written into the host filesystem.

Use a fixed-buffer streaming kernel contract with explicit consumed/produced counts and status, conceptually:

```text
step(input_window, output_window, budget) ->
    consumed, produced, NeedInput | NeedOutput | Yield | Finished
```

This is a contract sketch, not proposed compilable API code. Initialization validates parameters. End-of-input is delivered once; draining buffered final output is a distinct state. Partial consumption, empty chunks, failures, cancellation, and repeated calls after terminal state have defined behavior. Caller-owned buffers avoid requiring a specific third-party buffer type.

In-place mutation is an optional optimization available only under exclusive ownership. Immutable fan-out can share an allocation; a modifying consumer must obtain a unique buffer or make a charged copy. The contract must remain correct without an in-place path.

## 8. Execution engine and resource accounting

Classify operations accurately:

| Class | Example workload | Storage requirement |
|---|---|---|
| Streaming transform | Encoding, XOR, many framing conversions | Bounded input/output and carry state. |
| Reduction | Hash, byte histogram, global entropy | Small state, final result after end-of-input. |
| Bounded window | Framed parsing, selected matchers | Explicit maximum window and boundary policy. |
| Seekable/two-pass | Reverse a large file, some archive indexes | Seekable artifact or bounded spool. |
| Whole-input bounded | A provider requiring a full syntax tree | Admission check and a declared whole-input ceiling. |
| Side-effecting | HTTP request, sleep, current time, randomness | Host capability and explicit replay/cache policy. |

An arbitrary regex, Unicode grapheme segment, syntax tree, or nested archive cannot be assumed to have a small fixed buffer. Every implementation must either enforce a bound, spill through an allowed artifact store, or reject the requested size explicitly.

The initial scheduler should be a deterministic, cooperative execution loop over ready nodes, rather than one Tokio task per recipe node. Execute a bounded unit of work, charge input/output/state resources, yield to the host, and continue. The native host can schedule jobs in a worker pool; the browser host can assign independent jobs or independent regions to workers.

Compile the graph first. Validate node/port existence, allowed types, required arguments, declared capabilities, fan-in policy, cardinality, and control-flow bounds. By default a data port has one producer; multiple producers require an explicit join with defined ordering. Freeze a key/configuration input before processing dependent data, or define a genuine synchronized keystream operation. Do not let scheduling races change the key.

Transport chunk boundaries are not semantic record boundaries. Splitting a file into 64 KiB versus 1 MiB buffers must not change XOR offsets, text decoding, framing, hashes, register values, or output ordering. A demultiplexer must operate on declared records, not whichever buffers happened to arrive.

Charge memory by allocation capacity and lifetime, including retained buffers, provider allocations, output staging, branch queues, previews, indexes, and cache manifests. Shared buffers are not copied, but they remain live while any consumer retains them. Keep both physical-byte accounting and logical-output/fan-out limits. Bound queue bytes and message count.

A DAG with bounded channels can still stall through join/read ordering and fan-out dependencies. Test reconverging graphs under tiny queue budgets. Use a scheduler readiness model, explicit join semantics, fair scheduling, deadlock diagnostics, and spill points where appropriate. Sequentially awaiting every output consumer is not a universal scheduler.

All runs own their tasks and resources. Cancellation changes the run state, prevents new work, unwinds buffers, interrupts I/O, and schedules cleanup. Dropping a future is not sufficient to stop arbitrary blocking code. Browser hosts terminate and recreate a worker after a hard deadline; native hosts terminate the isolated worker process when cooperative cancellation fails.

Every UI execution has a monotonically increasing generation. Events from old generations cannot update current previews, publish results, or replace current errors. Positioning a graph node is presentation state and does not trigger execution. Editing a semantic parameter does.

## 9. Recipes: friendly linear view, optional graphs, complete control flow

Keep the quick operation-list → recipe → input/output workflow as the default. A graph is an advanced view, not a mandatory replacement for simple recipes.

The recipe IR needs nodes, typed ports, connections, source/sink bindings, constants, scoped registers, compatibility profile, semantic revisions, and control-flow regions. Represent bounded iteration and conditionals explicitly. Inside each region use an ordinary acyclic dataflow plan where possible.

Implement a small compatibility interpreter for imported CyberChef control flow where faithful lowering is not straightforward. It can execute Label, Jump, Conditional Jump, Return, Fork, Merge, Subsection, and Register according to the pinned reference. Bound total executed instructions, backward jumps, recursive nesting, expanded records, and output growth. A maximum per-loop iteration count alone does not bound nested work.

Support disabled steps, comments, breakpoints, single-step execution, intermediate inspection, undo/redo, reusable subrecipes, ordered multi-input workflows, and deterministic branch joins. A breakpoint must remain meaningful even when prior pure computation has a cached result.

Export the native recipe format with explicit schema and operation revisions. Import older native formats through tested migrations. Never silently retarget a saved operation to a new semantic revision. Export to CyberChef only when the recipe is representable without loss; otherwise identify the unsupported node/feature and preserve the native export.

## 10. Artifact storage, streaming I/O, and cache correctness

Keep durable metadata separate from large artifacts. The database stores ownership, recipe revisions, run state, manifests, retention, references, and access controls. File/object storage stores payload chunks. Browser IndexedDB stores metadata; OPFS can store larger local artifacts. OPFS is origin-scoped and quota-limited; it is not a guarantee of unlimited or durable disk space [S16].

The artifact API supports immutable completed objects, bounded sequential readers, range readers, transactional/staged writers, leases, quota reservation, retention, and deletion. The application does not expose raw filesystem paths. A native filesystem adapter must use traversal/symlink-safe creation and extraction rules. Browser adapters must work in their actual worker context rather than assuming `window` is available.

Separate source access from transformed artifacts. A selected local file can be range-read without copying the entire original into OPFS. A non-seekable stream may require a spool for replay or random access. Do not claim instant random access to arbitrary compressed output without an index or materialized artifact.

**Cache only when justified.** Default to ephemeral, per-workspace/per-run caching of pure operations on nonsensitive inputs. Persistent intermediate caching is opt-in. Secret-bearing inputs, decrypted data, randomness, time, external fetches, and side effects are noncacheable by default.

A cache identity includes a versioned domain separator, operation ID and semantic revision, implementation/provider identity, canonical typed parameters, ordered input ports, input artifact identities, text/compatibility settings, and relevant data-table versions. Encode fields with unambiguous framing. Object key order in ordinary JSON text must not accidentally change identity, and ambiguous concatenation must not conflate different parameter sets.

Byte-stream identity is independent of transport chunking. Hash logical bytes in order; for records or multiple ports, include canonical length/type/port framing and defined ordering. A content digest is known only after the unknown source has been read. Reusing cached computation may still require reading and hashing input. When immutable input artifact IDs are already available, a plan can look up results before executing the node.

Do not expose cache digests as authorization tokens or globally deduplicate sensitive tenants. Low-entropy secrets can be attacked through publicly visible digests. Use tenant/workspace scopes, opaque public IDs, and, when justified, keyed internal identities. Caching secret-derived values is a separate security design, not an automatic consequence of adding encryption at rest.

Write chunks to staging, verify lengths and digests, then publish a complete manifest atomically. A failed/cancelled run never publishes a successful cache entry. LRU and byte quotas use recorded sizes and bounded metadata scans; they do not deserialize giant payload arrays to determine what to evict. Handle transaction completion/abort, cache corruption, browser quota exhaustion, database schema upgrades, concurrent tabs, crash recovery, and orphan cleanup.

Encrypting or deleting browser data does not guarantee erasure from browser copies, swap, backups, or a compromised origin. State those limitations. For sensitive work, memory-only operation and a trusted offline distribution are stronger defaults than silently persisting everything.

## 11. Website and browser architecture

Use a Rust DOM UI, preferably a thin Leptos application, with generated JavaScript bindings only where required for browser APIs. Keep business operations and use cases outside UI components. Leptos supports client-side rendering; this avoids tying the workbench API to framework-specific server functions [S12]. A separate static documentation site can handle search-indexed public documentation.

Build the modern experience around clarity and speed: searchable operation palette, resizable panes, command palette, keyboard navigation, light/dark/high-contrast themes, responsive layouts, typed parameter forms, visible processing location, structured errors with byte offsets, side-by-side comparisons, and an inspectable provenance trail.

Keep large input out of reactive string state. The UI holds source/artifact handles and small windows. Use a paged hex viewer and virtualized text/record views. Provide accessible text/DOM alternatives and keyboard selection. Canvas or WebGPU may enhance specialized visualizations, but the entire application must not become an inaccessible painted bitmap.

The baseline is one real Dedicated Worker running a single-threaded Wasm engine. Add independent worker pools after measuring benefits. Treat shared-memory Wasm as an optional acceleration profile that needs cross-origin isolation and deployment headers; provide a non-shared-memory fallback [S17]. Thread capability must not determine whether ordinary decoding works.

Do not retain JavaScript views into mutable Wasm memory across calls that can grow or reuse it. Use ownership/lease rules and explicit copying or transferable buffers at well-defined boundaries. Untrusted plugins never share the privileged engine memory.

Use feature detection for file picking, range access, OPFS, persistence, and streaming export. Support normal file input and bounded fallback export when optional APIs are unavailable. A fallback may report a limit; it may not secretly upload data. Test Firefox explicitly alongside Chromium and WebKit because no single browser-specific file API should define the product.

The service worker caches application assets and installed packs, not arbitrary API responses or payload data. Updates are versioned and coordinated with open workspaces. An update must not replace a running worker's code underneath an execution. Allow users to retain a compatible offline version and export their work before a schema upgrade.

## 12. API contract and server execution

The public API starts during the first vertical slice and grows with every operation. Do not wait until the UI is complete to expose it. The browser workbench must use the same validation and execution semantics as the HTTP client.

Suggested initial resource structure:

| Route | Contract |
|---|---|
| `GET /api/v1/capabilities` | Supported operation revisions, limits, execution profiles, installed packs, and schema versions. |
| `GET /api/v1/operations` | Paginated/searchable descriptors, independent of UI categories. |
| `POST /api/v1/recipes/validate` | Typed validation with node/argument errors and missing capabilities. |
| `POST /api/v1/recipes/plan` | Explain execution location, required uploads, buffering, side effects, and limits. |
| `POST /api/v1/uploads` | Reserve quota and create an expiring, tenant-scoped upload session. |
| `PATCH /api/v1/uploads/{id}` | Bounded binary upload with checked offset, length, and integrity metadata. |
| `POST /api/v1/uploads/{id}/complete` | Verify/finalize an immutable input artifact. |
| `POST /api/v1/runs` | Submit a run; return 202 and an opaque run ID. |
| `GET /api/v1/runs/{id}` | Run state, progress, terminal error, and authorized artifact references. |
| `GET /api/v1/runs/{id}/events` | Bounded SSE stream with event sequence IDs and reconnect semantics. |
| `POST /api/v1/runs/{id}/cancel` | Idempotent cancellation request. |
| `GET /api/v1/artifacts/{id}` | Authorized binary download; defined range support and safe disposition. |
| `GET/POST /api/v1/recipes` | Optional saved recipe metadata and revisions. |
| `POST /api/v1/compat/cyberchef/import` | Untrusted recipe import without automatic execution. |
| `POST /api/v1/compat/cyberchef/export` | Export or a precise nonrepresentability report. |

Author a versioned OpenAPI contract and schema tests. Stable wire errors have machine-readable codes, safe messages, node/parameter locations, byte offsets where meaningful, retryability, and a correlation ID. Internal provider errors, paths, stack traces, secrets, and SQL must not cross the API boundary.

Use JSON for control metadata and binary bodies for artifacts. A small explicitly bounded inline-input convenience form is acceptable; large Base64-in-JSON payloads are not the data path. Preserve parameter types and large integers. Reject duplicate/conflicting control fields and unknown security-critical enum values.

Run state is explicit: submitted → validating → queued → running/paused → succeeded, failed, cancelled, or expired. Define races between cancellation and completion. A successful response is published only after output manifests are committed. Progress reflects observed input or phases; unknown total work is shown as indeterminate rather than a fictional percentage.

Scope idempotency keys to the principal/workspace and request fingerprint. Duplicated submission cannot create duplicate intended work. Worker retries are at-least-once; do not claim exactly-once external HTTP side effects. Side-effecting operations need an explicit retry policy and cannot be auto-replayed blindly.

Separate the control-plane server from execution workers. Initially support remote execution on a hardened Linux worker host: non-root identity, restricted filesystem, no inherited application secrets, network disabled unless separately granted, process-level memory/CPU limits, and supervisor-enforced deadlines. The API process never runs arbitrary high-cost operation bodies on its request loop.

## 13. Database independence as a tested capability

Start with PostgreSQL, but do not put database types or SQL into the application model. Use use-case-shaped repository methods rather than a generic `execute_sql` facade or an ORM entity model shared throughout the application.

Representative contracts include `load_recipe_revision`, `save_recipe_revision(expected_revision, ...)`, `list_visible_recipes`, `grant_share`, `revoke_share`, `reserve_upload`, `claim_run_lease`, `renew_run_lease`, `commit_run_result`, `append_audit_event`, and `mark_artifacts_for_expiry`.

Specify semantics before writing SQL: authorization scope, transaction boundary, consistency, stable ordering, pagination, optimistic concurrency, idempotency, retryable conflict behavior, unique constraints, and lease fencing. Multiple repository operations that must commit atomically are an application unit of work or a single explicit atomic command, not unrelated method calls disguised by an interface.

Logical metadata model:

```text
principals / workspaces / memberships
recipes / recipe_revisions / recipe_tags
shares / share_grants / revocations
runs / run_leases / run_events
uploads / artifacts / artifact_references
outbox / audit_events / schema_migrations
```

Keep payload bytes out of PostgreSQL by default. A small embedded artifact mode may exist for tests, not as an accidental large-file architecture. Operation computation must not depend on PostgreSQL functions, JSONB queries, row-level security, stored procedures, or notifications.

PostgreSQL-specific indexes or row-level security may be additional defenses/optimizations behind the adapter. They are not the only implementation of application authorization or correctness. Polling/outbox correctness must work without LISTEN/NOTIFY.

Choose portable logical types: application-generated IDs with documented encoding, UTC timestamps with explicit precision, checked integer ranges, boolean semantics, canonical recipe documents, and deterministic comparison rules. Specify collation and case-folding; do not let one backend's case-insensitive default redefine recipe uniqueness. Do not assume PostgreSQL and MySQL treat JSON, NULL, timestamps, sequences, upserts, DDL rollback, or isolation identically.

Use separate, versioned backend migrations under `migrations/postgres` and later `migrations/mysql`. A shared application schema version maps to both. Prefer expand/migrate/contract changes, with compatibility windows and restore plans. Keep migration tools separate from request-serving code and use a narrowly privileged database identity at runtime.

Before 1.0, implement a MySQL **portability proof adapter** covering the entire repository conformance suite, even if MySQL is not advertised as a production-supported deployment yet. A second in-memory fake does not prove relational portability. Run the same tests for authorization, concurrency, lease fencing, pagination, transaction failure, data limits, and export/import on both real databases.

The practical migration workflow is maintenance-window export first: freeze writes; produce a versioned logical export and artifact manifest; import into the target adapter; verify counts, entity digests, references, permissions, timestamps, and representative recipe replays; switch configuration; retain a tested rollback path. Zero-downtime dual-write migration is a separate later feature, not a prerequisite for meeting the user's request.

### Cross-store consistency

There is no ordinary single transaction covering an external artifact store and the SQL database. Use staged immutable objects, a database manifest/state transition, an outbox, and an idempotent reconciler. Publish only completed referenced artifacts; garbage-collect orphans after a grace period. Workers include a fencing token in completion so a stale lease cannot overwrite a newer result.

## 14. Vef and Brynja migration boundaries

Keep HTTP and TLS independently replaceable. Do not fuse them into one interface named after the current framework. Keep their abstractions in the project initially; do not force unfinished sibling crates into the required dependency graph.

| Boundary | Initial implementation | Future replacement |
|---|---|---|
| Inbound HTTP routing/transport | Axum/Hyper adapter | Project-owned Vef adapter. |
| Native outbound HTTP | A single Hyper-based/selected client adapter | Vef client adapter. |
| Native TLS client/server | Rustls adapter | Brynja adapter. |
| PostgreSQL TLS | `tokio-postgres` TLS extension implementation | Brynja-backed implementation of the same database-specific boundary. |
| Browser fetch and browser HTTPS | Browser platform | Remains browser-owned; not replaced by a Wasm TLS library. |
| Forensic HTTP/TLS artifact parsing | Analysis operation/provider | May reuse suitable Vef/Brynja parsing primitives after conformance review; never inherits connection policy automatically. |

`tokio-postgres` explicitly accepts external TLS implementations [S14]. This makes it a useful starting driver for the requested TLS migration. Still test PostgreSQL negotiation, certificate identity, and channel-binding behavior; do not blindly wrap a PostgreSQL TCP connection in TLS before its required negotiation.

The HTTP boundary defines bounded request/response metadata, streaming bodies, cancellation, deadlines, limits, disconnects, proxy trust, header handling, and SSE semantics. Business authorization, upload policy, quotas, and idempotency live above it. Do not make Axum extractors or Tower layers the sole home of indispensable business rules.

All native outbound consumers use one policy-aware boundary: user HTTP operations, DNS-over-HTTPS, identity-provider metadata, key retrieval, and optional object-store integrations. A third-party SDK with its own hidden HTTP/TLS client must be isolated and documented as an adapter replacement risk. Browser API calls are a separate host implementation, not a bypass of browser security.

TLS configuration uses provider-independent policy: trusted roots, certificate identity requirements, client authentication, protocol policy, ALPN, session behavior, timeouts, certificate reload, and nonsecret diagnostics. Provider-specific cipher or verifier types do not leak into recipes or public HTTP schemas. Preserve fail-closed behavior and prevent downgrade/fallback during migration.

A forensic parser may inspect malformed or historical records to explain them. A live TLS endpoint must not become permissive merely because an analysis operation can decode such records. Historical algorithms in the workbench are isolated from transport security policy.

Migration gates are contract tests, not compilation alone: request framing and smuggling cases; streaming/backpressure; disconnect cleanup; response limits; redirects and destination policy; certificate names/expiry/trust; ALPN; mTLS; database TLS; and browser behavior against either native server stack. If Vef/Brynja are still unavailable, mock adapters verify the boundary and the current stack remains supported. Their release dates do not block 1.0.0.

## 15. Extensibility and heavyweight features

First make adding a trusted Rust operation easy: one implementation, a descriptor, conformance vectors, a resource declaration, documentation, and a registration entry. A scaffold command generates the files and a failing completeness test. Adding an operation must not require hand-editing API routes, web forms, CLI parsing, and help text independently.

Separate operation packs by capability and size: core encodings, text, structured formats, modern crypto, legacy crypto, archives, forensics, and media. Keep a small default browser boot bundle; make large packs installable and available in the offline distribution. Feature combinations must be tested, and missing packs must have explicit diagnostics.

Support untrusted extensions only after the core contract is mature. Start with a versioned core-Wasm ABI, isolated memory, a small import allowlist, bounded host calls, resource handles rather than process pointers, and host-enforced time/memory limits. Native execution uses a reviewed Wasm runtime or an isolated process. Wasm memory isolation is valuable, but runtime configuration and imported capabilities still determine what a guest can do [S18].

For browsers, a trusted host creates a separate worker/instance. Do not accept arbitrary JavaScript plugin bootstraps with application-origin privileges. Terminate runaway workers. Validate plugin metadata, decompressed size, exported ABI, imported functions, integrity, and publisher identity. A signature identifies an artifact; it does not prove the code is safe.

Add a WIT/component-model adapter after it passes browser/native tests. Component tooling may generate JavaScript shims; inspect and package those as trusted application assets. Do not assume direct native browser support for component binaries [S09].

Hard compatibility work is planned, not hidden. JavaScript/XRegExp semantics differ from a fast Rust regex engine, whose documentation explicitly excludes some constructs [S19, S20]. Keep a fast, bounded native regex profile and a separately specified compatibility execution profile. Likewise, Jq, JSONata, XPath, YARA, public-key formats, OCR, and disassemblers each require real language/format coverage, not an operation with a matching title.

Prefer Rust implementations and Rust providers for the engine. A non-Rust runtime or external executable would be a documented scope exception requiring an explicit project decision; this plan does not silently introduce one to claim Rust parity. If a required Rust implementation is immature or missing, extend pre-1.0 development and implement/qualify it rather than calling a partial subset complete.

## 16. Security model

Treat inputs, recipes, imported parameters, file names, archives, query expressions, plugins, and rendered outputs as untrusted. Local execution still processes attacker-controlled files; optional remote execution adds cross-user and host-security risks.

Default product policies:

- No network, filesystem, secret, clipboard, or arbitrary code capability unless granted for that operation/run.
- No application HTML from raw operation output. Use typed rendering, sanitization where required, and isolated document/media previews without ambient credentials or network fetches.
- No automatic recipe execution after importing a link/file. Show operations, external requests, required secrets, expensive work, and data movement first.
- No payloads, keys, request bodies, query contents, or decoded outputs in normal logs, metrics labels, URLs, analytics, traces, or crash reports.
- No global cache or artifact lookup that lets one tenant infer another tenant's content.
- No bypass of user authorization merely because an opaque identifier is hard to guess.

For native network operations, enforce destination policy both at name resolution and connection establishment. Cover loopback, private/link-local ranges, IPv6 representations, redirects, DNS rebinding, metadata-service addresses, credential forwarding, and response/decompression limits. Allow a deliberate private-network profile only in an operator-approved environment; do not turn a public service into a proxy [S21]. Browser-native fetch remains subject to browser restrictions and is not a raw arbitrary-HTTP transport.

Archive handling enforces total expanded bytes, nesting, entry count, per-entry size, path rules, symlinks/hard links, sparse-file behavior, duplicate names, and cancellation. A compression ratio threshold can be a warning or one layer of policy, but total resource budgets are authoritative.

Cryptographic operations use validated providers and explicit parameters. Separate modern recommendations from legacy analysis. Obtain production randomness only from host-provided secure entropy. Never commit or expose unauthenticated decrypted plaintext as a successful result. Streaming authenticated decryption may require bounded spooling until final authentication succeeds; that cost belongs in the execution plan.

Prefer no unsafe code in first-party orchestration, parsing glue, authorization, and metadata layers. When a performance/provider boundary requires unsafe code, isolate it, document invariants, and test it separately. A first-party `forbid(unsafe_code)` attribute does not make transitive dependencies unsafe-free.

Optional accounts use a standard identity-provider integration or another reviewed authentication design rather than a new authentication protocol. Cookie-based sessions need origin/CSRF defenses and secure cookie configuration. Native clients after 1.0 receive an appropriate separate authorization flow; do not reuse browser session secrets by copying them into URLs or local storage.

Retention, export, deletion, audit trails, and deployment documentation should support operator privacy obligations. Do not claim that a software feature checklist automatically confers legal compliance or certification.

## 17. Testing and performance gates

Every feature release has implementation, documentation, conformance, negative input, resource/cancellation, target, dependency, and security-impact evidence. Operation releases additionally need chunk-boundary invariance, empty/truncated input cases, all declared options, and browser/native agreement. These gates apply before the final hardening phase.

Use unit tests, property tests, fuzzing, reference differentials, adversarial parsers, browser end-to-end tests, real-database conformance, crash injection, and performance regression tests. Apply Miri to suitable unsafe boundaries and model/property tools to small critical algorithms when useful. Keep independent security review and production-like isolation tests before 1.0.

Important test examples: Base64 padding split across calls and data after padding; UTF-8 split inside a character; all possible chunk sizes around a cipher block; zero-capacity output; tiny graph queues; a join with one failed input; a revoked artifact grant during a run; cancellation during final authentication; stale worker lease completion; quota failure during a manifest commit; and a provider crash after creating temporary output.

The following are **initial engineering targets**, to confirm or revise through measured ADRs—not performance claims about an existing implementation:

| Area | Initial target / policy |
|---|---|
| Auto-run preview | At most 64 KiB of sampled input by default; full execution is explicitly distinguishable. |
| Interactive preview storage | A bounded byte window, never a full reactive text copy. |
| Browser engine budget | 128 MiB tracked working-memory profile initially; separate accounting for UI/browser overhead and large-operation profiles. |
| Hosted worker budget | An initial 512 MiB job profile with externally enforced limits; heavier profiles require explicit admission. |
| Graph safety | Initial policy ceilings of 512 nodes and 2,048 edges, plus aggregate work/loop/output budgets. |
| Cancellation | Target p95 cooperative response below 200 ms on the reference corpus; terminate non-cooperative work using a separate hard deadline. |
| UI responsiveness | Target p95 interactions below 100 ms while supported background workloads run on the reference devices. |
| Large-file streaming | Demonstrate a 10 GiB native fixture and a browser fixture beyond Wasm linear-memory size using bounded source/output windows where storage permits. |
| Browser support | Current supported Chromium, Firefox, and WebKit configurations, with documented baseline and optional-feature profiles. |
| Bundle size | Record compressed shell/core and each optional pack; establish a regression budget after the first real vertical slice. |

Use explicit hardware/browser versions, operation options, source/destination types, and peak-memory methodology in benchmarks. Compare cold/warm cache, small/large inputs, successful/error paths, and single/multiple workers. Rust, Wasm, WebGPU, and SIMD are implementation choices, not automatic evidence of superior performance.

## 18. Definition of 1.0.0

Release 1.0.0 only when the pinned compatibility inventory is accounted for and no required capability remains a gap; the native recipe format and public API are frozen and documented; browser-local privacy and offline operation are proven; resource limits and cancellation are enforced; output rendering and extension boundaries pass adversarial testing; PostgreSQL is operationally qualified; the MySQL conformance proof demonstrates portability; and HTTP/TLS replacement tests demonstrate the Vef/Brynja seams.

Also require upgrade/migration/restore drills, package integrity and SBOMs, dependency/license review, accessible core workflows, supported browser results, representative performance evidence, security review findings triaged and remediated, and documented retention/deletion behavior. No unresolved critical/high-risk exploitable finding belongs in the default production profile.

Desktop/mobile application code does not need to be built before this gate. Their future needs are covered by stable services, artifact handles, local/native engine portability, version negotiation, and transport-independent contracts. A CLI and headless worker before 1.0 are developer/automation interfaces, not a commitment to ship desktop or mobile applications early.

After 1.0: desktop client preview and platform adapters, desktop general availability, mobile remote-client preview, mobile sharing/file/secure-storage integration, and qualified offline mobile operation. Capability negotiation can explicitly limit a mobile device; it must not change recipe semantics or silently offload data.

## 19. First implementation slice

Make 0.1.0 concrete: pinned Rust workspace, a tiny no_std transformation kernel, one operation (hex encode/decode is enough), a browser worker invocation, one application service contract, a versioned recipe document, a reference fixture, and a build/test pipeline. This proves the central boundary rather than producing only folders and interfaces.

By 0.15.0, demonstrate a small useful browser workbench, a loopback-only API, parameter metadata, deterministic encoding operations, cancellation, malformed-input handling, operation registration, and the complete upstream inventory/risk plan. Remote/public exposure is still gated on the later authentication, quota, and worker-isolation work.

Work on the next release and its stated prerequisites. Do not simultaneously implement all 240 releases. At each tag, update the parity matrix, dependency report, threat model, known limitations, and release evidence. Large capability rows must be split into additional releases when their sub-language, formats, or provider qualification cannot honestly fit a single tested increment.

## 20. Source register

URLs are included as code-form references for offline traceability. Access/review date: 2 October 2026. The Git tag is the initial reference; resolve its commit and preserve source hashes in the implementation repository. No complete operation-by-operation differential suite was executed as part of writing this plan.

- **S01 — Rust 1.99.0 announcement:** `https://blog.rust-lang.org/2026/10/01/Rust-1.99.0/`
- **S02 — CyberChef reference package:** `https://raw.githubusercontent.com/gchq/CyberChef/v11.5.0/package.json`
- **S03 — CyberChef reference categories:** `https://raw.githubusercontent.com/gchq/CyberChef/v11.5.0/src/core/config/Categories.json`
- **S04 — CyberChef moving-branch categories, reviewed separately:** `https://raw.githubusercontent.com/gchq/CyberChef/master/src/core/config/Categories.json`
- **S05 — CyberChef Jump semantics:** `https://raw.githubusercontent.com/gchq/CyberChef/master/src/core/operations/Jump.mjs`
- **S06 — CyberChef worker integration:** `https://raw.githubusercontent.com/gchq/CyberChef/master/src/web/Manager.mjs`
- **S07 — wasm-bindgen-futures spawn_local:** `https://docs.rs/wasm-bindgen-futures/latest/wasm_bindgen_futures/fn.spawn_local.html`
- **S08 — IndexedDB transaction completion:** `https://developer.mozilla.org/en-US/docs/Web/API/IDBTransaction/complete_event`
- **S09 — Component Model in JavaScript/Jco:** `https://component-model.bytecodealliance.org/language-support/importing-and-reusing-components/javascript.html`
- **S10 — CyberChef HTTP request:** `https://raw.githubusercontent.com/gchq/CyberChef/v11.5.0/src/core/operations/HTTPRequest.mjs`
- **S11 — Rust no_std:** `https://doc.rust-lang.org/embedded-book/intro/no-std.html`
- **S12 — Leptos rendering and browser bindings:** `https://book.leptos.dev/` and `https://book.leptos.dev/web_sys.html`
- **S13 — Axum:** `https://docs.rs/axum/latest/axum/`
- **S14 — tokio-postgres TLS extension boundary:** `https://docs.rs/tokio-postgres/latest/src/tokio_postgres/lib.rs.html`
- **S15 — Rustls:** `https://docs.rs/rustls/latest/rustls/`
- **S16 — OPFS:** `https://developer.mozilla.org/en-US/docs/Web/API/File_System_API/Origin_private_file_system`
- **S17 — SharedArrayBuffer isolation:** `https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer`
- **S18 — Wasmtime security model:** `https://docs.wasmtime.dev/security.html`
- **S19 — Rust regex limits:** `https://docs.rs/regex/latest/regex/`
- **S20 — CyberChef regular-expression semantics:** `https://raw.githubusercontent.com/gchq/CyberChef/v11.5.0/src/core/operations/RegularExpression.mjs`
- **S21 — OWASP SSRF prevention:** `https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html`
- **S22 — CyberChef workbench features:** `https://raw.githubusercontent.com/gchq/CyberChef/master/README.md`
- **S23 — CyberChef YARA operation:** `https://raw.githubusercontent.com/gchq/CyberChef/v11.5.0/src/core/operations/YARARules.mjs`
- **S24 — CyberChef PDF preview operation:** `https://raw.githubusercontent.com/gchq/CyberChef/v11.5.0/src/core/operations/RenderPDF.mjs`
- **G01 — User-supplied Gemini draft:** `Pasted text(20261002-183143).txt`, 2,856 source lines, supplied in this conversation.
