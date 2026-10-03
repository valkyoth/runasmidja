"""Reviewed prerequisite passes; source owners and acceptance remain additive."""

SOURCE_CONTEXT = {
'0.39.0': 'This pass qualifies local native artifact manifests and browser IndexedDB/OPFS transaction completion, local event/outbox records and orphan recovery only. Hosted SQL manifest/run/outbox publication is owned by v0.112.0, not assumed here.',
'0.61.0': 'Current scope: private API schemas and the existing loopback transport, including lossless offsets/errors and bounded commands. Live session/object authority arrives in v0.110.0–v0.111.0, isolated-worker/supervisor proof in v0.119.0–v0.120.0, durable heartbeat/retry in v0.124.0 and egress in v0.125.0–v0.127.0. Those runtime suites remain pending, not schema-test PASS.',
'0.62.0': 'Current scope: lifecycle messages and existing private loopback runs with local generation/cancellation tests; future lease/authorization cases are contract fixtures only. Minimal real SQL fencing is implemented in v0.107.0; deployed object authority qualifies in v0.110.0–v0.111.0, worker supervision in v0.119.0–v0.120.0, durable heartbeat/retry in v0.124.0 and egress in v0.125.0–v0.127.0 before v0.133.0 exposure. Do not claim durable or isolated execution here.',
'0.63.0': 'Current scope: bounded private upload/range/checksum/abort behavior on existing local artifact ports with local capability/generation tests. Hosted SQL publication/fencing waits for v0.112.0; live session/object authority for v0.110.0–v0.111.0; worker/supervisor and egress suites for v0.119.0–v0.120.0 and v0.125.0–v0.127.0. Contract fixtures do not qualify absent runtime controls.',
'0.64.0': 'Define the minimal authoritative publication lease: per-run monotonic checked fencing generation, committed acquisition/reassignment, expiry/revocation and compare-and-swap completion/publication. Contract fixtures cover duplicate/racing/stale callers. The actual PostgreSQL implementation is required in v0.107.0 before v0.112.0 publication; heartbeat/retry expansion belongs to v0.124.0.',
'0.65.0': 'Implement the v0.106.0 minimal lease/fencing contract on real PostgreSQL now: atomic committed acquisition/reassignment, checked generation advance, expiry/revocation and conditional completion/publication. Test concurrent claimers, rollback, duplicate completion and stale/expired/revoked tokens with controlled time. Issue tokens only after commit; authorization remains a separate current-state check. This is a prerequisite of v0.112.0, not deferred to v0.124.0.',
'0.71.0': 'Expand the minimal SQL lease/fencing primitive already qualified in v0.107.0 and used by v0.112.0. Add durable queue/heartbeat/renewal/reclaim, retry eligibility and idempotency lifecycle; rerun the earlier concurrent/stale/expiry/publication suite. This pass does not introduce fencing for the first time.',
}

PUBLICATION_PREREQUISITES = (
    'Storage transaction discipline', 'Repository contracts',
    'PostgreSQL adapter', 'Workspace authorization',
)

FOUNDATION_AFTER_BAO = [
('Workflow reference policy',
 'Harden workflow admission for both .yml and .yaml, quoted/block/expression forms and action/reusable-workflow references. Define separate full-commit remote, reviewed same-repository local and digest-pinned container policies; preserve CodeQL Default setup.',
 'Unpinned, dynamic, malformed and advanced-CodeQL references reject in both suffixes; approved remote/local/container fixtures pass. Do not mistake comments or unrelated YAML strings for executed references; current bypass regressions are exercised.'),
('Feature and target admission gates',
 'Replace scaffold-only dependency/no_std heuristics with reviewed package profiles and normal/build/dev/optional/target dependency graphs. Require inherited unsafe-forbid/lint policy, real target/feature builds and public contract isolation; keep dependency admission explicit.',
 'Comment-spoofed no_std, target/build dependency leakage, default-feature std/alloc and feature-unification leaks reject. Reviewed std adapters and portable providers can be admitted without disabling checks; bare-metal no-alloc, alloc, Wasm and native graphs are tested separately.'),
('Fixture ownership and drift',
 'Require project/service ownership before every container/network/volume mutation, including stop; verify immutable image and nonsecret resource/mount/port/network/config fingerprints before reuse. Reconcile only documented safe differences and refuse destructive replacement.',
 'Name collisions, wrong labels/digests, changed mounts/ports/limits and unowned volume/network tests refuse mutation. Partial startup and drift preserve owned database/vault state; fingerprints/logs contain no secret values and no unrelated object is stopped.'),
]

