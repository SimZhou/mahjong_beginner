---
name: translate-japanese-webpage
description: Translate original Japanese webpage HTML into clear, faithful Chinese while preserving all meaning and all important presentation elements. Use when working from raw Japanese HTML pages or article bodies and the task is to produce Chinese markdown/HTML that keeps every example, diagram, table, heading, emphasis, warning, and important visual cue without adding agent narration or dropping information.
---

# Translate Japanese Webpage

## Overview

Translate Japanese webpage content into plain, readable Chinese while preserving structure and information density.

The output must keep:

1. all text information
2. all example order
3. all diagrams and image references
4. all tables and table structure
5. all headings and section boundaries
6. all emphasis signals such as bold text, color emphasis, warning phrases, and key conclusions

Do not add agent-style narration such as "我将..."、"下面进行翻译..."、"这里我会...".

## Required Workflow

1. Read the original Japanese HTML or extracted article body first.
2. Identify every content-bearing element before translating:
   - headings
   - paragraphs
   - lists
   - tables
   - inline tile/figure images
   - standalone diagrams under `../images/...`
   - emphasized text such as `<strong>`, colored spans, warning classes, green summary blocks
3. Translate in original order. Do not merge sections unless the original already does.
4. Preserve every example block. If the original has `例1`, `例2`, keep them all.
5. Preserve every diagram reference. If the original shows an article diagram, the Chinese page must also show it.
6. Preserve tables structurally. Translate headers and cells, but do not collapse a table into prose unless the target format truly cannot represent tables.
7. Preserve emphasis. If the original marks something as important with bold/color/summary styling, express that importance in the target markdown/HTML.
8. After translating, compare the source and output again for omissions.

## Fidelity Rules

Treat these as hard requirements:

1. Do not omit any paragraph, example, condition, footnote-like caution, or theory summary.
2. Do not replace concrete examples with summaries.
3. Do not drop repeated example hands just because they look similar.
4. Do not remove tables.
5. Do not remove image blocks.
6. Do not remove inline image-based tile examples.
7. Do not weaken strong wording when the original is intentionally emphatic.
8. Do not invent new theory, new examples, or explanatory meta-text not supported by the source.

## Translation Style

Use Chinese that is:

1. accurate first
2. readable second
3. concise only when the source is concise

Prefer:

1. natural Chinese teaching prose
2. explicit logical links when the Japanese source makes them explicit
3. stable Chinese Mahjong terminology within the project

Avoid:

1. machine-translation wording
2. untranslated Japanese technical terms when a clear Chinese rendering exists
3. agent narration
4. decorative rewriting that changes the meaning or density

## Element Preservation Rules

### Diagrams

If the original contains standalone article diagrams such as:

- `<img src="../images/...">`

keep them in place relative to the surrounding explanation.

Do not move a diagram away from the text that explains it.

### Tables

If the original contains a table, preserve:

1. row and column structure
2. header meaning
3. numeric values
4. warning or ranking relationships shown by the table

Markdown tables are acceptable if the target file is markdown.

### Emphasis and importance

Preserve importance signals such as:

1. bolded key conclusions
2. red warning phrases
3. green summary blocks
4. highlighted theory lines

If color-specific HTML cannot be preserved exactly, preserve the emphasis semantically using markdown or equivalent HTML.

## Final Checks

Before considering the translation done, verify:

1. no original example is missing
2. no standalone diagram is missing
3. no table is missing
4. no bold/summary/warning content was flattened away
5. no agent-style narration was introduced
6. no Japanese source text remains unless it is intentionally kept as a proper noun or unavoidable label

## Output Constraint

The translated page must read like the finished page itself, not like commentary about translation work.
