import pandas as pd
from scipy.stats import linregress

# ------------------------------------
# LOAD DATA
# ------------------------------------

nav = pd.read_csv(
    "Bluestock-Capstone/data/raw/02_nav_history.csv"
)

benchmark = pd.read_csv(
    "Bluestock-Capstone/data/raw/10_benchmark_indices.csv"
)

nav["date"] = pd.to_datetime(nav["date"])
benchmark["date"] = pd.to_datetime(benchmark["date"])

# Use NIFTY50 only

benchmark = benchmark[
    benchmark["index_name"] == "NIFTY50"
]

benchmark = benchmark.sort_values("date")

benchmark["benchmark_return"] = (
    benchmark["close_value"]
    .pct_change()
)

results = []

# ------------------------------------
# ALPHA BETA
# ------------------------------------

for code in nav["amfi_code"].unique():

    temp = nav[
        nav["amfi_code"] == code
    ].copy()

    temp = temp.sort_values("date")

    temp["fund_return"] = (
        temp["nav"]
        .pct_change()
    )

    merged = pd.merge(
        temp,
        benchmark[
            ["date", "benchmark_return"]
        ],
        on="date",
        how="inner"
    )

    merged = merged.dropna()

    if len(merged) > 50:

        slope, intercept, r, p, stderr = linregress(
            merged["benchmark_return"],
            merged["fund_return"]
        )

        beta = slope

        alpha = intercept * 252 * 100

        results.append(
            [code, alpha, beta]
        )

alpha_beta = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "alpha",
        "beta"
    ]
)

alpha_beta.to_csv(
    "Bluestock-Capstone/data/processed/alpha_beta.csv",
    index=False
)

print(alpha_beta.head())

print("\nAlpha Beta Analysis Complete")