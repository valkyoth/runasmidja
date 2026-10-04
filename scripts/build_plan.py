#!/usr/bin/env python3
"""Render Runasmidja release handoffs from reviewed source plus service passes."""
import json
from pathlib import Path
from plan_hardening import (ADDITIONS, PUBLICATION_PREREQUISITES, SOURCE_CONTEXT,
    order_source, strengthen_foundation)

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / 'docs'
SOURCE = DOCS / 'reference/workbench-plan/roadmap.json'

# A row crossing provider/algorithm boundaries is split before implementation.
SPLITS = {
12: ['Regex compatibility feasibility', 'Query-language feasibility', 'YARA feasibility', 'Cryptographic-provider feasibility', 'Compression-provider feasibility', 'Disassembly feasibility', 'OCR and media feasibility'],
17: ['Integer representations', 'Floating-point representations', 'BCD representations'],
19: ['Base32 variants', 'Base45 variants'],
20: ['Base58 variants', 'Bech32 variants'],
21: ['Base62', 'Base85', 'Base92', 'Generic bounded base conversion'],
22: ['Percent encoding', 'HTML entity encoding', 'Quoted-printable'],
23: ['Unicode escape semantics', 'Unicode normalization'],
29: ['Braille encoding', 'Punycode encoding', 'Modhex encoding', 'COBS framing', 'Caret and control encodings', 'MIME decoding'],
76: ['Lossless JSON', 'CSV semantics'],
77: ['XML data processing', 'HTML data processing'],
78: ['XPath dialect', 'CSS selector dialect'],
79: ['JSONPath dialect', 'JMESPath dialect', 'jq dialect if inventoried', 'JSONata dialect if inventoried'],
80: ['YAML semantics', 'Rison semantics'],
81: ['MessagePack semantics', 'CBOR semantics'],
82: ['AMF variants', 'Avro schemas'],
107: ['SHA-2 variants', 'HMAC construction'],
108: ['SHA-3 variants', 'Keccak variants', 'SHAKE output semantics'],
109: ['BLAKE variants', 'BLAKE3 enhancement assessment'],
111: ['PBKDF2', 'HKDF', 'Residual inventoried KDFs'],
112: ['bcrypt variants', 'scrypt variants', 'Argon2 enhancement assessment'],
113: ['AES block-mode inventory and provider qualification', 'AES ECB analysis', 'AES CBC analysis', 'AES CFB analysis', 'AES OFB analysis', 'AES CTR analysis', 'Residual inventoried AES modes'],
114: ['AEAD parameter contracts', 'AEAD authenticated encryption', 'AEAD staged decryption publication'],
116: ['ChaCha stream variants', 'Poly1305 authentication', 'ChaCha authenticated combinations'],
117: ['Salsa20', 'XSalsa20'],
119: ['Deterministic analysis PRNGs', 'Secure random generation', 'Bounded prime generation'],
122: ['DES analysis', 'Triple DES analysis'],
123: ['Blowfish analysis', 'RC2 analysis'],
124: ['RC4 and drop analysis', 'Rabbit analysis'],
125: ['TEA analysis', 'XTEA analysis', 'XXTEA analysis'],
126: ['RC6 analysis', 'Twofish analysis', 'PRESENT analysis', 'Residual block-cipher inventory closure'],
127: ['SM4 analysis', 'GOST encryption parameter sets'],
129: ['MD-family historical digests', 'SHA-0 analysis', 'RIPEMD variants', 'Residual historical digest closure'],
130: ['GOST digests', 'SM3 digest', 'Whirlpool digest', 'Snefru variants', 'HAS-160 digest', 'Residual specialist digest closure'],
132: ['ROT and substitution analysis', 'Vigenere analysis', 'Morse encoding', 'Bacon encoding', 'Affine cipher', 'Atbash cipher', 'A1Z26 encoding', 'Residual classical substitution closure'],
133: ['Bifid analysis', 'Rail Fence analysis', 'Caesar Box analysis', 'Residual classical transposition closure'],
134: ['Enigma analysis', 'Typex analysis', 'Lorenz analysis', 'SIGABA analysis', 'Bombe search if inventoried', 'Colossus search if inventoried'],
135: ['EVP legacy compatibility', 'CipherSaber analysis', 'Citrix compatibility', 'LS47 analysis', 'Residual legacy acceptance'],
136: ['BER parsing', 'DER canonical parsing', 'ASN.1 display', 'OID conversion'],
138: ['X.509 fields and extensions', 'Certificate-bundle parsing delta'],
139: ['CRL analysis', 'CSR analysis'],
140: ['RSA key generation', 'RSA encryption and decryption', 'RSA signing and verification'],
141: ['ECDSA curve and key formats', 'ECDSA signatures'],
142: ['SM2 identity and signatures', 'GOST signature and wrap variants'],
143: ['OpenPGP packet inspection', 'OpenPGP key inspection', 'OpenPGP key generation'],
145: ['OpenPGP signing and verification', 'OpenPGP combined encrypt and sign'],
174: ['QR generation', 'Barcode generation'],
175: ['QR recognition', 'Barcode recognition'],
177: ['EXIF metadata', 'ID3 metadata', 'Residual media metadata'],
179: ['PDF preview isolation', 'HTML preview isolation', 'Media preview isolation'],
}

