# Presentation Conventions and Word Export

Shared by `exa-de-cuong`, `exa-viet-bai`, `exa-thong-ke`, `exa-ve-hinh`, and
`exa-tim-tai-lieu`. The conventions below were derived from two accepted reference documents:
a master's thesis of Hanoi Medical University (2024) and an original article accepted by
Tạp chí Y học Cộng đồng (2026). An institution's or journal's current written rules always win.

## Contents

- Thesis structure conventions
- Vietnamese journal article conventions
- Tables, figures, and comments
- Citations and references
- Word export

## Thesis structure conventions

Front matter, in order: bìa ngoài; bìa phụ (adds chuyên ngành, mã số, cán bộ hướng dẫn khoa
học); LỜI CẢM ƠN; LỜI CAM ĐOAN (place and date, signature, right-aligned); MỤC LỤC; CÁC CHỮ
VIẾT TẮT (two-column table: abbreviation, full term); DANH MỤC BẢNG; DANH MỤC BIỂU ĐỒ;
DANH MỤC HÌNH.

Main text: ĐẶT VẤN ĐỀ (ends with the objectives) → CHƯƠNG 1 TỔNG QUAN TÀI LIỆU → CHƯƠNG 2
ĐỐI TƯỢNG VÀ PHƯƠNG PHÁP NGHIÊN CỨU → CHƯƠNG 3 KẾT QUẢ NGHIÊN CỨU → CHƯƠNG 4 BÀN LUẬN →
KẾT LUẬN → KIẾN NGHỊ (if any) → TÀI LIỆU THAM KHẢO → PHỤ LỤC.

- Chapter headings: "CHƯƠNG n" on one line, the chapter title in capitals on the next, centred.
- Section numbering: 1.1. (level 2), 1.1.1. (level 3).
- Chương 2 default subsections: Thời gian và địa điểm nghiên cứu; Đối tượng nghiên cứu (tiêu
  chuẩn lựa chọn, tiêu chuẩn loại trừ); Phương pháp nghiên cứu (thiết kế, cỡ mẫu, phương tiện,
  quy trình); Thu thập và xử lý số liệu (biến số, phương pháp xử lý số liệu); Khía cạnh đạo đức
  của nghiên cứu; Sơ đồ nghiên cứu.
- Chương 3 and Chương 4 are organised **by objective** (3.1 ↔ objective 1, 3.2 ↔ objective 2);
  Bàn luận mirrors the order of Kết quả.
- KẾT LUẬN: one numbered block per objective ("1. Về ...", "2. Về ..."), no new numbers or
  citations.
- PHỤ LỤC: research case record form (mẫu bệnh án nghiên cứu), scales and diagnostic criteria
  used, each as "PHỤ LỤC n: TÊN".

## Vietnamese journal article conventions

Order: title (Vietnamese, centred) → authors (right-aligned, superscript affiliation numbers) →
affiliations → tác giả liên hệ (name, email) → **TÓM TẮT** (structured, labelled paragraphs
beginning with "Đặt vấn đề:") → Từ khóa → English title → **SUMMARY** (structured, beginning
with "Background:") → Keywords → 1. ĐẶT VẤN ĐỀ (ends with the aims) → 2. ĐỐI TƯỢNG VÀ PHƯƠNG
PHÁP NGHIÊN CỨU → 3. KẾT QUẢ → 4. BÀN LUẬN → 5. KẾT LUẬN → TÀI LIỆU THAM KHẢO.

- Tables are numbered across the article (Bảng 1, Bảng 2, ...); the caption states n.
- The text after a table interprets it in one or two sentences ("Bảng 2 cho thấy ...").
- Phone numbers and personal contact details come only from the author; never fill them in.

## Tables, figures, and comments

- Table caption **above** the table, bold, centred: `Bảng 3.1. Tuổi trung bình theo giới (n = 206)`.
- Chart and figure captions **below** the image, bold italic, centred: `Biểu đồ 3.1. ...`,
  `Hình 1.1. ...`, `Sơ đồ 2.1. ...`. Numbering is per chapter in theses, continuous in articles.
- In thesis results, every table or chart is followed by a **"Nhận xét:"** paragraph stating the
  main finding with numbers, without interpretation (interpretation belongs in Bàn luận).
- Standard column headers: `Tần suất (n) | Tỷ lệ (%)`; `Trung bình ± SD | Trung vị | Tứ phân vị
  | Thấp nhất | Cao nhất`; group comparisons `Nhóm A (n = ...) | Nhóm B (n = ...) | p`;
  associations `OR (KTC 95%) | p`.
- Decimal comma in Vietnamese documents (`9,2%`, `p = 0,032`).

## Citations and references

- Reference list numbered in order of first citation; Vietnamese and English sources in one list.
- Style: AMA/Vancouver — `Author AA, Author BB, Author CC, et al. Title. Journal. Year;Vol(Issue):pages. doi:...`
  Vietnamese sources keep full Vietnamese names and use "và cs." after the listed authors.
- In-text markers: **superscript** numbers in theses (`¹,²`, `³⁻⁵`); **square brackets** in
  Tạp chí Y học Cộng đồng articles (`[4]`). Write markers as `[1,2]` in Markdown; the Word export
  converts them to the profile's style.

## Word export

Deliverables are written in Markdown, then converted to Word:

```bash
python skills/nature-shared/vn/scripts/md_to_docx.py input.md output.docx --profile <profile>
```

Requires `python -m pip install python-docx pyyaml`. Markdown rules: YAML front matter for
cover or article header fields; `#`/`##`/`###` headings; pipe tables; caption lines
`Bảng …`/`Biểu đồ …`/`Hình …`; images `![Biểu đồ 3.1. ...](file.png)`; `[[TOC]]` for the table
of contents; `<!-- section -->` before ĐẶT VẤN ĐỀ to restart page numbering;
`<!-- pagebreak -->`.

Community edition: export with `--profile generic`, a clean general layout (A4, 2.5 cm margins,
Times New Roman 13, line spacing 1.15). Tell the user to adjust margins, font size, and line
spacing to their institution's or journal's rules before submission. Exact institutional and
journal profiles (thesis covers, table of contents, page-number placement, citation style) are
Exacta Pro capabilities; if requested, follow `community-edition.md`.
