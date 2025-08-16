
# From Ward to Features — Memo (Template)

## Clinical context
Briefly describe the setting (e.g., general medicine ward, ICU, care home).

## Candidate covariates
- Polypharmacy (counts, high-risk classes)
- Observation frequency (vitals cadence, escalation triggers)
- Mobility & ADLs (fall risk proxies)
- Comorbidity burden (e.g., Elixhauser/Charlson-like features)
- Recent admissions / ED visits
- Labs, vitals summaries (min/max/trajectories)

## Bias & confounding risks
- Immortal-time bias (define time origin carefully)
- Confounding by indication (treatments given to sicker patients)
- Measurement bias (who gets measured and when)
- Missingness mechanisms and planned handling (MICE, indicators)

## Labels & horizons
Define event(s) and time horizons (30/90-day mortality or readmission) and justify choices.

## Operational notes
Feasibility, reproducibility plan (seeded splits, versioned code), and intended external validation (e.g., MIMIC/eICU).
