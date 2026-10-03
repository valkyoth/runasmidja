#!/bin/sh
# SPDX-License-Identifier: EUPL-1.2
set -eu
umask 077
[ "$(id -u)" != 0 ] || { echo 'PostgreSQL fixture refuses root' >&2; exit 1; }
[ "${PGDATA:-}" = /var/lib/postgresql/19/wolfi ] || { echo 'Unexpected database path' >&2; exit 1; }
[ "${POSTGRES_PASSWORD_FILE:-}" = /run/secrets/postgres.password ] || { echo 'Password file required' >&2; exit 1; }
[ -f "$POSTGRES_PASSWORD_FILE" ] && [ ! -L "$POSTGRES_PASSWORD_FILE" ] || exit 1
[ "${POSTGRES_PASSWORD+x}" != x ] || { echo 'Password environment refused' >&2; exit 1; }
[ "${POSTGRES_DB:-}" = runasmidja ] || { echo 'Unexpected database name' >&2; exit 1; }
[ "${POSTGRES_HOST_AUTH_METHOD:-scram-sha-256}" = scram-sha-256 ] || exit 1
[ "${POSTGRES_INITDB_ARGS:---auth-host=scram-sha-256}" = --auth-host=scram-sha-256 ] || exit 1
[ "$(wc -c < "$POSTGRES_PASSWORD_FILE")" -eq 64 ] || { echo 'Invalid password record' >&2; exit 1; }
grep -Eq '^[0-9a-f]{64}$' "$POSTGRES_PASSWORD_FILE" || exit 1
for path in /var/lib/postgresql/19 "$PGDATA" "$PGDATA/PG_VERSION" "$PGDATA/.runasmidja-ready"; do
    [ ! -L "$path" ] || { echo 'Database symlink refused' >&2; exit 1; }
done
if [ ! -f "$PGDATA/PG_VERSION" ]; then
    # Never initialize over unknown/partial data or a different historical layout.
    [ ! -e /var/lib/postgresql/19/docker ] || { echo 'Legacy data requires migration' >&2; exit 1; }
    mkdir -p "$PGDATA"
    [ -z "$(ls -A "$PGDATA")" ] || { echo 'Partial database requires recovery' >&2; exit 1; }
    initdb -D "$PGDATA" --username=postgres --pwfile="$POSTGRES_PASSWORD_FILE" \
        --auth-local=peer --auth-host=scram-sha-256 --encoding=UTF8 --locale=C.UTF-8
    printf '\nlisten_addresses = '\''*'\''\nunix_socket_directories = '\''/var/run/postgresql'\''\n' >> "$PGDATA/postgresql.conf"
    printf '\nhost all all 0.0.0.0/0 scram-sha-256\nhost all all ::/0 scram-sha-256\n' >> "$PGDATA/pg_hba.conf"
    pg_ctl -D "$PGDATA" -o '-c listen_addresses=' -w start
    trap 'pg_ctl -D "$PGDATA" -m fast -w stop >/dev/null 2>&1 || true' EXIT HUP INT TERM
    createdb --username=postgres runasmidja
    pg_ctl -D "$PGDATA" -m fast -w stop
    trap - EXIT HUP INT TERM
    (set -C; printf '19beta4:runasmidja\n' > "$PGDATA/.runasmidja-ready.next")
    sync -f "$PGDATA/.runasmidja-ready.next"
    mv "$PGDATA/.runasmidja-ready.next" "$PGDATA/.runasmidja-ready"
    sync -f "$PGDATA"
fi
[ "$(cat "$PGDATA/PG_VERSION")" = 19 ] || { echo 'Database version refused' >&2; exit 1; }
[ "$(cat "$PGDATA/.runasmidja-ready")" = 19beta4:runasmidja ] || { echo 'Incomplete database initialization' >&2; exit 1; }
exec postgres -D "$PGDATA"
