import pandas as pd

# =========================
# LOAD DATASETS
# =========================

funds = pd.read_csv(
    "Bluestock-Capstone/data/raw/01_fund_master.csv"
)

sip = pd.read_csv(
    "Bluestock-Capstone/data/raw/04_monthly_sip_inflows.csv"
)

investors = pd.read_csv(
    "Bluestock-Capstone/data/raw/08_investor_transactions.csv"
)

portfolio = pd.read_csv(
    "Bluestock-Capstone/data/raw/09_portfolio_holdings.csv"
)

performance = pd.read_csv(
    "Bluestock-Capstone/data/raw/07_scheme_performance.csv"
)

print("=" * 60)
print("MUTUAL FUND KPI DASHBOARD")
print("=" * 60)

# =========================
# FUND KPIs
# =========================

total_funds = funds["amfi_code"].nunique()
total_fund_houses = funds["fund_house"].nunique()
avg_expense_ratio = round(
    funds["expense_ratio_pct"].mean(), 2
)
avg_aum = round(
    performance["aum_crore"].mean(), 2
)

print("\nFUND KPIs")
print("-" * 30)

print("Total Funds:", total_funds)
print("Total Fund Houses:", total_fund_houses)
print("Average Expense Ratio:", avg_expense_ratio)
print("Average AUM (Crore):", avg_aum)

# =========================
# INVESTOR KPIs
# =========================

total_investors = investors["investor_id"].nunique()
total_transactions = len(investors)
total_investment = round(
    investors["amount_inr"].sum(), 2
)
avg_transaction = round(
    investors["amount_inr"].mean(), 2
)

print("\nINVESTOR KPIs")
print("-" * 30)

print("Total Investors:", total_investors)
print("Total Transactions:", total_transactions)
print("Total Investment Amount:", total_investment)
print("Average Transaction Size:", avg_transaction)

# =========================
# SIP KPIs
# =========================

latest_sip = sip.iloc[-1]["sip_inflow_crore"]
max_sip = sip["sip_inflow_crore"].max()
avg_sip = round(
    sip["sip_inflow_crore"].mean(), 2
)

print("\nSIP KPIs")
print("-" * 30)

print("Latest SIP Inflow:", latest_sip)
print("Maximum SIP Inflow:", max_sip)
print("Average SIP Inflow:", avg_sip)

# =========================
# PORTFOLIO KPIs
# =========================

sector = (
    portfolio.groupby("sector")["weight_pct"]
    .sum()
    .sort_values(ascending=False)
)

top_sector = sector.index[0]
num_sectors = portfolio["sector"].nunique()
avg_weight = round(
    portfolio["weight_pct"].mean(), 2
)

print("\nPORTFOLIO KPIs")
print("-" * 30)

print("Top Sector:", top_sector)
print("Number of Sectors:", num_sectors)
print("Average Portfolio Weight:", avg_weight)

print("\n")
print("=" * 60)
print("KPI ANALYSIS COMPLETE")
print("=" * 60)