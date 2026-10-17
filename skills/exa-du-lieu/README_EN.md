# exa-du-lieu — Exacta · Dữ liệu

[Tiếng Việt](README.md)

## What it does

Drafts or audits Data and Code Availability statements, controlled sharing routes for patient data, and thesis data management plans for Vietnamese clinical studies.

Vietnamese overlay for [`nature-data`](../nature-data/README_EN.md): loads the base skill, then applies Vietnamese rules.

## Example prompt

```text
Use exa-du-lieu to draft a Data Availability statement for my hospital-based cohort study.
```

## Shared rules

- Instructions are English; conversation with the user is Vietnamese.
- No manuscript or patient data is sent to external services.
- No invented data, references, or approval numbers; gaps are marked `[CẦN BỔ SUNG: ...]`.
- Full rules: [AGENTS.md](../../AGENTS.md).
