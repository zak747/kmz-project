# KMZ Replication

Replication of Kelly, Malamud and Zhou (2024), "The Virtue of Complexity in
Return Prediction", *Journal of Finance* 79(1), 459–506.

Part 1 of a UROP project at Imperial College Business School (12 weeks from
29 June 2026). Weeks 1–7 replicate KMZ's main empirical results from public
data. Weeks 8–12 use this code as the benchmark arm of a comparison against
theory-informed spectral feature maps on CRSP data.

## Data provenance

Goyal–Welch monthly predictor dataset, from Amit Goyal's website
(sites.google.com/view/agoyal145), linked under Goyal & Welch (2008).

- File: `raw/PredictorData2025.xlsx`
- Vintage: updated through 2025
- Downloaded: 17/07/2025
- Note: from 2022, `lty` sourced from FRED and `ltr`/`corpr` from Bloomberg
  indices. Post-dates the 1926–2020 replication sample, so cannot affect
  these results.

## Setup

    python3 -m pip install -r requirements.txt

## Structure

    data.py       Data module: loading, transformation, standardisation
    tests/        Unit tests (pytest)
    raw/          Raw downloaded data
    figures/      Generated figures

## Status

Step 1 (data module) in progress.

Replication of Kelly, Malamud and Zhou (2024), "The Virtue of Complexity in
Return Prediction", *Journal of Finance* 79(1), 459–506.

Part 1 of a UROP project at Imperial College Business School (12 weeks from
29 June 2026). Weeks 1–7 replicate KMZ's main empirical results from public
data. Weeks 8–12 use this code as the benchmark arm of a comparison against
theory-informed spectral feature maps on CRSP data.

## Data provenance

Goyal–Welch monthly predictor dataset, from Amit Goyal's website
(sites.google.com/view/agoyal145), linked under Goyal & Welch (2008).

- File: `raw/PredictorData2025.xlsx`
- Vintage: updated through 2025
- Downloaded: [DATE]
- Note: from 2022, `lty` sourced from FRED and `ltr`/`corpr` from Bloomberg
  indices. Post-dates the 1926–2020 replication sample, so cannot affect
  these results.

## Setup

    python3 -m pip install -r requirements.txt

## Structure

    data.py       Data module: loading, transformation, standardisation
    tests/        Unit tests (pytest)
    raw/          Raw downloaded data
    figures/      Generated figures

## Status

Step 1 (data module) in progress.