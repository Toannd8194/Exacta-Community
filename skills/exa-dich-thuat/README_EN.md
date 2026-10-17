# exa-dich-thuat — Exacta · Dịch thuật

[Tiếng Việt](README.md)

## What it does

Translates Vietnamese academic prose into Nature-style English or polishes English by Vietnamese authors, preserving facts, with a terminology table and Vietnamese change notes.

Vietnamese overlay for [`nature-polishing`](../nature-polishing/README_EN.md): loads the base skill, then applies Vietnamese rules.

## Example prompt

```text
Use exa-dich-thuat to translate this Vietnamese paragraph into Nature-style English and list terminology.
```

## Shared rules

- Instructions are English; conversation with the user is Vietnamese.
- No manuscript or patient data is sent to external services.
- No invented data, references, or approval numbers; gaps are marked `[CẦN BỔ SUNG: ...]`.
- Full rules: [AGENTS.md](../../AGENTS.md).
