#!/bin/bash

# validate_base_services.sh
# Validates the health of base services: falkordb, graphiti-mcp, crawl4ai

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

check_port() {
    local host=$1
    local port=$2
    local name=$3

    log_info "Checking $name on $host:$port..."
    if nc -z "$host" "$port" 2>/dev/null; then
        log_info "$name is reachable on port $port."
        return 0
    else
        log_error "$name is NOT reachable on port $port."
        return 1
    fi
}

check_http() {
    local url=$1
    local name=$2

    log_info "Checking HTTP health for $name at $url..."
    if curl -s -f "$url" > /dev/null; then
        log_info "$name HTTP health check PASSED."
        return 0
    else
        log_error "$name HTTP health check FAILED."
        return 1
    fi
}

# Check if services are running in Docker
log_info "Checking Docker container status..."
SERVICES=("falkordb" "graphiti-mcp" "crawl4ai")
ALL_RUNNING=true

for service in "${SERVICES[@]}"; do
    if docker ps --format '{{.Names}}' | grep -q "^${service}$"; then
        log_info "Container '$service' is running."
    else
        log_error "Container '$service' is NOT running."
        ALL_RUNNING=false
    fi
done

if [ "$ALL_RUNNING" = false ]; then
    log_warn "Some containers are not running. Please run 'docker compose up -d' first."
    # We continue to try to check ports/endpoints in case they are mapped differently or running elsewhere,
    # but mostly this script assumes localhost execution matching the compose file.
fi

echo "----------------------------------------"

# 1. FalkorDB (Redis protocol) - Port 6379, 3000
check_port "localhost" "6379" "FalkorDB (Redis Port)"
# check_port "localhost" "3000" "FalkorDB (Http Port)" # 3000 might not be a health check port, but exposed

echo "----------------------------------------"

# 2. Graphiti MCP - Port 8000
check_http "http://localhost:8000/health" "Graphiti MCP"

echo "----------------------------------------"

# 3. Crawl4AI - Port 11235
check_http "http://localhost:11235/health" "Crawl4AI"

echo "----------------------------------------"
log_info "Validation complete."
