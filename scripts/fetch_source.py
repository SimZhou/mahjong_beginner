#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import ProxyHandler, Request, build_opener

BASE_URL = "http://beginners.biz/"
PROXY = "http://127.0.0.1:10800"


def build_client():
    return build_opener(ProxyHandler({"http": PROXY, "https": PROXY}))


def fetch_bytes(opener, url: str, attempts: int = 3) -> bytes:
    headers = {"User-Agent": "Mozilla/5.0"}
    last_error = None
    for attempt in range(1, attempts + 1):
        try:
            with opener.open(Request(url, headers=headers), timeout=60) as resp:
                return resp.read()
        except Exception as exc:  # pragma: no cover - network retry path
            last_error = exc
            if attempt < attempts:
                time.sleep(attempt)
    raise RuntimeError(f"fetch failed: {url} :: {last_error}")


def looks_like_html_page(url: str) -> bool:
    parsed = urlparse(url)
    path = parsed.path
    if not path or path.endswith("/"):
        return True
    name = Path(path).name
    if "." not in name:
        return True
    return path.endswith(".html")


def extract_refs(html: str, page_url: str) -> set[str]:
    refs = set()
    for raw in re.findall(r"""(?:src|href)=["']([^"'#]+)["']""", html, re.I):
        full = urljoin(page_url, raw)
        parsed = urlparse(full)
        if parsed.scheme not in {"http", "https"}:
            continue
        if parsed.netloc != "beginners.biz":
            continue
        if looks_like_html_page(full):
            continue
        refs.add(full)
    return refs


def url_to_path(url: str, html_root: Path, asset_root: Path) -> Path:
    parsed = urlparse(url)
    rel = parsed.path.lstrip("/")
    if not rel or rel.endswith("/"):
        rel = rel.rstrip("/") + "/index.html"
        rel = rel.lstrip("/")
    elif rel.endswith(".html"):
        pass
    elif looks_like_html_page(url):
        rel = rel + "/index.html"
    if rel.endswith(".html"):
        return html_root / rel
    return asset_root / rel


def main() -> int:
    repo_root = Path.cwd()
    raw_root = repo_root / "raw_site"
    html_root = raw_root / "html"
    asset_root = raw_root / "assets"
    tmp_root = raw_root / "tmp"
    html_root.mkdir(parents=True, exist_ok=True)
    asset_root.mkdir(parents=True, exist_ok=True)
    tmp_root.mkdir(parents=True, exist_ok=True)

    page_list = tmp_root / "page_urls.txt"
    if not page_list.exists():
        print(f"missing {page_list}", file=sys.stderr)
        return 1

    opener = build_client()
    page_urls = [line.strip() for line in page_list.read_text("utf-8").splitlines() if line.strip()]
    extras = [
        BASE_URL,
        urljoin(BASE_URL, "kihon/"),
        urljoin(BASE_URL, "pairi/"),
        urljoin(BASE_URL, "teyaku/"),
        urljoin(BASE_URL, "dora/"),
        urljoin(BASE_URL, "naki/"),
        urljoin(BASE_URL, "reach/"),
        urljoin(BASE_URL, "mamori/"),
        urljoin(BASE_URL, "joukyou/"),
        urljoin(BASE_URL, "osihiki/"),
        urljoin(BASE_URL, "sitemap/"),
    ]
    queue = list(dict.fromkeys(page_urls + extras))
    seen_pages: set[str] = set()
    asset_urls: set[str] = set()

    for idx, url in enumerate(queue, 1):
        dest = url_to_path(url, html_root, asset_root)
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            body = fetch_bytes(opener, url)
            dest.write_bytes(body)
        else:
            body = dest.read_bytes()
        seen_pages.add(url)
        html = body.decode("utf-8", errors="ignore")
        asset_urls.update(extract_refs(html, url))
        print(f"page {idx}/{len(queue)} {url}")

    for idx, url in enumerate(sorted(asset_urls), 1):
        dest = url_to_path(url, html_root, asset_root)
        if dest.exists() or dest.is_dir():
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        body = fetch_bytes(opener, url)
        dest.write_bytes(body)
        print(f"asset {idx}/{len(asset_urls)} {url}")

    (tmp_root / "asset_urls.txt").write_text("\n".join(sorted(asset_urls)) + "\n", "utf-8")
    print(f"downloaded pages={len(seen_pages)} assets={len(asset_urls)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
