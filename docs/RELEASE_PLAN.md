# Runasmidja Release Plan To 1.0.0

Status: roadmap contract; v0.1.0/v0.2.0/v0.2.1/v0.2.2 tagged; v0.2.3 implementation candidate; maintainer pentest PASS; GitHub and tag pending.
The authorized Wolfi/PostgreSQL fixture passes scans and real qualification; see the
[assessment](../security/pentest/v0.2.0.md).

386 small pre-1.0 passes, starting at 0.1.0 and ending at 0.386.0. Add further minors whenever inventory, provider work or qualification needs a smaller pass. Version 1.0.0 is the first serious production release.

The supplied 240-release bundle is preserved under [reference](reference/workbench-plan/README.md). Runasmidja adds operational services and splits multi-provider/algorithm work; source-version mappings preserve every original workstream. Nothing in this plan claims an implementation or a completed pentest.

If mandatory gaps remain after 0.386.0, actual additional passes start at **v0.387.0**. Historical reference continuation numbers remain preserved as provenance, not actual version assignments.

## Setup and scope rules

- Run Rust 1.99.0 initially; review official stable, crate, tool, action and service metadata weekly and before changes.
- Before each pass, write its exact API/operation/argument scope, target profile, numeric resource ceilings and test IDs. One new algorithm, dialect, persistent contract or trust boundary per pass.
- All code files stay at or below 500 lines; focused crates and independently tested adapters preserve no_std and future Vef/Brynja extraction.
- OpenBao is the source for every project-operated initialization, runtime, build and release secret; consumers start only after scoped retrieval. Minimal vault bootstrap/recovery trust has separate custody; public Rust builds and browser-local user inputs require no vault.
- SearchService is an early portable contract. Repository search and optional Meilisearch are required implementation/test profiles before production; optional deployment is not deferred implementation. Index only approved nonsensitive metadata and recheck current database authorization.
- A family row is an inventory owner. If it contains independent algorithms or dialects after source reconciliation, split it into additional numbered passes before coding; never hide feature work in a patch.
- The predecessor is the baseline. A later capability is never assumed available; move or split the consumer if a concrete prerequisite is discovered.
- Freeze exact variants, targets/features, numeric byte/work/state/depth/deadline ceilings, capability policy, fixture provenance, test IDs and evidence locations in a reviewed scope manifest. TBD/placeholder fields block acceptance.
- The first hex seed is bounded by the earlier tested value/budget vocabulary and minimal worker messages. It proves one transformation, not the later scheduler or full recipe IR; fuel/byte limits apply from the first execution.
- API work before the integrated server security gate is loopback/private integration only. Public untrusted-job routes require verified authority, isolation, admission, fencing, egress, TLS and recovery together.
- Every fixture mutation needs verified ownership now, including concrete minimum checks in 0.2.0; the later ownership/drift pass expands fingerprints and negative coverage, never authorizes earlier name-only mutation or silent state reset.
- Imported operation names remain provisional until the immutable CyberChef inventory confirms exact variants and redistribution rights. Unsupported required variants remain blocking gaps.

## Every release gate

The [browser security profiles](BROWSER_SECURITY_PROFILES.md) define origin-compromise limits, separate local-only/remote applications and independently verified signed offline artifacts with network-disabled execution. Explicit seed/privacy/workbench/loader/offline/server/packaging owners qualify document/worker CSP, Trusted Types, COOP/COEP/CORP, framing and permissions; no browser enforcement is claimed by the foundation.

Run `scripts/checks.sh`, current dependency/license/advisory checks, freshness, applicable browser/reference/service/fuzz/fault suites and artifact SBOM generation. Update threat controls, limitations, parity evidence, CHANGELOG and release notes. Every numbered minor, patch, RC and 1.0 needs its own exact-source pentest, remediation and clean retesting before tagging; passing tests alone do not authorize a PASS report.

The [release runbook](RELEASE_RUNBOOK.md) and [version policy](VERSIONING_POLICY.md) define the handoff. Build and verify locally, commit completed candidates as needed, and stop for the maintainer’s pentest. Finalize acceptance only after green. The maintainer pushes; repeat GitHub fixes and affected pentest retests until green. Tag and push the version tag only when explicitly requested; distribution publication needs separate authorization.

The [search design](SEARCH_DESIGN.md) and [secret lifecycle](SECRETS_POLICY.md) define required trust boundaries. The current bounded patch is [v0.2.3 Wolfi OpenBao fixture](releases/v0.2.3-scope.md); v0.3.0 remains the next minor. The released [v0.2.0 fixture](releases/v0.2.0-scope.md) issues database/cache passwords in OpenBao; the legacy v0.1 fixture is retained unchanged. Temporary delivery, build/release identity and full drift qualification remain later numbered passes.

The [container and Fluxheim plan](CONTAINER_DEPLOYMENT_PLAN.md) proposes compatible v0.2.1-v0.2.3 image follow-ups, without renumbering the minor workstreams. Fluxheim Wolfi proxy qualification is required at v0.11.0 (health fixture), v0.12.0 (freshness), v0.129.0/v0.130.0/v0.133.0 (actual deployment/TLS/security) and v0.366.0/RC/1.0 (exact artifacts). Meilisearch preferred-base admission remains v0.115.0. v0.2.1/v0.2.2 are tagged; v0.2.3 is the current candidate, with maintainer pentest PASS; GitHub and tag pending.

