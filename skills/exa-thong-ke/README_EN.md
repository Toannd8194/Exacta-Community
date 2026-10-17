# exa-thong-ke — Exacta · Thống kê

[Tiếng Việt](README.md)

## What it does

Audits statistical reporting, test choice, and recomputes sample sizes for clinical studies, theses, and proposals, explaining in Vietnamese.

Vietnamese overlay for [`nature-statistics`](../nature-statistics/README_EN.md): loads the base skill, then applies Vietnamese rules.

## Example prompt

```text
Use exa-thong-ke to check the sample size and statistical reporting in my proposal and explain in Vietnamese.
```

## Shared rules

- Instructions are English; conversation with the user is Vietnamese.
- No manuscript or patient data is sent to external services.
- No invented data, references, or approval numbers; gaps are marked `[CẦN BỔ SUNG: ...]`.
- Full rules: [AGENTS.md](../../AGENTS.md).
