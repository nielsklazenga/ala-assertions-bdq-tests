#!/usr/bin/env bash
set -e

if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    uv venv
fi

echo "Installing dependencies..."
uv sync

if ! jupyter kernelspec list | grep -q quarto-analysis; then
    echo "Registering Jupyter kernel..."
    .venv/bin/python -m ipykernel install \
        --user \
        --name quarto-analysis \
        --display-name "Python (Quarto Analysis)"
fi

if ! grep -q "Activate project venv" ~/.bashrc; then
cat <<'EOF' >> ~/.bashrc

# Activate project venv
if [ -f /workspaces/bdq/.venv/bin/activate ]; then
    source /workspaces/bdq/.venv/bin/activate
fi
EOF
fi

echo "Done."