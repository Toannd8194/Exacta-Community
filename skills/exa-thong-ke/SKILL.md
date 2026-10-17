---
name: exa-thong-ke
description: "Vietnamese overlay for nature-statistics: audit or improve statistical reporting and sample-size justification in clinical studies, theses, and proposals by Vietnamese authors, with Vietnamese explanations. Use for kiểm tra thống kê, tính cỡ mẫu, viết phần xử lý số liệu, chọn kiểm định; compute new analyses only when data are supplied."
metadata:
  version: "0.1.0"
  base_skill: nature-statistics
---

# Exacta · Thống kê — Vietnamese Overlay

## Load order

1. Read [manifest.yaml](manifest.yaml) and every `always_load` file.
2. Read [../nature-statistics/SKILL.md](../nature-statistics/SKILL.md) and follow its routing
   protocol in full.
3. Apply the overrides below. On conflict, these overrides win.

Never load any file listed as frozen in `frozen/FROZEN.md`.

## Overrides

### Language

- Explanations, audit findings, and recommendations to the user: Vietnamese.
- Statistical methods text for an English manuscript: English.
- "Xử lý số liệu" / "Phương pháp phân tích số liệu" sections for Vietnamese proposals or
  theses: Vietnamese, using `../nature-shared/vn/medical-glossary-vi-en.md` terms.

### Sample size

Whenever a study states or needs a sample size, load
`references/vn-sample-size-and-designs.md` and:

1. Identify the primary objective and match it to a formula.
2. Check every input (α, power, p, σ, d, effect size) and where it came from.
3. Recompute the number and show the arithmetic.
4. Report mismatches between formula and objective, between sampling method and inference, and
   between planned and achieved sample.

### Data analysis

Community edition scope: auditing reported statistics, all sample-size formulas, test
selection, and reporting templates are complete. Running new analyses on the user's raw data,
the multivariable model check, and the common-errors audit for Vietnamese theses are Exacta
Pro capabilities; if requested, follow `../nature-shared/vn/community-edition.md`. Never ask
the user to send raw data elsewhere.

### Result tables

For theses and Vietnamese-language articles, use the column headers, caption placement, decimal
comma, and "Nhận xét:" convention in `../nature-shared/vn/formatting-profiles.md` § Tables,
figures, and comments.

### Output format

End every audit with:

```
## Kết luận kiểm tra thống kê
| Mức độ | Vấn đề | Vị trí | Cách sửa |
```

using the base skill's severity language translated as: Nghiêm trọng (Blocking), Lớn (Major),
Nhỏ (Minor).
