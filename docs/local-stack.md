# Automated Local Stack

Linux/rootless Podman, Python 3.11+, OpenSSL CLI and free loopback ports
15432/18200/16379 are required. Python orchestrates tests; product code is Rust.

```sh
python3 scripts/stack.py up
python3 scripts/stack.py smoke
python3 scripts/stack.py status
python3 scripts/stack.py stop
python3 scripts/stack_qualification.py
```

The v0.2 fixture uses `.local/stacks/v02` and `runasmidja-v02-*` containers,
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
There is no reset/remove command. Never discard custody to bypass an error.

## OpenBao first

Only OpenBao starts first. The fixture generates its startup TLS key/certificate
as the enumerated vault trust anchor, validates HTTPS against that certificate,
initializes persistent PebbleDB with one automated test recovery share and
requires OpenBao's declarative file audit. Recovery and initial root custody
stay outside container mounts. A single bootstrap checkpoint preserves the init
response before splitting recovery/root records; interrupted custody capture
fails closed instead of resetting an initialized vault.

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

Directories are private 0700, files 0600, same-user custody; private reads reject
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

Images stay digest-pinned in deploy/podman/images.json. Product Rust/crates,
GitHub tooling, service images and SDKs are checked weekly; local OS/Podman
packages follow daily Tumbleweed updates. The optional Meilisearch fixture and
OpenBao Rust SDK are not admitted by this pass.
