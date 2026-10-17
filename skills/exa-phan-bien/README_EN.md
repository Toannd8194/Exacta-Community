# exa-phan-bien — Exacta · Phản biện

[Tiếng Việt](README.md)

## What it does

Mutually blind mock peer review for biomedical manuscripts, adding review gates common in papers by Vietnamese authors (ethics, reporting guidelines, sample size, causal language) and a Vietnamese action table.

Vietnamese overlay for [`nature-reviewer`](../nature-reviewer/README_EN.md): loads the base skill, then applies Vietnamese rules.

> Community edition: one complete referee report. Three independent reviewers, synthesis, and in-depth numeric audit are in Exacta Pro.

## Example prompt

```text
Use exa-phan-bien to run mutually blind mock reviews of my manuscript and summarise actions in Vietnamese.
```

## Shared rules

- Instructions are English; conversation with the user is Vietnamese.
- No manuscript or patient data is sent to external services.
- No invented data, references, or approval numbers; gaps are marked `[CẦN BỔ SUNG: ...]`.
- Full rules: [AGENTS.md](../../AGENTS.md).
