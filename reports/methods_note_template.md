
# Methods Note (Template) — Survival Analysis for Hospital Outcomes

## Abstract
2–3 sentences on the question (e.g., 30-/90-day mortality or readmission), dataset, and main performance numbers (C-index, Brier, calibration).

## Data
- Cohort definition, inclusion/exclusion.
- Time origin, event definition, censoring rules.
- Covariates (clinical rationale), missing-data handling.

## Methods
- Cox proportional hazards (partial likelihood); checks for PH (Schoenfeld tests).
- Regularised Cox (L1/L2/elastic-net) if used; tree-based survival model if added.
- Any time-varying effects or competing-risks (Fine–Gray) if applicable.

## Evaluation
- Discrimination: Harrell’s C-index; time-dependent AUC.
- Calibration: calibration curves at clinically relevant horizons; Brier score.
- Uncertainty: bootstrap (e.g., 200 resamples) for optimism correction.

## Diagnostics & Sensitivity
- PH diagnostics and any fixes (interactions, stratification, time-varying terms).
- Influence diagnostics; alternative missing-data strategies.
- (If causal mini-study is added) DAG, IPTW/matching, balance diagnostics.

## Limitations
- Data provenance, measurement error, residual confounding, generalisability.

## Model. Cox proportional hazards with covariates: fin, race, mar, paro, prio, and age (binned).
- Assumptions. PH diagnostics flagged age-related terms in the baseline run; given this is a practice dataset, we       -proceeded with simple binning (and kept wexp as a stratum/handled separately if needed).
## Discrimination. Harrell’s C-index = 0.623 on the training data.
-Calibration. Decile-based calibration at 52 weeks showed broadly acceptable alignment (see figures/calibration_52w.png).
-Next. Replicate on hospital data with clinically relevant horizons (e.g., 30/90 days) and add bootstrap optimism - correction.
