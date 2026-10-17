# Sample Size and Design Matching for Vietnamese Clinical Studies

Notation: Z(1−α/2) = 1.96 for α = 0.05 (two-sided); Z(1−β) = 0.84 for 80% power, 1.28 for
90% power. Always round the final n **up** to the next integer.

## Contents

- Objective-to-formula map
- Formulas
- Adjustments
- Test selection
- Reporting template

## Objective-to-formula map

| Objective wording (Vietnamese) | Typical design | Formula |
|---|---|---|
| "Mô tả / xác định tỷ lệ ..." | Cross-sectional | F1 or F2 (one proportion) |
| "Mô tả đặc điểm ... (giá trị trung bình)" | Cross-sectional | F3 (one mean) |
| "So sánh tỷ lệ ... giữa hai nhóm" | Cross-sectional comparison, cohort, trial | F4 (two proportions) |
| "So sánh giá trị trung bình ..." | Two-group comparison, trial | F5 (two means) |
| "Đánh giá giá trị chẩn đoán (độ nhạy, độ đặc hiệu)" | Diagnostic accuracy | F6 |
| "Tìm hiểu mối tương quan giữa X và Y" | Correlation | F7 |
| "Xác định một số yếu tố liên quan" (multivariable) | Analytical cross-sectional | F1/F2 for the prevalence aim; model adequacy check in Exacta Pro |
| "Đánh giá kết quả điều trị" (single arm) | Before–after | F3/F1 with precision, or paired design; state lack of control |

When a study has several objectives, compute n for each and use the largest, or state which
objective drives the sample size.

## Formulas

**F1 — One proportion, absolute precision**

n = Z(1−α/2)² × p(1 − p) / d²

p from a cited comparable study; d is the absolute margin (for example 0.05). If p is unknown,
p = 0.5 gives the maximum n. Rule of thumb: d should be well below p (if p < 0.1, use
d ≤ p/2 or switch to F2).

**F2 — One proportion, relative precision**

n = Z(1−α/2)² × (1 − p) / (ε² × p)

ε is relative precision (for example 0.1 = ±10% of p).

**F3 — One mean**

n = Z(1−α/2)² × σ² / d²

σ from a cited study; d in the variable's units.

**F4 — Two independent proportions (per group)**

n = [Z(1−α/2) × √(2p̄(1 − p̄)) + Z(1−β) × √(p1(1 − p1) + p2(1 − p2))]² / (p1 − p2)²

with p̄ = (p1 + p2)/2.

**F5 — Two independent means (per group)**

n = 2σ² × (Z(1−α/2) + Z(1−β))² / Δ²

Δ is the minimal clinically important difference; σ the common SD.

**F6 — Diagnostic accuracy (Buderer)**

n(sensitivity) = Z(1−α/2)² × Se(1 − Se) / (d² × Prev)
n(specificity) = Z(1−α/2)² × Sp(1 − Sp) / (d² × (1 − Prev))

Use the larger n. Prev is the expected prevalence of the target condition in the study sample.
In case–control diagnostic designs, compute cases and controls separately with F1 on Se and Sp.

**F7 — Correlation**

n = [(Z(1−α/2) + Z(1−β)) / C]² + 3, where C = 0.5 × ln[(1 + r)/(1 − r)]

## Adjustments

- Cluster or multistage sampling: multiply by the design effect (DEFF), stating its source;
  DEFF = 1 + (m − 1) × ICC.
- Expected non-response or loss to follow-up r: n_final = n / (1 − r).
- Finite population (N known, n/N > 5%): n_adj = n / (1 + (n − 1)/N).

## Test selection

| Comparison | Normal / large sample | Non-normal / small sample |
|---|---|---|
| Two independent proportions | Chi-squared | Fisher's exact (any expected cell < 5) |
| Paired proportions | McNemar | Exact McNemar |
| Two independent means | Independent t-test (Welch if variances differ) | Mann–Whitney U |
| Paired means | Paired t-test | Wilcoxon signed-rank |
| ≥3 independent groups | One-way ANOVA + post hoc | Kruskal–Wallis + Dunn |
| Association, continuous | Pearson | Spearman |
| Adjusted association, binary outcome | Multivariable logistic regression | — |
| Time-to-event | Kaplan–Meier, log-rank, Cox | — |

Check normality by plots and context, not by a significance test alone.

## Reporting template

Vietnamese proposal or thesis:

> Cỡ mẫu được tính theo công thức ước lượng một tỷ lệ: n = Z²(1−α/2) × p(1 − p)/d², với
> α = 0,05 (Z = 1,96), p = [giá trị] theo nghiên cứu của [tác giả, năm] [số TLTK], d = [giá trị].
> Tính được n = [kết quả]; dự phòng [r]% mất mẫu, cỡ mẫu tối thiểu là [n_final].

English manuscript:

> The sample size was calculated to estimate a proportion of [p] (based on [ref]) with an
> absolute precision of [d] at a 95% confidence level, giving [n] participants; allowing for
> [r]% non-response, we aimed to enrol [n_final].
