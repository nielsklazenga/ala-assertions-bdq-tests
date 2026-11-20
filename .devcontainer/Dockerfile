FROM debian:bookworm-slim

ARG QUARTO_VERSION="1.6.42"

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    gdebi-core \
    git \
    graphviz \
    librsvg2-bin \
    openssh-client \
    python3 \
    python3-pip \
    python3-venv \
    build-essential \
    && HOST="github" \
    && TLD="com" \
    && ORG="quarto-dev" \
    && REPO="quarto-cli" \
    && DEB="quarto-${QUARTO_VERSION}-linux-amd64.deb" \
    && curl -LO "https://${HOST}.${TLD}/${ORG}/${REPO}/releases/download/v${QUARTO_VERSION}/${DEB}" \
    && gdebi -n "${DEB}" \
    && rm -f "${DEB}" \
    && apt-get purge -y gdebi-core \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --break-system-packages uv