---
name: exa-viet-bai
description: "Vietnamese overlay for nature-writing: draft or restructure English manuscript sections from Vietnamese notes, theses, or drafts, preserving the author's evidence and adding a Vietnamese author check. Use for viết bài báo tiếng Anh từ ghi chú tiếng Việt, chuyển luận văn thành bài báo, viết abstract/introduction/discussion; use exa-dich-thuat for language-only edits."
metadata:
  version: "0.1.0"
  base_skill: nature-writing
---

# Exacta · Viết bài — Vietnamese Overlay

## Load order

1. Read [manifest.yaml](manifest.yaml) and every `always_load` file.
2. Read [../nature-writing/SKILL.md](../nature-writing/SKILL.md) and follow its routing
   protocol (task, paper_type, section, journal axes).
3. Apply the overrides below. On conflict, these overrides win.

Never load any file listed as frozen in `frozen/FROZEN.md`.

## Overrides

### Language axis

Always set the base skill's `language` axis to `en`. Do **not** load the `zh-to-en` fragment or
`references/chinese-author-workflow.md`. Instead apply `../nature-shared/vn/vi-to-en.md` as the
language-specific layer (it takes the same priority slot: applied last).

### Thesis-to-article mode

Community edition scope: drafting any manuscript section from the author's notes is complete.
Converting a whole thesis or dissertation into a journal article is an Exacta Pro capability;
if requested, draft the sections the user supplies and follow
`../nature-shared/vn/community-edition.md`.

### Evidence boundary

Use only facts, numbers, and references the author supplied. Missing values become
`[CẦN BỔ SUNG: ...]`. Never invent ethics approval numbers, sample sizes, or citations.

### Output

English manuscript text first, then the Vietnamese author check block from
`../nature-shared/vn/language-policy.md`. Record recurring terms in the Terminology Ledger.