The [2026-10-03 planning revision](plan-revision-2026-10-03.md) records moved owners and qualification limits. Unpublished version assignments changed; the supplied source-version mapping remains intact.

The [gap reconciliation](gap-reconciliation-2026-10-03.md), [execution contracts](EXECUTION_CONTRACTS.md), [browser/performance policy](BROWSER_PERFORMANCE.md), [storage/host policy](STORAGE_HOST_CONTRACTS.md) and [strict gates](VERIFICATION_GATES.md) add reviewed requirements; no runtime remediation is claimed by this plan.

## Per-version handoffs

| Phase | Versions | Detailed handoffs |
| --- | --- | --- |
| Z: Repository and service foundation | 0.1.0–0.13.0 | [Milestones](releases/phase-z.md) |
| A: Foundation and useful vertical slice | 0.14.0–0.42.0 | [Milestones](releases/phase-a.md) |
| B: Bytes, text and foundational encodings | 0.43.0–0.72.0 | [Milestones](releases/phase-b.md) |
| C: Streaming, artifacts and execution foundations | 0.73.0–0.87.0 | [Milestones](releases/phase-c.md) |
| D: Modern browser workbench | 0.88.0–0.102.0 | [Milestones](releases/phase-d.md) |
| E: Remote API, PostgreSQL and secure server execution | 0.103.0–0.133.0 | [Milestones](releases/phase-e.md) |
| F: Structured formats, queries and utilities | 0.134.0–0.157.0 | [Milestones](releases/phase-f.md) |
| G: Compression and archives | 0.158.0–0.172.0 | [Milestones](releases/phase-g.md) |
| H: Modern hashing and cryptographic operations | 0.173.0–0.208.0 | [Milestones](releases/phase-h.md) |
| I: Legacy cryptography, hashes and classical ciphers | 0.209.0–0.259.0 | [Milestones](releases/phase-i.md) |
| J: Public keys, certificates and tokens | 0.260.0–0.286.0 | [Milestones](releases/phase-j.md) |
| K: Network and forensic analysis | 0.287.0–0.301.0 | [Milestones](releases/phase-k.md) |
| L: Images, media and document presentation | 0.302.0–0.322.0 | [Milestones](releases/phase-l.md) |
| M: Complete recipe semantics, Magic and compatibility | 0.323.0–0.337.0 | [Milestones](releases/phase-m.md) |
| N: Extensibility and replacement-adapter proof | 0.338.0–0.352.0 | [Milestones](releases/phase-n.md) |
| O: Portability, collaboration and operations | 0.353.0–0.371.0 | [Milestones](releases/phase-o.md) |
| P: Qualification and general-availability readiness | 0.372.0–0.386.0 | [Milestones](releases/phase-p.md) |

## Release candidates and production

### v1.0.0-rc.1

**Status:** planned.

**Setup:** every required pre-1.0 inventory row and qualification result is closed; PostgreSQL 19 GA, current OpenBao/Valkey, optional Meilisearch and exact artifacts are pinned. Both search profiles and OpenBao secret-source/initialization/build/recovery gates are qualified.

**Goal:** qualify the first complete production candidate.

**Scope:** freeze features; substantial missing work returns to new 0.x releases.

**Deliverables:** complete website/API, offline operation packs, five parity matrices, SBOM/notices, signed artifact manifests, deployment/recovery instructions and independent consumer examples.

**Verification:** actual supported browsers/native hosts; independent security assessment; auth/SSRF/cache/plugin/failure tests; real PostgreSQL/MySQL migration proof; backup/restore; Vef/Brynja seam tests; privacy and accessibility.

**Exit criteria:** exact artifacts pass the complete acceptance contract with no required gaps or exploitable critical/high findings. v1.0.0-rc.1 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

### v1.0.0-rc.N

**Status:** planned as needed.

**Setup:** preceding candidate and individually scoped blocking fixes.

**Goal:** qualify remediated candidate artifacts.

**Scope:** compatible fixes and artifact regeneration; missing features receive 0.x owners.

**Deliverables:** regressions, revised evidence/notes and newly built candidate artifacts.

**Verification:** rerun all affected suites and full candidate acceptance, including security and operational restoration.

**Exit criteria:** no remaining blocker; every previous finding has tested disposition. v1.0.0-rc.N implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

### v1.0.0

**Status:** planned.

**Setup:** qualifying exact RC source and artifacts; complete evidence reviewed.

**Goal:** release the first serious production-ready Runasmidja website, reusable engine and public API.

**Scope:** complete declared CyberChef functionality on browser/native profiles, PostgreSQL production support and verified replacement boundaries; future desktop/mobile GUI milestones remain post-1.0.

**Deliverables:** supported distributions, maintenance policy, full operation/API docs, production security/recovery guides and release notes.

**Verification:** verify all operation/argument/recipe/UI/target rows, both search profiles with live authorization, OpenBao-sourced project secrets from initialization through release, exact distribution provenance, current security findings and executed deployment/upgrade/recovery procedures.

**Exit criteria:** all required functionality and evidence pass; no beta database or unsupported production claim remains. v1.0.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.

## After 1.0

1.1: Linux/Windows/BSD/macOS desktop preview. 1.2: qualified desktop stable. 1.3: Android/iOS preview. 1.4: qualified mobile stable. Aesynx receives a separate conditional adapter/GUI milestone once runnable APIs exist. Each platform needs its own compile, runtime, filesystem/secret-storage, accessibility, packaging and update-security evidence. API compatibility survives independent client release versions.
