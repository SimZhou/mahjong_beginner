#!/opt/miniforge3/bin/python
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DOCS_SRC = ROOT / "site_src" / "docs"
EN_SRC = DOCS_SRC / "en"
DOCS_OUT = ROOT / "docs"
EN_OUT = DOCS_OUT / "en"
SITE_PREFIX = "https://simzhou.com/riichi_mahjong_book/"
SITE_PREFIX_ROOT = "/riichi_mahjong_book/"

MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HTML_HREF_RE = re.compile(r"""href=["']([^"']+)["']""")
IGNORE_SUFFIXES = {
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".svg",
    ".webp",
    ".css",
    ".js",
    ".txt",
    ".xml",
    ".gz",
    ".pdf",
    ".zip",
}


@dataclass
class Problem:
    file: Path
    link: str
    resolved: str
    source: str
    kind: str


def strip_fragment_and_query(link: str) -> str:
    return link.split("#", 1)[0].split("?", 1)[0]


def is_external_non_site(link: str) -> bool:
    parsed = urlparse(link)
    return bool(parsed.scheme and not link.startswith(SITE_PREFIX))


def is_ignored_link(link: str) -> bool:
    if not link or link.startswith(("#", "mailto:", "javascript:", "tel:")):
        return True
    if is_external_non_site(link):
        return True
    bare = strip_fragment_and_query(link)
    suffix = Path(bare).suffix.lower()
    return suffix in IGNORE_SUFFIXES


def site_relative_path(link: str) -> str | None:
    if link.startswith(SITE_PREFIX):
        return link[len(SITE_PREFIX) :]
    if link.startswith(SITE_PREFIX_ROOT):
        return link[len(SITE_PREFIX_ROOT) :]
    return None


def looks_non_english(rel: str) -> bool:
    return bool(rel) and not rel.startswith("en/")


def resolve_markdown_target(link: str, file_path: Path) -> Path | None:
    rel = site_relative_path(link)
    if rel is not None:
        target = DOCS_SRC / rel
    else:
        parsed = urlparse(link)
        if parsed.scheme:
            return None
        target = (file_path.parent / strip_fragment_and_query(link)).resolve()
        try:
            target.relative_to(DOCS_SRC)
        except ValueError:
            return None

    if target.suffix == ".html":
        md_target = DOCS_SRC / target.relative_to(DOCS_SRC)
        md_target = md_target.with_suffix(".md")
        if md_target.exists():
            return md_target
    if target.is_dir():
        for candidate in (target / "index.md", target / "index.html"):
            if candidate.exists():
                return candidate
    if target.exists():
        return target
    if target.suffix == "":
        for candidate in (
            target.with_suffix(".md"),
            target.with_suffix(".html"),
            target / "index.md",
            target / "index.html",
        ):
            if candidate.exists():
                return candidate
    return target


def resolve_built_target(link: str, file_path: Path) -> Path | None:
    rel = site_relative_path(link)
    if rel is not None:
        target = DOCS_OUT / rel
    else:
        parsed = urlparse(link)
        if parsed.scheme:
            return None
        target = (file_path.parent / strip_fragment_and_query(link)).resolve()
        try:
            target.relative_to(DOCS_OUT)
        except ValueError:
            return None

    if target.is_dir():
        candidate = target / "index.html"
        if candidate.exists():
            return candidate
    if target.exists():
        return target
    if target.suffix == "":
        candidate = target / "index.html"
        if candidate.exists():
            return candidate
        candidate = target.with_suffix(".html")
        if candidate.exists():
            return candidate
    return target


def check_link(
    link: str,
    file_path: Path,
    base_root: Path,
    english_root: Path,
    source: str,
) -> list[Problem]:
    if is_ignored_link(link):
        return []

    problems: list[Problem] = []
    site_rel = site_relative_path(link)
    if site_rel is not None and looks_non_english(site_rel):
        problems.append(
            Problem(
                file=file_path.relative_to(ROOT),
                link=link,
                resolved=site_rel,
                source=source,
                kind="non_english_internal_link",
            )
        )

    resolver = resolve_markdown_target if source == "markdown" else resolve_built_target
    target = resolver(link, file_path)
    if target is None:
        return problems

    try:
        target.relative_to(base_root)
    except ValueError:
        return problems

    if not target.exists():
        problems.append(
            Problem(
                file=file_path.relative_to(ROOT),
                link=link,
                resolved=str(target.relative_to(base_root)),
                source=source,
                kind="broken_internal_link",
            )
        )
        return problems

    try:
        target.relative_to(english_root)
    except ValueError:
        if site_rel is None:
            problems.append(
                Problem(
                    file=file_path.relative_to(ROOT),
                    link=link,
                    resolved=str(target.relative_to(base_root)),
                    source=source,
                    kind="non_english_internal_link",
                )
            )

    return problems


def scan_markdown() -> list[Problem]:
    problems: list[Problem] = []
    for path in sorted(EN_SRC.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        links = set(MARKDOWN_LINK_RE.findall(text))
        links.update(HTML_HREF_RE.findall(text))
        for link in sorted(links):
            problems.extend(check_link(link, path, DOCS_SRC, EN_SRC, "markdown"))
    return problems


class MainHrefParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tag_stack: list[str] = []
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tag_stack.append(tag)
        if tag != "a" or "main" not in self.tag_stack:
            return
        attr_map = dict(attrs)
        href = attr_map.get("href")
        if href:
            self.hrefs.append(href)

    def handle_endtag(self, tag: str) -> None:
        for idx in range(len(self.tag_stack) - 1, -1, -1):
            if self.tag_stack[idx] == tag:
                del self.tag_stack[idx]
                break


def scan_built_html() -> list[Problem]:
    problems: list[Problem] = []
    if not EN_OUT.exists():
        raise FileNotFoundError("docs/en does not exist yet; build the site before checking built HTML.")

    for path in sorted(EN_OUT.rglob("*.html")):
        parser = MainHrefParser()
        parser.feed(path.read_text(encoding="utf-8"))
        for link in sorted(set(parser.hrefs)):
            problems.extend(check_link(link, path, DOCS_OUT, EN_OUT, "built-html"))
    return problems


def print_grouped(problems: list[Problem], source: str) -> None:
    source_problems = [p for p in problems if p.source == source]
    non_english = [p for p in source_problems if p.kind == "non_english_internal_link"]
    broken = [p for p in source_problems if p.kind == "broken_internal_link"]

    print(f"{source}_files_scanned={sum(1 for _ in (EN_SRC if source == 'markdown' else EN_OUT).rglob('*.md' if source == 'markdown' else '*.html'))}")
    print(f"{source}_non_english_internal_links={len(non_english)}")
    for item in non_english:
        print(f"{source}:NON_ENGLISH: {item.file}: {item.link} -> {item.resolved}")
    print(f"{source}_broken_internal_links={len(broken)}")
    for item in broken:
        print(f"{source}:BROKEN: {item.file}: {item.link} -> {item.resolved}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check whether English pages still link to non-English pages or to broken internal targets."
    )
    parser.add_argument(
        "--check-built",
        action="store_true",
        help="Also scan generated docs/en HTML and inspect only links inside <main>.",
    )
    args = parser.parse_args()

    md_problems = scan_markdown()
    print_grouped(md_problems, "markdown")

    html_problems: list[Problem] = []
    if args.check_built:
        try:
            html_problems = scan_built_html()
        except FileNotFoundError as exc:
            print(str(exc))
            return 1
        print_grouped(html_problems, "built-html")

    return 1 if (md_problems or html_problems) else 0


if __name__ == "__main__":
    raise SystemExit(main())
