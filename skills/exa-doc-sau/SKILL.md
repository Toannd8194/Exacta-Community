---
name: exa-doc-sau
description: "Vietnamese overlay for nature-paper-card: build a structured deep-reading Paper Card for one scientific paper in Vietnamese, analysing methods, experiment-to-claim evidence, limitations, applicability to Vietnamese practice, and research ideas. Use for thẻ đọc bài báo, phân tích phương pháp, đánh giá bằng chứng, journal club; not full translation or formal peer review."
metadata:
  version: "0.1.0"
  base_skill: nature-paper-card
---

# Exacta · Đọc sâu — Vietnamese Overlay

## Load order

1. Read [manifest.yaml](manifest.yaml) and every `always_load` file.
2. Read [../nature-paper-card/SKILL.md](../nature-paper-card/SKILL.md) and follow its routing
   protocol: source boundary, paper type, evidence base before drafting, fixed Sections 01–16,
   groundedness QA.
3. Apply the overrides below. On conflict, these overrides win.

Never load any file listed as frozen in `frozen/FROZEN.md`.

## Overrides

### Language

Write the card's headings and prose in Vietnamese. Keep canonical technical terms, outcome
names, statistical quantities, and formulas in English (with Vietnamese gloss on first use).
Quote the paper only in its original language.

### Additional section (after the base card's final section)

```
## Khả năng áp dụng tại Việt Nam
- Đối tượng trong nghiên cứu khác gì người bệnh tại cơ sở của tôi (tuổi, mức độ bệnh, bệnh kèm, chủng tộc)?
- Can thiệp/xét nghiệm có sẵn và chi trả được (BHYT) không?
- Kết cục có phù hợp với ưu tiên lâm sàng tại chỗ không?
- Có thể làm một nghiên cứu nhân rộng/kiểm chứng tại Việt Nam không — thiết kế gợi ý, cỡ mẫu sơ bộ cần tính lại bằng exa-thong-ke.
```

Every point must be marked either "theo bài báo" (grounded in the paper) or "suy luận"
(inference); never present inference as the paper's finding.

### Clinical evidence grading

Name the study design in one line. A structured risk-of-bias assessment is an Exacta Pro
capability; if requested, follow `../nature-shared/vn/community-edition.md`.
