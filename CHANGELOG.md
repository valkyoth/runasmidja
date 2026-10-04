# Changelog

## 0.2.3 — remediated candidate; pentest RETEST REQUIRED

- Detect embedded relative traversal at punctuation/token boundaries, retaining
  the strict source-relative module exception and ordinary prose controls.

- Reject ambiguous dot-segment paths while preserving simple scanner-relative
  module identifiers, dotted filenames and ordinary advisory prose.

- Preserve private-root evidence during URI normalization by checking both
  original and normalized strings and matching only complete file schemes.

- Reject case-insensitive file/share URIs in public evidence, with exhaustive
  casing tests and retained HTTPS/package URL controls.

- Check parsed evidence strings/keys against known private build/temp/cache roots
  and network paths; bound the public tree to 256 entries and 128 MiB of JSON.

- Reject unpaired Unicode surrogates in public JSON keys and string values;
  preserve valid surrogate pairs and literal Unicode with regression coverage.

- Enforce image service binding at every directory depth; require BOM-free
  UTF-8 public JSON and reject non-standard or overflowing non-finite numbers.

- Anchor public inventory reads to verified directory descriptors, reject
  unsafe ownership/write permissions, and reject duplicate JSON keys.

- Reject placeholder, linked and oversized public inventories; validate minimum
  CycloneDX structure and explicit historical service identities.

- Bind public SBOM export destinations to services and independently check
  canonical inventory identities, including concurrent and manual-swap regressions.

- Bound per-service evidence retention and reject private-tree/source-alias
  export destinations; add quota, custody, concurrency and no-mutation regressions.

- Follow-up SAST confirms SAST-001 fixed. Fix SAST-002 (Low) with serialized
  service evidence transactions, image/content-keyed immutable snapshots,
  atomic probe annotation, bound public export and concurrency regressions.
- Make OpenBao validation success-only; archive reads require held custody.

- Fix SAST-001 (Low): serialize global OpenBao cache writers, lock receipt/archive
  readers through scans, recheck concurrent automatic builds, and add real
  multiprocessing/custody/publication-failure regressions.

- Assemble the verified static OpenBao 2.7.1 executable on signed Wolfi; retain
  exact input/image/archive provenance, upstream license and per-image inventory.
- Isolate new fixture custody; test fresh startup, retained same-version image
  switching/rollback, scoped auth, audit exhaustion and recovery.
- Add admission/publication/retry regressions and monitor packaging-pin drift.
- Keep heavy tests local, six crates publish=false and portable Rust unchanged.
- See [scope](docs/releases/v0.2.3-scope.md),
  [notes](release-notes/v0.2.3.md) and [assessment](security/pentest/v0.2.3.md).

## 0.2.2 — released 2026-10-04

Signed tag points to 4d6f40e; Rust CI and CodeQL Default are green.

Maintainer accepted 8a814ec on 2026-10-04 with no new actionable findings.
All three prior findings are resolved: root/rootful service execution, rollback
instance scope and build/probe containment. Release automation is metadata-only;
all six workspace crates remain 0.2.2/publish=false. The preparation history
below describes the fixes leading to this accepted candidate.

- Follow-up Low remediation: share rootless enforcement across public builds,
  probes, archive export and image import; test namespace entry and AST bypasses.

- Remediate the Medium rootless-enforcement and Low rollback-scope findings;
  add side-effect-denial regressions; maintainer retest subsequently accepted.
- Adopt public signed Wolfi Valkey 9.1.2 with exact index/platform admission and
  weekly/manual freshness checks; retain the previous official digest for rollback.
- Separate fixture custody, OpenBao-issued ACLs, real eviction, outage/restart,
  nonpersistence and kernel/resource qualification; bounded fixture RESP client.
- Preserve native/scratch/Wolfi probe regressions and code-only GitHub CI.
- See [scope](docs/releases/v0.2.2-scope.md),
  [notes](release-notes/v0.2.2.md) and [assessment](security/pentest/v0.2.2.md).

## 0.2.1 — released 2026-10-04

Maintainer accepted 74b52fc on 2026-10-04 with no actionable findings. Full local
release qualification passes; no remediation was required. The accompanying
SAST report limits are retained in the assessment. Version/publishing review
confirms all six crates remain 0.2.1/publish=false; metadata automation cannot
push or publish.

Add a minimal signed-base Wolfi static image for the existing health probe;
retain native and scratch profiles. Scan the exact base/built archive, bind
archive config/layers and copied executable, check actual kernel limits and
zero capabilities, use an ephemeral loopback port, and clean up only the captured
owned container. Add negative regressions, base freshness and public inventories.
Heavy qualification remains local; no runtime Rust dependencies or website/API
features are added. See [scope](docs/releases/v0.2.1-scope.md).

## 0.2.0 — tagged 2026-10-04

Signed tag points to 4e5b4e1; Rust CI and CodeQL Default are green. The following
entries retain the preparation history; pending statements below are historical.

GitHub scope update (2026-10-04): remove the container job entirely at the
maintainer's request. Builds, image admission and real service/resource checks
remain local pre-push requirements. Push/PR CI keeps code checks, unit tests,
no_std compilation, a native smoke test and dependency audits with a 15-minute
job ceiling. CodeQL remains Default setup. This supersedes the intermediate
Ubuntu 26.04 container-runner correction; runtime/build scripts are unchanged.

Release review (2026-10-04): the maintainer accepted the c73805e retest with
zero new Critical/High/Medium/Low findings. All prior issues are resolved within
the bounded fixture scope. Final verification and release-automation review
pass; all crates remain publish=false and release readiness performs no push or
publish. GitHub and explicit tag authorization remain pending. The following
entries preserve the preparation history and its then-pending assessment states.

