---
name: exa-de-cuong
description: "Draft, revise, or audit Vietnamese research proposals and thesis documents for health sciences: institutional research projects, master's, specialist (CKI/CKII), residency and doctoral thesis proposals, full thesis structure, and ethics committee dossiers. Use for viết đề cương nghiên cứu, đề cương luận văn, đề cương luận án, hồ sơ hội đồng đạo đức, rà soát đề cương; not for English journal manuscripts."
metadata:
  version: "0.1.0"
  replaces: nature-proposal-writer
---

# Exacta · Đề cương — Vietnamese Research Proposals and Theses

Standalone skill. It replaces the frozen `nature-proposal-writer`, which targets Chinese grant
conventions. Instructions are English; the deliverable is Vietnamese.

## Routing protocol

### 1. Load the manifest and core layer

Read [manifest.yaml](manifest.yaml) and every `always_load` file.

### 2. Intake (ask before drafting)

Establish, in Vietnamese, in one short message:

| Item | Values |
|---|---|
| Document type | `de-tai-co-so` (institutional project) / `de-cuong-thac-si` / `de-cuong-ckii` / `de-cuong-cki` / `de-cuong-bsnt` / `de-cuong-tien-si` / `luan-van-full` / `ho-so-dao-duc` |
| Task | `draft` / `revise` / `audit` |
| Institution template | Has the institution supplied a template or presentation regulation (quy định trình bày)? If yes, it overrides the default structure |
| Topic, setting, population, design | From the user |
| Evidence available | Prior studies, pilot data, local statistics the user can cite |
| Reference style | Usually Vancouver; confirm |

If the user cannot answer some items, proceed with defaults and mark gaps as
`[CẦN BỔ SUNG: ...]`.

### 3. Load matching references

- Document structure: `references/document-templates.md` (always for draft or audit).
- Objectives, variables, methods: `references/objectives-and-methods.md` (always for draft).
- Sample size and statistics: hand off to `exa-thong-ke` rules
  (`../exa-thong-ke/references/vn-sample-size-and-designs.md`).
- Literature search for the review chapter: `exa-tim-tai-lieu`.

### 4. Community edition scope

Deliver, for document types A, B, and D in `references/document-templates.md`:

1. A **detailed outline**: every heading of the chosen structure, each with 1–3 lines of
   guidance tailored to the user's topic (what goes there, which evidence is needed).
2. The **objective → design → sample size → variables → analysis alignment table** from
   `references/objectives-and-methods.md`, with every mismatch flagged.
3. A short list of gaps (`[CẦN BỔ SUNG: ...]`) and decisions for the supervisor.

Full-text drafting, `revise` and `audit` against the QA checklist, institution-specific
templates, doctoral proposals (C), and ethics dossiers (E) are Exacta Pro capabilities. If
requested, deliver items 1–3 and follow `../nature-shared/vn/community-edition.md`. The red
lines in step 5 apply in full.


### 5. Red lines

- Never invent data, prevalence figures, references, regulation numbers, approval numbers, or
  budget norms. Use `[CẦN BỔ SUNG: ...]`.
- Regulations (training regulations, thesis presentation rules, research-ethics regulations,
  budget norms) come only from documents the user provides or that are verified in the session.
- Dummy tables in "Dự kiến kết quả" contain no numbers.
- Apply `../nature-shared/vn/privacy-offline.md` to any pilot data.

### 6. Delivery

Deliver the document in Markdown (or DOCX through the user's tooling if requested), followed by
a short Vietnamese list of open gaps and decisions the supervisor must confirm.
