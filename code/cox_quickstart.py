
from lifelines.datasets import load_rossi
from lifelines import CoxPHFitter, KaplanMeierFitter
from lifelines.utils import concordance_index
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs("figures", exist_ok=True)

# 1) Load a survival dataset (practice, instantly available)
df = load_rossi()                  # time column: 'week', event: 'arrest' (1=event)
T, E = "week", "arrest"
df["age_bin"] = pd.cut(df["age"], bins=[10,25,35,45,55,65,90],
                       labels=False, include_lowest=True)

# 2) Fit Cox PH with a simple formula
cph = CoxPHFitter()
cph.fit(
    df,
    duration_col=T,
    event_col=E,
    # treat age_bin as categorical; keep other covariates
    formula="fin + race + mar + paro + prio + C(age_bin)",
    strata=["wexp"],   # stratify on wexp to handle its PH issue
)
print("\n=== COX PH SUMMARY ===")
print(cph.summary)                 # coefficients + CIs

# 3) PH assumption checks (Schoenfeld-style tests + diagnostic plots)
print("\n=== PROPORTIONAL HAZARDS CHECKS ===")
# This will print a table and, in interactive sessions, draw diagnostic plots.
# Not all environments render plots; the textual test results are what you need in a pinch.
cph.check_assumptions(df, p_value_threshold=0.05, show_plots=False)

# 4) Harrell's C-index (higher is better; ~0.5 = chance)
# Use negative partial hazard so higher value indicates higher predicted risk
risk = -cph.predict_partial_hazard(df).values.ravel()
cidx = concordance_index(df[T], risk, df[E])
print(f"\nHarrell's C-index: {cidx:.3f}")

# 5) Simple calibration at a fixed horizon (e.g., 52 weeks)
time_horizon = 52
# Predict survival S(t) per individual; convert to risk = 1 - S(t)
X = df.drop(columns=[T, E])
surv_at_t = cph.predict_survival_function(X, times=[time_horizon]).iloc[0].values
pred_risk = 1 - surv_at_t
cal = pd.DataFrame({ "pred_risk": pred_risk, T: df[T], E: df[E] })
cal["bin"] = pd.qcut(cal["pred_risk"], 10, labels=False, duplicates="drop")

# Observed event rate by horizon using Kaplan–Meier
kmf = KaplanMeierFitter()
obs, exp = [], []
for b in sorted(cal["bin"].unique()):
    g = cal[cal["bin"] == b]
    kmf.fit(durations=g[T], event_observed=g[E])
    S_t = float(kmf.survival_function_at_times(time_horizon).values[0])
    obs.append(1 - S_t)                  # observed risk
    exp.append(float(g["pred_risk"].mean()))  # mean predicted risk

plt.figure()
plt.plot(exp, obs, marker="o")
plt.plot([0, 1], [0, 1], "--", linewidth=1)
plt.xlabel(f"Mean predicted risk by {time_horizon} weeks")
plt.ylabel(f"Observed event rate by {time_horizon} weeks (KM)")
plt.title("Calibration plot (deciles) — Cox PH")
plt.tight_layout()
plt.savefig("figures/calibration_52w.png", dpi=200)
print("Saved calibration plot → figures/calibration_52w.png")

print("\nDone. Next: swap in your hospital dataset, keep the same structure, and adjust the time horizon to 30/90 days as needed.")
cph.summary.to_csv("reports/cox_summary.csv")