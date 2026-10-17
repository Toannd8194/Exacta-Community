# exa-doc-song-ngu — Exacta · Đọc song ngữ

[Tiếng Việt](README.md)

## What it does

Builds source-grounded English–Vietnamese paper readers aligned by paragraph with figures, tables, and equations, or answers source-linked questions in Vietnamese.

Vietnamese overlay for [`nature-reader`](../nature-reader/README_EN.md): loads the base skill, then applies Vietnamese rules.

## Example prompt

```text
Use exa-doc-song-ngu to build a Vietnamese-English bilingual reader for this PDF.
```

## Shared rules

- Instructions are English; conversation with the user is Vietnamese.
- No manuscript or patient data is sent to external services.
- No invented data, references, or approval numbers; gaps are marked `[CẦN BỔ SUNG: ...]`.
- Full rules: [AGENTS.md](../../AGENTS.md).
