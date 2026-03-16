#!/opt/miniforge3/bin/python
from __future__ import annotations

import argparse
import gzip
import json
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SITEMAP = ROOT / "docs" / "sitemap.xml"
ENDPOINT = "https://api.indexnow.org/indexnow"
KEY = "6f0d3cf671bf4bb3b4dfe2dfef4f11d6"
KEY_LOCATION = f"https://simzhou.com/riichi_mahjong_book/{KEY}.txt"
HOST = "simzhou.com"


def load_urls(sitemap_path: Path) -> list[str]:
    if sitemap_path.suffix == ".gz":
        with gzip.open(sitemap_path, "rt", encoding="utf-8") as fh:
            content = fh.read()
        root = ET.fromstring(content)
    else:
        root = ET.parse(sitemap_path).getroot()

    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [node.text.strip() for node in root.findall("sm:url/sm:loc", namespace) if node.text]
    urls = [url for url in urls if not url.endswith("/404.html")]
    if not urls:
        raise ValueError(f"no urls found in {sitemap_path}")
    return urls


def submit(urls: list[str], dry_run: bool) -> None:
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if dry_run:
        return

    request = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        print(f"status: {response.status}")
        body = response.read().decode("utf-8", errors="replace")
        if body:
            print(body)


def main() -> None:
    parser = argparse.ArgumentParser(description="Submit sitemap URLs to IndexNow")
    parser.add_argument("--sitemap", default=str(DEFAULT_SITEMAP), help="Path to sitemap.xml or sitemap.xml.gz")
    parser.add_argument("--dry-run", action="store_true", help="Print payload only")
    args = parser.parse_args()

    urls = load_urls(Path(args.sitemap))
    submit(urls, args.dry_run)


if __name__ == "__main__":
    main()
