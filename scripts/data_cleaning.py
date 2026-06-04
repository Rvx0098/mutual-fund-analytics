import pandas as pd
import os

os.makedirs(
    "Bluestock-Capstone/data/processed",
    exist_ok=True
)

# =========================
# NAV HISTORY
# =========================

nav = pd.read_csv(
    "Bluestock-Capstone/data/raw/02_nav_history.csv"
)

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv(
    "Bluestock-Capstone/data/processed/02_nav_history_clean.csv",
    index=False
)

print("NAV cleaned")

# =========================
# INVESTOR TRANSACTIONS
# =========================

inv = pd.read_csv(
    "Bluestock-Capstone/data/raw/08_investor_transactions.csv"
)

inv["transaction_date"] = pd.to_datetime(
    inv["transaction_date"]
)

inv = inv[inv["amount_inr"] > 0]

inv = inv.drop_duplicates()

inv.to_csv(
    "Bluestock-Capstone/data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("Investor transactions cleaned")

# =========================
# SCHEME PERFORMANCE
# =========================

perf = pd.read_csv(
    "Bluestock-Capstone/data/raw/07_scheme_performance.csv"
)

perf = perf[
    (perf["expense_ratio_pct"] >= 0.1)
    &
    (perf["expense_ratio_pct"] <= 2.5)
]

perf.to_csv(
    "Bluestock-Capstone/data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("Performance data cleaned")

# =========================
# COPY REMAINING FILES
# =========================

files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:

    df = pd.read_csv(
        f"Bluestock-Capstone/data/raw/{file}"
    )

    df.to_csv(
        f"Bluestock-Capstone/data/processed/{file}",
        index=False
    )

print("All datasets processed")