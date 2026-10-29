# ==============================================================================
# AICTE NEXUS INDIA (Tech Guys) - MULTI-STAGE OPTIMIZED DOCKERFILE
# Ministry of Education | Government of India
# Sovereign National Regulatory Command Center & Fraud Interception Grid
# ==============================================================================

# ------------------------------------------------------------------------------
# STAGE 1: Builder Stage (Compile Wheels & Dependencies)
# ------------------------------------------------------------------------------
FROM python:3.10-slim-bullseye AS builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /build

# Install essential system build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency manifest
COPY requirements.txt .

# Install dependencies into temporary directory
RUN pip install --user --no-warn-script-location -r requirements.txt

# ------------------------------------------------------------------------------
# STAGE 2: Runtime Production Image
# ------------------------------------------------------------------------------
FROM python:3.10-slim-bullseye AS runner

LABEL maintainer="Tech Guys <security@aicte-nexus.gov.in>" \
      org.opencontainers.image.title="AICTE Nexus India (Tech Guys)" \
      org.opencontainers.image.description="National APAAR Regulatory Command Center" \
      org.opencontainers.image.version="5.0.0" \
      org.opencontainers.image.vendor="Ministry of Education, Government of India"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/home/aicte/.local/bin:${PATH}" \
    PYTHONPATH="/app" \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ADDRESS="0.0.0.0" \
    STREAMLIT_SERVER_HEADLESS="true" \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS="false" \
    API_PORT=8080

WORKDIR /app

# Install minimal runtime system utilities and curl for healthchecks
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Create dedicated non-root security service account
RUN groupadd -g 10001 aicte && \
    useradd -u 10001 -g aicte -m -s /bin/bash aicte && \
    mkdir -p /app/data /app/logs && \
    chown -R aicte:aicte /app

# Copy installed Python packages from builder stage
COPY --from=builder --chown=aicte:aicte /root/.local /home/aicte/.local

# Copy application source code
COPY --chown=aicte:aicte . .

# Ensure start script has executable permissions
RUN chmod +x /app/start.sh /app/scripts/*.py

# Switch to unprivileged security context
USER aicte

# Expose Streamlit Command Hub (8501) and FastAPI REST Gateway (8080)
EXPOSE 8501 8080

# Production Healthcheck against Streamlit Core Health Endpoint
HEALTHCHECK --interval=20s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Launch the unified startup script
ENTRYPOINT ["/app/start.sh"]
CMD ["--all"]
