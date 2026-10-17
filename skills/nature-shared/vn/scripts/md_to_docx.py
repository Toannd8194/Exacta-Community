#!/usr/bin/env python3
"""Convert an Exacta Markdown deliverable into a formatted Word (.docx) file.

Usage:
    python md_to_docx.py input.md output.docx --profile generic
    python md_to_docx.py --list-profiles

Requires: python-docx, PyYAML (pip install python-docx pyyaml).

Markdown supported:
    YAML front matter (--- ... ---) for cover or article header fields
    # / ## / ### headings, paragraphs, "- " bullets, pipe tables, ![caption](image.png)
    **bold**, *italic*, ^superscript^, citation markers [1], [2,3], [4–6]
    Caption lines "Bảng 3.1. ...", "Biểu đồ 3.1. ...", "Hình 1.1. ...", "Sơ đồ 2.1. ..."
    [[TOC]] (table of contents field), <!-- pagebreak -->, <!-- section --> (new section,
    page numbering restarts at 1)

Runs fully offline. Never embeds patient identifiers: the caller must pass de-identified text.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

try:
    from docx import Document
    from docx.enum.section import WD_SECTION
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Cm, Pt, RGBColor
except ImportError:  # pragma: no cover - environment guard
    raise SystemExit("Missing dependency: python-docx. Install with `python -m pip install python-docx`.")

HERE = Path(__file__).resolve().parent
PROFILES = HERE.parent / "docx-profiles.yaml"
ALIGN = {"left": WD_ALIGN_PARAGRAPH.LEFT, "center": WD_ALIGN_PARAGRAPH.CENTER,
         "right": WD_ALIGN_PARAGRAPH.RIGHT, "justify": WD_ALIGN_PARAGRAPH.JUSTIFY}
CAPTION_RE = re.compile(r"^(Bảng|Biểu đồ|Hình|Sơ đồ|Table|Figure)\s+\d+(\.\d+)*[.:]")
INLINE_RE = re.compile(r"(\*\*[^*]+\*\*|\*[^*\s][^*]*\*|\^[^^]+\^|\[\d+(?:\s*[,–-]\s*\d+)*\])")
MISSING = "[CẦN BỔ SUNG: {}]"


def load_profiles() -> dict:
    return yaml.safe_load(PROFILES.read_text(encoding="utf-8"))["profiles"]


def set_font(run, name: str, size: float | None = None, bold=None, italic=None, superscript=False):
    run.font.name = name
    rpr = run._element.get_or_add_rPr()
    fonts = rpr.find(qn("w:rFonts"))
    if fonts is None:
        fonts = OxmlElement("w:rFonts")
        rpr.append(fonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        fonts.set(qn(attr), name)
    if size:
        run.font.size = Pt(size)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic
    if superscript:
        run.font.superscript = True
    run.font.color.rgb = RGBColor(0, 0, 0)


def para_format(paragraph, line_spacing: float, align: str | None, space_after: float = 0,
                space_before: float = 0, first_indent: float = 0):
    fmt = paragraph.paragraph_format
    fmt.line_spacing = line_spacing
    fmt.space_after = Pt(space_after)
    fmt.space_before = Pt(space_before)
    if first_indent:
        fmt.first_line_indent = Cm(first_indent)
    if align:
        paragraph.alignment = ALIGN[align]


def add_inline(paragraph, text: str, prof: dict, size: float, bold=False, italic=False):
    """Add text with **bold**, *italic*, ^sup^ and citation markers."""
    font = prof["font"]["name"]
    for token in INLINE_RE.split(text):
        if not token:
            continue
        if token.startswith("**") and token.endswith("**"):
            set_font(paragraph.add_run(token[2:-2]), font, size, True, italic)
        elif token.startswith("^") and token.endswith("^"):
            set_font(paragraph.add_run(token[1:-1]), font, size, bold, italic, superscript=True)
        elif token.startswith("*") and token.endswith("*") and len(token) > 2:
            set_font(paragraph.add_run(token[1:-1]), font, size, bold, True)
        elif re.fullmatch(r"\[\d+(?:\s*[,–-]\s*\d+)*\]", token):
            if prof.get("citations") == "superscript":
                set_font(paragraph.add_run(token[1:-1].replace(" ", "")), font, size, bold, italic, superscript=True)
            else:
                set_font(paragraph.add_run(token), font, size, bold, italic)
        else:
            set_font(paragraph.add_run(token), font, size, bold, italic)


def add_field(paragraph, instr: str, prof: dict, size: float):
    """Insert a Word field (PAGE, TOC) that Word fills in when the document is opened."""
    run = paragraph.add_run()
    set_font(run, prof["font"]["name"], size)
    begin, text, sep, end = (OxmlElement("w:fldChar"), OxmlElement("w:instrText"),
                             OxmlElement("w:fldChar"), OxmlElement("w:fldChar"))
    begin.set(qn("w:fldCharType"), "begin")
    text.set(qn("xml:space"), "preserve")
    text.text = instr
    sep.set(qn("w:fldCharType"), "separate")
    end.set(qn("w:fldCharType"), "end")
    run._r.append(begin)
    run._r.append(text)
    run._r.append(sep)
    placeholder = OxmlElement("w:t")
    placeholder.text = "1" if instr.strip().startswith("PAGE") else "Nhấn F9 để cập nhật mục lục"
    run._r.append(placeholder)
    run._r.append(end)


def setup_section(section, prof: dict, margins: dict, page_numbers: bool, restart: bool):
    section.page_width, section.page_height = Cm(21.0), Cm(29.7)
    section.top_margin, section.bottom_margin = Cm(margins["top"]), Cm(margins["bottom"])
    section.left_margin, section.right_margin = Cm(margins["left"]), Cm(margins["right"])
    for part in (section.header, section.footer):
        part.is_linked_to_previous = False
        for p in part.paragraphs:
            p.text = ""
    if restart:
        pg = OxmlElement("w:pgNumType")
        pg.set(qn("w:start"), "1")
        section._sectPr.append(pg)
    if page_numbers:
        where = section.header if prof.get("page_number") == "header" else section.footer
        p = where.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        add_field(p, " PAGE ", prof, prof["font"]["size"] - 1)


def centered(doc, text: str, prof: dict, size=None, bold=True, before=0, after=0, upper=False):
    p = doc.add_paragraph()
    para_format(p, 1.15, "center", after, before)
    set_font(p.add_run(text.upper() if upper else text), prof["font"]["name"], size or prof["font"]["size"], bold)
    return p


def thesis_cover(doc, meta: dict, prof: dict, warnings: list):
    def field(key, default=None):
        value = meta.get(key, default)
        if value in (None, ""):
            warnings.append(f"front matter field missing: {key}")
            return MISSING.format(key)
        return value

    ministry = f"{meta.get('ministry_left', 'BỘ GIÁO DỤC VÀ ĐÀO TẠO')}            {meta.get('ministry_right', 'BỘ Y TẾ')}"
    for inner in (False, True):
        centered(doc, ministry, prof, 14)
        centered(doc, field("university"), prof, 14, after=60)
        centered(doc, field("author"), prof, 14, after=60, upper=True)
        centered(doc, field("title"), prof, 16, upper=True, after=24)
        if inner:
            spec = doc.add_paragraph()
            para_format(spec, 1.5, None)
            spec.paragraph_format.left_indent = Cm(4)
            add_inline(spec, f"Chuyên ngành: {field('specialty')}", prof, 14)
            code = doc.add_paragraph()
            para_format(code, 1.5, None)
            code.paragraph_format.left_indent = Cm(4)
            add_inline(code, f"Mã số: {field('code')}", prof, 14)
        centered(doc, field("degree", "LUẬN VĂN THẠC SĨ Y HỌC"), prof, 15, before=18, after=18)
        if inner:
            centered(doc, "CÁN BỘ HƯỚNG DẪN KHOA HỌC:", prof, 14, bold=False)
            for name in meta.get("supervisors") or [MISSING.format("supervisors")]:
                centered(doc, f"{name}", prof, 14)
        centered(doc, field("place_year"), prof, 14, before=120)
        if not inner:
            doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def article_header(doc, meta: dict, prof: dict, warnings: list):
    size = prof["font"]["size"]
    font = prof["font"]["name"]
    title = meta.get("title") or MISSING.format("title")
    centered(doc, title, prof, size + 2, upper=True, after=6)
    authors = meta.get("authors") or []
    if not authors:
        warnings.append("front matter field missing: authors")
    p = doc.add_paragraph()
    para_format(p, 1.0, "right")
    for i, author in enumerate(authors):
        name = author.get("name", MISSING.format("author name")) if isinstance(author, dict) else str(author)
        affs = ",".join(str(a) for a in (author.get("aff") or [])) if isinstance(author, dict) else ""
        set_font(p.add_run(name), font, size, True)
        if affs:
            set_font(p.add_run(affs), font, size, True, superscript=True)
        if i < len(authors) - 1:
            set_font(p.add_run(", "), font, size, True)
    for i, aff in enumerate(meta.get("affiliations") or [], 1):
        a = doc.add_paragraph()
        para_format(a, 1.0, "right")
        set_font(a.add_run(str(i)), font, size - 1, False, True, superscript=True)
        set_font(a.add_run(f" {aff}"), font, size - 1, False, True)
    corr = meta.get("corresponding") or {}
    if corr:
        c = doc.add_paragraph()
        para_format(c, 1.0, "left", space_before=6)
        details = "; ".join(f"{k.capitalize()}: {v}" for k, v in corr.items() if k != "name")
        add_inline(c, f"**Tác giả liên hệ:** {corr.get('name', MISSING.format('corresponding name'))}"
                      + (f"; {details}" if details else ""), prof, size)


def parse_table(lines: list[str]) -> list[list[str]]:
    rows = []
    for line in lines:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
            continue
        rows.append(cells)
    return rows


def add_table(doc, rows: list[list[str]], prof: dict):
    width = max(len(r) for r in rows)
    table = doc.add_table(rows=len(rows), cols=width)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    tsize = prof["table"]["font_size"]
    for r, row in enumerate(rows):
        for c in range(width):
            cell = table.cell(r, c)
            cell.text = ""
            p = cell.paragraphs[0]
            para_format(p, prof["table"]["line_spacing"], "center" if r == 0 or c > 0 else "left")
            add_inline(p, row[c] if c < len(row) else "", prof, tsize, bold=(r == 0))


def convert(src: Path, dst: Path, profile_name: str) -> list[str]:
    profiles = load_profiles()
    warnings: list[str] = []
    if profile_name not in profiles:
        warnings.append(f"profile '{profile_name}' is not available in this edition; using 'generic'")
        profile_name = "generic"
    prof = profiles[profile_name]
    text = src.read_text(encoding="utf-8")
    meta = {}
    if text.startswith("---"):
        _, fm, text = text.split("---", 2)
        meta = yaml.safe_load(fm) or {}

    doc = Document()
    normal = doc.styles["Normal"]
    normal.font.name = prof["font"]["name"]
    normal.font.size = Pt(prof["font"]["size"])
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), prof["font"]["name"])

    has_sections = "<!-- section -->" in text
    first = doc.sections[0]
    if prof.get("front") == "hmu-thesis":
        setup_section(first, prof, prof.get("cover_margins", prof["page"]["margins"]), False, False)
        thesis_cover(doc, meta, prof, warnings)
        body = doc.add_section(WD_SECTION.NEW_PAGE)
        setup_section(body, prof, prof["page"]["margins"], not has_sections, True)
    else:
        setup_section(first, prof, prof["page"]["margins"], not has_sections, False)
        if prof.get("front") == "article":
            article_header(doc, meta, prof, warnings)

    para = prof["paragraph"]
    lines = text.splitlines()
    i = 0
    pending_caption = None
    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()
        if not stripped:
            i += 1
            continue
        if stripped == "<!-- pagebreak -->" or stripped == "\\newpage":
            doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        elif stripped == "<!-- section -->":
            sec = doc.add_section(WD_SECTION.NEW_PAGE)
            setup_section(sec, prof, prof["page"]["margins"], True, True)
        elif stripped == "[[TOC]]":
            p = doc.add_paragraph()
            add_field(p, ' TOC \\o "1-3" \\h \\z \\u ', prof, prof["font"]["size"])
        elif stripped.startswith("|"):
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i])
                i += 1
            add_table(doc, parse_table(block), prof)
            continue
        elif m := re.match(r"^(#{1,3})\s+(.*)$", stripped):
            level = len(m.group(1))
            spec = prof["headings"][level]
            p = doc.add_paragraph(style=f"Heading {level}")
            para_format(p, para["line_spacing"], spec.get("align"), 6, 12 if level == 1 else 6)
            content = m.group(2).upper() if spec.get("upper") else m.group(2)
            add_inline(p, content, prof, spec["size"], spec.get("bold", False), spec.get("italic", False))
        elif m := re.match(r"^!\[(.*?)\]\((.*?)\)$", stripped):
            image = (src.parent / m.group(2)).resolve()
            if image.exists():
                usable = 21.0 - prof["page"]["margins"]["left"] - prof["page"]["margins"]["right"]
                doc.add_picture(str(image), width=Cm(min(15.0, usable)))
                doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                warnings.append(f"image not found: {m.group(2)}")
            if m.group(1):
                cap = prof["figure_caption"]
                p = doc.add_paragraph()
                para_format(p, para["line_spacing"], cap["align"], 6)
                add_inline(p, m.group(1), prof, prof["font"]["size"], cap["bold"], cap["italic"])
        elif CAPTION_RE.match(stripped):
            is_table = stripped.startswith(("Bảng", "Table"))
            cap = prof["table_caption"] if is_table else prof["figure_caption"]
            p = doc.add_paragraph()
            para_format(p, para["line_spacing"], cap["align"], 3, 6)
            add_inline(p, stripped, prof, prof["font"]["size"], cap["bold"], cap["italic"])
        elif re.match(r"^[-*]\s+", stripped):
            p = doc.add_paragraph()
            para_format(p, para["line_spacing"], para["align"], para["space_after"])
            p.paragraph_format.left_indent = Cm(0.75)
            p.paragraph_format.first_line_indent = Cm(-0.5)
            add_inline(p, "– " + re.sub(r"^[-*]\s+", "", stripped), prof, prof["font"]["size"])
        else:
            buf = [stripped]
            while i + 1 < len(lines) and lines[i + 1].strip() and not re.match(
                    r"^(#|\||!\[|[-*]\s|<!--|\[\[TOC\]\])", lines[i + 1].strip()) and not CAPTION_RE.match(lines[i + 1].strip()):
                i += 1
                buf.append(lines[i].strip())
            content = " ".join(buf)
            p = doc.add_paragraph()
            para_format(p, para["line_spacing"], para["align"], para["space_after"],
                        first_indent=para.get("first_line_indent", 0))
            label = re.match(r"^(Nhận xét|Từ khóa|Keywords|Ghi chú)\s*:", content)
            if label and not content.startswith("**"):
                content = f"**{label.group(0)}**{content[label.end():]}"
            add_inline(p, content, prof, prof["font"]["size"])
        i += 1

    doc.save(dst)
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("output", nargs="?", type=Path)
    parser.add_argument("--profile", default="generic")
    parser.add_argument("--list-profiles", action="store_true")
    args = parser.parse_args()
    if args.list_profiles:
        for name, prof in load_profiles().items():
            print(f"{name}: {prof.get('description', '').strip()}")
        return 0
    if not args.input or not args.output:
        parser.error("input and output are required")
    warnings = convert(args.input, args.output, args.profile)
    print(f"wrote {args.output}")
    for w in warnings:
        print(f"warning: {w}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
