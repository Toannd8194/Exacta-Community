# Review Gates for Manuscripts by Vietnamese Clinical Authors

Run every gate. A gate that does not apply is recorded as "not applicable" with a reason. Each
failure becomes a concern in the base skill's ledger with the suggested default severity; adjust
severity using the base skill's taxonomy.

## Contents

- G1 Ethics and consent
- G2 Reporting guideline
- G3 Design–claim match
- G4 Sample size and sampling
- G5 Outcome definitions and instruments
- G6 Statistical reporting
- G7 Generalisation and setting
- G8 Literature positioning
- G9 Language and presentation

## G1 Ethics and consent — default: Blocking

- Ethics committee named, with approval number and date. Missing or placeholder values are
  Blocking.
- Informed consent described (written/verbal, waiver justified for retrospective record review).
- Case reports and identifiable images: patient consent for publication stated.
- Trial registration number for prospective interventional studies.

## G2 Reporting guideline — default: Major

Identify the matching guideline and check the core items:

| Design | Guideline |
|---|---|
| Cross-sectional, cohort, case–control | STROBE |
| Randomised trial | CONSORT |
| Diagnostic accuracy | STARD |
| Case report | CARE |
| Systematic review / meta-analysis | PRISMA |
| Prediction model | TRIPOD |
| Quality improvement | SQUIRE |
| Qualitative | COREQ / SRQR |

Missing flow diagram (participants screened, excluded, analysed) is a frequent Major concern.

## G3 Design–claim match — default: Major

- Cross-sectional or single-time-point data described with causal verbs ("gây ra", "làm tăng",
  "ảnh hưởng đến", "causes", "leads to").
- Uncontrolled before–after studies presented as proof of effectiveness.
- "Associated factors" analysis based only on bivariate tests without adjustment.
- Conclusions that answer questions the stated objectives did not ask.

## G4 Sample size and sampling — default: Major

- Sample size formula stated with every input value and its source.
- Formula matches the objective (a single-proportion formula does not justify an association or
  comparison analysis).
- Sampling method matches the inference (convenience or consecutive sampling cannot support
  population prevalence claims without caveats).
- Achieved sample versus planned sample, with reasons for shortfall.

## G5 Outcome definitions and instruments — default: Major

- Diagnostic criteria named with version and year (for example a specific guideline edition).
- Cut-offs justified; population-specific cut-offs (for example Asian BMI thresholds) stated
  explicitly.
- Questionnaires: validated Vietnamese version cited, or translation and validation procedure
  described.
- Laboratory methods: analyser, assay, and reference ranges.

## G6 Statistical reporting — default: Major

- Tests named for every p-value.
- Effect sizes with 95% CI reported for main results, not only p-values.
- Continuous variables summarised appropriately for their distribution.
- Multivariable models: variable selection strategy, events per parameter, and model checks.
- Percentages with denominators; missing data reported.

## G7 Generalisation and setting — default: Minor (Major if the title or conclusion overreaches)

- Single-centre tertiary hospital data generalised to the national population.
- Setting described (hospital level, catchment, referral pattern) so readers can judge
  transferability.

## G8 Literature positioning — default: Minor

- Claims of being "first in Vietnam" supported by a described search.
- Comparison with international and regional studies, not only Vietnamese single-centre reports.
- Discussion explains differences in findings rather than listing studies.

## G9 Language and presentation — default: Minor

- Tense, article, and plural errors typical of Vietnamese authors (see
  `../nature-shared/vn/vi-to-en.md`).
- Decimal commas in English text.
- Tables that duplicate the text in full.
