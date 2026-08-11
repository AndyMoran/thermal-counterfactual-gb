#!/usr/bin/env bash
# thermal-counterfactual-gb — WSL bootstrap
#
# Run this from INSIDE your WSL shell (not PowerShell/cmd), from wherever
# you want the project to live.
#
# WSL PERFORMANCE NOTE: keep this project under your Linux home directory
# (e.g. ~/projects/thermal-counterfactual-gb), NOT under /mnt/c/... — file
# IO across the Windows/Linux boundary is dramatically slower, and it will
# make Jupyter + Polars/Parquet feel sluggish for no good reason. If you
# unzipped this on the Windows side, move the folder into WSL first:
#   mkdir -p ~/projects && mv /mnt/c/path/to/thermal-counterfactual-gb ~/projects/
#   cd ~/projects/thermal-counterfactual-gb

set -euo pipefail

PROJECT_NAME="thermal-counterfactual-gb"

echo "== ${PROJECT_NAME} setup =="

# 1. Install uv if missing
if ! command -v uv &> /dev/null; then
    echo "-- uv not found, installing..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # shellcheck disable=SC1091
    source "$HOME/.local/bin/env" 2>/dev/null || export PATH="$HOME/.local/bin:$PATH"
fi
echo "-- uv version: $(uv --version)"

# 2. Warn if running from a Windows-mounted drive
if [[ "$PWD" == /mnt/* ]]; then
    echo "!! WARNING: you're running this from $PWD, a Windows-mounted drive."
    echo "!! Jupyter/Polars/Parquet IO will be noticeably slower here than on"
    echo "!! the native Linux filesystem. Consider moving to ~/projects/ first."
fi

# 3. Sync the environment — creates .venv/, installs everything in pyproject.toml
echo "-- Syncing environment with uv..."
uv sync

# 4. Register the Jupyter kernel so notebooks can select it explicitly
#    (PROJECT.md Section 4.1: cross-project kernel usage is prohibited —
#    always select this named kernel, never a default/global one)
echo "-- Registering Jupyter kernel..."
uv run python -m ipykernel install --user --name="${PROJECT_NAME}" --display-name "Python (${PROJECT_NAME})"

echo ""
echo "== Done =="
echo "Next steps:"
echo "  uv run jupyter lab                                    # launch Jupyter Lab"
echo "  uv run python -c \"import polars, numpy, scipy, matplotlib; print('env OK')\""
echo "  uv run streamlit run demo/app.py                      # Week 4 demo app (once wired up)"
echo ""
echo "When opening notebooks/*.ipynb, select the '${PROJECT_NAME}' kernel — not a default one."
