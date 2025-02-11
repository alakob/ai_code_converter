# Stage 1: Base development image
FROM ubuntu:22.04 as builder

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install essential build tools and compilers
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.10 \
    python3-pip \
    python3.10-venv \
    build-essential \
    gcc \
    g++ \
    openjdk-17-jdk \
    curl \
    ca-certificates \
    git \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Install Julia
RUN curl -fL https://julialang-s3.julialang.org/bin/linux/x64/1.9/julia-1.9.3-linux-x86_64.tar.gz | tar xz -C /opt \
    && ln -s /opt/julia-1.9.3/bin/julia /usr/local/bin/julia

# Install Go
RUN curl -L https://go.dev/dl/go1.21.6.linux-amd64.tar.gz | tar -C /usr/local -xzf -
ENV PATH="/usr/local/go/bin:${PATH}"
ENV GOPATH="/go"
ENV PATH="${GOPATH}/bin:${PATH}"

# Create app user
RUN useradd -m -s /bin/bash app
WORKDIR /app

# Copy project files
COPY --chown=app:app . .

# Create and activate virtual environment
RUN python3 -m venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime image
FROM ubuntu:22.04

# Install runtime dependencies
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.10 \
    python3-pip \
    gcc \
    g++ \
    openjdk-17-jdk \
    curl \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Install Julia
RUN curl -fL https://julialang-s3.julialang.org/bin/linux/x64/1.9/julia-1.9.3-linux-x86_64.tar.gz | tar xz -C /opt \
    && ln -s /opt/julia-1.9.3/bin/julia /usr/local/bin/julia

# Install Go runtime
COPY --from=builder /usr/local/go /usr/local/go
ENV PATH="/usr/local/go/bin:${PATH}"
ENV GOPATH="/go"
ENV PATH="${GOPATH}/bin:${PATH}"

# Create app user
RUN useradd -m -s /bin/bash app
WORKDIR /app

# Copy virtual environment and application files from builder
COPY --from=builder --chown=app:app /app/.venv /app/.venv
COPY --from=builder --chown=app:app /app /app

# Set environment variables
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONPATH="/app/src" \
    PYTHONUNBUFFERED=1 \
    GRADIO_SERVER_NAME=0.0.0.0 \
    GRADIO_SERVER_PORT=7860

# Create necessary directories with correct permissions
RUN mkdir -p /app/logs /app/downloads \
    && chown -R app:app /app/logs /app/downloads

# Verify installations
RUN node --version && \
    java -version && \
    julia --version && \
    go version

# Switch to non-root user
USER app

# Expose port
EXPOSE 7860

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:7860/healthz || exit 1

# Set entrypoint and default command
ENTRYPOINT ["python3"]
CMD ["run.py"] 