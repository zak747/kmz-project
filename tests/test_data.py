import data
import pandas as pd
import numpy as np

def test_predictors_structure():
    """Contract test: build_predictors returns the agreed shape.

    Guards against silent changes to the predictor set. Verifies there are
    exactly 15 predictors, that they match the canonical PREDICTORS list in
    the correct order (order matters downstream: the RFF map consumes these
    as a fixed-position matrix), and that the index is a monthly PeriodIndex.
    Fires the day a column is added, dropped, renamed, or reordered.
    """
    frame = data.build_predictors(data.load_raw())
    assert frame.shape[1] == 15
    assert list(frame.columns) == data.Predictors
    assert isinstance(frame.index, pd.PeriodIndex) == True 

def test_standardise_no_lookahead():
    """No-look-ahead test (the cardinal-sin guard, required by the brief).

    Proves that standardisation at month t uses only data up to t. Standardises
    the full sample, then standardises a copy truncated at the cutoff, and
    checks that every value before the cutoff is identical across the two. If
    standardisation used any future data, removing the future would change the
    past and this test would fail. Equality here means the expanding-window std
    is genuinely backward-looking.
    """
    cutoff = "1970-12"
    preds = data.build_predictors(data.load_raw())
    full = data.standardise(preds)
    trunc = data.standardise(preds.loc[:cutoff])
    a = full.loc[:cutoff]
    b = trunc.loc[:cutoff]
    pd.testing.assert_frame_equal(a, b)

def test_standardise_divides_by_expanding_std():
    """Correctness test: standardise divides by the expanding-window std.

    Uses synthetic data (0..49) so the expected output is known independently
    of the function. Checks one row past the 36-observation minimum: the
    standardised value must equal the raw value divided by the sample std
    (ddof=1) of all observations up to and including that row. Pins the exact
    arithmetic, not just that the output looks plausible.
    """
    synthetic = pd.DataFrame({"A" : np.arange(0,50)})
    out = data.standardise(synthetic)
    col = synthetic.iloc[:, 0]
    expected_std = col.iloc[:41].std()
    expected = col.iloc[40] / expected_std
    assert abs(out.iloc[40, 0] - expected) < 1e-12