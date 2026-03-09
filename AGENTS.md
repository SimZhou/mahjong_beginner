# Mahjong Site Rebuild Notes

## Current Branch

- This branch rebuilds the site from scratch from locally mirrored Japanese source pages.
- Source content lives under `site_src/`.
- Built static output must land in `docs/` for GitHub Pages deployment.
- Raw mirrored source and assets live under `raw_site/`.

## Key Directories

- `site_src/docs/`: translated Chinese markdown pages
- `site_src/mkdocs.yml`: MkDocs config for the rebuilt site
- `docs/`: deployable static site output
- `raw_site/articles/`: local snapshots of original Japanese article bodies
- `raw_site/assets/`: mirrored original images and other assets
- `scripts/build_site.sh`: canonical build entrypoint

## Build Rules

- Always build with:

```bash
scripts/build_site.sh
```

- Do not build into any directory other than `docs/`.
- Acceptance must be based on generated `docs/`, not only markdown source.

## Translation Rules

- Translate from local Japanese source snapshots under `raw_site/articles/`.
- Do not use external translation APIs.
- Keep the original article logic, example order, and conclusion structure aligned with the Japanese source.
- Keep the page-end source link:

```md
原始日文页：<http://beginners.biz/...>
```

## Diagram Rules

- Article diagrams are mandatory content, not decoration.
- For each page, compare original `../images/...` references against:
  - `site_src/docs/...`
  - generated `docs/...`
- If the original page contains an article diagram, the translated page must also contain it.
- Decorative assets outside article content are lower priority than article diagrams.

## Regression Checklist

For page-by-page review, always check all three items:

1. Whether article diagrams are missing
2. Whether translation meaning is wrong or drifted
3. Whether layout has defects

Minimum review flow:

1. Compare `raw_site/articles/<page>.html` with `site_src/docs/<page>.md`
2. Compare original `../images/...` references with generated `docs/<page>.html`
3. Check generated HTML heading structure and page-end source link
4. Check for residual Japanese kana in translated markdown

## Live Sampling Checklist

- Local `docs/` being correct does not prove the deployed site is correct.
- After meaningful batches, sample deployed pages on `https://simzhou.com/mahjong_beginner/`.
- Live sampling should verify:
  - page returns real article content, not `404`
  - article diagrams load on the deployed domain
  - page-end source link is present

- Treat network resets and TLS failures separately from confirmed content failures.
- A page that consistently returns `404 - Not found` on the live domain is a real deployment issue, not a transient fetch error.

## Current Sampling Findings

Sampled live pages confirmed normal:

- `kihon/kihon08.html`
- `teyaku/teyaku07.html`
- `dora/dora04.html`
- `naki/naki12.html`
- `reach/reach04.html`
- `osihiki/osihiki02.html`

Confirmed live deployment issue:

- `https://simzhou.com/mahjong_beginner/joukyou/joukyou09.html`
  - currently returns `404 - Not found`
  - local `docs/joukyou/joukyou09.html` exists and is tracked
  - this indicates a live deployment mismatch or stale publish state, not a missing local build artifact

## Deployment Verification Update

- The earlier live `404` on `joukyou/joukyou09.html` was caused by GitHub Pages not yet pointing to this branch's `docs/`.
- After Pages was switched to this branch's `docs/`, live sampling confirmed the rebuilt site is now being served.

Rechecked live pages confirmed normal:

- `joukyou/joukyou09.html`
- `reach/reach04.html`
- `mamori/mamori12.html`
- `naki/naki12.html`
- `dora/dora04.html`
- `teyaku/teyaku07.html`
- `pairi/pairi20.html`

For those pages, live checks confirmed:

1. article page renders instead of `404`
2. article diagrams load on the deployed domain
3. page-end source link is present
4. no Japanese kana residue detected in sampled HTML

## Practical Rule

- When the user reports a live page problem, verify the deployed URL first.
- Do not assume that because `docs/` is correct locally, the live site is already updated.
