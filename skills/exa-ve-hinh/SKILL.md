---
name: exa-ve-hinh
description: "Vietnamese overlay for nature-figure: create, revise, or audit publication and thesis figures in Python or R, with a clinical figure catalogue (Kaplan–Meier, forest plot, ROC, CONSORT/STROBE flow diagram, Bland–Altman) and Vietnamese thesis conventions. Use for vẽ biểu đồ, vẽ hình bài báo, biểu đồ luận văn, sơ đồ chọn mẫu; not for statistics-only analysis."
metadata:
  version: "0.1.0"
  base_skill: nature-figure
---

# Exacta · Vẽ hình — Vietnamese Overlay

## Load order

1. Read [manifest.yaml](manifest.yaml) and every `always_load` file.
2. Read [../nature-figure/SKILL.md](../nature-figure/SKILL.md) and follow its routing protocol:
   figure contract, Python/R backend gate, backend fragment, multi-panel architecture, and the
   full rendered QA (panel alignment, `validate_figure.py`, `audit_pdf_text.py`,
   `audit_figure_collisions.py`).
3. Apply the overrides below. On conflict, these overrides win.

Never load any file listed as frozen in `frozen/FROZEN.md`.

## Overrides

### Frozen route

The base skill's OpenRouter / AI image-generation route is frozen. Never call
`scripts/generate_openrouter_schematic.py` or read `references/openrouter-image-generation.md`.
If the user asks for an AI-generated schematic or graphical abstract, offer the base skill's
hand-built vector-schematic route instead (SVG, drawn locally).

### Data handling

Run the identifier screen in `../nature-shared/vn/privacy-offline.md` before reading any data
file. Plot from aggregated or de-identified data. Never print identifiers in labels, point
annotations, or file names.

### Output mode

Decide once per task and state it in one line:

- **international** — English labels, decimal point, journal specification from the base skill.
- **vn-document** — thesis, proposal, or Vietnamese-language journal. Load
  `references/vn-figure-conventions.md`: Vietnamese labels with diacritics, decimal comma,
  chapter-based numbering, captions in Vietnamese.

### Clinical figures

When the figure is a standard clinical display (survival, ratio estimates, diagnostic accuracy,
participant flow, agreement, proportions), load `references/clinical-figure-catalog.md` and
apply its required elements checklist in addition to the base QA.

### Delivery

Report in Vietnamese: what the figure shows, files produced (PDF/SVG for journals, 300 dpi PNG
for Word theses), QA results, and any element still missing from the checklist.
