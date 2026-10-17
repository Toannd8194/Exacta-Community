---
name: exa-doc-song-ngu
description: "Vietnamese overlay for nature-reader: build source-grounded Vietnamese–English paper readers with aligned paragraphs, figures, tables, and equations, or answer source-linked questions about a paper in Vietnamese. Use for dịch song ngữ Anh–Việt, đọc hiểu bài báo, đối chiếu bản dịch; respect a requested excerpt without generating a full reader."
metadata:
  version: "0.1.0"
  base_skill: nature-reader
---

# Exacta · Đọc song ngữ — Vietnamese Overlay

## Load order

1. Read [manifest.yaml](manifest.yaml) and every `always_load` file.
2. Read [../nature-reader/SKILL.md](../nature-reader/SKILL.md) and follow its routing protocol
   (source-format detection, source map first, output contract, grounding rules).
3. Apply the overrides below. On conflict, these overrides win.

Never load any file listed as frozen in `frozen/FROZEN.md`.

## Overrides

### Language pair

Everywhere the base skill specifies Chinese as the translation language, use Vietnamese:

| Base skill label | Use instead |
|---|---|
| `**中文:**` | `**Tiếng Việt:**` |
| `**中文说明:**` | `**Giải thích (Tiếng Việt):**` |
| `**中文图注:**` | `**Chú thích hình (Tiếng Việt):**` |
| Chinese short figure title (`### Fig. 1. 中文短标题`) | `### Fig. 1. [Tiêu đề ngắn tiếng Việt]` |
| `公式索引` | `Chỉ mục công thức` (or `Equation Index`) |

All other rules are unchanged: block-level pairing, translate for meaning, never degrade to a
summary, every display equation shown once, figures attached to their captions.

### Terminology

Use `../nature-shared/vn/medical-glossary-vi-en.md` for standard pairs. Keep an English term in
parentheses on first use when the Vietnamese equivalent is not universal. Record terms in the
Terminology Ledger as the base skill requires.

### Math check

The base skill's `scripts/validate_reader_math.py` scans only Chinese-labelled lines for
pseudo-math. After running it, also check `**Tiếng Việt:**` lines manually: no `(I_0)`-style
pseudo-math; use `$I_0$` inline math instead.

### Copyright

Readers are for the user's personal study of papers they have lawful access to. Do not publish
or share the generated reader.
