# Heartbeat — Periodic Self-Check

You are running a scheduled heartbeat. Perform these checks and report results concisely.

## Core Checks

1. **Tool Availability** — Call `list_tools` or equivalent to verify your MCP tools are reachable. Report any connection failures.
2. **Memory Review** — Read `MEMORY.md` and check for any pending follow-up tasks or action items. List any that are overdue.
3. **Cron Log** — Read `CRON_LOG.md` and check for recent errors (❌). Summarize any failures from the last 24 hours.
4. **Peer Agents** — Read `AGENTS.md` and note if any registered peers need attention.
5. **Self-Diagnostics** — Report your current model, available tool count, and any anomalies.

## Orchestrated Agent Checks

## Response Format

### If everything is healthy:
```
HEARTBEAT_OK — All systems nominal. Orchestrated sub-agents verified.
```

### If issues found:
```
HEARTBEAT_ALERT — [summary of issues found]
- Agent name: [issue description]
```
