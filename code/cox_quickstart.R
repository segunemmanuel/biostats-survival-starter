
# Quick Cox PH in R with PH checks and calibration
suppressPackageStartupMessages({
  library(survival)
  library(survminer)
  library(Hmisc)
  library(rms)
})

# Built-in clinical dataset
data(lung)                           # time (days), status (1=censored, 2=death)
lung <- na.omit(lung)
lung$event <- as.integer(lung$status == 2)

# Cox PH
fit <- coxph(Surv(time, event) ~ age + sex + ph.ecog + ph.karno, data = lung)
cat("\n=== COX PH SUMMARY ===\n")
print(summary(fit))

# PH assumption (Schoenfeld tests + plots)
cat("\n=== PROPORTIONAL HAZARDS CHECKS ===\n")
ph <- cox.zph(fit)
print(ph)
# ggcoxzph(ph)  # uncomment to draw diagnostic plots

# Harrell's C-index
cat("\n=== DISCRIMINATION (Harrell's C) ===\n")
c_idx <- rcorr.cens(predict(fit), Surv(lung$time, lung$event))["C Index"]
print(c_idx)

# Calibration at 365 days with rms::cph + calibrate()
dd <- datadist(lung); options(datadist = "dd")
fit_rms <- cph(Surv(time, event) ~ age + sex + ph.ecog + ph.karno,
               data=lung, x=TRUE, y=TRUE, surv=TRUE)
set.seed(42)
cal <- calibrate(fit_rms, method="boot", u=365, m=80, B=200)  # u=horizon
plot(cal, xlab="Predicted survival at 365 days", ylab="Observed survival (bootstrap)",
     main="Calibration — Cox PH (lung)")
cat("\nSaved calibration plot to the active graphics device. Use dev.copy(png, 'figures/calibration_365d.png'); dev.off() to save.\n")
