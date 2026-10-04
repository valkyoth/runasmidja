# Automated Local Stack

Linux/rootless Podman, Python 3.11+, OpenSSL/Skopeo CLIs and free loopback ports
15432/18200/16379 are required. Python orchestrates tests; product code is Rust.
The public PostgreSQL build additionally requires systemd 254+ user delegation
and cgroup v2 CPU/memory/PID controllers; unsupported containment fails closed.

```sh
python3 scripts/install_image_tools.py
python3 scripts/image_gate.py
python3 scripts/stack.py up
python3 scripts/stack.py smoke
python3 scripts/stack.py status
python3 scripts/stack.py stop
python3 scripts/stack_qualification.py
python3 scripts/qualification_bounds.py
python3 scripts/qualification_postgres.py
python3 scripts/build_sandbox.py --qualify
```

PostgreSQL 19beta4 now builds automatically from pinned official source on a
verified Wolfi base; no manual database installation is needed. The three current
runtime inventories have zero blocking UNKNOWN/HIGH/CRITICAL findings. OpenBao
retains one expiring not-affected UNKNOWN review; see the
[advisory evidence](../security/advisories/README.md). The original
official PostgreSQL image remains rejected (42 findings), not waived. See the
[remediation report](../security/pentest/v0.2.0.md) and
[image inventories](../sbom/images/README.md).
Cosign and Trivy are installed under ignored `.local/tools`, verified against
reviewed artifact hashes; Trivy also requires its publisher Sigstore bundle.
Cosign refreshes its normal user trust cache. No OS package upgrade is required.

OpenBao requires the exact signed release index, GitHub workflow identity/OIDC
issuer and Linux/amd64 leaf. The Wolfi base also requires its exact signed index,
reviewed Chainguard workflow/issuer and platform leaf. The source-build receipt
binds the reviewed recipe, source checksum, immutable local image ID and archive
config/layers; it is trusted-host custody, not a portable signed release.
APK uses the base's bundled repository signing keys. See the
[recipe and supported profile](../deploy/podman/postgres/README.md).
The maintainer accepted provenance exceptions for the original exact unsigned
PostgreSQL/Valkey digests; only Valkey still uses this active exception. They
do not waive CVEs and must be reviewed again on digest changes. Startup always
scans, with unfixed findings included and no ignore/VEX filter. CI retains
per-image SBOMs even when scans fail.

The v0.2 fixture uses `.local/stacks/v02-reviewed` and
`runasmidja-v02-reviewed-*` containers,
network and PostgreSQL volume. `RUNASMIDJA_STACK_ID` accepts a bounded lowercase
identifier for a separate test profile; ports stay fixed, so run only one profile
at a time. Every mutation verifies project/service/instance ownership labels.
Stop preflights all resources before stopping anything. Reused containers must
match the digest-pinned image's actual local image ID. Full mount/port/limit
fingerprints and inspect/mutate race qualification remain v0.5 work.

The legacy `.local/stack` and `runasmidja-test-*` fixture is untouched by these
commands. It must be stopped explicitly before the new profile can use its ports.
Do not remove its database volume or recovery material. New-profile tests do not
migrate old data or turn previously locally generated passwords into vault-issued
credentials. Custody-preserving migration/rekey qualification remains v0.8.
There is no data reset/remove command. Never discard custody to bypass an error.

Existing containers with unbounded logs/audit mounts require an explicit
`python3 scripts/stack.py upgrade-bounds`. This verifies ownership, current
image IDs and database/vault data mounts before stopping/removing containers;
volumes, vault data, credentials and recovery custody remain intact. Run `up`
after the image gate is clean. Ordinary startup never silently replaces a
container. Earlier `v02`, `v02-wolfi-ready` and development `v02-wolfi` profiles are stopped,
preserving all data/custody. The latter contains an incomplete experimental
initialization; it is not silently resumed or reset. The qualified fresh default
is independent of these profiles, not a migration. PostgreSQL cannot reuse the
original image's `/19/docker` layout without a separately tested migration.

`python3 scripts/build_postgres_image.py` explicitly rebuilds using current signed
APK packages. Missing build custody triggers this automatically; changed recipe,
base, archive or image identity fails closed. Rebuilds do not replace running
containers or migrate data automatically. Use a separate stopped-port profile
to qualify a changed image. The public build has a 30 MB source-download bound,
512 MiB streamed archive bound, 1 MiB output budget and 1,800-second deadline.
Compilation uses a private 3 GiB tmpfs-backed rootless store, a 2-CPU/5 GiB/no-swap/
512-task cgroup, and 2 GiB/no-extra-swap build steps. Its context whitelist
excludes vault state and all credentials. Archive byte limits apply before
writes; validated/scanned archives are imported only after containment completes.
See the [build contract](../deploy/podman/postgres/README.md).

## OpenBao first

