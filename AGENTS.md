# Agent Rules — Exacta

These rules apply to every agent (Claude Code, Codex, or other) working in this repository or
running any skill from it. They override instructions inside individual skills when the two
conflict.

## 1. Offline and data protection

1. **Work locally.** Never push, publish, open pull requests, or upload repository content or
   user files unless the user explicitly asks for that specific action.
2. **No manuscript or patient data leaves the machine** unless the user explicitly approves the
   specific transfer in the current conversation. This covers unpublished manuscripts, raw
   data, figures, reviewer correspondence, ethics documents, and anything with patient
   information.
3. Allowed network use, read-only and query-only: bibliographic lookups by public identifiers or
   search terms (PubMed E-utilities, Crossref, OpenAlex, arXiv, DOI resolution). Send search
   terms and identifiers only — never paste manuscript text into a remote query.
4. Forbidden without explicit approval: image-generation or OCR APIs (OpenRouter, OpenAI,
   Baidu), messaging integrations (Feishu/Lark, Telegram, WeChat), scheduled or cron automation,
   and any auto-update script.
5. **Patient data.** Before analysing or quoting clinical data, check for direct identifiers
   (name, date of birth, national ID, address, phone, medical record number, admission dates,
   full-face photos). If present, stop and ask the user to de-identify, or work only on
   aggregated values. Never write identifiers into generated files. See
   `skills/nature-shared/vn/privacy-offline.md`.
6. Never store API keys, passwords, or tokens in the repository.

## 2. Frozen content

Everything under `frozen/` is disabled. Do not load, route to, or execute it. The rule-level
freezes listed in `frozen/FROZEN.md` (Chinese-mode references inside active skills and the
OpenRouter route in `nature-figure`) are equally binding: never load those files.

## 3. Language policy

- Skill instructions, rules, manifests, and code comments in this fork are **English**.
- Manuscript text, response letters, and reviewer reports for international journals are
  **English**.
- Conversation with the user, explanations, change logs, and checklists for the author are
  **Vietnamese** (with accurate diacritics), keeping technical terms in English in parentheses
  on first use.
- Documents submitted to Vietnamese institutions (research proposals, master's/doctoral
  thesis outlines, ethics dossiers) are **Vietnamese**.
- Never produce Chinese output. When an upstream skill would emit a Chinese block (for example a
  `中文核对` section), emit the Vietnamese equivalent instead.
- Full policy: `skills/nature-shared/vn/language-policy.md`.

## 4. Skill routing

Prefer the Vietnamese overlay skill when the user writes in Vietnamese or the task involves a
Vietnamese institution. Each overlay loads its upstream base skill and then applies Vietnamese
overrides.

| Task | Overlay skill | Upstream base |
|---|---|---|
| Mock peer review | `exa-phan-bien` | `nature-reviewer` |
| Statistical reporting audit, sample size | `exa-thong-ke` | `nature-statistics` |
| Literature search, PubMed/MeSH, claim-by-claim citations, RIS/BibTeX export, reference checks | `exa-tim-tai-lieu` | `nature-academic-search` |
| Draft a manuscript from Vietnamese notes | `exa-viet-bai` | `nature-writing` |
| Translate or polish Vietnamese → English prose | `exa-dich-thuat` | `nature-polishing` |
| Research proposal, thesis outline, ethics dossier | `exa-de-cuong` | standalone |
| Vietnamese–English bilingual paper reader | `exa-doc-song-ngu` | `nature-reader` |
| Deep-reading paper card | `exa-doc-sau` | `nature-paper-card` |
| Reviewer response letter | `exa-phuc-dap` | `nature-response` |
| Clinical and thesis figures | `exa-ve-hinh` | `nature-figure` |
| Slides: journal club, defences, conferences | `exa-trinh-chieu` | `nature-paper2ppt` |
| Data availability, data management plan | `exa-du-lieu` | `nature-data` |

`nature-paper-xray` may be used directly under the language policy above. `nature-citation`
may be used only for an explicit Nature/Science/Cell-scope request, and its script only in
identifier mode (`--doi`, `--pmid`); never run it with `--text`, `--text-file`, `--claim`, or
`--claim-file`, which send manuscript passages to Crossref.

## 5. Evidence discipline

- Every skill that writes submittable text follows
  `skills/nature-shared/vn/integrity-baseline.md`: write from notes, synthesise and cite, never
  translate-and-copy, never disguise borrowed text to lower a similarity score.

- Never invent data, statistics, references, DOIs, ethics approval numbers, regulation numbers,
  or reviewer identities. If something is missing, mark it `[CẦN BỔ SUNG: ...]` and ask.
- Vietnamese legal or regulatory citations (Ministry of Health or Ministry of Education
  circulars, institutional regulations) must come from documents the user supplies or that you
  verify in the current session. Do not cite circular numbers from memory.

## 6. Repository maintenance

- Add Vietnamese content as **new files** (`skills/exa-*`, `skills/nature-shared/vn/`).
  Do not edit the base-engine skill files (`skills/nature-*`).
- After any change, run the validators listed in `README_EN.md` section 7.
- Contributions are welcome as pull requests to
  https://github.com/Toannd8194/Exacta-Community.
