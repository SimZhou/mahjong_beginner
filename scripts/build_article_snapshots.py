#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from extract_article import extract_main


def main() -> int:
    repo_root = Path.cwd()
    html_root = repo_root / "raw_site" / "html"
    article_root = repo_root / "raw_site" / "articles"
    article_root.mkdir(parents=True, exist_ok=True)

    count = 0
    for html_path in sorted(html_root.rglob("*.html")):
        rel = html_path.relative_to(html_root)
        body = extract_main(html_path.read_text("utf-8", errors="ignore"))
        out = article_root / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(body, "utf-8")
        count += 1
    print(f"snapshots={count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
