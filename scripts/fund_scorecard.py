import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# -----------------------------------
# LOAD FILES
# -----------------------------------

metrics = pd.read_csv(
    "Bluestock-Capstone/data/processed/performance_metrics.csv"
)

alpha_beta = pd.read_csv(
    "Bluestock-Capstone/data/processed/alpha_beta.csv"
)

funds = pd.read_csv(
    "Bluestock-Capstone/data/raw/01_fund_master.csv"
)

# -----------------------------------
# MERGE
# -----------------------------------

df = metrics.merge(
    alpha_beta,
    on="amfi_code"
)

df = df.merge(
    funds[
        [
            "amfi_code",
            "scheme_name",
            "expense_ratio_pct"
        ]
    ],
    on="amfi_code"
)

# -----------------------------------
# NORMALIZATION
# -----------------------------------

scaler = MinMaxScaler()

df["cagr_score"] = scaler.fit_transform(
    df[["cagr_pct"]]
)

df["sharpe_score"] = scaler.fit_transform(
    df[["sharpe_ratio"]]
)

df["alpha_score"] = scaler.fit_transform(
    df[["alpha"]]
)

# lower expense ratio is better

df["expense_score"] = 1 - scaler.fit_transform(
    df[["expense_ratio_pct"]]
)

# smaller drawdown is better

df["drawdown_score"] = 1 - scaler.fit_transform(
    df[["max_drawdown_pct"]]
)

# -----------------------------------
# FINAL SCORE
# -----------------------------------

df["fund_score"] = (

    df["cagr_score"] * 30 +

    df["sharpe_score"] * 25 +

    df["alpha_score"] * 20 +

    df["expense_score"] * 15 +

    df["drawdown_score"] * 10

)

df["fund_score"] = (
    df["fund_score"]
    .round(2)
)

# -----------------------------------
# SAVE
# -----------------------------------

output = df[
    [
        "amfi_code",
        "scheme_name",
        "fund_score"
    ]
].sort_values(
    "fund_score",
    ascending=False
)

output.to_csv(
    "Bluestock-Capstone/data/processed/fund_scorecard.csv",
    index=False
)

print("\nTOP 10 FUNDS")

print(output.head(10))

print("\nFund Scorecard Created")