FOUNDATION_AFTER_BUILD = [
('Release evidence trust contract',
 'Define scope/evidence schemas and reviewed assessor/reviewer identity, exact-source lineage, severity disposition and artifact evidence references. Describe check_release as metadata validation, not assessment authentication; plan trusted attestation enforcement before distribution.',
 'Report-shape PASS alone cannot authorize publishing; missing assessment identity/review/target evidence blocks the reviewed release checklist. Define tampered/fabricated evidence regressions and keep no-report NOT RUN rejection; no signing provider is invented.'),
]

FOUNDATION_AFTER_FRESHNESS = [
('Seed value and budget vocabulary',
 'Implement the smallest no_std/no-alloc checked ID/offset/value-kind/error and byte/work reservation vocabulary for a one-operation hex seed. Define explicit EOF and terminal counts without requiring the later compiler/scheduler.',
 'Checked conversions, reserve/refund, overflow, zero limits and L-1/L/L+1 have unit tests on native/bare-metal/Wasm. Freeze a seed manifest: 32 KiB input, 64 KiB output, 4 KiB windows and 256 KiB tracked engine state; choose finite fuel and host deadlines before admission, with no hidden dynamic growth.'),
]

ADDITIONS = {
9: [
('Browser privacy and secret publication',
 'Implement sensitivity joins and opaque ephemeral handles at browser serialization/UI/storage boundaries before rich viewers or crypto. Add explicit reveal/export grants, generation rechecks and supervisor-owned cleanup; browser-entered user keys never require OpenBao/upload.',
 'Sentinel inputs/keys/derived material stay absent from IndexedDB/OPFS/CacheStorage, history, URLs, clipboard, search, diagnostics and network by default. Revoked disclosure/stale page/cancel/crash tests deny publication; document unavoidable DOM/JS copies and no guaranteed erasure.'),
],
11: [
('Pack manifest and resource contract',
 'Define a minimal first-party browser-pack manifest before heavy feasibility providers: operation/engine/ABI revisions, source/hash/license, target/import/capability requirements and transfer/decompressed/compile/memory ceilings. Keep third-party plugin admission separate.',
 'Tampered, incompatible, unlicensed, oversized and forbidden-import pack fixtures reject before activation. Disabled packs have no default dependency or bundle cost; declared required operations remain visible when a pack is absent.'),
('Minimal lazy browser pack loader',
 'Implement bounded same-origin loading/installation of reviewed first-party packs in a Dedicated Worker, with cancellation, atomic activation and an explicit selected offline set. Qualify one small pack before large providers; later extensibility passes expand the catalogue/plugin model.',
 'Real browsers exercise failed/interrupted downloads, hash/ABI mismatch, cancellation, quota and offline absence. A failed activation preserves the previous pack set; loading never uploads payloads or fetches hidden CDN assets; measure decode/compile/instantiate/copy and retained-memory costs.'),
],
15: [
('Performance baseline and regression profiles',
 'After the actual alpha, freeze benchmark hardware/corpora, per-profile numeric envelopes and reproducible engine versus File/worker/Wasm/viewer measurements. Start with UI p95 <100 ms and cooperative cancel p95 <200 ms goals; freeze bundle/hard-kill caps from real measurements.',
 'Record correctness and source/artifact/browser/tool identities, repetitions, cold/warm p50/p95/p99/max, JS/Wasm/RSS/disk/copy memory and cleanup. Goals are unmet until measured; budget regressions and event floods fail the gate. No seed measurement claims full-provider/large-input performance.'),
],
68: [
('Hosted artifact publication fencing',
 'With repositories and workspace authority available, qualify object completion followed by manifest/run/outbox transaction. Recheck current authorization and server lease/generation fences; publish only through committed manifests and reconcile inaccessible orphan stages.',
 'Crash each finalize/commit/publish/cleanup cut point; duplicate completion, failed SQL commit, corrupt object, disk full, revoked reader and stale worker cannot publish partial/unauthorized output. Read bytes to verify hashes; cleanup never deletes a live referenced object.'),
],
69: [
('Worker isolation fault qualification',
 'Qualify actual delegated cgroup/namespace/seccomp/MAC, nonroot/capability/descriptor policies and bounded scratch for isolated untrusted jobs. Keep supervisor/deadline enforcement outside the worker and kill the complete process tree.',
 'CPU spin, OOM, PID/fork/FD/temp exhaustion, forbidden mounts/syscalls/egress and malformed IPC are tested on the deployment kernel. Descendants stop after kill and staged output remains inaccessible; missing kernel controls reject the profile rather than silently weaken it.'),
],
72: [
('DNS and connection destination binding',
 'Implement canonical native destination admission with all A/AAAA validation, IPv4-mapped IPv6 normalization, policy-owned resolution and connection to approved addresses while preserving Host/SNI. Revalidate retry/pool/TTL/policy changes and peer identity.',
 'Controlled DNS/TLS fixtures reject mixed public/private answers, rebinding between resolve/connect, metadata/private/link-local/reserved addresses, scoped/ambiguous forms and unknown peers. No SDK/client re-resolution bypass remains; explicit private-network operator policy is separately scoped.'),
('Redirect and outbound transport policy',
 'Qualify each redirect/credential/timeout/decompression decision in the native broker; disable ambient proxy/Alt-Svc/coalescing bypasses. Inventory SDK/identity/search/object-store transports and isolate any client lacking required transport hooks.',
 'Private redirects, loops, retry/deadline/byte excess, signed-URL/header leaks, cross-origin credentials, ambient proxy and stale pooled-policy tests fail. An intentional proxy enforces final destinations; browser Fetch limitations are explicit and cannot trigger silent remote fallback.'),
],
215: [
('Migration integrity and canonicalization',
 'Freeze portable entity/key/revision/grant/timestamp/null/numeric canonicalization and artifact reference semantics before MySQL/cutover drills. Define a maintenance-window job quiesce/fence protocol and rollback that preserves writes after cutover.',
 'Two-tenant/revoked-grant/case/Unicode/large-number/tombstone fixtures and corrupt/truncated/duplicate exports reject precisely. Equality requires key sets, canonical digests, byte-read artifact hashes, permissions and revision/idempotency outcomes; missing/duplicate/unexpected records and references are zero.'),
],
222: [
('Distribution assessment and provenance binding',
 'Bind trusted reviewed assessment to exact source, toolchain, artifact/pack/model/SBOM hashes, required target evidence and signing/provenance identities. Implement rejection gates distinct from local report metadata, remote CodeQL Default settings and publication authority.',
 'Tampered/substituted artifact, stale SBOM, forged/untrusted PASS, missing target/CI evidence and bad signature/issuer/source bindings reject. Independent clean builds verify manifests; secrets come from OpenBao and no test creates a real assessment PASS or publication authorization.'),
],
}


def strengthen_foundation(rows):
    result = []
    for row in rows:
        result.append(row)
        if row[0] == 'OpenBao-first secret provisioning':
            result.extend(FOUNDATION_AFTER_BAO)
        if row[0] == 'Build and release secret delivery':
            result.extend(FOUNDATION_AFTER_BUILD)
        if row[0] == 'Freshness and supply-chain controls':
            result.extend(FOUNDATION_AFTER_FRESHNESS)
    return result


def order_source(releases):
    # Full replay/spooling qualification needs actual artifacts, not a future port.
    replay = next(row for row in releases if row['version'] == '0.36.0')
    result = [row for row in releases if row is not replay]
    index = next(i for i, row in enumerate(result) if row['version'] == '0.39.0')
    result.insert(index + 1, replay)
    return result
