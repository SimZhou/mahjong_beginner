#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-/home/zhou/.conda/envs/mahjang/bin/python}"
POST_PYTHON_BIN="${POST_PYTHON_BIN:-/opt/miniforge3/bin/python}"

cd "$ROOT_DIR"
rm -rf docs
cd site_src
"$PYTHON_BIN" -m mkdocs build -d ../docs
cd "$ROOT_DIR"
"$POST_PYTHON_BIN" scripts/add_missing_img_alt.py
"$POST_PYTHON_BIN" scripts/generate_locale_sitemaps.py
