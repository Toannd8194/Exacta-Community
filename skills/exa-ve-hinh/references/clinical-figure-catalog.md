# Clinical Figure Catalogue

Required elements for standard clinical displays. A figure missing a required element is not
ready for delivery; list the gap in the delivery report.

## Contents

- Kaplan–Meier survival curve
- Forest plot
- ROC curve
- Proportions and continuous outcomes
- Backend pointers

## Kaplan–Meier survival curve

Required:
- Step function per group, censoring marks (`+`), y-axis as probability or % from 0 to 1 (or 100)
- Time axis with units (days, months) and sensible breaks
- **Number-at-risk table** aligned under the time axis
- Effect estimate in the figure or legend: HR with 95% CI (Cox) and log-rank P
- Optional shaded 95% CI bands; avoid if more than two groups overlap heavily
Avoid: truncating the y-axis without stating it; extending curves where fewer than ~10% remain at
risk without noting instability.

## Forest plot

Required:
- One row per study or subgroup: label, n or events/total, point estimate, 95% CI
- **Log scale** for ratios (OR, RR, HR) with the null line at 1; linear scale with null at 0 for
  differences
- Direction labels under the axis ("Favours intervention" / "Favours control")
- Overall or pooled estimate as a diamond (meta-analysis) with heterogeneity (I², P)
- Subgroup plots: P for interaction per subgrouping variable
Avoid: marker size implying weight without stating it; mixing adjusted and unadjusted estimates
without labelling.

## ROC curve

Required:
- Sensitivity (y) vs 1 − specificity (x), both 0–1, square aspect ratio
- Diagonal reference line
- AUC with 95% CI in the legend
- Chosen cut-off marked, with its sensitivity and specificity, and the method (for example
  Youden index)
- When comparing tests: same axes, DeLong test P if claimed different
Avoid: smoothing an empirical curve without saying so.

## Participant flow, agreement, and calibration figures

CONSORT/STROBE flow diagrams, Bland–Altman plots, and calibration plots are Exacta Pro
capabilities. If requested, follow `../../nature-shared/vn/community-edition.md`.

## Proportions and continuous outcomes

- Proportions: bar or dot charts with n/N and 95% CI; no 3D, no pie charts for comparisons
- Continuous outcomes: show distribution (box, violin, or individual points for small n), not
  bar-plus-SD ("dynamite") plots
- Paired measurements: connect pairs (before–after lines)
- Always state n per group in the axis or legend

## Backend pointers

- Python: the base skill's `make_forest_plot` helper (see `../../nature-figure/references/api.md`);
  survival with `lifelines`; ROC with `scikit-learn` metrics. Check the packages exist before
  use and follow the base missing-runtime rule.
- R: the base skill's template index row for survival, Cox, subgroup, ROC, and forest plots
  (`../../nature-figure/references/r-template-index.md`): `survival`, `survminer`, `forestplot`,
  `pROC` or `timeROC`.
