# Code Enhancement: genius-agent

> Automated code enhancement review for genius-agent. Covers 17 analysis domains.

## User Stories

- As a **developer**, I want to **address Project Analysis findings (grade: C, score: 74)**, so that **improve project project analysis from C to at least B (80+)**.
- As a **developer**, I want to **address Test Coverage findings (grade: C, score: 75)**, so that **improve project test coverage from C to at least B (80+)**.
- As a **developer**, I want to **address Concept Traceability findings (grade: F, score: 30)**, so that **improve project concept traceability from F to at least B (80+)**.
- As a **developer**, I want to **address Test Execution findings (grade: F, score: 25)**, so that **improve project test execution from F to at least B (80+)**.
- As a **developer**, I want to **address Changelog Audit findings (grade: C, score: 75)**, so that **improve project changelog audit from C to at least B (80+)**.
- As a **developer**, I want to **address Environment Variables findings (grade: D, score: 60)**, so that **improve project environment variables from D to at least B (80+)**.
- As a **developer**, I want to **address analyze_xdg_kg findings (grade: F, score: 0)**, so that **improve project analyze_xdg_kg from F to at least B (80+)**.

## Functional Requirements

- **FR-001**: Minor update: pytest-xdist 3.6.0 (constraint — not installed) -> 3.8.0
- **FR-002**: Minor update: agent-utilities 0.2.40 (installed) -> 0.16.0
- **FR-003**: Test suite lacks intent diversity (only one type)
- **FR-004**: 9 potential doc-test drift items
- **FR-005**: README.md missing sections: usage|quick start
- **FR-006**: 1 broken internal links in README.md
- **FR-007**: README.md is short (160 lines) — consider expanding
- **FR-008**: README missing: Environment variables documentation table
- **FR-009**: README missing: MCP tools mapping table with descriptions
- **FR-010**: README missing: Has a Table of Contents
- **FR-011**: README missing: Has usage examples with code blocks
- **FR-012**: README missing: Documents all environment variables in a table or section
- **FR-013**: README missing: Has MCP tools mapping table with descriptions
- **FR-014**: No discernible layer architecture (no domain/service/adapter separation)
- **FR-015**: Low traceability ratio: 0% concepts fully traced
- **FR-016**: 11 orphaned concepts (only in one source)
- **FR-017**: 27 test functions missing concept markers
- **FR-018**: Total lint findings: 0 (high/error: 0, medium/warning: 0, low: 0)
- **FR-019**: 2 hook(s) may be outdated: ruff-pre-commit, uv-pre-commit
- **FR-020**: 8 rogue/throwaway scripts detected (fix_*, validate_*, patch_*, etc.): scripts/debug_mcp.py, scripts/debug_stdio.py, scripts/validate_agent.py, scripts/debug_portainer_call.py, scripts/validate_falkordb.py
- **FR-021**: CHANGELOG.md exists but could not be parsed — check format compliance
- **FR-022**: No changelog entries within the last 30 days
- **FR-023**: keepachangelog not installed — pip install 'universal-skills[code-enhancer]'
- **FR-024**: No @pytest.mark.parametrize usage — consider data-driven tests
- **FR-025**: 3 tests have no assertions
- **FR-026**: 4 tests use weak assertions (assert result is not None, assert True, etc.)
- **FR-027**: Only 24% of env vars documented in README.md
- **FR-028**: Undocumented env vars: AUTH_TYPE, CRONTOOL, DEFAULT_MODEL_ID, DEFAULT_PROVIDER, DISKTOOL, EUNOMIA_POLICY_FILE, EUNOMIA_TYPE, FILESYSTEMTOOL, FIREWALL_MANAGEMENTTOOL, GRAPHDB_PASSWORD
- **FR-029**: 11 Python env vars not in .env.example: DEFAULT_MODEL_ID, DEFAULT_PROVIDER, GRAPHDB_PASSWORD, GRAPH_DB_PATH, LLM_API_KEY
- **FR-030**: Analysis error: No module named 'agent_utilities.knowledge_graph'

## Success Criteria

- Overall GPA: 2.47 → 3.0
- Domains at B or above: 10 → 17
- Actionable findings: 30 → 0
