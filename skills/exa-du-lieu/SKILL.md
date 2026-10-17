---
name: exa-du-lieu
description: "Vietnamese overlay for nature-data: draft or audit Data and Code Availability statements, data-sharing routes, and data management plans for clinical studies by Vietnamese authors, where patient data usually cannot be public. Use for tuyên bố dữ liệu (Data Availability), chia sẻ dữ liệu, kế hoạch quản lý dữ liệu luận văn; not data cleaning or statistical analysis."
metadata:
  version: "0.1.0"
  base_skill: nature-data
---

# Exacta · Dữ liệu — Vietnamese Overlay

## Load order

1. Read [manifest.yaml](manifest.yaml) and every `always_load` file.
2. Read [../nature-data/SKILL.md](../nature-data/SKILL.md) and follow its workflow: identify the
   journal, inventory datasets, classify each into one access route, choose repository and
   identifiers, draft the statement, cite datasets, run the FAIR audit.
3. Apply the overrides below. On conflict, these overrides win.

Never load any file listed as frozen in `frozen/FROZEN.md`, including the base skill's
`static/core/chinese-mode.md` and `references/chinese-author-alignment.md`.

## Overrides

### Language

- Statement text: English for international journals; Vietnamese for Vietnamese-language
  journals or thesis documents.
- Explanations, the dataset inventory, and open questions: Vietnamese.
- Replace the base `中文核对` block with the Vietnamese author check block from
  `../nature-shared/vn/language-policy.md`.

### Clinical data in Vietnamese settings

Load `references/vn-clinical-data-sharing.md` whenever the study includes patient-level data.
It covers the usual restricted-access routes, how to make "available on request" specific
enough to pass journal checks, and thesis data management plans.

### Red lines

- Never invent repository names, DOIs, accession numbers, ethics approval numbers, custodian
  contacts, or retention periods. Use `[CẦN BỔ SUNG: ...]`.
- Never recommend publishing patient-level data unless the user confirms that consent and
  ethics approval cover public release and the data are de-identified.
- This skill drafts statements only; it does not upload data anywhere.
