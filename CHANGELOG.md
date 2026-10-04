# Changelog

## 0.2.0 — release prepared, GitHub and tag pending

GitHub follow-up (2026-10-04): pin the container runner to Ubuntu 26.04 for
required Podman build inheritance controls, check those switches explicitly,
and run existing kernel build-limit qualification before service startup.
Raise the overall job deadline to 45 minutes to accommodate the bounded build
and remaining gates. No runtime/build script or security limit changes; hosted
verification of the correction remains pending.

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
