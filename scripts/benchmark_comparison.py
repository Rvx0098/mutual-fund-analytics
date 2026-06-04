import pandas as pd
import matplotlib.pyplot as plt

nav = pd.read_csv(
    "Bluestock-Capstone/data/raw/02_nav_history.csv"
)

benchmark = pd.read_csv(
    "Bluestock-Capstone/data/raw/10_benchmark_indices.csv"
)

fund_code = 120505

fund = nav[
    nav["amfi_code"] == fund_code
].copy()

fund["date"] = pd.to_datetime(
    fund["date"]
)

benchmark = benchmark[
    benchmark["index_name"] == "NIFTY50"
].copy()

benchmark["date"] = pd.to_datetime(
    benchmark["date"]
)

plt.figure(figsize=(12,6))

plt.plot(
    fund["date"],
    fund["nav"],
    label="Fund NAV"
)

plt.plot(
    benchmark["date"],
    benchmark["close_value"] /
    benchmark["close_value"].iloc[0]
    *
    fund["nav"].iloc[0],
    label="NIFTY50"
)

plt.legend()

plt.title(
    "Fund vs Benchmark"
)

plt.tight_layout()

plt.savefig(
    "Bluestock-Capstone/charts/benchmark_comparison.png"
)

plt.show()

print("benchmark_comparison.png created")