EXTRAS = {
0: [
('Repository foundation', 'Initialize EUPL-1.2 workspace, copied and adapted GitHub files, Rust 1.99.0, no_std facade, 500-line gates, reference provenance and pending release evidence.', 'Default/release tests, bare-metal and Wasm checks, policy rejection fixtures, documentation links and dependency audits pass; no product parity is claimed.'),
('OpenBao-first secret provisioning', 'Remediate the current local-password-first harness: start and initialize TLS OpenBao before credential-consuming services; generate project-owned credentials through OpenBao, persist references/versions there and separate minimal vault trust/recovery custody. Configure audit, scoped provisioning/runtime identities and bootstrap root revocation.', 'An empty-state run obtains PostgreSQL admin/runtime and Valkey credentials from OpenBao before service initialization; sealed/unavailable/denied OpenBao prevents dependent startup without local generation or fallback. Partial failure/retry preserves vault credential versions and data; bootstrap root is revoked only after scoped provisioning succeeds; diagnostics never expose secrets.'),
('PostgreSQL 19 beta 4 test fixture', 'Pin PostgreSQL 19 beta 4 by digest; automate rootless Podman, OpenBao-sourced initial admin and runtime credentials, readiness and a separate runtime role.', 'A real container reports 19beta4, transaction rollback works, runtime role has no superuser or role-management powers, wrong passwords fail, and only loopback ports are published.'),
('Valkey test fixture', 'Automate digest-pinned rootless Valkey with OpenBao-sourced application ACL credentials, prefix isolation, TTLs and memory limits.', 'Authenticated set/get/delete, TTL/countdown and observed expiration pass; unauthenticated access and foreign key prefixes fail; eviction cannot become authoritative application state. Grant only the additional TTL-test command permissions needed; the current EX-option smoke does not establish expiry.'),
('Initialization secret delivery', 'Inventory every fixture/provisioning secret; deliver OpenBao-issued values through bounded memory/IPC or private short-lived tmpfs files when a service requires files. Replace persistent plaintext password/ACL copies and scope restart grants independently from runtime grants.', 'No project credential remains in .local plaintext custody, argv, container metadata, environment dumps or logs; interruption cleans delivery files. Restart after root revocation resolves the same vault-owned credential version; expiry, denied provisioning identity and missing TLS fail closed.'),
('Build and release secret delivery', 'Make public Rust initialization/builds secret-free. For private registries, publishing, signing and deployment, authenticate a bounded developer/workload identity to OpenBao and resolve project secrets there; qualify GitHub OIDC claim binding and secret-free pull-request workflows.', 'Public rustup/Cargo/checks need no secret or vault. Credential-requiring jobs deny sealed vault, wrong repository/ref/environment/audience and fork PRs; no project secret is stored in GitHub Secrets, committed Cargo credentials, artifacts or build caches. Short-lived delivery and cleanup/renewal are tested.'),
('Service lifecycle harness', 'Exercise idempotent start, stop/restart, readiness deadlines and failed provisioning recovery without touching unrelated containers.', 'Two starts converge; sealed OpenBao is unsealed from local test recovery material; PostgreSQL persists; cache can be empty; failures return nonzero.'),
('Freshness and supply-chain controls', 'Schedule weekly upstream checks, pin tool archive hashes and action commits, monitor SDK/services and record review decisions.', 'Newer stable, yanked, unavailable and prerelease metadata fixtures fail as specified; exact current upstream versions are verified before dependency changes.'),
],
3: [
('OpenBao SDK admission', 'Admit the latest stable openbao SDK into a dedicated std adapter with minimal reviewed features and server compatibility checks; keep it outside portable defaults.', 'Use the real TLS OpenBao fixture and compatibility policy; token and error diagnostics are redacted; no SDK transport types reach application APIs.'),
('Application secret references', 'Define service/build SecretRef resolution through scoped OpenBao identity, bounded delivery and lease/version metadata; inventory database/cache/search/bootstrap, session/signing/encryption, external integration and release credentials. Exclude user operation keys from default persistence.', 'Missing, expired and revoked credentials fail closed; no root token or recovery key is delivered to API/worker/build processes; cross-workspace secret requests fail; no host/SDK type enters portable contracts and no hardcoded/environment/file secret fallback exists.'),
('Secret rotation lifecycle', 'Implement token renewal, AppRole re-provisioning, credential rotation and restart convergence behind secret-store contracts.', 'Expiry, rotation during work, OpenBao outage and audit failure are exercised; old grants cannot be reused and no static secret fallback appears.'),
('Search service contracts', 'Define portable SearchService request/results, bounds, opaque cursors and declared capabilities during application contracts. Keep operation-picker search local. Plan repository and optional Meilisearch saved-metadata adapters with unchanged UI/API/schema and a std-only feature/runtime selector.', 'Default no_std graph admits no Meilisearch dependency; offline catalogue search and both hosted-backend contract fixtures cover query bounds, metadata projection and authorization. Ranking differences are explicit; filters/SDK types stay adapter-owned and unavailable features return declared errors.'),
],
66: [
('OpenBao database leases', 'Evaluate and qualify the current PostgreSQL database plugin; separate migration and runtime identities and map lease revocation to pool behavior.', 'Real leased login/expiry/revocation fixtures pass; stale pooled credentials are discarded; unsupported beta/plugin compatibility gets a new owned pass.'),
],
68: [
('Repository metadata search', 'With PostgreSQL persistence and workspace authorization available, implement bounded saved-recipe metadata search behind SearchService. Approve names, descriptions, tags/categories and collection IDs; exclude secret-bearing or sensitive metadata, operation arguments and all payloads.', 'Real PostgreSQL tests prove tenant/object permissions, malformed/bounded queries, deterministic pagination and immediate deletion/revocation. The UI/API works with Meilisearch disabled; local browser recipe search stays local.'),
('Search projection and outbox', 'Commit revisioned allowlisted search projections and outbox events atomically with repository changes; add idempotent retry, deletion tombstones, replay watermarks and bounded task/error retention.', 'Transaction rollback leaves no event; crashes, duplicate/reordered delivery, concurrent edit/delete and poison events cannot resurrect old projections. Projection contains no recipe/input/result/SecretRef values and is fully rebuildable from authorized metadata.'),
('Meilisearch Podman fixture', 'Admit the latest reviewed Meilisearch image into an explicitly enabled rootless Podman profile with resource bounds, private network and qualified TLS. Obtain its initial master key from OpenBao before startup; persist service-issued scoped API keys in OpenBao before delivery, separating provisioning, index writer and search reader.', 'Actual optional service start/restart passes; disabled profile starts no Meilisearch container and requests no Meilisearch credentials. Missing/revoked vault secrets, wrong TLS identity, unauthenticated requests and excessive key privileges fail; master keys never reach browser or application readers.'),
('Meilisearch metadata adapter', 'Implement runasmidja-search-meilisearch outside portable defaults using a current reviewed minimal client/SDK. Consume outbox projections, track asynchronous task completion/failure and expose bounded search candidates through the owned contract.', 'Real server tests cover task acceptance versus completion, failed indexing, retry, queue ceilings, malformed queries, deadlines, scoped reader/writer credentials and exact projection fields. Shared repository/Meilisearch conformance passes without backend DTOs leaking into API types.'),
('Search authorization and revocation', 'Enforce server-owned tenant filters and authoritative current database permission/revision checks before returning metadata. Derive visible snippets, facets, counts and pagination only from authorized current state; keep browsers behind the application API.', 'Two-tenant and same-tenant revoked-reader tests with a deliberately stale index reveal no hit, title, snippet, facet, count or object existence. Forged filter/cursor, stale edit/delete/revoke, permissions changed during a request and database outage deny access without trusting index grants.'),
('Search backend switching and recovery', 'Qualify explicit repository/meilisearch runtime selection, std-only optional feature and an authorized repository fallback on Meilisearch outage. Rebuild/switch using outbox watermarks without data/schema/UI migration; declare ranking/freshness differences and enforce bounded recovery.', 'Run website/API tests in both compiled profiles and both runtime modes; disabled mode needs no search service/secrets. Outage, task failure, key rotation, corrupted/lost index, pagination across switches and cutover/replay drills preserve current permissions and database truth; performance measurements tune deployment choice rather than cancel adapter work.'),
],
70: [
('Valkey application adapter', 'Implement bounded optional metadata/cache access behind application-owned CacheStore with scoped keys and revision-aware identities.', 'Cache miss, outage, poison, stale revision and cross-tenant probes pass against Valkey; authoritative data and permissions survive without cache.'),
('Valkey invalidation and outage', 'Prove TTL, revocation invalidation, resource ceilings and eviction behavior without giving cache authority over authorization.', 'Revoked grants are checked against authoritative state; connection failures do not bypass quotas; cache poisoning and invalidation races have regressions.'),
],
74: [
('Service TLS deployment policy', 'Qualify native PostgreSQL/Valkey/OpenBao TLS, certificate identity, trust roots and private service networks independently of local fixture shortcuts.', 'Wrong names, unknown roots, expired certificates, missing TLS and unauthorized service clients fail; deployment never publishes administrative endpoints.'),
('OpenBao production recovery custody', 'Separate production recovery shares, initial bootstrap identity and app credentials; automate operational configuration and rehearse restore and rotation.', 'Independent custody/recovery, audit-disk failure, snapshot restore and expired bootstrap identity are tested; one-share local test material is rejected in production.'),
('PostgreSQL beta-to-GA upgrade drill', 'When available admit PostgreSQL 19 GA after upstream review; rehearse dump/restore or documented upgrade from the beta baseline.', 'Restore and repository/authorization fixtures pass on pinned GA; no beta data directory is reused blindly; rollback is executable and 1.0 uses GA.'),
],
211: [
('Shared-collection search integration', 'Extend the already-qualified repository and Meilisearch search projections to server collections, sharing and revision policies through the same SearchService contract.', 'Both backends pass collection-sharing, inherited/revoked grants, revision edits, stale-index and recovery tests; names/tags remain an approved projection and secret-bearing collection metadata is excluded.'),
],
225: [
('Integrated service recovery gate', 'Rehearse coordinated PostgreSQL/artifact restore, OpenBao recovery/rotation, Valkey cold start and optional search rebuild.', 'A restored deployment serves authorized recipes and can run them; cache/search loss does not lose authoritative data; all recovery steps are automated or explicitly custody-gated.'),
],
}

