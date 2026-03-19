#!/opt/miniforge3/bin/python
from __future__ import annotations

import html
import re
from pathlib import Path


IMG_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
SRC_RE = re.compile(r'\bsrc\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)
ALT_RE = re.compile(r"\balt\s*=", re.IGNORECASE)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.IGNORECASE | re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>")

SUIT_NAMES = {
    "man": "万",
    "pin": "筒",
    "sou": "索",
}

HONOR_NAMES = {
    "ton": "东",
    "nan": "南",
    "sha": "西",
    "pei": "北",
    "haku": "白",
    "hatu": "发",
    "tyun": "中",
    "ura": "牌背",
}

NUMBER_NAMES = {
    "1": "一",
    "2": "二",
    "3": "三",
    "4": "四",
    "5": "五",
    "6": "六",
    "7": "七",
    "8": "八",
    "9": "九",
}


def strip_tags(text: str) -> str:
    text = TAG_RE.sub("", text)
    return html.unescape(" ".join(text.split()))


def tile_alt_from_name(name: str) -> str | None:
    stem = name.rsplit(".", 1)[0]
    if stem.startswith("y") and len(stem) > 1:
        stem = stem[1:]
    if stem.endswith("m") and len(stem) > 1:
        stem = stem[:-1]

    if stem in HONOR_NAMES:
        return f"{HONOR_NAMES[stem]}牌图"

    for suit, suit_name in SUIT_NAMES.items():
        if stem.startswith(suit):
            num = stem[len(suit) :]
            if num in NUMBER_NAMES:
                return f"{NUMBER_NAMES[num]}{suit_name}牌图"
    return None


def generic_alt(src: str, page_title: str) -> str:
    name = src.split("/")[-1]
    if "/hai/" in src:
        return tile_alt_from_name(name) or "麻将牌图"
    if "/images/" in src:
        if page_title:
            return f"{page_title}配图"
        return "麻将示意图"
    if page_title:
        return f"{page_title}插图"
    return "麻将插图"


def add_alt_to_img(tag: str, page_title: str) -> str:
    if ALT_RE.search(tag):
        return tag
    src_match = SRC_RE.search(tag)
    if not src_match:
        return tag
    alt = html.escape(generic_alt(src_match.group(1), page_title), quote=True)
    if tag.endswith("/>"):
        return tag[:-2] + f' alt="{alt}" />'
    return tag[:-1] + f' alt="{alt}">'


def process_html_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    h1_match = H1_RE.search(text)
    page_title = strip_tags(h1_match.group(1)) if h1_match else ""
    new_text = IMG_RE.sub(lambda m: add_alt_to_img(m.group(0), page_title), text)
    if new_text == text:
        return False
    path.write_text(new_text, encoding="utf-8")
    return True


def main() -> None:
    docs_dir = Path(__file__).resolve().parent.parent / "docs"
    changed = 0
    for html_file in docs_dir.rglob("*.html"):
        if process_html_file(html_file):
            changed += 1
    print(f"updated_html_files={changed}")


if __name__ == "__main__":
    main()
