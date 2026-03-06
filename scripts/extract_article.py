#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


def extract_main(html: str) -> str:
    patterns = [
        r'<div class="contents">(.*?)(?:<div id="ad2">|<div id="footer-banner">)',
        r'<div class="contents">(.*?)(?:</div>\s*</div>\s*<!--/main-in-->)',
    ]
    for pattern in patterns:
        match = re.search(pattern, html, re.S)
        if match:
            body = match.group(1)
            body = re.sub(r"<script.*?</script>", "", body, flags=re.S)
            body = re.sub(r"<style.*?</style>", "", body, flags=re.S)
            return body.strip()
    raise ValueError("article body not found")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: extract_article.py RAW_HTML_PATH", file=sys.stderr)
        return 2
    src = Path(sys.argv[1])
    html = src.read_text("utf-8", errors="ignore")
    print(extract_main(html))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
