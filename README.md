
# Biostats Survival — Hospital Outcomes (Starter)

This is a minimal starter repo to get you **from zero to a working Cox model** with PH checks, C-index, and a calibration plot. It includes **Python** and **R** quickstarts using built-in practice datasets so you can prove the pipeline today, then swap in real hospital data (e.g., MIMIC) later.

## Quickstart — Python (lifelines)
```bash
# 1) Create and activate a virtual environment
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 2) Install deps
pip install -r requirements.txt

# 3) Run the quickstart
python code/cox_quickstart.py
# Output: coefficients and PH checks in console, C-index, and a calibration plot at figures/calibration_52w.png
```

## Quickstart — R (survival + rms)
```r
install.packages(c("survival","survminer","Hmisc","rms"))
source("code/cox_quickstart.R")
# Output: model summary, PH tests/plots, C-index, and a bootstrap-corrected calibration curve
```

## Files
- `code/cox_quickstart.py` — Python Cox model with PH checks and a decile calibration plot at a fixed horizon.
- `code/cox_quickstart.R` — R Cox model with Schoenfeld tests and `rms::calibrate` at one year.
- `reports/methods_note_template.md` — 2–3 page structure you can fill as you run the analysis.
- `reports/ward_to_features_memo_template.md` — prompts to translate clinical workflow into covariates and biases.
- `requirements.txt` — minimal Python dependencies.
- `figures/` — calibration plots saved here.
- `data/` — (empty; gitignored) put real datasets here when you’re ready.

## Next steps
- Replace the practice dataset with your hospital dataset when ready.
- Add a tree-based survival model (e.g., scikit-survival) and competing-risks if relevant.
- Push the repo to GitHub (private until applications are submitted).
