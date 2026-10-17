# Claim-by-Claim Citation and Reference-Manager Export

Find supporting literature for each claim in a draft, without journal-family restriction and
without sending manuscript text to any remote service. Adapted from the claim-to-source method
of `nature-citation`, whose script is not used here (it sends draft passages to Crossref and is
limited to Nature/Science/Cell journals).

## Contents

- Step 1: Claim ledger (local)
- Step 2: Concept queries
- Step 3: Search
- Step 4: Grade support
- Step 5: Export
- Output

## Step 1: Claim ledger (local)

Read the draft locally and list every statement that needs a citation:

| ID | Vị trí | Luận điểm (tóm tắt) | Loại | Cần trích dẫn? |
|---|---|---|---|---|

Types: background fact, epidemiological number, mechanism, method or instrument, guideline
recommendation, comparison with prior studies. Claims about the authors' own results need no
citation.
Process at most 10 claims per request (the first 10 in document order, or the 10 the user
chooses). List the remaining claims so the user can send them in a follow-up request.

## Step 2: Concept queries

For each claim, build a query from **concepts only** (PICO elements, MeSH terms, key outcome
words). Never paste the claim sentence or any manuscript wording into a query. Prefer:

- Epidemiological numbers → `[condition] AND (prevalence OR incidence) AND [population/region]`
- Treatment effects → systematic reviews and RCTs first
- Recommendations → current guideline from the issuing society (name and year)
- Methods/instruments → the original validation paper, and the Vietnamese validation study if
  a translated instrument was used

## Step 3: Search

Use the base skill's multi-source search and MeSH workflows (PubMed first for clinical
claims). Apply filters only when they match the claim: humans, publication types, date range
(usually the last 5–10 years unless a seminal source is needed). For claims about Vietnam,
also give the user Vietnamese search strings (see `pico-to-mesh-vn.md` § Step 4).

## Step 4: Grade support

Read the abstract (or the full text the user supplies) before citing. Grade each candidate:

| Mức | Ý nghĩa | Dùng được? |
|---|---|---|
| Hỗ trợ trực tiếp | The source reports this finding or number | Yes |
| Hỗ trợ một phần | Supports part of the claim, or a different population/setting | Yes, with the claim narrowed |
| Liên quan, không hỗ trợ | Same topic, does not support the statement | No |
| Mâu thuẫn | Contradicts the claim | Tell the author; do not hide |

Never cite a source on the strength of its title. Prefer higher evidence (guideline, systematic
review, RCT) for clinical claims; prefer the primary source for numbers instead of a review that
quotes them.

## Step 5: Export

Export verified sources by identifier only, using the base skill's converter:

```bash
python skills/nature-academic-search/scripts/format-converter.py --pmid <PMID1,PMID2> --format ris
```

Use `--doi` for records without PMID. RIS imports into Zotero, EndNote, and Mendeley.
Sources without DOI/PMID (Vietnamese journals, theses) are entered manually by the user;
never fabricate fields for them.

## Output

1. Claim → source table: `ID | Luận điểm | Nguồn đề xuất (tác giả, năm, tạp chí, PMID/DOI) | Mức hỗ trợ | Ghi chú`
2. Suggested citation markers in the draft, numbered in order of first citation, written as
   `[n]` (the Word export renders superscript for theses and brackets for Tạp chí Y học Cộng
   đồng; see `../../nature-shared/vn/formatting-profiles.md` § Citations and references)
3. Path of the exported RIS/BibTeX file
4. **Luận điểm chưa có nguồn**: claims that found no direct support, with a suggestion to supply
   a source, narrow the wording, or remove the claim
