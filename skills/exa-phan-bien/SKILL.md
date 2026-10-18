---
name: exa-phan-bien
description: "Vietnamese overlay for nature-reviewer: evidence-grounded mock peer review of clinical and biomedical manuscripts by Vietnamese authors, with English referee reports and a Vietnamese action summary. Use for phản biện thử, tự thẩm định trước khi nộp bài, góp ý bản thảo; not for writing the authors' response letter."
metadata:
  version: "0.1.0"
  base_skill: nature-reviewer
---

# Exacta · Phản biện — Vietnamese Overlay

## Load order

1. Read [manifest.yaml](manifest.yaml) and every `always_load` file (language policy,
   privacy rules, Vietnamese manuscript review gates).
2. Read [../nature-reviewer/SKILL.md](../nature-reviewer/SKILL.md) and follow its routing
   protocol in full: its manifest, mutually blind reviewer workflow, severity tiers, forensic
   audit, and QA checklist all apply.
3. Apply the overrides below. On conflict, these overrides win.

Never load any file listed as frozen in `frozen/FROZEN.md`.

## Overrides

### Venue mode

Ask (or infer from the user's message) which venue the manuscript targets:

- **international** — referee reports in English, following the base skill's report structure.
- **vietnamese-journal** — referee reports in Vietnamese, same structure and severity tiers,
  with English technical terms in parentheses on first use.

### Additional review gates

Always run the gates in `references/vn-manuscript-review-gates.md` in addition to the base
skill's domain gates. Record each finding in the base skill's concern ledger with its severity;
do not create a separate list that bypasses tiering.

### Community edition scope

Produce **one** complete referee report (Reviewer 1) that runs every gate in
`references/vn-manuscript-review-gates.md` and the base skill's severity tiers. Skip the
additional mutually blind reviewers, the post-review synthesis, the forensic consistency audit,
and the author action summary: with the Vietnamese gates, these are Exacta Pro capabilities.
The base skill `nature-reviewer` still provides them to a general international standard. If
the user asks for them, follow `../nature-shared/vn/community-edition.md`.

### Data handling

Apply `../nature-shared/vn/privacy-offline.md`. If the manuscript includes patient-identifying
details (for example in a case report or a figure), raise it as a Blocking concern.
