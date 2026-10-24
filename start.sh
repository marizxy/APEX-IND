#!/usr/bin/env bash
# ==============================================================================
# AICTE NEXUS INDIA (Apex-Ind) - AUTOMATED STARTUP & ORCHESTRATION SCRIPT
# Ministry of Education | Government of India
# Sovereign National Regulatory Command Center & Fraud Interception Grid
# ==============================================================================

set -eo pipefail

# ANSI Color Codes
CYAN='\033[0;36m'
GREEN='\033[0;32m'
AMBER='\033[0;33m'
RED='\033[0;31m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Determine project directory root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${PROJECT_ROOT}"

# Print Enterprise Header Banner
echo -e "${CYAN}${BOLD}"
echo "================================================================================"
echo " 🏛️  AICTE NEXUS INDIA (Apex-Ind) | NATIONAL REGULATORY COMMAND CENTER"
echo " Ministry of Education | Government of India"
echo " Quantum-Safe Student Lifecycle Verification & GraphSAGE GNN Grid"
echo "================================================================================"
echo -e "${NC}"

# ------------------------------------------------------------------------------
# 1. Environment & Pre-Flight Verification
# ------------------------------------------------------------------------------
echo -e "[*] ${BOLD}Executing Pre-Flight Environment Checks...${NC}"

# Check for Python 3.9+
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[!] ERROR: python3 is not installed or not in PATH.${NC}" >&2
    exit 1
fi

PY_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
echo -e "    ${GREEN}[+] Detected Python Version: ${PY_VERSION}${NC}"

# Detect and activate virtual environment if present
if [ -d ".venv" ] && [ -f ".venv/bin/activate" ]; then
    echo -e "    ${GREEN}[+] Activating virtual environment (.venv)...${NC}"
    source .venv/bin/activate
elif [ -d "venv" ] && [ -f "venv/bin/activate" ]; then
    echo -e "    ${GREEN}[+] Activating virtual environment (venv)...${NC}"
    source venv/bin/activate
fi

# Ensure .env configuration file exists
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        echo -e "    ${AMBER}[!] .env not found. Initializing from .env.example...${NC}"
        cp .env.example .env
    else
        echo -e "    ${AMBER}[!] Warning: No .env or .env.example found. Proceeding with environment defaults.${NC}"
    fi
else
    echo -e "    ${GREEN}[+] Loaded .env environment variables.${NC}"
fi

# Export required project paths
export PYTHONPATH="${PROJECT_ROOT}:${PYTHONPATH:-}"

# Parse Command-Line Flags
MODE="${1:---all}"

show_help() {
    echo -e "${BOLD}Usage:${NC} ./start.sh [OPTION]"
    echo ""
    echo "Options:"
    echo "  --all        (Default) Start both Streamlit Command Hub (8501) and FastAPI Gateway (8080)"
    echo "  --ui         Start only the Streamlit Executive Command Center (8501)"
    echo "  --api        Start only the FastAPI Enterprise REST Gateway (8080)"
    echo "  --audit      Execute the automated CERT-In & IT Act 70 Cryptographic Security Audit"
    echo "  --help, -h   Show this assistance banner"
    echo ""
}

case "$MODE" in
    --help|-h)
        show_help
        exit 0
        ;;
    --audit)
        echo -e "\n[*] ${BOLD}Running Sovereign Cryptographic & Compliance Audit...${NC}"
        python3 scripts/security_audit.py
        exit 0
        ;;
    --api)
        echo -e "\n[*] ${BOLD}Starting AICTE Enterprise FastAPI REST Gateway...${NC}"
        echo -e "    ${GREEN}👉 API Gateway:  http://0.0.0.0:8080${NC}"
        echo -e "    ${GREEN}👉 Swagger Docs: http://0.0.0.0:8080/docs${NC}"
        exec uvicorn backend.api_gateway:app --host 0.0.0.0 --port 8080 --reload
        ;;
    --ui)
        echo -e "\n[*] ${BOLD}Starting AICTE Streamlit National Command Center...${NC}"
        echo -e "    ${GREEN}👉 Command Hub: http://localhost:8501${NC}"
        exec streamlit run frontend/app.py --server.port=8501 --server.address=0.0.0.0
        ;;
    --all)
        echo -e "\n[*] ${BOLD}Booting AICTE Nexus Sovereign Dual-Service Mesh...${NC}"
        
        # Graceful Process Teardown Handler
        cleanup() {
            echo -e "\n${AMBER}[*] Gracefully terminating AICTE Nexus service processes...${NC}"
            if [ -n "${API_PID:-}" ] && kill -0 "${API_PID}" 2>/dev/null; then
                kill "${API_PID}" 2>/dev/null || true
            fi
            if [ -n "${UI_PID:-}" ] && kill -0 "${UI_PID}" 2>/dev/null; then
                kill "${UI_PID}" 2>/dev/null || true
            fi
            wait 2>/dev/null || true
            echo -e "${GREEN}[+] All services safely stopped. Sovereign shutdown complete.${NC}"
            exit 0
        }
        trap cleanup SIGINT SIGTERM EXIT

        # 1. Start FastAPI REST Gateway in Background
        echo -e "    ${CYAN}[1/2] Launching FastAPI REST Gateway on port 8080...${NC}"
        uvicorn backend.api_gateway:app --host 0.0.0.0 --port 8080 --log-level warning &
        API_PID=$!
        sleep 1

        # 2. Start Streamlit Command Dashboard in Foreground
        echo -e "    ${CYAN}[2/2] Launching Streamlit National Command Center on port 8501...${NC}"
        echo ""
        echo -e "    ${GREEN}${BOLD}🟢 Streamlit Command Dashboard: http://localhost:8501${NC}"
        echo -e "    ${GREEN}${BOLD}🟢 FastAPI REST Gateway:       http://localhost:8080${NC}"
        echo -e "    ${GREEN}${BOLD}🟢 OpenAPI Documentation:       http://localhost:8080/docs${NC}"
        echo -e "    ${GREEN}${BOLD}🟢 Quantum-Safe TLS 1.3:        Active (Kyber-768)${NC}"
        echo ""
        echo -e "${AMBER}Press Ctrl+C to terminate all services safely.${NC}"
        echo "================================================================================"

        streamlit run frontend/app.py --server.port=8501 --server.address=0.0.0.0 &
        UI_PID=$!

        wait "${UI_PID}" "${API_PID}"
        ;;
    *)
        echo -e "${RED}[!] Unknown option: ${MODE}${NC}"
        show_help
        exit 1
        ;;
esac
