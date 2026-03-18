<h1 align="center">Japanese Mahjong: From Beginner to Master</h1>

<p align="center">
  <a href="./README.md">English</a> | <a href="./README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <a href="https://simzhou.com/riichi_mahjong_book/en/"><img alt="Live Site" src="https://img.shields.io/badge/site-online-0f766e?style=flat-square"></a>
  <img alt="Chinese Edition" src="https://img.shields.io/badge/chinese-complete-2563eb?style=flat-square">
  <img alt="English Edition" src="https://img.shields.io/badge/english-complete-2563eb?style=flat-square">
  <img alt="Built with MkDocs" src="https://img.shields.io/badge/built%20with-MkDocs-526CFE?style=flat-square">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-16a34a?style=flat-square">
</p>

A complete rebuild of a classic Japanese mahjong tutorial site, turned into a modern, multilingual documentation project.

Faithful to the original lessons. Cleaner to read. Easier to maintain. Ready to keep growing.

Live site: <https://simzhou.com/riichi_mahjong_book/en/>

## What This Repo Is

This repository turns a locally mirrored Japanese mahjong teaching site into a maintainable MkDocs project with:

- a complete Chinese edition
- a complete English edition
- preserved article logic, diagrams, tables, and example hands
- deployable static output for GitHub Pages
- modern publishing and deployment workflow

This is not a loose summary project. The goal is to preserve the original teaching sequence and rebuild the entire site page by page.

## Why It Stands Out

Most old mahjong tutorial sites have one of two problems:

- strong content but fragile structure
- readable summaries but missing original depth

This project tries to keep both:

- the original teaching value
- a modern documentation workflow
- cleaner navigation and presentation
- a finished bilingual reading experience

## Highlights

- Complete Chinese coverage of the mirrored source site
- 113 mirrored Japanese source pages mapped to 113 rebuilt article pages
- Chapter order aligned with the original sitemap
- Diagram-heavy articles preserved instead of flattened into plain text
- Dedicated appendix section for author info, links, and resource recommendations
- Responsive homepage and resource-card layouts
- English edition fully online under `/en/`

## Quick Start

```bash
scripts/build_site.sh
```

Output:

```text
docs/
```

## Live Site

- English: <https://simzhou.com/riichi_mahjong_book/en/>
- Chinese: <https://simzhou.com/riichi_mahjong_book/>

## What You Can Read

Both language editions currently cover the full mirrored tutorial:

1. Mahjong Basics
2. Tile Efficiency and Tile Theory
3. Yaku
4. Dora and Red Dora
5. Calling
6. Riichi
7. Defense
8. Situational Judgment
9. Push/Fold Decisions

Appendix pages also exist in both languages:

- Author profile
- Mahjong links
- Recommended books, magazines, lecture pages, and related resources
- Full sitemap

## Repository Structure

```text
site_src/
  docs/          Source Markdown, metadata, templates, styles, and multilingual pages
  mkdocs.yml     MkDocs configuration
docs/            Built static output for GitHub Pages
raw_site/
  articles/      Local snapshots of original Japanese article HTML
  assets/        Mirrored original images and assets
scripts/         Build and maintenance scripts
```

## Translation Principles

- Translate from the local Japanese snapshots in `raw_site/articles/`
- Do not use external translation APIs
- Keep the original example order, teaching flow, and conclusion structure
- Preserve article diagrams as mandatory content
- Keep the source link at the bottom of each translated page

## Multilingual Setup

Current routing strategy:

- Chinese: `/riichi_mahjong_book/`
- English: `/riichi_mahjong_book/en/`

English pages mirror Chinese paths where available, for example:

- Chinese: `/riichi_mahjong_book/kihon/kihon01.html`
- English: `/riichi_mahjong_book/en/kihon/kihon01.html`

## Notes

- The original Japanese source pages are preserved locally for comparison and rebuilding.
- The translated pages keep a source link back to the original article.

## Acknowledgment

This rebuild is based on the locally mirrored content of the original Japanese tutorial site:

- <http://beginners.biz/>

## Contributing

If you want to improve wording, layout, diagrams, or multilingual coverage, prioritize:

- fidelity to the original article logic
- correctness of mahjong terminology
- preservation of diagrams and example hands
- generated `docs/` output, not only source Markdown
