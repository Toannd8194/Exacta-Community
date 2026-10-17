---
name: exa-trinh-chieu
description: "Vietnamese overlay for nature-paper2ppt: build Vietnamese (or English) PPTX presentations with source figures and speaker notes for journal club, scientific meetings, proposal defence, master's/specialist thesis defence, doctoral defence, and conference talks. Use for làm slide, trình chiếu journal club, slide bảo vệ đề cương, slide bảo vệ luận văn/luận án, báo cáo hội nghị."
metadata:
  version: "0.1.0"
  base_skill: nature-paper2ppt
---

# Exacta · Trình chiếu — Vietnamese Overlay

## Load order

1. Read [manifest.yaml](manifest.yaml) and every `always_load` file.
2. Read [../nature-paper2ppt/SKILL.md](../nature-paper2ppt/SKILL.md) and follow its routing
   protocol: paper-type arc, toolchain, workflow, figure assets, design and self-review.
3. Apply the overrides below. On conflict, these overrides win.

Never load any file listed as frozen in `frozen/FROZEN.md`.

## Overrides

### Language (replaces the base Chinese-by-default rule)

- Default slide language: **Vietnamese**. Use English only when the user asks (for example an
  international conference).
- Never produce Chinese. Rename the base planning files accordingly:
  `ppt_outline_cn.md` → `ppt_outline_vi.md`,
  `ppt_script_cn_with_figures.md` → `ppt_script_vi_with_figures.md`;
  every "Chinese caption" in the base workflow becomes a Vietnamese caption.
- Keep technical terms, gene/drug names, outcome names, and statistics as the base skill
  specifies; add a Vietnamese gloss on first use when helpful.
- Speaker notes in Vietnamese, written to be spoken.

### Occasion (new axis)

Identify the occasion and load `references/vn-presentation-arcs.md`:

`journal-club` / `sinh-hoat-khoa-hoc` / `bao-ve-de-cuong` / `bao-ve-luan-van` /
`bao-ve-luan-an` / `hoi-nghi`.

For `journal-club` and `hoi-nghi` about a published paper, combine the occasion arc with the
base paper-type arc. For defences, the source is the user's own proposal or thesis; the
occasion arc replaces the paper-type arc.

### Community edition scope

Deliver the slide plan as Markdown: slide-by-slide titles, 2–4 bullets, suggested figure or
table per slide (with source label), and speaker notes. For defences, use a generic
thesis-presentation outline (title, background, objectives, methods, results by objective,
discussion, conclusions). Generating the PPTX file, figure extraction into slides, the
occasion-specific defence arcs, and the PPTX quality audit are Exacta Pro capabilities. If
requested, follow `../nature-shared/vn/community-edition.md`.

### Fonts

Use Office-safe fonts with complete Vietnamese glyphs (Arial, Calibri, Times New Roman,
Segoe UI). Check slide text for broken diacritics after generation.

### Quality scan

The base `scripts/audit_pptx_quality.py` still runs for layout and structure, but its
template-phrase scan only covers Chinese. Also scan all slide text and notes against the
Vietnamese phrase list in `references/vn-presentation-arcs.md` § Template phrases and rewrite
each hit into a source-specific statement.

### Privacy

Case presentations: no patient names, faces, record numbers, or exact dates on slides or in
notes; crop or mask identifiers in images. Apply `../nature-shared/vn/privacy-offline.md`.
