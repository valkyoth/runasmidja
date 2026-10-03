# Project Secret Lifecycle

Status: mandatory target policy. The current test harness generates service
passwords locally and then seeds OpenBao; it does not yet enforce this policy.
The next bounded implementation pass is OpenBao-first secret provisioning.
This planning change introduces no runtime compliance claim.

## Source and scope

OpenBao is the authoritative source for all project-operated secrets, from first
service initialization through runtime, development, CI, signing and release.
Generate project-owned passwords/keys using reviewed OpenBao random or secrets
engine APIs and retain their version/lease there. Third-party-issued credentials
must be securely ingested into OpenBao before any project consumer receives
them. Avoid exporting keys when a qualified OpenBao signing/encryption service
can perform the required operation. This policy applies to disposable fixture
credentials as well as production credentials.

| Consumer | Secret coverage |
| --- | --- |
| Provisioning and migrations | PostgreSQL initial admin/migration identities, Valkey initial ACL credentials, Meilisearch initial master key and scoped keys |
| Runtime adapters/workers | Database leases, cache/search reader/writer keys, artifact-store access, external API/identity-provider credentials |
| Application security | Session/JWT signing, encryption/wrapping keys, webhook credentials, service TLS private keys and certificate issuance |
| Developer/Rust setup/build | Private registry/source credentials, authenticated tool downloads and any secret-bearing bootstrap configuration |
| CI/release/deployment | Publishing tokens, signing identities/keys, deployment credentials, backup encryption/access and renewal grants |

Public rustup downloads, ordinary Cargo builds and checks need no secrets and
no vault connection. If initialization/build needs a credential, its source is
OpenBao. Public negative fixtures and published cryptographic test vectors are
test data rather than live service credentials; do not use them as credentials.
Public endpoints, role IDs, certificate chains and secret path references are
configuration, not secret values; still apply metadata exposure controls.

Browser-local user inputs and operation keys remain local unless the user
explicitly authorizes a supported remote capability. This rule never silently
uploads user data to OpenBao. Future saved user secret references need a separate
consented, workspace-scoped lifecycle. Account password verifiers belong to the
qualified identity subsystem; they are not plaintext project credentials.

## Bootstrap trust and custody

OpenBao cannot retrieve its first TLS private key or unseal itself using only
secrets locked inside that same sealed instance. Define a minimal, enumerated
bootstrap trust boundary: vault startup TLS identity, external seal identity if
used, operator/workload initial authentication and unseal/recovery custody.
These are the only infrastructure trust anchors handled outside the vault.
They are not an exception for database, cache, search, build or app secrets.

OpenBao creates its initialization root token and unseal/recovery material.
Capture it without logs, keep root access restricted to short-lived provisioning,
establish renewable least-privilege identities, then revoke the root token.
Production custody is independent, encrypted and quorum-controlled with a
tested restore path; recovery material must remain usable if this vault is lost.
An existing independent custody vault/HSM may supply startup trust when available.
Do not invent a second-vault or KMS dependency merely to hide secret-zero custody.
Local single-share automation is an explicitly isolated test profile.

OpenBao-issued AppRole credentials and response-wrapped handoff belong to this
identity lifecycle. Platform-issued workload assertions (including GitHub OIDC)
are short-lived authentication proof exchanged for scoped OpenBao grants.
They do not justify storing project secrets in GitHub Secrets or local dotenv
files. Inventory issuer, scope, lifetime, delivery and renewal for every trust
anchor. New exceptions require an explicit threat-reviewed policy change.

## Initialization order and delivery

1. Establish the minimal vault trust/custody profile; start only TLS OpenBao.
2. Initialize/unseal, configure audit and policies, authenticate the scoped
   provisioning identity and establish durable vault-owned secret versions.
3. Retrieve the required initial PostgreSQL, Valkey and enabled Meilisearch
   credentials from OpenBao. Start each dependent service only after retrieval.
4. Configure separate migration/runtime/cache/search identities. Persist any
   service-issued credentials in OpenBao before granting consumer access.
5. Verify scoped retrieval and restart behavior, revoke bootstrap root access,
   then start consumers. Resume retries through scoped identity, not root reuse.

Use bounded memory, stdin or authenticated local IPC for delivery. A consumer
that requires a file gets a private short-lived tmpfs file with restrictive
ownership/mode and cleanup on success, error and interruption. There is no
persistent plaintext password or secret-bearing ACL/config fallback in `.local`.
Secret values never enter argv, container inspect metadata, ordinary environment
dumps, logs, diagnostics, metrics, caches, search projections or build artifacts.
Configuration stores SecretRef/role/policy identifiers. Do not require SDK or
transport types in portable contracts. Inventory the unavoidable in-process
copies; never claim guaranteed memory/swap/backup erasure.

Cold-start/restart is idempotent: reuse the recorded vault version for an existing
service instead of generating a mismatched password. Partial provisioning keeps
data and credential versions; resume deterministically after interruption.
Existing local-password fixtures need a custody-preserving migration/rekey pass;
never reset a database or discard existing secrets silently to satisfy the policy.

## Lifetime, CI and failure

Each secret has an owner, approved vault path/role, purpose, provisioning versus
runtime policy, version/lease, rotation/revocation procedure, delivery method and
test IDs. Prefer dynamic database credentials after plugin qualification;
long-lived provider tokens still require rotation and independent scope.
Use OpenBao PKI for service certificate/key issuance where compatible; qualify
renewal and identity checks independently of vault startup TLS custody.

Developer authentication and CI workload exchange obtain short-lived grants.
Bind CI JWT issuer/audience and repository/ref/environment/workflow claims;
untrusted fork/PR code has no secret-bearing role. Check current claim semantics
before implementation. Qualify a private reachable vault route/runner instead
of publicly exposing administrative OpenBao endpoints for CI. Publishing/signing
secrets are resolved only in the trusted bounded job and cleaned afterward.

Sealed/unavailable OpenBao, denied scope, bad TLS, audit failure and exhausted
renewal stop new provisioning/secret acquisition. Already issued usable leases
may live only within their explicitly tested validity policy; expiry/revocation
stops their use. Never generate substitute local credentials or enable anonymous
access. Public builds and anonymous browser-local operations remain independent.

## Required evidence and upstream basis

Real-vault tests must prove empty-state Bao-first startup, restart after root
revocation, interrupted provisioning, custody-preserving migration, least
privilege, version reuse, expiry/rotation/revocation, vault outage/seal, bad TLS,
audit failure and temporary-file cleanup. Capture logs/argv/environment/container
metadata/artifacts with planted sentinel secrets and prove no disclosure.
Test private-build and CI identity denials alongside secret-free public builds.
Exact-source pentest remains required; planning and tests cannot attest PASS.

Reviewed upstream: [JWT/OIDC authentication](https://openbao.org/docs/auth/jwt/)
supports scoped workload authentication; [PKI](https://openbao.org/docs/secrets/pki/)
supports dynamic certificates. The source/exception boundaries, delivery rules
and gates above are Runasmidja policy, not claims of implemented SDK behavior.
Verify current random/secrets-engine APIs and SDK support during admission.