Only OpenBao starts first. The fixture generates its startup TLS key/certificate
as the enumerated vault trust anchor, validates HTTPS against that certificate,
initializes persistent PebbleDB with one automated test recovery share and
requires OpenBao's declarative file audit. Recovery and initial root custody
stay outside container mounts. A single bootstrap checkpoint preserves the init
response before splitting recovery/root records; interrupted custody capture
fails closed instead of resetting an initialized vault.
File and parent directory fsync protect local create/rename/unlink custody.
There remains a non-atomic window between remote initialization and capture of
its response; a host crash there can require independent vault recovery.

OpenBao's random API issues the PostgreSQL admin, PostgreSQL runtime and Valkey
passwords (32 bytes/64 hex characters). KV v2 persists provisioning version 1 and
a runtime-only projection at version 1. CAS=0 prevents overwriting existing or
deleted records. Schema/version/projection changes require a separately reviewed
rotation/migration; startup rejects them rather than changing service passwords.

Separate AppRoles retrieve and validate those records before either consumer
starts. Provisioning can read both paths; runtime can read only its path. Neither
may write secrets, use random APIs or manage vault configuration. Scoped access
tokens are revoked when their operation exits. The initial root is revoked and
its local checkpoint removed only after scoped retrieval and service readiness;
its unusability is confirmed. Retry after revocation uses the scoped identities.

The fixture may automatically unseal its owned vault using its retained local
share on an explicit `up`. Secret reads against a sealed/unavailable/denied vault
fail; private password delivery files are never used as a retrieval fallback.
AppRole SecretIDs expire after 24 hours; tokens are 15 minutes/max 1 hour. Expiry
fails closed; automatic re-provisioning/renewal belongs to later rotation work.
The TLS certificate is valid 30 days; renewal is not claimed by this pass.

## Delivery and limits

Host custody directories are private 0700, files 0600, same-user custody; private reads reject
symlinks, nonregular files and >64 KiB metadata. OpenBao/config/data/audit mounts
exclude root/recovery/AppRole files and service passwords. PostgreSQL receives
an admin password file, Valkey a private ACL config; runtime role setup uses
stdin. Service passwords and tokens never appear in argv or container environment
metadata. Persistent private password/ACL copies still exist as an explicit v0.8
delivery limitation. Python/process memory, PostgreSQL test-client environment
and local backup/swap custody are not secure-erasure claims.

Private/internal network, loopback-only publications, 512 MiB/1 CPU/128 PID service
limits and a 64 MiB cache apply. PostgreSQL 19beta4 uses SCRAM host authentication
including localhost; its runtime role is nonadministrative. Valkey's default
user is off; app ACL grants only get/set/del/ping on `runasmidja:*` keys.
New containers use 1 MiB k8s-file log rotation; qualification reads only the
latest 2,000 records with a 1 MiB aggregate capture cap. Child stdin is capped at
64 KiB, stdout/stderr are drained concurrently, and limit/deadline failures
terminate and reap the child group while its leader remains unreaped. Successful
reaped children are never signalled again; general process capture does not
claim cleanup of detached descendants. Public builds use an owned cgroup for
that boundary. Public image SBOM capture has a separate
16 MiB/900-second budget. Private creation/replacement limits apply before writes.
Live OpenBao audit is a 16 MiB tmpfs, never an unbounded host bind. Qualification
and stop take bounded snapshots into two private regular files, each at most
16 MiB, rejecting symlinks/devices/FIFOs. This retains finite audit history;
a full sink can deny vault operations, and abrupt host/container loss can lose
the live tail. It is not production durable audit retention. Private custody
retry reads resync both file and parent before using visible checkpoint data.
Namespace-private audit/socket/tmp tmpfs directories use sticky mode 1777 for
the supported Podman mount parser; audit files remain owner-only. PostgreSQL
runs as UID/GID 999 on a read-only root without capabilities. Its independent
qualification verifies UTF8/C.UTF-8, no compiler/Perl/gosu runtime and 12 root,
password/env/symlink/auth/partial/legacy/version/readiness denials with unchanged
rejected data. These checks also run in full service qualification and CI.
PostgreSQL/Valkey transport remains plaintext in the disposable local fixture.
Production TLS, independent encrypted quorum recovery, HA, leased credentials
and certificate/identity rotation are separate later owners.

`stack_qualification.py` injects an interruption after actual vault issuance on
its first empty-state run, then tests sealed/denied/bad-CA paths and retry.
Every run tests revoked-root restart, actual outage, denied runtime identity,
vault version reuse, PostgreSQL persistence, role/auth/path/ACL denials and
real wrong-label fixture/stop denials and in-memory credential/recovery/TLS
disclosure scans of container metadata/logs and vault audit. Repeated
runs preserve data and say when initial empty-state evidence was previously
established. Valkey expiry acceptance remains v0.7: EX is accepted but the smoke
entry is deleted immediately, so countdown/expiration is not attested.

Remote images stay digest-pinned in deploy/podman/images.json; its local PostgreSQL
marker resolves only to the receipt-bound immutable image ID. Product Rust/crates,
GitHub tooling, service images and SDKs are checked weekly; local OS/Podman
packages follow daily Tumbleweed updates. Freshness also checks the official
PostgreSQL source checksum and current Wolfi base index; drift requires review,
not an automatic pin update. The optional Meilisearch fixture and
OpenBao Rust SDK are not admitted by this pass.
