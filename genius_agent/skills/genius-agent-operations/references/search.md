# Governed search workflow

Use the discovered Genius Agent search action to obtain a bounded list of titles,
snippets, source references, and provider metadata. Provider selection, endpoint,
credentials, proxy, and TLS trust come only from the referenced AgentConfig profile.

1. State the information need and freshness window.
2. Discover the live search action and schema.
3. Request the smallest useful result count.
4. Prefer authoritative primary sources and retain their opaque source references.
5. Treat snippets as discovery evidence; crawl load-bearing sources before concluding.
6. Return citations without persisting raw query identities or provider credentials.

Fail closed when the provider profile, TLS policy, tenant, or tool schema is unavailable.
Never use an insecure transport switch or place secrets in arguments.
