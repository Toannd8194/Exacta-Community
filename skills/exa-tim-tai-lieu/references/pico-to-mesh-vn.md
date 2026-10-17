# Vietnamese Question → PICO → MeSH, Local Sources, and Reference Checks

## Contents

- Step 1: PICO table
- Step 2: Concept expansion
- Step 3: PubMed query assembly
- Step 4: Vietnamese literature
- Reference checks

## Step 1: PICO table

Show this table to the user in Vietnamese before searching:

| Thành phần | Tiếng Việt (từ câu hỏi) | English concept |
|---|---|---|
| P – Đối tượng | | |
| I/E – Can thiệp / phơi nhiễm | | |
| C – So sánh | | |
| O – Kết cục | | |
| Thiết kế ưu tiên (tùy chọn) | | |

Ask the user to confirm or correct it. Translate concepts with
`../nature-shared/vn/medical-glossary-vi-en.md`; when unsure, offer two candidate English terms.

## Step 2: Concept expansion

For each PICO element, list:

- MeSH heading(s) — verify they exist through the base skill's MeSH workflow; never invent one
- Entry terms and free-text synonyms (spelling variants: anaemia/anemia)
- Truncation where safe (`diabet*`)

Optional filters for local evidence: `Vietnam[MeSH] OR Vietnam*[tiab] OR Viet Nam[tiab]`.

## Step 3: PubMed query assembly

```
(P_mesh[MeSH] OR P_free[tiab]) AND (I_mesh[MeSH] OR I_free[tiab]) AND (O_mesh[MeSH] OR O_free[tiab])
```

Add C only when it narrows meaningfully. Report the hit count and the first-page relevance check
to the user, then refine. Save the final string and date of search for the methods section.

## Step 4: Vietnamese literature

Give the user search strings in Vietnamese, both with and without diacritics, for:

- Vietnam Journals Online (VJOL)
- Tạp chí Y học Việt Nam and other Vietnamese medical journals' own websites
- University thesis and dissertation repositories (the user's institution library)
- Google Scholar with Vietnamese keywords

The agent does not scrape these sites; the user runs the searches and shares results.

## Reference checks

Apply the base skill's citation-verification workflow, plus:

| Situation | Action |
|---|---|
| Reference has DOI or PMID | Verify author, title, year, volume, pages against the registry record |
| Vietnamese journal article without DOI | Mark "không xác minh trực tuyến được — cần kiểm tra bản in/trang tạp chí"; do not guess fields |
| Vietnamese thesis or textbook | Check author, title, institution/publisher, year format; mark as unverifiable online |
| Author names | Vietnamese names keep full form in Vancouver style used by Vietnamese journals (for example "Nguyễn Văn A") unless the target journal requires family-name-plus-initials; state which rule is applied |
| Reference cannot be found anywhere | Flag as possibly fabricated or mis-cited; never "repair" it by inventing details |
| Style | Default to AMA/Vancouver with DOI (as in the reference thesis and article in `../../nature-shared/vn/formatting-profiles.md`); Vietnamese sources list full Vietnamese names and end the author list with "và cs.". Confirm the target's rule when the user has it |

Output a table: `# | Trạng thái (Đúng / Sai trường / Không xác minh được / Không tìm thấy) | Trường lệch | Đề xuất sửa`.
