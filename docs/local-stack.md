# Automated Local Stack

Prerequisites: Linux, rootless Podman, Python 3.11+, OpenSSL CLI and free loopback
ports 15432/18200/16379. Python is test orchestration only; product code is Rust.

```sh
python3 scripts/stack.py up
python3 scripts/stack.py smoke
python3 scripts/stack.py status
python3 scripts/stack.py stop
python3 scripts/smoke_probe.py
python3 scripts/smoke_probe.py --container
```

`up` creates only named/labeled Runasmidja test resources. It initializes a
PostgreSQL database, SCRAM host authentication (including loopback), and nonadministrative runtime login, OpenBao KV v2/AppRole
and private Valkey ACL. Concurrent provisioning is locked. Repeated starts and
stop/start preserve database/OpenBao state. No unrelated container is stopped.
There is no automatic destructive reset command.

OpenBao uses HTTPS with a generated 30-day test certificate verified for localhost,
persistent PebbleDB and declarative file audit required by OpenBao 2.7. It is not
`-dev` mode. Bootstrap creates runtime secrets, issues scoped AppRole credentials
and revokes/removes the initial root token. One unseal share is retained privately
for fully automated test restarts. This is a local custody shortcut, not a
production configuration or HA claim.

Current origin limitation: scripts generate PostgreSQL/Valkey passwords locally
before OpenBao starts, then seed runtime values into KV. Persistent private
password/ACL files are still present. This violates the new
[project secret source policy](SECRETS_POLICY.md). The next bounded pass moves
OpenBao startup and credential issuance ahead of dependent services; subsequent
delivery qualification removes persistent plaintext copies. Existing state must
be migrated/rekeyed safely rather than discarded. These are planned changes,
not behavior provided by the commands above.

Only OpenBao config/certificate files, its data and audit directories are mounted
into the OpenBao container; its mount excludes host bootstrap recovery material
and plaintext service passwords. PostgreSQL receives its admin password file;
Valkey receives its private ACL config. Application bootstrap data is in ignored
`.local/stack`, directory 0700 and secret files 0600. Tools never print secrets or
pass passwords/token values as process arguments.

AppRole tokens expire after 15 minutes with a one-hour maximum; SecretID expires
after 24 hours. After expiry, do not reset data or keep an application root token:
re-provision through an operator recovery procedure (scheduled rotation pass).
The initial fixture smoke suite must run within this credential lifetime.
The certificate likewise requires an explicit renewal procedure after expiry.

The private Podman network has no outbound routing. Published service ports bind
127.0.0.1 only. PostgreSQL and Valkey transport is plaintext in this disposable
loopback fixture; production qualification adds TLS, identity checks and private
unpublished service networks. PostgreSQL 19 beta 4 is intentionally used for
compatibility testing; the pre-1.0 upgrade pass must test transition to 19 GA.

Images are digest-pinned in deploy/podman/images.json; friendly tags and checked
upstream versions are retained separately for drift review. Local Podman/OS packages follow the user's daily Tumbleweed updates and are not
freshness blockers. Product Rust/crates, GitHub tooling, service images and SDKs
are checked against current upstream sources.

The smoke suite checks exact PostgreSQL beta version, transaction rollback and
runtime role/login/password/privileged-table denials, OpenBao TLS/AppRole/path denials and Valkey authentication,
key-prefix isolation and expiring cache writes. Planned SDK application
integration and production secret rotation are separate milestones.

The planned optional Meilisearch profile is added with hosted metadata search,
using an OpenBao-sourced initial master key and scoped keys delivered through
OpenBao. Disabled mode needs neither container nor Meilisearch credentials.
Both backend modes require actual runtime qualification; see
[search design](SEARCH_DESIGN.md). The current harness starts no Meilisearch.
