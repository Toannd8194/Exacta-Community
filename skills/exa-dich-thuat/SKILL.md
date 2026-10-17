---
name: exa-dich-thuat
description: "Vietnamese overlay for nature-polishing: translate Vietnamese academic prose into Nature-style English, or polish English written by Vietnamese authors, preserving facts and evidence boundaries, with a consistent terminology table and Vietnamese change notes. Use for dịch bài báo sang tiếng Anh, sửa tiếng Anh học thuật, chuốt văn; use exa-viet-bai to draft or restructure."
metadata:
  version: "0.1.0"
  base_skill: nature-polishing
---

# Exacta · Dịch thuật — Vietnamese Overlay

## Load order

1. Read [manifest.yaml](manifest.yaml) and every `always_load` file.
2. Read [../nature-polishing/SKILL.md](../nature-polishing/SKILL.md) and follow its routing
   protocol (paper_type, section, language, journal axes).
3. Apply the overrides below. On conflict, these overrides win.

Never load any file listed as frozen in `frozen/FROZEN.md`.

## Overrides

### Language axis

Set the base skill's `language` axis to `en`. Do not load any `zh-to-en` fragment. Apply
`../nature-shared/vn/vi-to-en.md` as the language-specific layer, applied last.

### Modes

- **translate** — input is Vietnamese. Translate meaning, not sentence structure. Keep every
  number, unit, and reference marker exactly.
- **polish** — input is English by a Vietnamese author. Fix grammar, tense, articles, and claim
  strength; do not change scientific content.

Community edition scope: `translate` and `polish` are complete. The `reverse` mode
(English → Vietnamese for Vietnamese-language journals) and whole-manuscript terminology
consistency checks are Exacta Pro capabilities; if requested, follow
`../nature-shared/vn/community-edition.md`.

### Fidelity rules

- Never add data, citations, or claims. Never remove a hedge the evidence requires.
- Where the Vietnamese is ambiguous, choose the safest reading and list it in the author notes.
- Keep a terminology table for the document and use one English term per concept throughout.

### Output

1. Polished or translated text.
2. Terminology table (`Tiếng Việt | English | Ghi chú`) for terms that recur or were uncertain.
3. Vietnamese author check block from `../nature-shared/vn/language-policy.md`, listing changes
   that alter emphasis or claim strength.
