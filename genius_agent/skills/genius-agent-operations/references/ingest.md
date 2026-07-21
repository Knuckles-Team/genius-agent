# Governed ingestion workflow

Use the signed Genius connector bundle to materialize search and crawl evidence into
Epistemic Graph. Search queries, results, providers, pages, and documents receive stable
source identities, provenance, tenant policy, schema fingerprints, and cursor state.

1. Verify GraphSession authority and the connector manifest, signature, and schema pin.
2. Map approved source fields; keep identities, credentials, endpoints, and paths out.
3. Submit one bounded ChangeEnvelope so objects, relationships, documents, lineage,
   cursor, and outbox state commit atomically.
4. Retry only with the same idempotency identity; never report engine absence as success.
5. Confirm committed counts, delta or tombstone state, provenance, and graph read-back.
6. Link the operation to its privacy-safe Langfuse trace and governed evidence record.

Embeddings remain governed by the configured engine provider and budgets; this workflow
never creates a second model client.
