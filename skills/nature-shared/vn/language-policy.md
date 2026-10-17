# Vietnamese Fork Language Policy

Shared by every `exa-*` skill. Load it once per task.

## Output language by artifact

| Artifact | Language |
|---|---|
| Manuscript text for international journals (any section) | English |
| Reviewer reports (mock peer review) | English |
| Response-to-reviewers letter and cover letter | English |
| Explanations, plans, change logs, QA checklists addressed to the author | Vietnamese |
| Research proposal, thesis outline, ethics dossier for a Vietnamese institution | Vietnamese |
| Manuscript for a Vietnamese-language journal | Vietnamese, with an English abstract when the journal requires one |
| Bilingual reader | Vietnamese–English, aligned |
| Paper card | Vietnamese prose with canonical English terms |

Never produce Chinese. If a loaded upstream file asks for a Chinese block, produce the
Vietnamese equivalent with the same purpose.

## Vietnamese writing conventions

- Use full, correct diacritics. Never output unaccented Vietnamese.
- Use the formal academic register: avoid colloquial pronouns and filler; refer to the study
  as "nghiên cứu này" and to the author as "tác giả" or "nhóm nghiên cứu".
- On first use, give the English term in parentheses: "tỷ số chênh (odds ratio, OR)". After
  that, use the abbreviation consistently.
- Keep statistical notation in international form: `p < 0,05` in Vietnamese documents (decimal
  comma) and `P < 0.05` in English manuscripts (decimal point, per target-journal style).
  State which convention a document uses and keep it consistent.
- Units follow SI; dates in Vietnamese documents use `dd/mm/yyyy`.
- Drug names: international nonproprietary names (INN), not brand names, unless the brand is
  the object of study.

## Terminology

Use `vn/medical-glossary-vi-en.md` for standard term pairs. When a term is not in the
glossary, prefer the term used by the Vietnamese Ministry of Health or major Vietnamese medical
universities, and flag uncertain translations as `[thuật ngữ cần kiểm tra]`. Record every
recurring term in the shared Terminology Ledger (`../core/terminology-ledger.md`).

## Author check block

When English output is produced from Vietnamese input, end with a short Vietnamese block:

```
### Ghi chú cho tác giả
- Thay đổi cấu trúc quan trọng: ...
- Chỗ đã làm mềm/khẳng định lại mức độ kết luận: ...
- Thông tin còn thiếu cần bổ sung: [CẦN BỔ SUNG: ...]
- Thuật ngữ cần tác giả xác nhận: ...
```

Keep it short. It lets the author verify intent without re-reading the English line by line.
