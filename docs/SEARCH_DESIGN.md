# Search Design

Status: required design; neither hosted search backend is implemented yet.
The [release plan](RELEASE_PLAN.md) assigns early contracts and separate bounded
passes alongside hosted persistence and workspace authorization.

## Local and hosted search

The operation picker searches local descriptors in the browser. Browser-local
recipes/workspaces also search locally. Neither sends queries or content to a
hosted search service. Saved server recipes and collections use the application
API and an application-owned `SearchService` contract.

Implement and qualify both repository search and Meilisearch before 1.0.
Meilisearch is optional to deploy, with implementation scheduled from the start.
Repository mode works without a Meilisearch process, client dependency or key.
Measurements guide which backend operators enable and its resource ceilings.

## Contracts and crates

Place portable requests/results, query/resource bounds, opaque cursors and
capability descriptions in `runasmidja-ports`; application use cases enforce
permissions. Keep the contract no_std and use bounded/fallible alloc only in
the separately qualified profile that needs it. Implement repository search in
the database adapters and extract `runasmidja-search-meilisearch` as a std adapter.

An optional Cargo feature admits the Meilisearch adapter only in hosted builds.
A runtime selector chooses `repository` or `meilisearch` when compiled support
exists; unsupported configuration fails clearly. UI/API contracts and persistent
recipe schemas do not depend on the selected provider. Publish capabilities
for ranking, typo tolerance, query syntax and freshness; do not promise equal
rank ordering. Provider filters, SDK DTOs and native cursor syntax stay private.
Bind cursors to principal/workspace, query, backend and revision/watermark;
reject incompatible cursors on a backend switch and let clients restart paging.

## Metadata and authorization

Use a reviewed allowlist: approved nonsensitive recipe/collection names,
descriptions, tags/categories, opaque IDs and revision/tenant identifiers.
Metadata can itself contain secrets: sensitivity classification and explicit
publication approval are required before projection. Exclude recipe bodies,
operation arguments, SecretRef values, inputs, outputs, decoded/decrypted text,
keys, tokens and raw user payloads. Do not assume a field is safe because it is
called a title or tag. Queries and raw task/error bodies are absent from logs.

The server owns tenant filters; clients cannot supply unrestricted provider
filters. Meilisearch returns bounded candidate IDs to the application. The
application rechecks current database permissions and revisions before
returning current metadata. Same-tenant object permissions matter as well as
tenant separation. Missing authority fails closed. Index results and cached
permissions never grant access.

Do not forward provider highlights, snippets, totals, facets or pagination
metadata that could disclose stale or forbidden documents. Produce visible
metadata and aggregates from currently authorized state, or omit unsupported
aggregates. Bound candidate scans and avoid unauthorized-hit-dependent error
details. Cover access changes during a request with a defined authorization
snapshot/revalidation rule. No browser gets direct search-service credentials.

## Index lifecycle and failure

Repository changes and a revisioned allowlisted outbox event commit in one
transaction. Process events idempotently with revision fencing, delete
tombstones, bounded retry and dead-letter diagnostics containing opaque IDs.
Track accepted asynchronous tasks through completion or failure before marking
an event applied. Reordered updates must not resurrect deleted/stale metadata.

The database remains authoritative. Rebuild from a consistent metadata snapshot,
replay events after its watermark, verify catch-up, then switch the active index.
Outbox payload retention must respect metadata deletion and sensitivity changes.
Index loss or outage cannot lose saved recipes. An explicitly configured
repository fallback uses the same authorization contract; reject stale backend
cursors. Backend selection/switching requires no domain-schema or UI rewrite.

## Deployment and verification

The enabled profile starts a current reviewed digest-pinned Meilisearch container
in rootless Podman, with bounded memory/disk/queue/time, private networking and
qualified TLS. The disabled profile starts none. The initial master key comes
from OpenBao before initialization. Service-issued API keys enter OpenBao before
delivery; provisioning, index writer and query reader are distinct identities.
The master key stays out of browser/API readers. See [secrets](SECRETS_POLICY.md).

Required evidence: actual PostgreSQL and Meilisearch conformance, both Cargo and
runtime profiles, offline operation search, malformed/oversized queries, poisoned
projection, partial transactions, crash/reordered replay, index lag, lost index,
key rotation, outage/fallback, backend switching and bounded pagination.
Cross-tenant and revoked same-tenant fixtures inspect hits, metadata, snippets,
counts and facets with a deliberately stale index. Mocks cannot qualify these
service claims. Every pass retains its exact-source pentest exit.

## Reviewed upstream basis

Meilisearch indexing uses asynchronous tasks; accepted work needs completion
tracking. See [task lifecycle](https://specs.meilisearch.dev/specifications/text/0060-tasks-api.html).
Tenant-token rules constrain queries but do not supply live Runasmidja object
authorization. See [tenant-token specification](https://github.com/meilisearch/specifications/blob/main/text/0089-tenant-tokens.md).
These motivate the outbox and database rechecks above; they are our design rules.
Credential scopes follow the [self-hosting security guide](https://www.meilisearch.com/docs/resources/self_hosting/security/basic_security).
Review current client/server compatibility and licenses before admission.
