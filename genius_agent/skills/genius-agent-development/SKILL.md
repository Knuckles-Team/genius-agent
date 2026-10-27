---
name: genius-agent-development
skill_type: skill
description: >-
  Develop and validate genius-agent changes using the repository's specifications,
  tests, and release gates.
license: MIT
tags: [genius-agent, development]
metadata:
  author: Repository Maintainers
  version: '0.1.0'
---

# Genius Agent Development

Use this skill with the repository `AGENTS.md`, specifications, and focused tests.
The central delivery row is pipelines-owned; consumer commits use
`Spec: none (PIPE-CONNSPEC-R123.3/.4 are pipelines-owned; consumer specs do not define those central rows)`.

## Rapid delivery: the 5-minute contract

Specs are already designed. Deliver one small, reviewable slice at a time. Read the
owning specification and focused tests, preserve repository boundaries, run the
required checks, and report any publication evidence that remains outstanding.
