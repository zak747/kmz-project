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