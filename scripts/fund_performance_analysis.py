import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("Bluestock-Capstone/charts", exist_ok=True)

df = pd.read_csv(
    "Bluestock-Capstone/data/raw/07_scheme_performance.csv"
)

# ==========================
# TOP 10 FUNDS BY 5Y RETURN
# ==========================

top_returns = (
    df.sort_values(
        "return_5yr_pct",
        ascending=False
    )
    .head(10)
)

plt.figure(figsize=(10,6))

plt.barh(
    top_returns["scheme_name"],
    top_returns["return_5yr_pct"]
)

plt.title("Top 10 Funds by 5-Year Return")
plt.xlabel("5-Year Return (%)")

plt.tight_layout()

plt.savefig(
    "Bluestock-Capstone/charts/top_returns.png"
)

plt.close()

print("top_returns.png created")

# ==========================
# TOP ALPHA FUNDS
# ==========================

top_alpha = (
    df.sort_values(
        "alpha",
        ascending=False
    )
    .head(10)
)

plt.figure(figsize=(10,6))

plt.barh(
    top_alpha["scheme_name"],
    top_alpha["alpha"]
)

plt.title("Top 10 Funds by Alpha")
plt.xlabel("Alpha")

plt.tight_layout()

plt.savefig(
    "Bluestock-Capstone/charts/alpha_analysis.png"
)

plt.close()

print("alpha_analysis.png created")

# ==========================
# TOP SHARPE RATIO FUNDS
# ==========================

top_sharpe = (
    df.sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(10)
)

plt.figure(figsize=(10,6))

plt.barh(
    top_sharpe["scheme_name"],
    top_sharpe["sharpe_ratio"]
)

plt.title("Top 10 Funds by Sharpe Ratio")
plt.xlabel("Sharpe Ratio")

plt.tight_layout()

plt.savefig(
    "Bluestock-Capstone/charts/sharpe_analysis.png"
)

plt.close()

print("sharpe_analysis.png created")