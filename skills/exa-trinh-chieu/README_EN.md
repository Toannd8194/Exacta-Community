# exa-trinh-chieu — Exacta · Trình chiếu

[Tiếng Việt](README.md)

## What it does

Builds Vietnamese (or English) PPTX decks with source figures and speaker notes for journal club, departmental meetings, proposal defence, thesis and doctoral defence, and conference talks.

Vietnamese overlay for [`nature-paper2ppt`](../nature-paper2ppt/README_EN.md): loads the base skill, then applies Vietnamese rules.

> Community edition: slide outline with speaker notes. Finished PPTX files and defence arcs are in Exacta Pro.

## Example prompt

```text
Use exa-trinh-chieu to build Vietnamese thesis defence slides from my thesis chapters.
```

## Shared rules

- Instructions are English; conversation with the user is Vietnamese.
- No manuscript or patient data is sent to external services.
- No invented data, references, or approval numbers; gaps are marked `[CẦN BỔ SUNG: ...]`.
- Full rules: [AGENTS.md](../../AGENTS.md).
