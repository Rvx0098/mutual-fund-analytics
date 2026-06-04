import pandas as pd
import numpy as np

print("=" * 60)
print("PERFORMANCE ANALYTICS")
print("=" * 60)

# --------------------------------------------------
# LOAD NAV DATA
# --------------------------------------------------

nav = pd.read_csv(
    "Bluestock-Capstone/data/raw/02_nav_history.csv"
)

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

# --------------------------------------------------
# DAILY RETURNS
# --------------------------------------------------

nav["daily_return"] = (
    nav.groupby("amfi_code")["nav"]
    .pct_change()
)

print("\nDaily Returns Calculated")

# --------------------------------------------------
# CAGR CALCULATION
# --------------------------------------------------

results = []

for code in nav["amfi_code"].unique():

    temp = nav[
        nav["amfi_code"] == code
    ].copy()

    start_nav = temp["nav"].iloc[0]
    end_nav = temp["nav"].iloc[-1]

    years = (
        (temp["date"].max() - temp["date"].min()).days
        / 365
    )

    cagr = (
        (end_nav / start_nav)
        ** (1 / years)
        - 1
    ) * 100

    results.append(
        [code, cagr]
    )

cagr_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "cagr_pct"
    ]
)

print("CAGR Calculated")

# --------------------------------------------------
# SHARPE RATIO
# --------------------------------------------------

rf = 0.065

sharpe_results = []

for code in nav["amfi_code"].unique():

    temp = nav[
        nav["amfi_code"] == code
    ]

    mean_return = (
        temp["daily_return"].mean()
        * 252
    )

    volatility = (
        temp["daily_return"].std()
        * np.sqrt(252)
    )

    sharpe = (
        (mean_return - rf)
        / volatility
    )

    sharpe_results.append(
        [code, sharpe]
    )

sharpe_df = pd.DataFrame(
    sharpe_results,
    columns=[
        "amfi_code",
        "sharpe_ratio"
    ]
)

print("Sharpe Ratio Calculated")

# --------------------------------------------------
# SORTINO RATIO
# --------------------------------------------------

sortino_results = []

for code in nav["amfi_code"].unique():

    temp = nav[
        nav["amfi_code"] == code
    ]

    mean_return = (
        temp["daily_return"].mean()
        * 252
    )

    downside = temp[
        temp["daily_return"] < 0
    ]["daily_return"]

    downside_std = (
        downside.std()
        * np.sqrt(252)
    )

    sortino = (
        (mean_return - rf)
        / downside_std
    )

    sortino_results.append(
        [code, sortino]
    )

sortino_df = pd.DataFrame(
    sortino_results,
    columns=[
        "amfi_code",
        "sortino_ratio"
    ]
)

print("Sortino Ratio Calculated")

# --------------------------------------------------
# MAXIMUM DRAWDOWN
# --------------------------------------------------

drawdown_results = []

for code in nav["amfi_code"].unique():

    temp = nav[
        nav["amfi_code"] == code
    ].copy()

    temp["running_max"] = (
        temp["nav"]
        .cummax()
    )

    temp["drawdown"] = (
        temp["nav"]
        - temp["running_max"]
    ) / temp["running_max"]

    max_dd = (
        temp["drawdown"]
        .min()
        * 100
    )

    drawdown_results.append(
        [code, max_dd]
    )

drawdown_df = pd.DataFrame(
    drawdown_results,
    columns=[
        "amfi_code",
        "max_drawdown_pct"
    ]
)

print("Maximum Drawdown Calculated")

# --------------------------------------------------
# SAVE OUTPUT
# --------------------------------------------------

output = (
    cagr_df
    .merge(sharpe_df, on="amfi_code")
    .merge(sortino_df, on="amfi_code")
    .merge(drawdown_df, on="amfi_code")
)

output.to_csv(
    "Bluestock-Capstone/data/processed/performance_metrics.csv",
    index=False
)

print("\nSaved Updated Metrics")