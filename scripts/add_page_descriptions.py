#!/opt/miniforge3/bin/python
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "site_src" / "docs"

SKIP_FILES = {
    DOCS_DIR / "index.md",
    DOCS_DIR / "404.md",
}


def clean_line(text: str) -> str:
    text = re.sub(r"!\[[^\]]*]\([^)]*\)", "", text)
    text = re.sub(r"<img[^>]*>", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\[([^\]]+)]\([^)]*\)", r"\1", text)
    text = text.replace("`", "")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def split_frontmatter(text: str) -> tuple[str | None, str]:
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 5 :]


def extract_heading(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return clean_line(line[2:])
    return ""


def extract_paragraphs(body: str) -> list[str]:
    paragraphs: list[str] = []
    current: list[str] = []
    in_comment = False

    for raw_line in body.splitlines():
        line = raw_line.strip()
        if line.startswith("<!--"):
            in_comment = True
        if in_comment:
            if "-->" in line:
                in_comment = False
            continue
        if not line:
            if current:
                paragraph = clean_line(" ".join(current))
                if paragraph:
                    paragraphs.append(paragraph)
                current = []
            continue
        if line.startswith("#"):
            continue
        if line == "---":
            if current:
                paragraph = clean_line(" ".join(current))
                if paragraph:
                    paragraphs.append(paragraph)
                current = []
            continue
        if line.startswith("原始日文页："):
            break
        if line.startswith("<div ") or line.startswith("</div") or line.startswith("<a "):
            continue
        if line.startswith("![") or line.startswith("<img"):
            continue
        if re.fullmatch(r"[*_`#>\-<>=0-9 .|:]+", line):
            continue
        current.append(line)

    if current:
        paragraph = clean_line(" ".join(current))
        if paragraph:
            paragraphs.append(paragraph)
    return paragraphs


def build_description(path: Path, body: str) -> str | None:
    heading = extract_heading(body)
    paragraphs = extract_paragraphs(body)
    if not heading or not paragraphs:
        return None

    chosen = ""
    for paragraph in paragraphs:
        if paragraph == heading:
            continue
        chosen = paragraph
        if len(chosen) >= 24:
            break

    if not chosen:
        return None

    description = f"{heading}：{chosen}"
    description = re.sub(r"\s+", " ", description).strip(" ：")
    if len(description) > 88:
        description = description[:87].rstrip("，、。；： ") + "。"
    return description


def inject_description(text: str, description: str) -> str:
    frontmatter, body = split_frontmatter(text)
    if frontmatter is None:
        return f"---\ndescription: {description}\n---\n\n{body.lstrip()}"
    if re.search(r"^description:\s*", frontmatter, flags=re.M):
        return text
    return f"---\n{frontmatter}\ndescription: {description}\n---\n{body}"


def main() -> None:
    updated = 0
    for path in sorted(DOCS_DIR.rglob("*.md")):
        if path in SKIP_FILES:
            continue
        if path.parts[-2:] == ("blog", "home_archive.md"):
            continue
        text = path.read_text(encoding="utf-8")
        if re.search(r"^description:\s*", text, flags=re.M):
            continue
        description = build_description(path, text)
        if not description:
            continue
        path.write_text(inject_description(text, description), encoding="utf-8")
        updated += 1
        print(f"updated {path.relative_to(ROOT)}")
    print(f"total updated: {updated}")


if __name__ == "__main__":
    main()
