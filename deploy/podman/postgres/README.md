# PostgreSQL 19 beta 4 on Wolfi

This is a disposable Linux/amd64 test image built by Runasmidja, not a
Chainguard/OpenSerbia/PostgreSQL-maintained distribution or production claim.
The maintainer authorized the source-build approach on 2026-10-03.

The official [PostgreSQL tarball and checksum](https://www.postgresql.org/ftp/source/v19beta4/)
are pinned in source.lock.json. The Wolfi base is an immutable platform leaf
authorized by its signed index and exact reviewed Chainguard workflow/issuer.
APK verifies repository/package signatures using the base image's bundled keys;
current repository packages are resolved during each rebuild. Builds are not
claimed bit-for-bit reproducible; their final dependency inventories are retained.

The example [postgres-wolfi](https://github.com/openserbia/postgres-wolfi/) at
3f87615e52a712d65e66aea1e49ef7a3d86db808 was reviewed as a design reference.
Its recipe/entrypoint are not copied. Its PostgreSQL 16–18 package approach does
not supply 19 beta 4. Our separate compiler stage builds the official source
and bundled contrib extensions; the runtime has neither compiler, Perl nor gosu.

Only the current fixture is supported: fixed database `runasmidja`, peer local
authentication, SCRAM host authentication, a validated 64-byte lowercase-hex
password file and fixed PGDATA. Password envs, root, symlinks, partial/legacy
data and other database/auth settings are rejected. Initialization runs a
socket-only temporary server, then starts the final server after setup completes.
The image runs UID/GID 999 with a read-only root, no capabilities and mapped
rootless host ownership. The database volume remains writable; socket/temp
directories are bounded namespace-private sticky tmpfs mounts.
`qualification_postgres.py` verifies actual UTF8/C.UTF-8, runtime package absence
and 12 fail-closed startup profiles. Full stack qualification calls it too.
ICU/readline and unqualified optional integrations are outside this profile.

Use `python3 scripts/build_postgres_image.py` to build/scan, or ordinary
`stack.py up` to build a missing image and validate it. The image gate requires
the current recipe fingerprint, local owner-only receipt, immutable image ID,
archive/config/layer SHA-256 binding and a current scan before execution.
No signing secret is created: public-source builds need none. Local receipts
trust the host user; they are not cryptographically authenticated release
provenance. Production signing/build identity retains its later owner.

Weekly freshness checks detect upstream PostgreSQL releases/checksum drift and
new Wolfi base indexes. Review/update pins, rebuild, rescan and requalify before
admission. A new image ID cannot silently replace an existing container.
The old official PostgreSQL pin and data stay retained, with no CVE waiver.
The application component is recorded with its source hash in the runtime SBOM;
Trivy's OS scan does not automatically analyze advisories for compiled C source.
PostgreSQL upstream security/release review remains a separate requirement.
The [security information](https://www.postgresql.org/support/security/),
[19 beta 4 announcement](https://www.postgresql.org/about/news/postgresql-19-beta-4-released-3386/)
and [preceding security update](https://www.postgresql.org/about/news/postgresql-186-1711-1615-1519-1424-and-19-beta-3-released-3365/)
were reviewed on 2026-10-03. This beta fixture does not certify all PostgreSQL
features; the existing beta-to-GA upgrade and production qualification passes
remain required.

The recipe/entrypoint are EUPL-1.2. PostgreSQL remains under its
[PostgreSQL License](https://www.postgresql.org/about/licence/), not EUPL;
Wolfi packages retain their individual SBOM licenses/source notices. Public image
redistribution needs the complete corresponding notices/source obligations and
separate publishing authorization. This task publishes no image or tag.
