# Vietnamese-to-English Drafting and Repair

Use when the author's notes or draft are Vietnamese, mixed Vietnamese–English, or English
written by a Vietnamese author. Replaces the upstream `zh-to-en.md` fragment and Chinese-author
references in this fork.

## Contents

- Translate intent, not syntax
- Drafting sequence
- Structural repairs
- Grammar repairs typical of Vietnamese authors
- Claim-strength repairs typical of Vietnamese clinical papers
- Output convention

## Translate intent, not syntax

Vietnamese academic prose often opens with broad social importance, stacks several clauses with
commas, and states conclusions before evidence. Before writing English, split each note into:

- claim
- evidence (with numbers and comparator)
- condition (population, setting, time)
- comparison
- implication
- limitation

Then write English in the order the target section requires.

## Drafting sequence

1. Restate the author's intended claim in one Vietnamese sentence.
2. List missing evidence or boundaries as `[CẦN BỔ SUNG: ...]`.
3. Draft the English paragraph.
4. Add the Vietnamese author check block from `language-policy.md`.

## Structural repairs

| Vietnamese-draft pattern | English repair |
|---|---|
| Opening with national burden ("Ở Việt Nam, bệnh X đang là vấn đề sức khỏe cộng đồng...") before the research gap | Keep one sentence of burden with a cited figure, then move quickly to the specific knowledge gap |
| "Mục tiêu" listed as verbs without measurable endpoints | Rewrite each aim with population, exposure/intervention, outcome, and time frame |
| Results section that repeats every table cell in prose | Report the primary outcome and key contrasts; point to the table for the rest |
| Discussion that restates results then compares with each prior study one by one | Organise by claim: finding → comparison → explanation → limitation |
| "Kết luận" that introduces new data or recommendations not tested | Limit conclusions to the stated aims; move recommendations to implications |
| Long sentences joined by commas ("..., ..., do đó ...") | Split into separate sentences with explicit connectives |

## Grammar repairs typical of Vietnamese authors

Vietnamese has no inflection for tense, number, or articles. Check these explicitly:

| Problem | Repair |
|---|---|
| Missing tense marking | Past tense for methods and findings of this study; present tense for established facts and for what a table or figure shows |
| Missing plurals ("many patient", "the result showed") | Decide singular/plural for every count noun |
| Missing or wrong articles | Use `the` for previously defined entities; no article for general uncountable nouns; `a/an` for first mention of a countable noun |
| Subject–verb agreement after collective nouns ("the data shows", "patients was") | Match number; treat `data` as plural unless the journal style says otherwise |
| Literal "according to" chains ("theo nghiên cứu của...") | Use the citation directly: "X et al. reported..." or a numeric citation |
| Overuse of "In addition", "Besides", "Moreover" at sentence start | Use them sparingly; let paragraph logic carry the connection |
| "Rate" vs "proportion" vs "prevalence" used interchangeably ("tỷ lệ") | Choose by meaning: prevalence (existing cases), incidence (new cases over time), proportion (part of a whole), rate (per unit time) |
| "Tỷ lệ nam/nữ" written as a ratio when a percentage is meant | Report "x% were men" or "male-to-female ratio of a:b", not both |
| Vietnamese decimal comma copied into English (`12,5%`) | Use decimal point in English (`12.5%`) |

## Claim-strength repairs typical of Vietnamese clinical papers

| Pattern | Repair |
|---|---|
| Cross-sectional association described as cause ("X gây ra Y", "X làm tăng Y") | "X was associated with Y" |
| "Có ý nghĩa thống kê" used as proof of clinical importance | Report effect size with 95% CI and discuss clinical relevance separately |
| Single-centre convenience sample generalised to "người bệnh Việt Nam" | Bound the claim to the setting and population studied |
| "Lần đầu tiên tại Việt Nam" without a search to support it | Use a bounded claim ("to our knowledge, few studies in Vietnam have...") and cite the search |
| Before–after study without control described as proving effectiveness | Describe as change observed; note lack of a control group |
| p-values without the test or the effect size | Name the test; report effect size and 95% CI |

## Output convention

Provide the English text first, then the Vietnamese author check block. Never interleave
Vietnamese inside the English manuscript text.