Latest re-review (2026-10-04): reject every scanner operational failure before
parsing output; enforce vulnerability policy only on completed reports. Validate
and scan a candidate PostgreSQL archive, import/verify it, then publish the final
receipt. Failed scans/imports preserve prior committed artifacts; interrupted
publication allows automatic rebuild. Added scanner/candidate-mutation/publication/
retry regressions (111 normal/optimized tests), removed trailing EOF whitespace,
and added a committed-whitespace CI check. Earlier fixture data is retained;
the rebuilt image uses v02-admission-ready. Maintainer retest is pending.

- Start TLS OpenBao and verify scoped identities before any dependent startup.
- Issue PostgreSQL admin/runtime and Valkey passwords through OpenBao; preserve
  version-1 KV records with CAS=0 and reject schema/version/projection drift.
- Separate provisioning/runtime permissions and recovery/root custody; confirm
  root revocation and preserve versions across partial failures and restart.
- Require project/service/instance ownership before fixture mutations and pinned
  image identity before container reuse. Add unit and real-service fault tests.
- Retain legacy fixture data; use a separate v02 profile without silent migration.

Pentest remediation (2026-10-03): bind CI installation to the verified archive,
bound child/log/audit resources, add exact-image provenance/vulnerability/SBOM
gates and fsync custody directory mutations. Maintainer approved unsigned-image
exceptions for the two original exact PostgreSQL/Valkey fixture pins. The original
PostgreSQL image's 42 reported HIGH/CRITICAL findings remain blocked and retained
as historical evidence. The authorized replacement builds official PostgreSQL
19beta4 on a signed Wolfi base, removes gosu/compiler/Perl from the runtime, and
binds every scanned archive layer/config to the executed immutable image ID.
All current images scan clean at that threshold without a CVE waiver. Full
remediated service qualification and 12 real PostgreSQL initialization denials
pass. Earlier fixture data is retained separately; GitHub and maintainer retest
remain pending.

Pentest RETEST REQUIRED. The original candidate was committed locally for the
maintainer-requested review; remediation is committed locally at their explicit
request for retest and no tag is authorized.
See [candidate notes](release-notes/v0.2.0.md).

Re-review remediation (2026-10-04): address one medium/three low findings with
checked CPU/memory/PID build cgroups, private 3 GiB rootless storage, pre-write
512 MiB atomic archive bounds, strict UNKNOWN admission, expiring exact-image
not-affected evidence, public SBOM path rejection and safe unreaped-only process
group signalling. OpenBao's affected legacy OpenPGP packages are absent from
its pinned binary; its UNKNOWN advisory stays visible and the review expires
2026-11-02. All 106 normal/optimized regressions, actual contained build/resource
probe and fresh full service qualification pass. Earlier data is retained;
default v02-reviewed uses the rebuilt image without migration/reset. Locally
committed for maintainer retest; GitHub, acceptance and tagging remain pending.

## 0.1.0 — 2026-10-03

Signed `v0.1.0` points to `9d6ec75`; GitHub checks, containers and CodeQL passed.
The paragraphs below preserve the preparation history of this tagged release.

Release review (2026-10-03): the maintainer accepted the green retest, resolving
all three submitted findings with no new actionable security issue. Full local
verification and version/documentation review pass; the monitored, unadmitted
OpenBao SDK was refreshed to 2.2.2. Pentest PASS covers the foundation only;
GitHub checks, tagging and publication remain pending.

The notes below preserve the earlier candidate's preparation history.

Pentest remediation (2026-10-03): addressed the browser origin threat-model gap,
assigned profile/header/independent offline verification owners, replaced
optimization-removable smoke assertions, and verified native probes using the
live child's announced ephemeral port. Added adversarial regressions and fixed
angle-bracket Markdown link checking. All 34 Python tests and optimized actual
native/container probes pass; maintainer retest is pending, not pentest PASS.

Foundation handoff (2026-10-03): reverified the v0.1.0 scope, common gates,
dependency/freshness checks, real native/container probes and service restart;
refreshed the SBOM and documented known limits for the maintainer's pentest.
The release loop now commits only after their green result, waits for GitHub,
and tags/pushes a version tag only on explicit instruction. Pentest is NOT RUN.

### Foundation scope

- Initialized EUPL-1.2/Rust 1.99.0 workspace with five no_std boundary crates
  and a Linux development health probe.
- Adapted Eth/Brynja repository files, dependency/CI/freshness controls and
  executable file-size/documentation/graph gates.
- Added automated PostgreSQL 19 beta 4, TLS OpenBao and ACL Valkey Podman tests.
- Preserved the idea/planning bundle and defined 386 pre-1.0 passes, including
  service lifecycle, provider feasibility, parity and operational qualification.
- Revised planned search to early portable contracts and mandatory qualification
  of repository/optional Meilisearch backends alongside hosted persistence.
- Required OpenBao as the source for initialization/runtime/private-build/release
  secrets; made local-password-first fixture remediation the next bounded pass.
- Reconciled the submitted gap analysis against source and official documentation;
  retained every original acceptance and added 240 reviewed verification gates.
- Added 15 bounded ownership/admission/seed/pack/privacy/performance/migration/
  isolation/egress/distribution prerequisites; actual artifacts now precede full
  seekable replay. Documented verified enforcement gaps without claiming fixes.
- Tightened unchanged 386-pass numbering: minimal SQL fencing at 0.107.0 precedes
  hosted publication at 0.112.0; local storage and early API test scopes are
  explicit, and actual continuation starts at 0.387.0. Generator rejects blank
  or nonstring verification gates before writing output.

No product parity or production readiness is claimed. Pentest is accepted;
GitHub checks, tagging and publication are pending. See release-notes/v0.1.0.md.
