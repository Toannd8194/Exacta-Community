# Vietnamese Thesis and Journal Figure Conventions

Defaults for `vn-document` mode. **The institution's presentation regulation overrides these**;
ask for it when the figure is for a thesis.

## Contents

- Numbering and captions
- Labels and numbers
- Fonts and diacritics
- Export for Word theses
- Checklist

## Numbering and captions

- Number by chapter: `Biểu đồ 3.1`, `Hình 1.2`, `Sơ đồ 2.1`, `Bảng 3.4`.
  - *Biểu đồ*: data charts. *Hình*: images, illustrations, photos. *Sơ đồ*: flow and process
    diagrams (for example the participant flow diagram).
- Common default placement: figure captions **below** the figure, table titles **above** the
  table. Confirm with the institution's rule.
- Caption pattern: `Biểu đồ 3.1. Phân bố người bệnh theo nhóm tuổi (n = 210)`.
- Reused or adapted figures carry a source line: `Nguồn: [Tác giả] ([năm]) [số TLTK]`.
- Do not put the caption inside the image file when the thesis template places captions in Word;
  deliver caption text separately.

## Labels and numbers

- Vietnamese labels with full diacritics; keep standard abbreviations (BMI, HbA1c, OR, KTC 95%).
  On first use in a thesis, "khoảng tin cậy 95% (KTC 95%)".
- **Decimal comma** and space or dot for thousands consistently (`12,5%`; `1.250` or `1 250`).
  - Python: format tick labels with a `FuncFormatter` that replaces `.` with `,`, rather than
    changing the system locale.
  - R: `scales::label_number(decimal.mark = ",", big.mark = ".")` or
    `scales::label_percent(decimal.mark = ",")`.
- Units in parentheses after the axis title: `Tuổi (năm)`, `Glucose máu (mmol/L)`.
- P-values: `p < 0,05`, `p = 0,032` in Vietnamese documents.

## Fonts and diacritics

- Use a font with complete Vietnamese glyphs: Arial, Times New Roman, or DejaVu Sans. Match the
  thesis body font when the institution requires it (Times New Roman is common).
- After rendering, check for missing-glyph boxes or split diacritics (for example in "ượ", "ữ",
  "ặ"). In Python, treat any "Glyph ... missing from font" warning as a failure.
- Keep PDF fonts embedded as TrueType (the base backend settings already set `pdf.fonttype` 42).

## Export for Word theses

- PNG at 300 dpi (600 dpi for line art if the file size is acceptable) at the final printed
  width, typically 15–16 cm for a full-width figure on A4.
- Use colours that remain distinguishable in grayscale printing; add line styles or markers.
- Keep one source script per figure in the project folder so figures can be regenerated after
  committee revisions.

## Checklist

- [ ] Numbered by chapter with the correct type word
- [ ] Caption text in Vietnamese, with n where relevant
- [ ] Decimal comma throughout ticks, labels, and annotations
- [ ] No missing or broken diacritics
- [ ] Readable in grayscale
- [ ] Source line for reused figures
