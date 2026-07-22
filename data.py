import pandas as pd
import numpy as np

raw_path = "raw/PredictorData2025.xlsx"
Predictors = ["dp", "dy", "ep", "de", "tms", "dfy", "dfr", "ltr",
              "tbl", "lty", "ntis", "infl", "svar", "bm", "mkt_lag"]

def load_raw(path = raw_path):
    data = pd.read_excel(path, sheet_name = "Monthly")
    data = data.rename(columns = {"b/m" : "bm"})
    data.index = pd.PeriodIndex(data["yyyymm"].astype(str), freq = "M")
    data.index.name = "Date"
    data = data.drop(columns = ["csp", "yyyymm"])
    
    return data


def build_excess_return(data):  
    excess_return = data["CRSP_SPvw"] - data["Rfree"]
    sigma = ((excess_return ** 2).rolling(12).mean() ** 0.5)
    standardised_target = (excess_return / sigma)
    data2 = pd.DataFrame({"Excess Returns" : excess_return, "Standardised Target" : standardised_target})

    return data2


def build_predictors(data):
    dp = np.log(data["D12"]) - np.log(data["Index"])
    dy = np.log(data["D12"]) - np.log(data["Index"].shift(1))
    ep = np.log(data["E12"]) - np.log(data["Index"])
    de = np.log(data["D12"]) - np.log(data["E12"])
    tms = data["lty"] - data["tbl"]
    dfy = data["BAA"] - data["AAA"]
    dfr = data["corpr"] - data["ltr"]
    mkt_lag = (data["CRSP_SPvw"] - data["Rfree"]).shift(1)
    Series = [dp, dy, ep, de, tms, dfy, dfr, data["ltr"], data["tbl"], data["lty"], data["ntis"], 
              data["infl"], data["svar"], data["bm"], mkt_lag]
    data3 = pd.DataFrame(dict(zip(Predictors, Series)))
    
    return data3[Predictors]

def standardise(data, min_periods = 36):
    expanding_std = data.expanding(min_periods = min_periods).std()
    data4 = data / expanding_std
    return data4 


if __name__ == "__main__":
    raw = load_raw()
    preds = standardise(build_predictors(raw))
    print(preds.shape)

