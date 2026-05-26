# Verification Checklist: Code Enhancement: genius-agent

## Functional Requirements Verification
- [ ] **FR-001**: Test suite lacks intent diversity (only one type)
- [ ] **FR-002**: 6 potential doc-test drift items
- [ ] **FR-003**: README.md missing sections: overview, installation, usage|quick start
- [ ] **FR-004**: README missing: MCP tools mapping table with descriptions
- [ ] **FR-005**: README missing: Has a Table of Contents
- [ ] **FR-006**: README missing: Has usage examples with code blocks
- [ ] **FR-007**: README missing: Has architecture overview or diagram
- [ ] **FR-008**: README missing: References /docs directory material
- [ ] **FR-009**: README missing: Has MCP tools mapping table with descriptions
- [ ] **FR-010**: No discernible layer architecture (no domain/service/adapter separation)
- [ ] **FR-011**: Low traceability ratio: 0% concepts fully traced
- [ ] **FR-012**: 23 test functions missing concept markers
- [ ] **FR-013**: Total lint findings: 6 (high/error: 2, medium/warning: 3, low: 1)
- [ ] **FR-014**: 2 hook(s) may be outdated: ruff-pre-commit, uv-pre-commit
- [ ] **FR-015**: Low pass rate: 55% (11/20)
- [ ] **FR-016**: 3 test execution error(s)
- [ ] **FR-017**: FAILED: tests/test_graph_flow_integration.py::test_mcp_config_exists
- [ ] **FR-018**: FAILED: tests/test_graph_flow_integration.py::test_mcp_registry_contains_repository
- [ ] **FR-019**: FAILED: tests/test_graph_flow_integration.py::test_mcp_registry_tool_count
- [ ] **FR-020**: FAILED: tests/test_graph_flow_integration.py::test_graph_topology_validation
- [ ] **FR-021**: FAILED: tests/test_graph_flow_integration.py::test_graph_has_repository_domain
- [ ] **FR-022**: FAILED: tests/test_graph_flow_integration.py::test_run_graph_returns_graphresponse_not_string
- [ ] **FR-023**: FAILED: tests/test_graph_flow_integration.py::test_run_graph_flow_tool_returns_string_not_graphresponse
- [ ] **FR-024**: FAILED: tests/test_graph_flow_integration.py::test_git_status_via_graph
- [ ] **FR-025**: FAILED: tests/test_portainer_flow.py::test_portainer_stack_listing
- [ ] **FR-026**: 8 rogue/throwaway scripts detected (fix_*, validate_*, patch_*, etc.): scripts/debug_mcp.py, scripts/debug_stdio.py, scripts/validate_agent.py, scripts/debug_portainer_call.py, scripts/validate_falkordb.py
- [ ] **FR-027**: CHANGELOG.md exists but could not be parsed — check format compliance
- [ ] **FR-028**: No changelog entries within the last 30 days
- [ ] **FR-029**: keepachangelog not installed — pip install 'universal-skills[code-enhancer]'
- [ ] **FR-030**: Missing conftest.py for shared fixtures
- [ ] **FR-031**: No @pytest.mark.parametrize usage — consider data-driven tests
- [ ] **FR-032**: No shared fixtures in conftest.py
- [ ] **FR-033**: 2 tests have no assertions
- [ ] **FR-034**: 4 tests use weak assertions (assert result is not None, assert True, etc.)
- [ ] **FR-035**: Partial env var documentation: 32% coverage
- [ ] **FR-036**: Undocumented env vars: ALLOWED_CLIENT_REDIRECT_URIS, AUTH_TYPE, DEBUG, DEFAULT_MODEL_ID, DEFAULT_PROVIDER, DEFAULT_SYSTEM_PROMPT, EUNOMIA_POLICY_FILE, EUNOMIA_REMOTE_URL, EUNOMIA_TYPE, GRAPH_DB_PATH
- [ ] **FR-037**: 11 Python env vars not in .env.example: DEBUG, DEFAULT_AGENT_NAME, DEFAULT_MODEL_ID, DEFAULT_PROVIDER, GRAPHDB_PASSWORD

## User Stories / Acceptance Criteria
- [ ] As a **developer**, I want to **address Project Analysis findings (grade: C, score: 74)**, so that **improve project project analysis from C to at least B (80+)**.
- [ ] As a **developer**, I want to **address Test Coverage findings (grade: C, score: 70)**, so that **improve project test coverage from C to at least B (80+)**.
- [ ] As a **developer**, I want to **address Concept Traceability findings (grade: F, score: 35)**, so that **improve project concept traceability from F to at least B (80+)**.
- [ ] As a **developer**, I want to **address Test Execution findings (grade: D, score: 60)**, so that **improve project test execution from D to at least B (80+)**.
- [ ] As a **developer**, I want to **address Changelog Audit findings (grade: C, score: 75)**, so that **improve project changelog audit from C to at least B (80+)**.
- [ ] As a **developer**, I want to **address Environment Variables findings (grade: C, score: 75)**, so that **improve project environment variables from C to at least B (80+)**.

## Success Criteria
- [ ] Overall GPA: 2.71 → 3.0
- [ ] Domains at B or above: 11 → 17
- [ ] Actionable findings: 37 → 0

## Technical Quality Gates
- [x] Pre-commit linting (Ruff check/format) passed
- [x] Repository standards checked and verified
- [x] Zero deprecated / local absolute `file:///` URLs

## Review & Acceptance
- **Overall Verification Score**: 0%
- **Final Review Status**: **Needs Revision**
