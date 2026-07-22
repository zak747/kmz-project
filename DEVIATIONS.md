# Deviations Log

This file records every place where our implementation makes a documented choice 
that departs from, or resolves an ambiguity in, Kelly, Malamud & Zhou (2024) 

---

## Notation

| Our code / brief | KMZ paper | Meaning |
|------------------|-----------|---------|
| `lambda`, $\lambda$ | $z$ | Ridge shrinkage penalty |
| $c$ | $c = P/T$ | Complexity ratio (same in both) |
| $T$ | $T$ | Rolling training window length |
| $P$ | $P$ | Number of random Fourier features |

The paper uses $z$ for the ridge penalty throughout; the brief and our code use 
$\lambda$. These refer to the same quantity.

---

## Design choices and resolved ambiguities

### D1 — Number of feature-draw seeds
- **Paper:** averages performance over 1,000 independent RFF draws (Section V.C).
- **Our choice:** we average over [N] seeds (brief requires ≥ 10), reporting the 
  seed-to-seed spread. 
- **Reason:** computational budget. To be revisited if results are unstable 
  across seeds.

### D2 — Position construction
- **Paper:** timing position $\pi_t = \hat{\beta}' S_t$, proportional to the 
  forecast with no constraints (equation 6).
- **Our choice:** identical — no capping, scaling or normalisation of positions, 
  even where leverage becomes large near $c = 1$. The large positions near the 
  interpolation boundary are part of the phenomenon being replicated.

### D3 — Source text limitation
- **Paper + Internet Appendix (IA):** the brief states the IA wins where the main 
  text is ambiguous.
- **Our status:** design notes were compiled from the main published text. The IA 
  has not yet been consulted. Any ambiguity in standardisation windows, exact 
  sample dates, or feature scaling resolved against the main text is flagged here 
  and should be reconciled against the IA before v1.0.

---

## Numerical discrepancies (to be filled during Steps 4–7)

_(Log here any figure or statistic that falls outside the brief's acceptance 
tolerances, with the diagnosis.)_

## Design decisions

These are deliberate implementation choices, distinct from the paper-ambiguity
deviations (D1–D3) below. Recorded per the brief's instruction to document
every non-obvious choice.

**DD1 — Time convention (Convention A).** Every series is stored at its natural
observation time: row t holds predictors observable at end of month t and the
market excess return realised during month t. The forecast lag (predict t+1 from
t) is applied by the experiment layer, not by data.py. Rationale: keeps data.py
a faithful record of what was known when, so the no-look-ahead test is a
statement about raw data, and the forecast horizon can change without editing
the data module.

**DD2 — Target definition.** The prediction target is the market excess return
(CRSP_SPvw − Rfree) scaled by its own trailing 12-month uncentered second moment
(root-mean-square of the trailing 12 excess returns, current month included).
The trailing window uses only months ≤ t, so scaling introduces no look-ahead.
The raw (unscaled) excess return is retained alongside the scaled target, since
strategy P&L is earned in raw returns while forecasts target the scaled series.
Scaling lives in data.py as a target-definition choice made consistently by KMZ.

## Design decisions

**DD1 — Time convention (Convention A).** Every series is stored at its natural
observation time: row t holds predictors observable at end of month t and the
market excess return realised during month t. The forecast lag (predict t+1
from t) is applied by the experiment layer, not by data.py. Rationale: keeps
data.py a faithful record of what was known when, so the no-look-ahead test is
a statement about raw data, and the forecast horizon can change without editing
the data module.

**DD2 — Target definition.** The prediction target is the market excess return
(CRSP_SPvw − Rfree) scaled by its own trailing 12-month uncentered second
moment (RMS of the trailing 12 excess returns, current month included). The
window uses only months ≤ t, so scaling introduces no look-ahead. The raw
excess return is retained alongside the scaled target: strategy P&L is earned
in raw returns while forecasts target the scaled series. Scaling lives in
data.py as a target-definition choice made consistently by KMZ.

## Deviations

**D4 — Inflation lag [RESOLVED against paper: no lag].** KMZ footnote 33 use the
Goyal-Welch-Zafirov (2023) inflation date convention, which treats month-t CPI
as part of the time-t information set — i.e. NOT lagged. Earlier we applied
.shift(1) out of caution; this is removed to match the paper. KMZ note results
are essentially unchanged whether inflation is included at all, so impact is
minimal. Reconcile against authors' code in Week 7.

**D5 — Predictor standardisation: rescale only [CONFIRMED against paper].**
KMZ Section V.A: predictors are standardized by an expanding-window historical
standard deviation, 36-month minimum, no demeaning ("volatility-standardize").
Verified against the paper directly; no longer a deviation, retained here as a
resolved design note. Persistent predictors (dp, dy, ep) consequently have
large standardised magnitudes (~10+); this is expected behaviour, absorbed
downstream by the RFF bandwidth γ.

**D6 — RFF training-window standardisation (features/experiment stage).**
KMZ footnote 39: RFFs are volatility-standardised by their *training-sample*
standard deviations before each estimation, separately from the predictor
standardisation in data.py. Not implemented in Step 1; belongs to features.py /
the rolling experiment. Logged here so it is not missed.