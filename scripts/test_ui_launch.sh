#!/usr/bin/env bash
# test_ui_launch.sh
#
# Helper script to spin up the Genius Agent harness alongside the UIs for testing.
# This validates that the newly synchronized global mcp_config.json works properly
# when attached to the `agent-utilities` harness via `genius-agent`.

# Exit on error
set -e

echo "====================================================="
echo "1. Starting the Genius Agent Backend Server"
echo "====================================================="
# We assume the user's workspace virtualenv is active and genius-agent is installed.
# We set AGENT_PORT explicitly if we want to change it, default is usually 8000.
echo "Running 'genius-agent' in the background..."
genius-agent &
AGENT_PID=$!

echo "Waiting for the backend to initialize (5s)..."
sleep 5

echo "====================================================="
echo "2. Launching Agent Terminal UI"
echo "====================================================="
echo "The terminal UI will now open. Press Ctrl+C or Ctrl+D inside the TUI to exit."
echo "Using default AGENT_URL (http://localhost:8000)..."

AGENT_URL="http://localhost:8000" agent-terminal-ui

echo ""
echo "====================================================="
echo "3. Web UI Instructions"
echo "====================================================="
echo "Terminal UI has exited. To test the Web UI against this backend, run:"
echo ""
echo "    cd /home/apps/workspace/agent-packages/agent-webui"
echo "    pnpm run dev:server"
echo "    pnpm run dev"
echo ""
echo "Make sure AGENT_URL or backend config points to http://localhost:8000."
echo ""

echo "====================================================="
echo "Cleaning up Background Processes"
echo "====================================================="
echo "Killing genius-agent (PID: $AGENT_PID)..."
kill $AGENT_PID || true
echo "Done!"