PHASE_VERIFY = {
'Z': 'Exercise real services, startup failure, authorization denials, restart and redacted diagnostics.',
'A': 'Exercise browser/native boundary, malformed contracts, stale worker generations and absence of payload network traffic.',
'B': 'Run independent/reference vectors, malformed/empty inputs, each argument variant and exhaustive short-input chunk partitions.',
'C': 'Use tiny budgets, reconverging joins, cancellation at terminal transitions, process crashes and orphaned artifacts.',
'D': 'Run real Chromium/Firefox/WebKit workflows with keyboard use, hostile output, quota failure and no optional browser APIs.',
'E': 'Run real services and permission/lifecycle negatives only for behavior introduced or retained by this bounded pass. Minimal SQL lease races belong to v0.107.0, hosted publication to v0.112.0, supervisor faults to v0.119.0–v0.120.0, heartbeat/retry to v0.124.0 and egress to v0.125.0–v0.127.0; run each suite when its implemented scope is reached. Earlier API schema/loopback fixtures do not attest these later runtime controls.',
'F': 'Run exact dialect fixtures, invalid syntax, depth/length/work exhaustion and browser/native representation comparisons.',
'G': 'Run truncated/corrupt format corpora, expansion/nesting/entry ceilings, short output windows and traversal/link attacks.',
'H': 'Run independently sourced crypto vectors, secret-lifecycle and bad-parameter tests; authenticated plaintext stays staged until verification.',
'I': 'Run historical vectors and exact argument semantics; all legacy-operation features must leave TLS/account security unchanged.',
'J': 'Run format/algorithm vectors, malformed keys and trust-confusion cases; parsing, validity and trust remain distinct.',
'K': 'Run passive-data fixtures and explicit network capability denials, SSRF/rebinding/redirect cases and hostile analysis cost limits.',
'L': 'Run codec/model provenance, malformed dimension/frame/decompression cases, inert previews and browser/native result comparisons.',
'M': 'Run whole-recipe differentials, backwards jumps, nested control, defaults, lossless interchange and work exhaustion.',
'N': 'Run alternate adapter/provider contracts, plugin hostile imports/memory/work tests and default builds without sibling directories.',
'O': 'Use real database backends and operational cutover, crash/restore/rollback, revocation and data-integrity drills.',
'P': 'Run the cumulative capability/argument/recipe/UI/target inventory on exact artifacts; missing evidence blocks production claims.',
}


