# COGS108 Final Project

## Overview
- **Goal:** Test how well the UCSD student “10% rule” predicts the chance of moving from the waitlist into COGS classes (FA22–SP24).
- **Question:** Is ~10% of total seats a reliable estimate of the number of students who will enroll from the waitlist, and how does this vary by course and quarter?
- **Scope:** Six quarters of Cognitive Science courses (undergraduate only), excluding cancelled classes, graduate sections, and independent studies.

## Repository Contents
- `FinalProject_Group027-FA24.ipynb` – final report notebook with narrative, analysis, figures, and discussion.
- `csv_data_cleaning.ipynb` – cleaning pipeline from the raw UCSD Historical Enrollment Data to the per-quarter cleaned CSVs.
- `csv_exploratory_analysis.ipynb` / `csv_exploratory_analysis.py` – exploratory analysis and utility functions used during development.
- `Cleaned_data/` – cleaned per-quarter snapshots (`fa22_simple.csv`, `wi23_simple.csv`, …) used in the final analysis.
- `time_series.csv` – full time-series scrape (~1M rows) with enrollment, waitlist, and seat-change history.
- `winter_summary.csv` – summary table used for intermediate validation.


## Data Sources
- Original raw data: UCSD Historical Enrollment Data repository (WebReg scrape).
- Cleaned dataset variables (common across per-quarter CSVs):
  - `sec_id`, `sec_code`, `prof`, `course_id`
  - `total` (max seats), `ten_percent` (0.1 × total)
  - `from_waitlist`/`off_waitlist` (students moved from waitlist)
  - `size_change` (seat count changes during the term)
- Time-series file adds timestamps, availability, waitlist counts, and enrollment counts across scrapes.

## Methods
- Filtered to COGS courses; removed seminars/independent study (99, 190+), graduate sections, and cancelled classes.
- Computed `ten_percent` threshold per class; compared to actual waitlist movement (`from_waitlist`/`off_waitlist`).
- Statistical tests on nonparametric data:
  - Spearman correlation between class size and waitlist enrollments (p << 0.05, positive correlation).
  - Wilcoxon signed-rank test comparing the 10% threshold vs. observed waitlist enrollments (failed to reject null at α = 0.05).
- Examined seat-count changes by quarter; ~24% of sections changed capacity at least once (mostly single adjustments).

## Key Findings
- Across six quarters, 49.2% of COGS classes met or exceeded the 10% rule threshold.
- Larger classes tended to pull more students from the waitlist (positive but weak relationship).
- No statistically significant difference between the 10% rule expectation and observed waitlist enrollments under Wilcoxon test → retain null hypothesis.
- Capacity changes are common enough to matter, but extreme multi-change cases are rare; classes with arbitrary size changes were excluded from the main analysis.

## Limitations and Notes
- Analysis covers only COGS undergraduate offerings from FA22–SP24; results may not generalize to other departments or time spans.
- Independence and normality assumptions are violated in some models; linear fits were used descriptively.
- Seat-count changes and special-topic courses can distort the 10% heuristic; these were filtered when possible, but edge cases remain.

## Contributors
Kris Chen, Beijie Cheng, Miles Davis, Alex Woods, Andrea Ruiz D'Argence
