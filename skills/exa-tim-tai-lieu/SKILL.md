---
name: exa-tim-tai-lieu
description: "Vietnamese overlay for nature-academic-search: turn a Vietnamese clinical question into a PICO-based PubMed/MeSH strategy, search international and Vietnamese literature, find supporting references claim by claim, export to Zotero/EndNote (RIS/BibTeX), and verify reference lists. Use for tìm tài liệu, chiến lược tìm kiếm PubMed, MeSH, bổ sung trích dẫn cho từng luận điểm, kiểm tra tài liệu tham khảo; not for drafting manuscript prose."
metadata:
  version: "0.1.0"
  base_skill: nature-academic-search
---

# Exacta · Tìm tài liệu — Vietnamese Overlay

## Load order

1. Read [manifest.yaml](manifest.yaml) and every `always_load` file.
2. Read [../nature-academic-search/SKILL.md](../nature-academic-search/SKILL.md) and follow
   its routing protocol in full (multi-source search, citation verification, MeSH strategy,
   reference management).
3. Apply the overrides below. On conflict, these overrides win.

Never load any file listed as frozen in `frozen/FROZEN.md`. The strict-other-citation and
citer-profile workflow (`wf6`) is allowed but must not be used to profile private individuals.

## Overrides

### Vietnamese question intake

When the question is in Vietnamese, load `references/pico-to-mesh-vn.md`, build the PICO table,
and show it to the user (in Vietnamese) before running searches. Then hand the English concepts
to the base skill's MeSH workflow.

### Network boundary

Remote queries contain only search terms and public identifiers. Never send manuscript text,
unpublished results, or patient details in a query.

### Vietnamese literature

International databases index few Vietnamese journals. When local evidence matters, provide
ready-to-use search strings for the Vietnamese sources listed in
`references/pico-to-mesh-vn.md` and let the user run them. Do not scrape these sites.

### Reference verification

For reference-list checks (formerly `nature-ref-verifier`, now frozen), use the base skill's
citation-verification workflow and add the Vietnamese rules in
`references/pico-to-mesh-vn.md` § Reference checks.

### Claim-by-claim citation and export

When the user asks to find references for the statements in a draft ("tìm tài liệu cho từng
luận điểm", "bổ sung trích dẫn"), or to export references to Zotero/EndNote/Mendeley, load
`references/claim-citation.md`. It replaces `nature-citation` for clinical work: no journal
restriction, concept-only queries, support grading, and RIS/BibTeX export by PMID/DOI.

Do not run `../nature-citation/scripts/nature_citation.py` with `--text`, `--text-file`,
`--claim`, or `--claim-file`: those modes send manuscript passages to Crossref.

### Community edition scope

- Claim-by-claim citation handles up to 10 claims per request and exports RIS.
- Whole-manuscript batches with merging and de-duplication, and BibTeX/nbib export, are Exacta
  Pro capabilities. If the user asks for them, follow
  `../nature-shared/vn/community-edition.md`.

### Output

Explanations and summaries in Vietnamese; search strings, MeSH terms, and citations in English
(Vietnamese titles kept in the original language with diacritics).