def build():
    baseline = json.loads(SOURCE.read_text())
    strict = json.loads((DOCS / 'roadmap-input/reference-verification.json').read_text())
    if not isinstance(strict, dict) or set(strict) != {row['version'] for row in baseline['releases']}:
        raise ValueError('Every source workstream needs one reviewed verification gate')
    if any(not isinstance(gate, str) or not gate.strip() for gate in strict.values()):
        raise ValueError('Every verification gate must be a nonblank string')
    rows = []
    def add(title, deliverable, acceptance, phase, source=None, narrow=False):
        number = len(rows) + 1
        rows.append(dict(version=f'0.{number}.0', title=title, deliverable=deliverable,
            acceptance=acceptance, phase=phase, source_version=source, narrow=narrow,
            strict_verification=strict[source] if source else '',
            status='planned', depends_on=[] if number == 1 else [f'0.{number-1}.0']))
        if source in SOURCE_CONTEXT:
            rows[-1]['scope_context'] = SOURCE_CONTEXT[source]
    for title, deliverable, acceptance in strengthen_foundation(EXTRAS[0]):
        add(title, deliverable, acceptance, 'Z')
    for item in order_source(baseline['releases']):
        minor = int(item['version'].split('.')[1])
        topics = SPLITS.get(minor)
        if topics:
            for topic in topics:
                deliverable = f"Deliver only {topic.lower()} within the source workstream: {item['deliverable']}"
                if minor == 12:
                    deliverable = f'Qualify {topic.lower().removesuffix(" feasibility")} in isolated native/browser spikes; record exact semantics, current provider versions, licenses, dependencies, limits and gaps. No production capability is implied.'
                add(topic, deliverable, 'For this scoped topic: ' + item['acceptance'], item['phase'], item['version'], True)
        else:
            add(item['title'], item['deliverable'], item['acceptance'], item['phase'], item['version'])
        # Concrete artifact/authority prerequisites precede their search consumers.
        for title, deliverable, acceptance in ADDITIONS.get(minor, []) + EXTRAS.get(minor, []):
            add(title, deliverable, acceptance, item['phase'])
    by_title = {row['title']: row for row in rows}
    container_context = {
        'Service lifecycle harness': 'At v0.11.0 add an actual rootless Fluxheim Wolfi proxy fixture for the bounded health probe, using only the official published proxy-wolfi image pinned by digest; do not build or repackage Fluxheim. Verify current version, publisher/platform, scans and inventory before admission. Test direct native/container backends and real proxy routing/rejections, outage/restart, timeout bounds and spoofed forwarding headers; freeze the minimal HTTP/TLS trust scope. Automate owned private-network configuration and cleanup without exposing admin services. This is health-fixture evidence only, not production/browser/session/upload qualification.',
        'Freshness and supply-chain controls': 'Include the admitted Fluxheim image/release, exact proxy/base/source identities and per-image scan/SBOM evidence. Review current accessible Wolfi service images; same-base packaging never replaces publisher, runtime or vulnerability checks.',
        'Meilisearch Podman fixture': 'Prefer a reviewed current minimal Wolfi runtime at v0.115.0 admission, with actual source/ABI/TLS/access/provenance qualification. Do not build an unused search service during v0.2 patches or assume a paid Chainguard OS image is Wolfi. Disabled search remains independent of its image and credentials.',
        'Server deployment profile': 'At v0.129.0 run the actual website/API directly and behind the current reviewed official focused Fluxheim Wolfi proxy image, pinned by digest without a Runasmidja rebuild. Qualify trusted proxy peers, forged Forwarded/X-Forwarded/PROXY claims, external scheme/host/origin, secure cookies/redirects, streaming/cancellation, limits, cache exclusions and admitted WebSocket/SSE behavior. Backend/admin bypass stays private; sibling paths are not deployment dependencies.',
        'Service TLS deployment policy': 'At v0.130.0 include real Fluxheim client and admitted upstream TLS/mTLS, wrong identities/roots/expiry and spoofed TLS-termination metadata, plus direct-TLS parity. Proxy termination does not replace database/cache/vault TLS. All project keys/credentials follow OpenBao policy and enumerated vault bootstrap trust custody.',
        'Server security gate': 'At v0.133.0 pentest the combined Fluxheim/Runasmidja deployment for forwarded identity, request framing/smuggling, auth/object/origin/cache/rate-limit bypass and backend/admin exposure. A separately green proxy cannot attest application integration.',
        'Release packaging': 'At v0.366.0 and RC/1.0 rerun direct and Fluxheim Wolfi deployment qualification on exact artifacts with reviewed proxy/config versions, notices/inventories and restore/rollback/upgrade evidence; retain both Meilisearch profiles.',
    }
    for title, context in container_context.items():
        row = by_title[title]
        row['scope_context'] = (row.get('scope_context', '') + ' ' + context).strip()
    publication = by_title['Hosted artifact publication fencing']
    publication['prerequisites'] = [by_title[title]['version'] for title in PUBLICATION_PREREQUISITES]
    if any(int(version.split('.')[1]) >= int(publication['version'].split('.')[1])
           for version in publication['prerequisites']):
        raise ValueError('Hosted publication requires earlier qualified fencing/storage/authority')
    continuation = f'0.{len(rows) + 1}.0'
    ga = next(row for row in rows if row['source_version'] == '0.240.0')
    ga['scope_context'] = ('The retained reference acceptance mentions 0.241.0 as historical reference numbering. '
        f'Actual additional Runasmidja passes start at v{continuation}; do not reuse historical reference versions.')
    plans = DOCS / 'releases'; plans.mkdir(exist_ok=True)
    data_dir = DOCS / 'roadmap'; data_dir.mkdir(exist_ok=True)
    index = ['# Runasmidja Release Plan To 1.0.0', '', 'Status: roadmap contract; v0.1.0/v0.2.0/v0.2.1 tagged; v0.2.2 implementation candidate; maintainer pentest PASS; GitHub and tag pending.',
             'The authorized Wolfi/PostgreSQL fixture passes scans and real qualification; see the',
             '[assessment](../security/pentest/v0.2.0.md).', '',
        f'{len(rows)} small pre-1.0 passes, starting at 0.1.0 and ending at {rows[-1]["version"]}. Add further minors whenever inventory, provider work or qualification needs a smaller pass. Version 1.0.0 is the first serious production release.', '',
        'The supplied 240-release bundle is preserved under [reference](reference/workbench-plan/README.md). Runasmidja adds operational services and splits multi-provider/algorithm work; source-version mappings preserve every original workstream. Nothing in this plan claims an implementation or a completed pentest.', '',
        f'If mandatory gaps remain after {rows[-1]["version"]}, actual additional passes start at **v{continuation}**. Historical reference continuation numbers remain preserved as provenance, not actual version assignments.', '',
        '## Setup and scope rules', '',
        '- Run Rust 1.99.0 initially; review official stable, crate, tool, action and service metadata weekly and before changes.',
        '- Before each pass, write its exact API/operation/argument scope, target profile, numeric resource ceilings and test IDs. One new algorithm, dialect, persistent contract or trust boundary per pass.',
        '- All code files stay at or below 500 lines; focused crates and independently tested adapters preserve no_std and future Vef/Brynja extraction.',
        '- OpenBao is the source for every project-operated initialization, runtime, build and release secret; consumers start only after scoped retrieval. Minimal vault bootstrap/recovery trust has separate custody; public Rust builds and browser-local user inputs require no vault.',
        '- SearchService is an early portable contract. Repository search and optional Meilisearch are required implementation/test profiles before production; optional deployment is not deferred implementation. Index only approved nonsensitive metadata and recheck current database authorization.',
        '- A family row is an inventory owner. If it contains independent algorithms or dialects after source reconciliation, split it into additional numbered passes before coding; never hide feature work in a patch.',
        '- The predecessor is the baseline. A later capability is never assumed available; move or split the consumer if a concrete prerequisite is discovered.',
        '- Freeze exact variants, targets/features, numeric byte/work/state/depth/deadline ceilings, capability policy, fixture provenance, test IDs and evidence locations in a reviewed scope manifest. TBD/placeholder fields block acceptance.',
        '- The first hex seed is bounded by the earlier tested value/budget vocabulary and minimal worker messages. It proves one transformation, not the later scheduler or full recipe IR; fuel/byte limits apply from the first execution.',
        '- API work before the integrated server security gate is loopback/private integration only. Public untrusted-job routes require verified authority, isolation, admission, fencing, egress, TLS and recovery together.',
        '- Every fixture mutation needs verified ownership now, including concrete minimum checks in 0.2.0; the later ownership/drift pass expands fingerprints and negative coverage, never authorizes earlier name-only mutation or silent state reset.',
        '- Imported operation names remain provisional until the immutable CyberChef inventory confirms exact variants and redistribution rights. Unsupported required variants remain blocking gaps.', '',
        '## Every release gate', '',
        'The [browser security profiles](BROWSER_SECURITY_PROFILES.md) define origin-compromise limits, separate local-only/remote applications and independently verified signed offline artifacts with network-disabled execution. Explicit seed/privacy/workbench/loader/offline/server/packaging owners qualify document/worker CSP, Trusted Types, COOP/COEP/CORP, framing and permissions; no browser enforcement is claimed by the foundation.', '',
        'Run `scripts/checks.sh`, current dependency/license/advisory checks, freshness, applicable browser/reference/service/fuzz/fault suites and artifact SBOM generation. Update threat controls, limitations, parity evidence, CHANGELOG and release notes. Every numbered minor, patch, RC and 1.0 needs its own exact-source pentest, remediation and clean retesting before tagging; passing tests alone do not authorize a PASS report.', '',
        'The [release runbook](RELEASE_RUNBOOK.md) and [version policy](VERSIONING_POLICY.md) define the handoff. Build and verify locally, commit completed candidates as needed, and stop for the maintainer’s pentest. Finalize acceptance only after green. The maintainer pushes; repeat GitHub fixes and affected pentest retests until green. Tag and push the version tag only when explicitly requested; distribution publication needs separate authorization.', '',
        'The [search design](SEARCH_DESIGN.md) and [secret lifecycle](SECRETS_POLICY.md) define required trust boundaries. The current bounded patch is [v0.2.2 Wolfi Valkey fixture](releases/v0.2.2-scope.md); v0.3.0 remains the next minor. The released [v0.2.0 fixture](releases/v0.2.0-scope.md) issues database/cache passwords in OpenBao; the legacy v0.1 fixture is retained unchanged. Temporary delivery, build/release identity and full drift qualification remain later numbered passes.', '',
        'The [container and Fluxheim plan](CONTAINER_DEPLOYMENT_PLAN.md) proposes compatible v0.2.1-v0.2.3 image follow-ups, without renumbering the minor workstreams. Fluxheim Wolfi proxy qualification is required at v0.11.0 (health fixture), v0.12.0 (freshness), v0.129.0/v0.130.0/v0.133.0 (actual deployment/TLS/security) and v0.366.0/RC/1.0 (exact artifacts). Meilisearch preferred-base admission remains v0.115.0. v0.2.1 is tagged; v0.2.2 has maintainer pentest acceptance; GitHub and tag are pending; v0.2.3 remains proposed.', '',
        'The [2026-10-03 planning revision](plan-revision-2026-10-03.md) records moved owners and qualification limits. Unpublished version assignments changed; the supplied source-version mapping remains intact.', '',
        'The [gap reconciliation](gap-reconciliation-2026-10-03.md), [execution contracts](EXECUTION_CONTRACTS.md), [browser/performance policy](BROWSER_PERFORMANCE.md), [storage/host policy](STORAGE_HOST_CONTRACTS.md) and [strict gates](VERIFICATION_GATES.md) add reviewed requirements; no runtime remediation is claimed by this plan.', '',
        '## Per-version handoffs', '', '| Phase | Versions | Detailed handoffs |', '| --- | --- | --- |']
    for phase in ['Z'] + [p['id'] for p in baseline['phases']]:
        group = [row for row in rows if row['phase'] == phase]
        filename = f'phase-{phase.lower()}.md'
        title = 'Repository and service foundation' if phase == 'Z' else next(p['title'] for p in baseline['phases'] if p['id'] == phase)
        text = [f'# Phase {phase}: {title}', '', 'Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).', '',
            'Verification checklists apply only to introduced or retained behavior in the reviewed bounded scope. Record absent later capabilities as pending with numbered owners; contract fixtures never attest their runtime PASS. A prerequisite needed by this pass must be implemented and verified first, rather than deferred. Every future owner still owes its full acceptance before exposure/1.0.', '']
        for row in group:
            version = row['version']
            predecessor = ', '.join(row['depends_on']) or 'empty initialized repository'
            prerequisite_note = (' Required qualified prerequisites: ' + ', '.join(row['prerequisites']) +
                '; PostgreSQL minimal lease/fencing implementation must already pass.') if row.get('prerequisites') else ''
            text += [f'## v{version} — {row["title"]}', '', '**Status:** planned.', '',
                f'**Setup:** baseline {predecessor}; verify current upstream sources and record a bounded scope manifest before coding.' + prerequisite_note, '',
                f'**Goal:** {row["title"]}.', '',
                f'**Scope:** one reviewable pass in this workstream. ' + (f'Source bundle owner {row["source_version"]}; implement only the named topic. Retained family acceptance/strict gates apply to this topic; other algorithms remain with their mapped owners. The source workstream closes only when every mapped owner qualifies.' if row['narrow'] else 'Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.'), '',
                '**Deliverables:** ' + ' '.join(filter(None, [row['deliverable'].replace('workbench-', 'runasmidja-'), row.get('scope_context')])) + ' Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.', '',
                '**Verification:** ' + ' '.join(filter(None, [row['acceptance'], row['strict_verification'], PHASE_VERIFY[phase]])) + ' Apply G0–G6 and applicable G7 from the strict gates. Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.', '',
                f'**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v{version} implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.', '']
        (plans / filename).write_text('\n'.join(text))
        # One record per line keeps data assets compact and reviewable.
        (data_dir / f'phase-{phase.lower()}.json').write_text('[\n' + ',\n'.join('  ' + json.dumps(row) for row in group) + '\n]\n')
        index.append(f'| {phase}: {title} | {group[0]["version"]}–{group[-1]["version"]} | [Milestones](releases/{filename}) |')
    index += ['', '## Release candidates and production', '',
        '### v1.0.0-rc.1', '', '**Status:** planned.', '', '**Setup:** every required pre-1.0 inventory row and qualification result is closed; PostgreSQL 19 GA, current OpenBao/Valkey, optional Meilisearch and exact artifacts are pinned. Both search profiles and OpenBao secret-source/initialization/build/recovery gates are qualified.', '',
        '**Goal:** qualify the first complete production candidate.', '', '**Scope:** freeze features; substantial missing work returns to new 0.x releases.', '',
        '**Deliverables:** complete website/API, offline operation packs, five parity matrices, SBOM/notices, signed artifact manifests, deployment/recovery instructions and independent consumer examples.', '',
        '**Verification:** actual supported browsers/native hosts; independent security assessment; auth/SSRF/cache/plugin/failure tests; real PostgreSQL/MySQL migration proof; backup/restore; Vef/Brynja seam tests; privacy and accessibility.', '',
        '**Exit criteria:** exact artifacts pass the complete acceptance contract with no required gaps or exploitable critical/high findings. v1.0.0-rc.1 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.', '',
        '### v1.0.0-rc.N', '', '**Status:** planned as needed.', '', '**Setup:** preceding candidate and individually scoped blocking fixes.', '',
        '**Goal:** qualify remediated candidate artifacts.', '', '**Scope:** compatible fixes and artifact regeneration; missing features receive 0.x owners.', '',
        '**Deliverables:** regressions, revised evidence/notes and newly built candidate artifacts.', '',
        '**Verification:** rerun all affected suites and full candidate acceptance, including security and operational restoration.', '',
        '**Exit criteria:** no remaining blocker; every previous finding has tested disposition. v1.0.0-rc.N implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.', '',
        '### v1.0.0', '', '**Status:** planned.', '', '**Setup:** qualifying exact RC source and artifacts; complete evidence reviewed.', '',
        '**Goal:** release the first serious production-ready Runasmidja website, reusable engine and public API.', '',
        '**Scope:** complete declared CyberChef functionality on browser/native profiles, PostgreSQL production support and verified replacement boundaries; future desktop/mobile GUI milestones remain post-1.0.', '',
        '**Deliverables:** supported distributions, maintenance policy, full operation/API docs, production security/recovery guides and release notes.', '',
        '**Verification:** verify all operation/argument/recipe/UI/target rows, both search profiles with live authorization, OpenBao-sourced project secrets from initialization through release, exact distribution provenance, current security findings and executed deployment/upgrade/recovery procedures.', '',
        '**Exit criteria:** all required functionality and evidence pass; no beta database or unsupported production claim remains. v1.0.0 implementation stop reached. Run the maintainer’s pentest for this exact source candidate before committing new work.', '',
        '## After 1.0', '', '1.1: Linux/Windows/BSD/macOS desktop preview. 1.2: qualified desktop stable. 1.3: Android/iOS preview. 1.4: qualified mobile stable. Aesynx receives a separate conditional adapter/GUI milestone once runnable APIs exist. Each platform needs its own compile, runtime, filesystem/secret-storage, accessibility, packaging and update-security evidence. API compatibility survives independent client release versions.', '']
    (DOCS / 'RELEASE_PLAN.md').write_text('\n'.join(index))
    (DOCS / 'VERSION_PLAN.md').write_text('# Runasmidja Version Plan\n\nThe authoritative [release plan](RELEASE_PLAN.md) links every detailed handoff.\n\n' +
        f'Pre-1.0: 0.1.0 through {rows[-1]["version"]}, then actual further passes starting at v{continuation} as required. RCs and 1.0 are evidence gates, not dates.\n\n' +
        'The [phase data](roadmap/phase-z.json) and remaining phase files preserve source-version mappings, predecessors, original acceptance and additive strict verification. Regenerate with `python3 scripts/build_plan.py`; every original baseline release has at least one mapped owner.\n\n' +
        'Current version owners and reviewed scheduling corrections are recorded in the [gap reconciliation](gap-reconciliation-2026-10-03.md). The preserved reference and earlier evidence/revisions keep their original version numbers.\n')
    print(f'Rendered {len(rows)} pre-1.0 milestones, through {rows[-1]["version"]}')

if __name__ == '__main__':
    build()
