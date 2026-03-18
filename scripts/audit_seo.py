#!/opt/miniforge3/bin/python
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path


DOCS_DIR = Path("docs")
HTML_FILES = sorted(
    p for p in DOCS_DIR.rglob("*.html") if p.is_file() and "search" not in p.parts
)


def extract(pattern: str, text: str) -> list[str]:
    return re.findall(pattern, text, flags=re.I | re.S)


def first(pattern: str, text: str) -> str:
    found = extract(pattern, text)
    return found[0].strip() if found else ""


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def main() -> int:
    results: dict[str, object] = {
        "html_pages": len(HTML_FILES),
        "missing_title": [],
        "missing_description": [],
        "missing_canonical": [],
        "missing_og_title": [],
        "missing_json_ld": [],
        "missing_hreflang_cluster": [],
        "duplicate_hreflang_labels": [],
        "unexpected_noindex": [],
        "duplicate_titles": {},
        "duplicate_descriptions": {},
    }

    title_map: defaultdict[str, list[str]] = defaultdict(list)
    desc_map: defaultdict[str, list[str]] = defaultdict(list)

    for path in HTML_FILES:
        rel = str(path.relative_to(DOCS_DIR))
        text = path.read_text(encoding="utf-8", errors="ignore")

        title = normalize(first(r"<title>(.*?)</title>", text))
        desc = normalize(first(r'<meta\s+name="description"\s+content="(.*?)"\s*/?>', text))
        canonical = normalize(first(r'<link\s+rel="canonical"\s+href="(.*?)"\s*/?>', text))
        og_title = normalize(first(r'<meta\s+property="og:title"\s+content="(.*?)"\s*/?>', text))
        robots = normalize(first(r'<meta\s+name="robots"\s+content="(.*?)"\s*/?>', text))
        json_ld_count = len(extract(r'<script\s+type="application/ld\+json">.*?</script>', text))
        hreflang_labels = extract(
            r'<link\s+rel="alternate"\s+hreflang="(.*?)"\s+href=".*?"\s*/?>',
            text,
        )

        if not title:
            results["missing_title"].append(rel)  # type: ignore[index]
        else:
            title_map[title].append(rel)

        if not desc:
            results["missing_description"].append(rel)  # type: ignore[index]
        else:
            desc_map[desc].append(rel)

        if not canonical:
            results["missing_canonical"].append(rel)  # type: ignore[index]

        if not og_title:
            results["missing_og_title"].append(rel)  # type: ignore[index]

        if json_ld_count == 0:
            results["missing_json_ld"].append(rel)  # type: ignore[index]

        if rel != "404.html":
            needed = {"zh-CN", "en", "x-default"}
            if not needed.issubset(set(hreflang_labels)):
                results["missing_hreflang_cluster"].append(rel)  # type: ignore[index]

        dupes = sorted(label for label, count in Counter(hreflang_labels).items() if count > 1)
        if dupes:
            results["duplicate_hreflang_labels"].append({"page": rel, "labels": dupes})  # type: ignore[index]

        if rel != "404.html" and robots and "noindex" in robots.lower():
            results["unexpected_noindex"].append(rel)  # type: ignore[index]

    results["duplicate_titles"] = {
        key: value for key, value in title_map.items() if len(value) > 1
    }
    results["duplicate_descriptions"] = {
        key: value for key, value in desc_map.items() if len(value) > 1
    }

    summary = {
        "html_pages": results["html_pages"],
        "missing_title": len(results["missing_title"]),  # type: ignore[arg-type]
        "missing_description": len(results["missing_description"]),  # type: ignore[arg-type]
        "missing_canonical": len(results["missing_canonical"]),  # type: ignore[arg-type]
        "missing_og_title": len(results["missing_og_title"]),  # type: ignore[arg-type]
        "missing_json_ld": len(results["missing_json_ld"]),  # type: ignore[arg-type]
        "missing_hreflang_cluster": len(results["missing_hreflang_cluster"]),  # type: ignore[arg-type]
        "duplicate_hreflang_labels": len(results["duplicate_hreflang_labels"]),  # type: ignore[arg-type]
        "unexpected_noindex": len(results["unexpected_noindex"]),  # type: ignore[arg-type]
        "duplicate_titles": len(results["duplicate_titles"]),  # type: ignore[arg-type]
        "duplicate_descriptions": len(results["duplicate_descriptions"]),  # type: ignore[arg-type]
    }

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
