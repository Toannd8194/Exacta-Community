# exa-phuc-dap — Exacta · Phúc đáp

[Tiếng Việt](README.md)

## What it does

Drafts, audits, or revises English responses to reviewers and revision cover letters, with a Vietnamese per-comment action plan for the authors.

Vietnamese overlay for [`nature-response`](../nature-response/README_EN.md): loads the base skill, then applies Vietnamese rules.

> Community edition: triage of all comments and replies to up to 5 comments per request. The base skill `nature-response` still drafts a full general-standard package. Pro drafts the complete package, editor letter, and marked manuscript with the Vietnamese plan and author check.

## Example prompt

```text
Use exa-phuc-dap to draft point-by-point responses to these reviewer comments with a Vietnamese plan.
```

## Shared rules

- Instructions are English; conversation with the user is Vietnamese.
- No manuscript or patient data is sent to external services.
- No invented data, references, or approval numbers; gaps are marked `[CẦN BỔ SUNG: ...]`.
- Full rules: [AGENTS.md](../../AGENTS.md).
