# CONN-GENIUS-AGENT-CONNECTOR-CONTENT — The connector serves its packaged content

Owner: genius-agent. Cross-repo IDs: `SCION-CONNECTOR-CONTROL-R071`, `SCION-CONNECTOR-CONTROL-R073`.

## Purpose and user stories

The `genius-agent` server serves its packaged skills, prompts and ontology to any client, with no wiring of its own.

## Why a new spec

The specs of this repository were read; none owns this capability. This spec states it for this connector only.

## Scope and interfaces

In scope: the rows of [requirements.md](requirements.md). Out of scope: the SDK modules and the engine, which own the shared capabilities.

## User Scenarios & Testing

### User Story 1 - The connector serves its packaged content (Priority: P1)

The `genius-agent` server serves its packaged skills, prompts and ontology to any client, with no wiring of its own.

**Acceptance Scenarios**:

1. **Given** the connector is configured, **When** the behaviour of row `CONN-GENIUS-AGENT-CONNECTOR-CONTENT-R001` (default content) is exercised, **Then** `resources/list` includes `skill://` and `ontology://`; `prompts/list` includes each packaged prompt. Planned test: `tests/test_default_content_surfaces.py::test_default_content_lists_skill_and_ontology_resources_and_prompts`.

### Edge Cases

- If `CONN-GENIUS-AGENT-CONNECTOR-CONTENT-R001` is not met, its proving test fails: default content.

## Requirements

- **FR-001**: Default content. Rows: `CONN-GENIUS-AGENT-CONNECTOR-CONTENT-R001`.

## Success Criteria

- **SC-001**: `resources/list` includes `skill://` and `ontology://`; `prompts/list` includes each packaged prompt. Planned test: `tests/test_default_content_surfaces.py::test_default_content_lists_skill_and_ontology_resources_and_prompts`. Rows: `CONN-GENIUS-AGENT-CONNECTOR-CONTENT-R001`.

## Assumptions

- The external system is reachable with operator-supplied credentials.
- The SDK and engine contracts the rows cite are at the floors declared in `pyproject.toml`.

## Traceability

| Label | Rows | Design section | Test ID | Evidence |
|---|---|---|---|---|
| FR-001 | `CONN-GENIUS-AGENT-CONNECTOR-CONTENT-R001` | [plan.md](plan.md) | T-001 | [test-spec.md](test-spec.md) |
