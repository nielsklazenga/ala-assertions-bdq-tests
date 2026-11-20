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

echo "Done."