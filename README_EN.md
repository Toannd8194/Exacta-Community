# Exacta Community

**Evidence-based AI tools for health-science research, built for the Vietnamese research community.**

<!-- validator marker: badge/skills-25-0ea5e9 -->

`Open source · Apache-2.0` · `12 Vietnamese skills` · `Runs on Claude Code` · `Your data stays on your machine` · [Tiếng Việt](README.md)

Developed by **Nguyen Duy Toan, MD, MSc** · [facebook.com/dutonezo](https://www.facebook.com/dutonezo)

*Exacta* is Latin for "exact". Exacta is a set of skills for an AI assistant (Claude Code) that
supports researchers through the whole cycle: framing the research question, finding and
appraising literature, designing the proposal, checking statistics, presenting data, writing and
translating the manuscript, reviewing before submission, and presenting results. Users work in
Vietnamese; outputs meet international journal standards and Vietnamese presentation rules.

## 1. Scientific principles

| Principle | How Exacta applies it |
|---|---|
| **Evidence-based** | Uses only facts supplied by the author or appraised sources. Never generates data, references, DOIs, or approval numbers; missing information is marked `[CẦN BỔ SUNG]`. |
| **Academic integrity** | Written from the author's notes and reasoning, synthesising and fully citing sources; never translate-and-copy, never disguise borrowed text. |
| **Transparent and verifiable** | Every citation carries a PMID/DOI and a support grade (direct, partial, unsupported, contradicting). Every sample-size formula shows all inputs and their sources. |
| **International reporting standards** | Checks manuscripts against STROBE, CONSORT, STARD, CARE, PRISMA, TRIPOD; keeps causal language consistent with the study design. |
| **Fit for Vietnamese research** | Presentation conventions checked against an accepted master's thesis and an accepted research article: chapters organised by objective, a "Nhận xét" after each table, caption placement, citation style; a Vietnamese–English medical glossary; Word export. |
| **Patient data protection** | Manuscripts and data stay on the user's machine; identifiers are screened before analysis; network use is limited to bibliographic lookups by keyword and public identifier. |

## 2. Academic support for everyone

| Who | What Exacta supports |
|---|---|
| Medical students, postgraduate trainees (master's, CKI/CKII, residency, PhD) | Proposal outlines, sample-size checks, literature search, thesis figures |
| Clinicians | Fast reading and appraisal of papers, journal club preparation, writing papers from practice data |
| Lecturers and supervisors | Reviewing trainees' proposals and manuscripts against consistent criteria |
| Research groups | Data availability statements, submission preparation, mock review, reviewer responses |

```mermaid
flowchart LR
    A["Research question"] --> B["Find and appraise literature<br/>exa-tim-tai-lieu"]
    B --> C["Proposal<br/>exa-de-cuong"]
    C --> D["Statistics, sample size<br/>exa-thong-ke"]
    D --> E["Data presentation<br/>exa-ve-hinh"]
    E --> F["Writing and translation<br/>exa-viet-bai · exa-dich-thuat"]
    F --> G["Pre-submission review<br/>exa-phan-bien"]
    G --> H["Submission, response<br/>exa-du-lieu · exa-phuc-dap"]
    H --> I["Presenting results<br/>exa-trinh-chieu"]
```

At every step, `exa-doc-song-ngu` (English–Vietnamese reader) and `exa-doc-sau` (deep-reading
card) support reading and appraisal.

## 3. Get started

1. Install [Git](https://git-scm.com/) and [Claude Code](https://claude.com/claude-code).
2. Download Exacta Community and install the skills (Windows):

   ```bash
   git clone https://github.com/Toannd8194/Exacta-Community.git exacta
   ```

   ```bash
   powershell -ExecutionPolicy Bypass -File exacta/scripts/vn-install-skills.ps1
   ```

   macOS/Linux: `bash exacta/scripts/vn-install-skills.sh`

3. Open a new Claude Code session in your project folder and ask in Vietnamese or English:

| Purpose | Example prompt |
|---|---|
| Search strategy | `Use exa-tim-tai-lieu to build a PubMed/MeSH strategy for: ...` |
| Sample-size check | `Use exa-thong-ke to check the sample-size formula in de-cuong.md.` |
| Proposal outline | `Use exa-de-cuong to outline a master's thesis proposal on ...` |
| Figures | `Use exa-ve-hinh to draw a Kaplan–Meier curve for my thesis.` |
| Mock review | `Use exa-phan-bien to review this manuscript as an international journal referee.` |

Need help installing? Contact the developer (section 5).

## 4. Privacy and research integrity

- Manuscripts, data, reviewer letters, and patient information are never sent to external services.
- No third-party image-generation, OCR, or messaging integrations; no scheduled jobs, no auto-update.
- References are cited only after the abstract is read; unverifiable references are reported,
  never "adjusted to fit".
- All rules live in [AGENTS.md](AGENTS.md) and load automatically in every session.

## 5. Developer, support, and Exacta Pro

**Nguyen Duy Toan, MD, MSc** develops and maintains Exacta, aiming for a precise, transparent,
and accessible research tool for health scientists in Vietnam.
Contact: [facebook.com/dutonezo](https://www.facebook.com/dutonezo)

- **Installation support:** the developer can help install and get started with Community.
- **Exacta Pro** is for individuals and institutions needing close support: departments,
  hospitals, universities, research groups. Pro includes every mode of all 12 skills,
  customisation to each institution's presentation rules, installation, training, and
  operational support, for a small fee.

Community has two layers. The **base engine** (13 upstream `nature-*` skills) is complete and
can be called directly, to a general international-journal standard. The **Vietnamese layer**
(12 `exa-*` skills) adds Vietnamese review criteria, explanations, and plans; some of its modes
are in Exacta Pro:

| Skill | Community | Added in Pro |
|---|---|---|
| `exa-de-cuong` | Detailed outline, objective–design–sample-size alignment table | Full drafting, checklist audit, doctoral proposals, ethics dossiers |
| `exa-phan-bien` | One referee report with Vietnamese review gates; `nature-reviewer` gives three blind reviewers to a general international standard | All three reviewers and the synthesis apply the Vietnamese gates, plus a Vietnamese action summary |
| `exa-phuc-dap` | Triage of all comments, replies to up to 5 per request; `nature-response` gives a full general-standard package | Complete response package, editor letter, marked manuscript, with Vietnamese plan and author check |
| `exa-trinh-chieu` | Slide outline with speaker notes; `nature-paper2ppt` builds a paper-report PPTX | PPTX for proposal, thesis, and doctoral defences and Vietnamese conferences, with quality audit |
| `exa-tim-tai-lieu` | Claim-by-claim citations, up to 10 claims per request, RIS export | Whole-manuscript batches with merging and de-duplication, BibTeX/nbib |
| `exa-thong-ke` | Audit of reported statistics, all sample-size formulas, test selection | Common-errors audit for Vietnamese theses, multivariable model check, raw-data analysis |
| `exa-ve-hinh` | Kaplan–Meier, forest plot, ROC, thesis charts | Ready templates for CONSORT/STROBE flow, Bland–Altman, calibration plots |
| `exa-viet-bai`, `exa-dich-thuat`, `exa-doc-sau` | Section drafting, Vietnamese → English translation and polishing, deep-reading card | Thesis-to-article conversion, English → Vietnamese, whole-manuscript terminology check, risk-of-bias assessment |
| Plagiarism | Integrity rules applied by default in every writing skill | Local similarity self-check against the Turnitin/DoIT limit, plagiarism check and repair |
| Word files | General layout; adjust margins and spacing yourself | Exact thesis and journal templates: covers, TOC, page numbers, citation style |

## 6. Skill catalogue

| Skill | Purpose |
|---|---|
| [`exa-de-cuong`](skills/exa-de-cuong/README_EN.md) | Proposal and thesis outlines (limited) |
| [`exa-dich-thuat`](skills/exa-dich-thuat/README_EN.md) | Vietnamese → English translation and polishing |
| [`exa-doc-sau`](skills/exa-doc-sau/README_EN.md) | Deep-reading card with local applicability |
| [`exa-doc-song-ngu`](skills/exa-doc-song-ngu/README_EN.md) | English–Vietnamese paper reader |
| [`exa-du-lieu`](skills/exa-du-lieu/README_EN.md) | Data availability, data management |
| [`exa-phan-bien`](skills/exa-phan-bien/README_EN.md) | Mock peer review (limited) |
| [`exa-phuc-dap`](skills/exa-phuc-dap/README_EN.md) | Response to reviewers (limited) |
| [`exa-thong-ke`](skills/exa-thong-ke/README_EN.md) | Statistics and sample size |
| [`exa-tim-tai-lieu`](skills/exa-tim-tai-lieu/README_EN.md) | PubMed/MeSH, citations, RIS export |
| [`exa-trinh-chieu`](skills/exa-trinh-chieu/README_EN.md) | Slide outlines (limited) |
| [`exa-ve-hinh`](skills/exa-ve-hinh/README_EN.md) | Kaplan–Meier, forest plot, ROC |
| [`exa-viet-bai`](skills/exa-viet-bai/README_EN.md) | English manuscript drafting |

<details>
<summary><b>Base engine</b> — 13 upstream skills the <code>exa-*</code> skills call; also callable directly for general international-standard work</summary>

| Skill | Role |
|---|---|
| [`nature-academic-search`](skills/nature-academic-search/README_EN.md) | Multi-source search, MeSH |
| [`nature-citation`](skills/nature-citation/README_EN.md) | Nature/CNS-scope citations |
| [`nature-data`](skills/nature-data/README_EN.md) | Data availability |
| [`nature-figure`](skills/nature-figure/README_EN.md) | Python/R figures |
| [`nature-paper-card`](skills/nature-paper-card/README_EN.md) | Paper card |
| [`nature-paper-xray`](skills/nature-paper-xray/README_EN.md) | Single-paper deep analysis |
| [`nature-paper2ppt`](skills/nature-paper2ppt/README_EN.md) | Paper to slides |
| [`nature-polishing`](skills/nature-polishing/README_EN.md) | English polishing |
| [`nature-reader`](skills/nature-reader/README_EN.md) | Bilingual reader |
| [`nature-response`](skills/nature-response/README_EN.md) | Reviewer responses |
| [`nature-reviewer`](skills/nature-reviewer/README_EN.md) | Independent mock review |
| [`nature-statistics`](skills/nature-statistics/README_EN.md) | Statistical reporting |
| [`nature-writing`](skills/nature-writing/README_EN.md) | Manuscript drafting |

</details>

## 7. Contributing

Feedback and contributions are welcome through Issues and Pull Requests. Rules are in
[AGENTS.md](AGENTS.md): add content as new files (`skills/exa-*`, `skills/nature-shared/vn/`)
and do not edit base-engine files. Components removed from the base engine are listed in
[frozen/FROZEN.md](frozen/FROZEN.md). Before submitting, run:

```bash
python scripts/validate-skill-metadata.py
python scripts/validate-repository.py
python scripts/validate-skill-index.py
python scripts/validate-readmes.py
python scripts/validate-readme-mirror.py
python -m pytest scripts/tests
```

## 8. License

Apache-2.0 — free to use, modify, and redistribute. Exacta builds on the open-source project
[Nature Skills](https://github.com/Yuan1z0825/nature-skills) by Yuan Yizhe and contributors; the
original copyright notice is retained in [LICENSE](LICENSE).
