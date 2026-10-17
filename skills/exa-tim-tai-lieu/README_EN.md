# exa-tim-tai-lieu — Exacta · Tìm tài liệu

[Tiếng Việt](README.md)

## What it does

Turns a Vietnamese clinical question into a PICO table and a PubMed/MeSH strategy, provides search strings for Vietnamese sources, finds supporting references claim by claim, exports RIS/BibTeX for Zotero/EndNote, and verifies reference lists.

Vietnamese overlay for [`nature-academic-search`](../nature-academic-search/README_EN.md): loads the base skill, then applies Vietnamese rules.

## Example prompt

```text
Use exa-tim-tai-lieu to turn my Vietnamese clinical question into a PubMed MeSH search strategy.
```

## Shared rules

- Instructions are English; conversation with the user is Vietnamese.
- No manuscript or patient data is sent to external services.
- No invented data, references, or approval numbers; gaps are marked `[CẦN BỔ SUNG: ...]`.
- Full rules: [AGENTS.md](../../AGENTS.md).
