# exa-doc-sau — Exacta · Đọc sâu

[Tiếng Việt](README.md)

## What it does

Builds a Vietnamese deep-reading card for one paper: methods, evidence chain, limitations, research ideas, and applicability to Vietnamese practice.

Vietnamese overlay for [`nature-paper-card`](../nature-paper-card/README_EN.md): loads the base skill, then applies Vietnamese rules.

## Example prompt

```text
Use exa-doc-sau to build a Vietnamese paper card for this clinical trial.
```

## Shared rules

- Instructions are English; conversation with the user is Vietnamese.
- No manuscript or patient data is sent to external services.
- No invented data, references, or approval numbers; gaps are marked `[CẦN BỔ SUNG: ...]`.
- Full rules: [AGENTS.md](../../AGENTS.md).
