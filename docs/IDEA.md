I want to build a modern website that is similar as CyberChef (https://github.com/gchq/CyberChef) but feels more 2026 but it should contain all the same functionalities and easy to add even more. It should be build in rust newest version 1.99.0 as of today. it should be API driven so we can easy build later on desktop apps and mobile apps (we should plan for this but this is for after 1.0.0)

We should try to limit the usage of external crates and if possible where we can be no std.

Make a very good version plan starting at 0.1.0 and go as high as you need does not matter if we end up into 0.500.0 etc but 1.0.0 will be the full release. desktop apps and mobile apps will come later based on the api.

I want you to try to make it also database independend maybe we start with postgresql for now but in future we maybe want to move to mysql or another database so it should be written in a way we can convert without a huge rewrite.

I also want you to be ready that all web and tls related thing in future can be easily migrated to ../vef and ../brynja when those crates are ready.

So the goal is a modern take on cyberchef with latest coding technology.

see attached the plan we made with gemini but take it with a grain of salt it maybe started to go into hallucination mode so take what is interesting and then build your own perfect plan.
…
Worked for 25m 15s

I would build this as a local-first, API-driven data-transformation workbench, with a reusable Rust engine underneath—not as a website whose processing is inseparable from its frontend or server.

That distinction is what will make PostgreSQL replaceable, Vef/Brynja integration manageable, and later desktop/mobile applications possible without rebuilding the product.

You are also correct about the compiler: Rust 1.99.0 was released on 1 October 2026. I would pin it initially rather than build against a moving stable toolchain.
The complete plan

I have written the architecture and 240 individually specified pre-1.0 releases, each with a deliverable and acceptance check.
Document	Contents
Complete planning bundle	All documents and the machine-readable roadmap.
Architecture	Engine, website, API, operations, storage, databases, Vef/Brynja boundaries, security and testing.
Version roadmap	Every release from 0.1.0 through 0.240.0, followed by release candidates, 1.0.0 and later application milestones.
Parity and risk register	Compatibility requirements, difficult implementation areas and evidence needed before declaring completion.
Machine-readable roadmap	Release objectives, acceptance checks, phase assignments and default dependencies.

The numbers are an initial work breakdown, not a ceiling. An unfinished capability means another 0.x release—not quietly moving that capability past 1.0.0.

The main architectural decisions follow.
1. What I would keep—and replace—from Gemini’s plan

The useful ideas are bounded streaming, optional graph editing, intermediate-result reuse, extensible operations and paged viewers. Those are worth retaining. The draft explicitly proposes these concepts, but its examples do not consistently deliver the guarantees claimed for them.

I would not use the supplied implementation as starter code.
Issue	Why it matters	Replacement
spawn_local is presented as isolating processing from rendering.	It runs the future on the current thread; it does not create a Web Worker.	Put the engine inside an actual Dedicated Worker.
The graph construction drops required wiring.	The example removes input receivers without inserting them into the node, and drains outputs belonging to other nodes.	A separately validated graph compiler and tested connection ownership.
The cache reads the complete input before checking for a hit.	That defeats the claimed bounded streaming behavior for unknown input streams.	Cache lookup from known immutable input identities; otherwise stream/hash/spool under explicit limits.
“Zero-copy” is used as a blanket description.	The XOR example explicitly copies the input into a new vector.	Treat copying as a measured, budgeted implementation detail.
A pure DAG is proposed as the whole recipe model.	CyberChef supports backward jumps, so a DAG-only engine cannot preserve all recipe behavior.	Acyclic dataflow regions plus explicitly bounded control flow.

The worker correction follows the official spawn_local documentation. The wiring, buffering and copying problems are visible directly in the supplied examples.

Also, I would not position the project on the premise that CyberChef has no worker architecture: its current source already initializes input, processing and background workers. Improvements need to be demonstrated through actual measurements, not inferred from “JavaScript versus Rust.”

The new product should promise predictable behavior, inspectable execution and clear security boundaries—not universal zero-copy, constant memory or automatic speedups.
2. The product boundary
Local processing remains the default

“API-driven” should not mean “everything must be uploaded.”

I would support three deployment/use modes:
Mode	Processing	Persistence
Local browser	Rust/Wasm in browser workers.	Memory by default; optional local workspace storage.
Self-hosted workbench	Local browser processing, with optional server execution.	PostgreSQL metadata and a separate artifact store when enabled.
Remote API client	Explicitly submitted server jobs.	Server-controlled retention, permissions and quotas.

Normal decoding, inspection and recipe execution should not require an account or database.

The interface should always show where processing happens. When a user chooses server execution, it should show which inputs will leave the device. An unsupported browser feature must never cause silent upload as a fallback.

For functionality that already inherently involves networking, such as an HTTP-request operation, that capability must remain explicit. CyberChef itself marks its HTTP operation for manual execution and uses browser Fetch behavior.
One application contract, several transports

The same conceptual interface should support:
Browser UI
    │
    ├── Local engine client ── worker messages ── Rust/Wasm engine
    │
    └── Remote engine client ── HTTP API ──────── native Rust engine

Later:
Desktop application ── same application contract ── local or remote engine
Mobile application  ── same application contract ── local or remote engine

This does not require serializing every local function call into JSON. Shared semantics matter; identical transport mechanics do not.
3. Architecture and crate boundaries

I would start with a modular monolith and a separate execution-worker executable. There is no need to introduce microservices, a message-broker cluster or a general distributed workflow system.

The dependency direction should be inward:
Website / API / future applications
                  │
         Application services
                  │
       Recipe compiler and runner
                  │
     Operation contracts and typed data
                  │
      Rust operations / provider interfaces

Outer adapters:
browser • native runtime • HTTP • TLS • database
artifact storage • randomness • clock • diagnostics

Suggested logical boundaries:
Boundary	Responsibility
workbench-types	IDs, lengths, limits, error codes and fundamental types.
workbench-operation	Operation descriptors and execution contracts.
workbench-recipe	Recipe representation, validation, compilation and migrations.
workbench-engine	Scheduling, budgets, cancellation and run state.
workbench-application	Use cases shared by local and remote clients.
workbench-api-model	Wire representations and schema mappings.
workbench-ops-*	Operation families: encoding, text, formats, crypto, archives, forensics and media.
workbench-compat-cyberchef	Recipe import/export and compatibility behavior.
Adapter packages	Browser APIs, native runtime, PostgreSQL, storage, HTTP and TLS.

These are ownership boundaries, not an instruction to create dozens of empty crates immediately. Start small and extract packages as there is real code to isolate.

The most important rule is:

    Core operation and application types must not expose Axum requests, PostgreSQL rows, Rustls configurations, Tokio handles or Leptos signals.

Otherwise, the purportedly replaceable infrastructure becomes part of the application’s public design.
Practical no_std

I would use three levels:
Level	Suitable components
no_std, no allocation	Fundamental types, limits and fixed-buffer transformations.
no_std + alloc where practical	Recipe representation, compilation and larger operation state.
Host-dependent code	Browser integration, UI, server, database, networking and heavyweight providers.

no_std and allocation-free are separate properties; a Wasm build alone does not demonstrate either.

The target should be minimal, justified dependencies, not an artificial zero-dependency claim for the entire application.

Own the small transformations, recipe semantics and security boundaries. Use reviewed Rust providers where reimplementing cryptography, decompression or complex parsing would increase risk.
Initial stack

My initial implementation choice would be:

Leptos client-side UI → browser workers → Rust engine, with Tokio + an Axum/Hyper adapter, Rustls, and tokio-postgres on the native server.

Those remain outer-layer choices, not foundational application dependencies. Leptos/browser integration still requires browser bindings; “written in Rust” should not be advertised as literally requiring no JavaScript bridge.

Exact dependency versions should be selected and locked after testing the Rust 1.99.0 target matrix. I have not invented a supposedly validated combination of latest crate versions.
4. The engine: bounded execution rather than “everything streams”

The engine needs to understand what kind of work an operation performs.
Execution class	Example	Required behavior
Streaming transform	Base64, XOR, many framing conversions.	Bounded carry state and partial input/output handling.
Reduction	Hashing, byte histogram, global entropy.	Small running state, result finalized at EOF.
Bounded window	Selected parsers and matchers.	Explicit maximum window.
Seekable/two-pass	Reversing a large file, certain archive operations.	Range access or a controlled spool.
Whole-input bounded	A provider requiring a complete syntax tree.	Admission checks and a declared size ceiling.
Capability-dependent	HTTP requests, randomness, clock access.	Explicit host permissions and replay/cache policy.

A large-file architecture must be honest about whole-input operations. It is better to report:

    “This operation requires a complete document and exceeds the selected memory profile.”

than to advertise streaming while allocating the complete input internally.
Buffer contract

At the portable-kernel level, I would use a contract conceptually like:
step(input_window, output_window, budget)
    → consumed bytes
    → produced bytes
    → NeedInput / NeedOutput / Yield / Finished

This allows caller-owned buffers and avoids forcing a particular external buffer crate into every operation.

An operation must define empty input, partial consumption, EOF, trailing data, failure and cancellation behavior. In-place mutation can be an optimization when ownership permits it; correctness must not depend on that optimization.

Transport chunks must not define data semantics. Processing a file in 64 KiB chunks versus 1 MiB chunks must not change the result.
Scheduling and cancellation

I would initially use a deterministic cooperative scheduler, rather than creating a Tokio task for every node.

The browser runs that scheduler in a real worker. The native host runs jobs in isolated worker processes where appropriate.

Cancellation needs both cooperative checkpoints and a hard-stop mechanism. A cancelled run must not later publish a successful artifact. Old UI generations must not overwrite newer results.

For multi-input operations, key/configuration material must be frozen before dependent processing starts, unless the operation explicitly defines synchronized streaming inputs. Scheduling races must never determine cryptographic or transformation semantics.
Recipes need more than a DAG

CyberChef’s Jump operation explicitly supports forward and backward movement. Therefore, full compatibility needs bounded loops or an interpreter capable of reproducing that behavior.

My proposed model is:

Simple linear recipes by default → optional dataflow graphs → explicit bounded control-flow regions.

Use a small compatibility interpreter where translating a CyberChef recipe into structured regions would otherwise lose behavior.

Bound total work, nested loops, recursion, output growth and expanded records—not only the iteration count of one loop.
5. Data representation and caching
Do not make everything a string

The engine should distinguish bytes, explicitly encoded text, records, structured values, tables, media and collections of artifacts.

That matters for binary correctness, large files and later API clients.

For example, an archive operation should return a collection of named artifact references—not one giant text string and not arbitrary paths to write into the host filesystem.

The UI should hold artifact handles and small viewing windows, not copies of complete files inside reactive string state.

Secrets should use separate references and sensitivity metadata. Derived outputs should retain that sensitivity unless an explicitly reviewed rule removes it.
Cache completed, deterministic work

Cache identity should include:
operation ID and semantic revision
canonical typed parameters
ordered input ports and immutable input identities
compatibility/text settings
relevant provider and data-table versions

Changing an operation’s default, Unicode tables or provider behavior can affect reproducibility even when its Rust API remains unchanged.

Unknown streams cannot have their final content digest known before being read. Therefore, cache reuse may still require reading and hashing input. When an immutable artifact identity already exists, lookup can happen before computation.

I would make persistent intermediate caching opt-in, with secrets, decrypted data and effectful operations excluded by default.

Cache writes should go through staging and publish a complete manifest only after successful completion. A cancelled or failed operation must never leave an apparently valid cache entry.

Browser persistence also needs transaction-completion handling: an individual IndexedDB request succeeding is not the same event as its transaction successfully committing.
6. Making operations easy to add

This is where a modern design can remove substantial maintenance work.

Each operation should have one authoritative descriptor containing its stable ID, semantic revision, argument schema, defaults, port types, execution class, required capabilities, sensitivity behavior, limits, help and examples.

From that descriptor, generate the catalogue, parameter forms, API schemas, documentation and common validation tests.

Adding an operation should normally involve:
implementation
+ descriptor
+ conformance fixtures
+ resource/security tests

It should not require editing the scheduler, adding bespoke API routes, changing the database schema and separately rebuilding a form.
First-party operations first, untrusted plugins later

Start with ordinary Rust operation modules and statically registered packs. Add lazy-loaded browser packs as the catalogue grows.

Third-party Wasm plugins come later in the pre-1.0 roadmap, behind a narrow ABI with separate memory, allowlisted imports, explicit capabilities and enforceable resource limits.

I would not make arbitrary Component Model binaries a day-one browser assumption. The official JavaScript integration documentation includes tooling and composition steps; this needs an actual tested adapter, not merely a WIT definition in the plan.

Nor should a signed plugin automatically be considered safe. Its signer and its permitted behavior are different questions.
Difficult compatibility must be investigated early

For example, CyberChef’s regular-expression operation uses XRegExp, while Rust’s regex documentation explicitly excludes constructs such as lookaround and backreferences. A superficially similar regex operation is not sufficient evidence of parity.

The same principle applies to query languages, YARA, OpenPGP variants, historical ciphers, OCR and disassembly.

That is why 0.12.0 is a hard-feature feasibility release. It must identify actual implementation strategies and gaps before the project has accumulated hundreds of operations around incorrect assumptions.
7. Database independence that is actually testable

I would make PostgreSQL the first production backend, but keep the application’s storage contract independent of SQL syntax and driver types.
Separate metadata from bulk artifacts

PostgreSQL should primarily hold recipes, revisions, ownership, permissions, job state, manifests and retention metadata.

Large input/output payloads should normally live behind a separate artifact-storage interface: local disk initially, with other backends later.

That avoids turning every large-file transformation into a database-blob workload.
Use application-shaped repository methods

Useful contracts look like:
load_recipe_revision(...)
save_recipe_revision(expected_revision, ...)
list_visible_recipes(...)
claim_run_lease(...)
commit_run_result(fencing_token, ...)
revoke_share(...)

They should not look like a generic execute_sql(...) interface pretending to provide portability.

Each method needs defined transaction, ordering, concurrency and authorization semantics. The PostgreSQL adapter implements those semantics using PostgreSQL; a later MySQL adapter implements the same semantics using MySQL.

SQL optimizations can remain backend-specific. Application correctness must not depend on a PostgreSQL-only feature.
Why I would consider tokio-postgres here

Your future Brynja requirement makes the database TLS boundary important. tokio-postgres explicitly accepts an external TLS implementation, providing a useful integration point instead of permanently embedding one TLS choice in the application.

This is a reason for the initial driver choice—not a claim that the driver itself makes database migration automatic.
Prove portability before 1.0

I would implement an actual MySQL proof adapter before 1.0, even while PostgreSQL remains the only initially production-supported deployment.

The same repository tests must run against both real databases, covering uniqueness, collation, timestamps, JSON values, pagination, transactions, revision conflicts and worker leases.

Then perform a migration drill:
Freeze writes
    → export portable logical records and artifact manifests
    → import into the other backend
    → verify counts, hashes, references and permissions
    → replay representative recipes
    → switch configuration
    → retain a tested rollback path

Moving databases will still require an adapter, migrations and qualification. The promise is that it does not require rewriting the engine, API, UI or authorization model.
8. Preparing for ../vef and ../brynja

I would keep HTTP and TLS as two independent replacement boundaries.
Area	Initial implementation	Future boundary
Incoming HTTP/API serving	Axum/Hyper adapter.	Vef server adapter.
Native outgoing HTTP	Controlled HTTP gateway.	Vef client adapter.
Incoming native TLS	Rustls provider.	Brynja server-side TLS adapter.
Outgoing native TLS	Rustls provider.	Brynja client-side TLS adapter.
PostgreSQL TLS	Replaceable database connector.	Brynja-compatible connector, when qualified.
Browser HTTPS	Browser networking stack.	Remains browser-controlled.

The last row is important: compiling Brynja to Wasm does not replace the browser’s HTTPS implementation used by Fetch. The browser integration uses browser APIs; the native server and native clients are the parts under your transport control.

I would also inventory less obvious native TLS consumers: identity-provider metadata, signing-key retrieval, object storage and user-request operations. Otherwise, the main HTTPS listener gets migrated while several transitive clients remain locked to the old stack.

The replacement tests must cover trust configuration, hostname verification, ALPN, limits, timeouts, shutdown and error mapping—not just whether a connection succeeds.

No imaginary Vef/Brynja APIs should be embedded now. Establish application-owned interfaces and conformance tests first. Add actual sibling adapters when those repositories expose usable, qualified APIs. The default build should remain usable without their directories.
9. What makes the website feel modern

I would preserve the fast operation-list → recipe → input/output workflow, rather than force every user into a node graph.

The improvements should center on daily work: a command palette, keyboard-first editing, resizable panes, typed parameter forms, multiple inputs, undo/redo, useful error locations and clearly visible execution location.

Large output should have paged hex/text views, structured tree/table views and explicit intermediate-result inspection. Breakpoints and single-step execution should remain useful even when earlier nodes are cached.

The graph editor becomes an optional advanced view for branches, joins and reusable subrecipes.

Canvas or WebGPU can help specialized visualizations, but neither should be required for the basic application. Core workflows need accessible DOM controls and keyboard alternatives.

For “Magic,” I would use bounded, explainable transform suggestions: evidence, candidate results and reproducible ranking. Suggestions should not automatically execute networking or expensive searches. An opaque AI feature is not necessary to deliver a modern workbench.
10. Version plan

The downloadable roadmap contains every release individually. This is the overall structure:
Versions	Workstream	Required outcome
0.1.0–0.15.0	Foundations and vertical slice.	Real browser/native execution, first UI/API, inventory and early risk investigation.
0.16.0–0.30.0	Bytes, text and encodings.	Correct common operations and explicit text semantics.
0.31.0–0.45.0	Streaming, artifacts and execution.	Resource accounting, joins, cancellation, storage and cache correctness.
0.46.0–0.60.0	Browser workbench.	Modern editing, viewers, debugging, sharing and offline packaging.
0.61.0–0.75.0	API, PostgreSQL and server security.	Optional remote execution with authentication, authorization and isolated workers.
0.76.0–0.90.0	Structured formats and queries.	Format conversions, query dialects, code/text utilities and numeric correctness.
0.91.0–0.105.0	Compression and archives.	Required formats with expansion, integrity and extraction controls.
0.106.0–0.120.0	Modern crypto and hashes.	Qualified providers, typed secrets and authenticated-output handling.
0.121.0–0.135.0	Legacy crypto and classical ciphers.	Long-tail compatibility without weakening application security.
0.136.0–0.150.0	Public keys, certificates and tokens.	Required parsing, key, signature, OpenPGP and token workflows.
0.151.0–0.165.0	Network and forensic operations.	Passive analysis, controlled network effects, YARA and disassembly.
0.166.0–0.180.0	Images, media and previews.	Required codecs, transforms, recognition and presentation behavior.
0.181.0–0.195.0	Complete recipe compatibility.	Full control flow, import/export, Magic and end-to-end parity candidate.
0.196.0–0.210.0	Extensibility and infrastructure replacement.	SDK, packs, plugin boundaries and HTTP/TLS adapter proof.
0.211.0–0.225.0	Portability and operations.	Sharing, real MySQL tests, migration drills, backup and deployment qualification.
0.226.0–0.240.0	Release qualification.	Complete scope audit, security, accessibility, performance and recovery evidence.
Additional 0.x releases	Unresolved gaps.	Every remaining mandatory capability or qualification issue is closed.
1.0.0-rc.*	Exact-artifact verification.	Candidate builds pass the complete release checklist.
1.0.0	Full release.	Complete website and API; desktop/mobile remain later work.
The first 15 releases

These deliberately produce working software before the project expands into the full catalogue.
Release	Deliverable
0.1.0	Rust 1.99.0 workspace, tiny portable kernel, one hex operation, native execution and a real browser-worker invocation.
0.2.0	Immutable CyberChef reference capture, operation/argument inventory and reconciliation of current-source differences.
0.3.0	Operation IDs, semantic revisions, errors, recipe envelopes, artifact references and application contracts.
0.4.0	no_std/allocation/host boundaries and target-feature checks.
0.5.0	Fixed-buffer processing, partial progress, EOF and cancellation contracts.
0.6.0	Operation descriptors and generated catalogue/argument controls.
0.7.0	Linear recipes with explicit byte/text conversion and chunk-invariant execution.
0.8.0	Versioned worker protocol, progress events and stale-generation protection.
0.9.0	Cooperative cancellation plus worker termination/recovery.
0.10.0	Accessible input, recipe and output panes with operation search.
0.11.0	Loopback API for catalogue, validation, execution, status and cancellation.
0.12.0	Feasibility evidence for difficult providers and dialects—not assumed compatibility.
0.13.0	Differential/reference testing harness and fixture provenance.
0.14.0	Initial threat review of imports, rendering, workers, logging and dependencies.
0.15.0	Useful small offline-capable workbench, save/load, API examples and operation-development guide.

Public remote execution should remain disabled until the later authentication, quota and isolation gates pass.
11. What “all CyberChef functionality” must mean

I used v11.5.0 as a reviewed planning anchor, not as a claim that I have already audited every operation and argument. The current source also contains differences to reconcile—for example, a certificate-bundle parsing entry—which the plan explicitly includes in its initial scope review.

The first-stage inventory must capture a precise source baseline. Otherwise, “all functionality” becomes both unverifiable and permanently moving.

Compatibility must cover operation variants and defaults, byte/text conversions, malformed-input behavior, complete recipes, workbench features and execution targets.

Two rules are especially important:

A similarly named operation is not evidence of equivalent behavior.

A server-only implementation does not satisfy a capability that users expect to run locally in the browser.

Heavy operation packs may load on demand and be included in a complete offline bundle. They should not require uploading private inputs merely because the local implementation is difficult.

Historical algorithms should remain available as analysis tools under explicit policies. Their presence must never enable obsolete algorithms in account security, storage protection or TLS.
12. Security and release acceptance

Security work belongs in every release, not just 0.226.0 onward.

The default policy should prohibit automatic imported-recipe execution, raw output becoming trusted HTML, payload logging, cross-workspace artifact access and undeclared network effects.

Hosted execution needs restricted workers and job-wide limits for CPU, memory, output, temporary storage, nesting and match counts. Native HTTP operations need destination checks covering resolution, connection establishment and redirects, rather than a single superficial URL check.

Before 1.0, require the full parity evidence, browser/native conformance, API and recipe compatibility policy, security findings resolved, accessible workflows, backup/restore drills, actual database-portability tests and proven HTTP/TLS replacement boundaries.

Performance targets in the documents are proposed engineering targets, not measured achievements. The same applies to provider availability: creating this plan does not establish that every required Rust implementation is already mature or browser-ready. The early feasibility and conformance work is there to establish that evidence.
13. Desktop and mobile after 1.0

The proposed sequence is:
Milestone	Scope
1.1	Desktop preview using the existing application contract and engine.
1.2	Desktop stable, including filesystem permissions, secure credential storage and qualified updates.
1.3	Mobile preview with touch-oriented workflows and API execution.
1.4	Mobile stable with file/share integration and lifecycle recovery.
1.5+	Expanded qualified on-device capabilities and other additions.

These are product milestones, not reasons to break API v1. Client applications can have independent version numbers while using the same recipe and operation contracts.

My central recommendation is to make 0.1.0 prove the shared engine, 0.2.0 define the complete scope, and 0.12.0 challenge the difficult assumptions. Then expand through small releases whose behavior is demonstrated by tests.

That gives you a modern Rust workbench where adding an operation does not require redesigning the website, replacing PostgreSQL does not rewrite the domain, and adopting Vef/Brynja does not force changes throughout the engine.
ARCHITECTURE.mdDocument
ROADMAP.mdDocument
PARITY_AND_RISK_REGISTER.mdDocument
1 more
sorry with local you mean we could not run a online version also?
Worked for 47s

Yes, absolutely—the plan includes a normal online website hosted on your server and accessible through your domain. My wording was confusing: “local” refers to where the data processing happens, not where the website is hosted.

Users would visit your website, get the full interface, and start using it. They would not need to install anything or run their own server.
One online website, two processing options
	Browser processing	Server processing
How users access it	Your normal online website.	The same online website, or directly through your API.
Where transformations run	The Rust engine compiled to WebAssembly runs in the visitor’s browser.	The native Rust engine runs on your server.
Does the input go to your server?	Not for the transformation itself.	Yes, when the user explicitly submits a server job.
Intended use	Everyday decoding, conversions and private-data analysis.	Explicit remote jobs, automation and workloads better suited to server resources.

For example, someone visits your website and pastes Base64 text. Under the proposed default, their browser decodes it and displays the result. The website is online, but their pasted data does not need to be uploaded for that operation.

The same website could also offer “Run on server.” That would submit the recipe and input through your HTTP API, execute it on your infrastructure, and return the result.
Your backend and database are still part of the plan

Accounts, saved recipes, shared workspaces, permissions and remote jobs would use your backend and PostgreSQL. Saving or sharing content would be a separate, explicit action from simply processing it in the browser.

Likewise, API-driven does not require every button click to send the input to a server: the browser and server implementations would expose the same application capabilities through their respective interfaces.

So the intended 1.0.0 product is the complete online website and API. Browser-local processing is a capability of that website; offline use is an additional option. Desktop and mobile applications still come afterward.
what could be a cool nordic asgardian name for this website?
Worked for 2m 30s

My favorite for this particular project is Eldrimnir. It has the Nordic fantasy feeling you like, and its inspiration fits a CyberChef-style website unusually well.

Rather than another name suggesting a shield or fortress, I would choose something associated with transformation, recipes, craftsmanship, or revealing hidden meaning.
1. Eldrimnir — my strongest overall choice

Inspired by Eldhrímnir, the cauldron used by the gods’ cook in Valhalla, as described in Grímnismál. That gives you a genuine mythological connection to the recipe-and-transformation idea.

Eldrimnir would be a deliberately simplified brand spelling—not the historical spelling. For something closer to the original, you could use Eldhrimnir.

I like the concept: you place raw data into an Asgardian cauldron, combine operations, and bring out something understandable. It preserves the playful recipe metaphor without sounding like “CyberChef, but in Rust.”

It also feels substantial enough to cover the website, engine, API, and future applications:
Eldrimnir
eldrimnir-core
eldrimnir-engine
eldrimnir-api
eldrimnir-cli

A possible tagline:

    Eldrimnir — Decode. Transform. Understand.

Visually, I picture an elegant Asgardian laboratory with a rune-inscribed cauldron or transformation chamber—not a cartoon cooking pot.
2. Runheim — strongest fit with your existing project family

A coined brand name, intended to evoke a “realm of runes,” rather than a claimed historical Old Norse expression.

To my ear, this sits naturally alongside Fluxheim, Skrifheim, Lykilheim, and Elderheim. It is short, clean, and less overtly tied to cooking.

For your project, I would use the rune motif to represent encoded symbols, hidden structure, and information waiting to be interpreted.

    Runheim — Reveal the meaning within.

My reservation: it conveys the atmosphere well, but the connection to transformation recipes is less specific than Eldrimnir’s.
3. Galdrheim — strongest magical-workshop atmosphere

Another coined brand name, inspired by galdr, an Old Norse word associated with incantations and spells. The complete name is a branding construction, not a historical term I am claiming to translate.

The product metaphor would be that operations are individual workings and recipes combine them into repeatable transformations.

It feels darker and more mysterious than Runheim, while still fitting your -heim naming style.

    Galdrheim — The art of data transformation.

My reservation: the ldr consonant cluster is a little less comfortable to pronounce for an international audience.
Other names worth considering
Name	Inspiration	My impression
Andhrimnir	Andhrímnir is the cook associated with Eldhrímnir in the mythological account. 	The most direct “Asgardian CyberChef” connection, but harder to spell and say.
Runasmidja	A coined “rune workshop” concept, using smiðja, meaning a smithy, as inspiration. 	Excellent craftsmanship imagery: raw data being worked into useful forms. Longer, but atmospheric.
Ketill	An Old Norse word for a kettle or cauldron. 	Short, understated, and suitable as a product name, though less obviously fantastical.
My recommendation

Eldrimnir is the one I would choose for this website: it has a story that actually fits the product, rather than just sounding Nordic.

Runheim would be my alternative for a cleaner, more restrained name that blends closely with your existing projects.

These are naming candidates; I have not verified domain, crates.io, or trademark availability.
most domains are taken but not Runasmidja so maybe we could go with that kind of fits
Worked for 37s

Yes—Runasmidja fits this project well, not just as a fallback because the other domains are taken. The “rune workshop” concept gives it an identity that connects naturally to what you are building: a place to inspect unfamiliar data, reveal its structure, and transform it into something useful.

I actually prefer the workshop metaphor over keeping CyberChef’s cooking theme. You are not just decoding text—you are assembling operations, examining intermediate results, working with binary formats, and building reusable pipelines. A workshop feels broad enough for all of that.

I would treat Runasmidja as a Nordic-inspired brand, rather than advertise it as a verified historical Old Norse name.
How I would present it

    Runasmidja
    Decode. Transform. Understand.

With a more descriptive line underneath:

    A security-first data workbench built in Rust.

Keep Runasmidja as the display name and runasmidja everywhere technical. That gives you a consistent family:
runasmidja
runasmidja-core
runasmidja-engine
runasmidja-api
runasmidja-cli

The main drawback I see is that people may need to see the spelling twice, particularly the smidja ending. I would keep the spelling consistent rather than introduce different accented, shortened, or anglicized versions.

For the visual identity, I picture an elegant Asgardian rune workshop—engraved metal, glowing symbols, and precise instruments transforming streams of data. That gives you room for the fantasy artwork you like while keeping the actual application clean and professional.

Runasmidja — an Asgardian workshop for data. That is a strong direction for this project.
