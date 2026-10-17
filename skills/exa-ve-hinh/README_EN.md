# exa-ve-hinh — Exacta · Vẽ hình

[Tiếng Việt](README.md)

## What it does

Creates, revises, or audits manuscript and thesis figures in Python or R, fully local: Kaplan–Meier, forest plot, ROC, CONSORT/STROBE flow diagrams, Bland–Altman; supports Vietnamese labels, decimal comma, and chapter-based numbering.

Vietnamese overlay for [`nature-figure`](../nature-figure/README_EN.md): loads the base skill, then applies Vietnamese rules.

## Example prompt

```text
Use exa-ve-hinh to draw a Kaplan-Meier curve with a number-at-risk table from my de-identified data.
```

## Shared rules

- Instructions are English; conversation with the user is Vietnamese.
- No manuscript or patient data is sent to external services.
- No invented data, references, or approval numbers; gaps are marked `[CẦN BỔ SUNG: ...]`.
- Full rules: [AGENTS.md](../../AGENTS.md).
