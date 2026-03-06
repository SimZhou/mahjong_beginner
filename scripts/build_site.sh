#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-/home/zhou/.conda/envs/mahjang/bin/python}"

cd "$ROOT_DIR"
rm -rf docs
cd site_src
"$PYTHON_BIN" -m mkdocs build -d ../docs
