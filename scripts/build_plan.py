#!/usr/bin/env python3
"""Render Runasmidja release handoffs from reviewed source plus service passes."""
import json
from pathlib import Path

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
('PostgreSQL 19 beta 4 test fixture', 'Pin PostgreSQL 19 beta 4 by digest; automate rootless Podman, private credentials, readiness and a separate runtime role.', 'A real container reports 19beta4, transaction rollback works, runtime role has no superuser or role-management powers, and only loopback ports are published.'),
('OpenBao test bootstrap', 'Automate TLS identity, persistent single-node storage, declarative audit, KV v2, scoped AppRole, root-token revocation and private recovery material.', 'Initialization and restart work; AppRole reads only runtime secrets; mounts and other secret paths return 403; no credential is printed or tracked.'),
('Valkey test fixture', 'Automate digest-pinned rootless Valkey with application ACL, prefix isolation, TTLs and memory limits.', 'Authenticated set/get/delete works; unauthenticated access and foreign key prefixes fail; eviction cannot become authoritative application state.'),
('Service lifecycle harness', 'Exercise idempotent start, stop/restart, readiness deadlines and failed provisioning recovery without touching unrelated containers.', 'Two starts converge; sealed OpenBao is unsealed from local test recovery material; PostgreSQL persists; cache can be empty; failures return nonzero.'),
('Freshness and supply-chain controls', 'Schedule weekly upstream checks, pin tool archive hashes and action commits, monitor SDK/services and record review decisions.', 'Newer stable, yanked, unavailable and prerelease metadata fixtures fail as specified; exact current upstream versions are verified before dependency changes.'),
],
66: [
('OpenBao SDK admission', 'Admit the latest stable openbao SDK into a dedicated std adapter with minimal reviewed features and server compatibility checks; keep it outside portable defaults.', 'Use the real TLS OpenBao fixture and compatibility policy; token and error diagnostics are redacted; no SDK transport types reach application APIs.'),
('Application secret references', 'Connect service configuration and SecretRef resolution to scoped AppRole with leased credentials; exclude recipe-operation keys from default persistence.', 'Missing, expired and revoked credentials fail closed; no root token or recovery key is delivered to API/worker processes; cross-workspace secret requests fail.'),
('Secret rotation lifecycle', 'Implement token renewal, AppRole re-provisioning, credential rotation and restart convergence behind secret-store contracts.', 'Expiry, rotation during work, OpenBao outage and audit failure are exercised; old grants cannot be reused and no static secret fallback appears.'),
('OpenBao database leases', 'Evaluate and qualify the current PostgreSQL database plugin; separate migration and runtime identities and map lease revocation to pool behavior.', 'Real leased login/expiry/revocation fixtures pass; stale pooled credentials are discarded; unsupported beta/plugin compatibility gets a new owned pass.'),
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
('Search boundary and measurement', 'Keep operation search local over descriptors; benchmark authorization-filtered saved-recipe search and define an optional SearchIndex boundary.', 'Offline catalogue search works; metadata search obeys permissions and revocation; payloads, keys and decoded results never enter a search index.'),
('Conditional Meilisearch qualification', 'Admit Meilisearch only if measured metadata-search needs justify another service; otherwise record the benchmark decision and use existing search.', 'If admitted: Podman TLS/auth, tenant isolation, outbox replay, revocation/deletion lag and index rebuild pass; if declined: documented thresholds and equivalent search tests pass.'),
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
'E': 'Run real PostgreSQL/OpenBao/Valkey tests, cross-principal object denials, lease races, egress and supervisor failures.',
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
    rows = []
    def add(title, deliverable, acceptance, phase, source=None, narrow=False):
        number = len(rows) + 1
        rows.append(dict(version=f'0.{number}.0', title=title, deliverable=deliverable,
            acceptance=acceptance, phase=phase, source_version=source, narrow=narrow,
            status='planned', depends_on=[] if number == 1 else [f'0.{number-1}.0']))
    for title, deliverable, acceptance in EXTRAS[0]:
        add(title, deliverable, acceptance, 'Z')
    for item in baseline['releases']:
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
        for title, deliverable, acceptance in EXTRAS.get(minor, []):
            add(title, deliverable, acceptance, item['phase'])
    plans = DOCS / 'releases'; plans.mkdir(exist_ok=True)
    data_dir = DOCS / 'roadmap'; data_dir.mkdir(exist_ok=True)
    index = ['# Runasmidja Release Plan To 1.0.0', '', 'Status: planned; workspace initialized, no release tagged.', '',
        f'{len(rows)} small pre-1.0 passes, starting at 0.1.0 and ending at {rows[-1]["version"]}. Add further minors whenever inventory, provider work or qualification needs a smaller pass. Version 1.0.0 is the first serious production release.', '',
        'The supplied 240-release bundle is preserved under [reference](reference/workbench-plan/README.md). Runasmidja adds operational services and splits multi-provider/algorithm work; source-version mappings preserve every original workstream. Nothing in this plan claims an implementation or a completed pentest.', '',
        '## Setup and scope rules', '',
        '- Run Rust 1.99.0 initially; review official stable, crate, tool, action and service metadata weekly and before changes.',
        '- Before each pass, write its exact API/operation/argument scope, target profile, numeric resource ceilings and test IDs. One new algorithm, dialect, persistent contract or trust boundary per pass.',
        '- All code files stay at or below 500 lines; focused crates and independently tested adapters preserve no_std and future Vef/Brynja extraction.',
        '- A family row is an inventory owner. If it contains independent algorithms or dialects after source reconciliation, split it into additional numbered passes before coding; never hide feature work in a patch.',
        '- The predecessor is the baseline. A later capability is never assumed available; move or split the consumer if a concrete prerequisite is discovered.',
        '- Imported operation names remain provisional until the immutable CyberChef inventory confirms exact variants and redistribution rights. Unsupported required variants remain blocking gaps.', '',
        '## Every release gate', '',
        'Run `scripts/checks.sh`, current dependency/license/advisory checks, freshness, applicable browser/reference/service/fuzz/fault suites and artifact SBOM generation. Update threat controls, limitations, parity evidence, CHANGELOG and release notes. Every numbered minor, patch, RC and 1.0 needs its own exact-source pentest, remediation and clean retesting before tagging; passing tests alone do not authorize a PASS report.', '',
        'The [release runbook](RELEASE_RUNBOOK.md) and [version policy](VERSIONING_POLICY.md) define the handoff. Tagging/publication is separate from this setup task.', '',
        '## Per-version handoffs', '', '| Phase | Versions | Detailed handoffs |', '| --- | --- | --- |']
    for phase in ['Z'] + [p['id'] for p in baseline['phases']]:
        group = [row for row in rows if row['phase'] == phase]
        filename = f'phase-{phase.lower()}.md'
        title = 'Repository and service foundation' if phase == 'Z' else next(p['title'] for p in baseline['phases'] if p['id'] == phase)
        text = [f'# Phase {phase}: {title}', '', 'Status: planned. Requirements below are additive to the [common gates](../RELEASE_PLAN.md).', '']
        for row in group:
            version = row['version']
            predecessor = ', '.join(row['depends_on']) or 'empty initialized repository'
            text += [f'## v{version} — {row["title"]}', '', '**Status:** planned.', '',
                f'**Setup:** baseline {predecessor}; verify current upstream sources and record a bounded scope manifest before coding.', '',
                f'**Goal:** {row["title"]}.', '',
                f'**Scope:** one reviewable pass in this workstream. ' + (f'Source bundle owner {row["source_version"]}; implement only the named topic, preserving the other topics for their mapped passes.' if row['narrow'] else 'Split independent remaining implementations before starting if the reconciled inventory exceeds this pass.'), '',
                '**Deliverables:** ' + row['deliverable'].replace('workbench-', 'runasmidja-') + ' Include descriptor/API documentation, negative fixtures, limitations and release notes for the scoped behavior.', '',
                '**Verification:** ' + row['acceptance'] + ' ' + PHASE_VERIFY[phase] + ' Run common gates and record actual commands, targets and evidence; mocks do not prove a real service/browser/provider capability.', '',
                f'**Exit criteria:** the scoped deliverables and verification pass, all required gaps have numbered owners, and security/doc/evidence deltas are reviewed. v{version} implementation stop reached. Run pentest for this exact commit.', '']
        (plans / filename).write_text('\n'.join(text))
        # One record per line keeps data assets compact and reviewable.
        (data_dir / f'phase-{phase.lower()}.json').write_text('[\n' + ',\n'.join('  ' + json.dumps(row) for row in group) + '\n]\n')
        index.append(f'| {phase}: {title} | {group[0]["version"]}–{group[-1]["version"]} | [Milestones](releases/{filename}) |')
    index += ['', '## Release candidates and production', '',
        '### v1.0.0-rc.1', '', '**Status:** planned.', '', '**Setup:** every required pre-1.0 inventory row and qualification result is closed; PostgreSQL 19 GA, current OpenBao/Valkey and exact artifacts are pinned.', '',
        '**Goal:** qualify the first complete production candidate.', '', '**Scope:** freeze features; substantial missing work returns to new 0.x releases.', '',
        '**Deliverables:** complete website/API, offline operation packs, five parity matrices, SBOM/notices, signed artifact manifests, deployment/recovery instructions and independent consumer examples.', '',
        '**Verification:** actual supported browsers/native hosts; independent security assessment; auth/SSRF/cache/plugin/failure tests; real PostgreSQL/MySQL migration proof; backup/restore; Vef/Brynja seam tests; privacy and accessibility.', '',
        '**Exit criteria:** exact artifacts pass the complete acceptance contract with no required gaps or exploitable critical/high findings. v1.0.0-rc.1 implementation stop reached. Run pentest for this exact commit.', '',
        '### v1.0.0-rc.N', '', '**Status:** planned as needed.', '', '**Setup:** preceding candidate and individually scoped blocking fixes.', '',
        '**Goal:** qualify remediated candidate artifacts.', '', '**Scope:** compatible fixes and artifact regeneration; missing features receive 0.x owners.', '',
        '**Deliverables:** regressions, revised evidence/notes and newly built candidate artifacts.', '',
        '**Verification:** rerun all affected suites and full candidate acceptance, including security and operational restoration.', '',
        '**Exit criteria:** no remaining blocker; every previous finding has tested disposition. v1.0.0-rc.N implementation stop reached. Run pentest for this exact commit.', '',
        '### v1.0.0', '', '**Status:** planned.', '', '**Setup:** qualifying exact RC source and artifacts; complete evidence reviewed.', '',
        '**Goal:** release the first serious production-ready Runasmidja website, reusable engine and public API.', '',
        '**Scope:** complete declared CyberChef functionality on browser/native profiles, PostgreSQL production support and verified replacement boundaries; future desktop/mobile GUI milestones remain post-1.0.', '',
        '**Deliverables:** supported distributions, maintenance policy, full operation/API docs, production security/recovery guides and release notes.', '',
        '**Verification:** verify all operation/argument/recipe/UI/target rows, exact distribution provenance, current security findings and executed deployment/upgrade/recovery procedures.', '',
        '**Exit criteria:** all required functionality and evidence pass; no beta database or unsupported production claim remains. v1.0.0 implementation stop reached. Run pentest for this exact commit.', '',
        '## After 1.0', '', '1.1: Linux/Windows/BSD/macOS desktop preview. 1.2: qualified desktop stable. 1.3: Android/iOS preview. 1.4: qualified mobile stable. Aesynx receives a separate conditional adapter/GUI milestone once runnable APIs exist. Each platform needs its own compile, runtime, filesystem/secret-storage, accessibility, packaging and update-security evidence. API compatibility survives independent client release versions.', '']
    (DOCS / 'RELEASE_PLAN.md').write_text('\n'.join(index))
    (DOCS / 'VERSION_PLAN.md').write_text('# Runasmidja Version Plan\n\nThe authoritative [release plan](RELEASE_PLAN.md) links every detailed handoff.\n\n' +
        f'Pre-1.0: 0.1.0 through {rows[-1]["version"]}, then further 0.x passes as required. RCs and 1.0 are evidence gates, not dates.\n\n' +
        'The [phase data](roadmap/phase-z.json) and remaining phase files preserve source-version mappings, predecessors and acceptance. Regenerate with `python3 scripts/build_plan.py`; every original baseline release has at least one mapped owner.\n')
    print(f'Rendered {len(rows)} pre-1.0 milestones, through {rows[-1]["version"]}')

if __name__ == '__main__':
    build()
