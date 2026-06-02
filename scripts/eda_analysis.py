import pandas as pd
import matplotlib.pyplot as plt
import os

# Create charts folder if it doesn't exist
os.makedirs("Bluestock-Capstone/charts", exist_ok=True)

# Load dataset
df = pd.read_csv(
    "Bluestock-Capstone/data/raw/07_scheme_performance.csv"
)

# Top 10 funds by AUM
top_funds = (
    df.sort_values("aum_crore", ascending=False)
      .head(10)
)

plt.figure(figsize=(12, 6))

plt.barh(
    top_funds["scheme_name"],
    top_funds["aum_crore"]
)

plt.xticks(rotation=90)

plt.title("Top 10 Mutual Funds by AUM")
plt.xlabel("Scheme Name")
plt.ylabel("AUM (Crore)")

plt.tight_layout()

plt.savefig(
    "Bluestock-Capstone/charts/top_funds_by_aum.png"
)

plt.close()

print("Chart saved: top_funds_by_aum.png")

# SIP Growth Trend

sip = pd.read_csv(
    "Bluestock-Capstone/data/raw/04_monthly_sip_inflows.csv"
)

plt.figure(figsize=(12,6))

plt.plot(
    sip["month"],
    sip["sip_inflow_crore"],
    marker="o"
)

plt.xticks(rotation=90)

plt.title("Monthly SIP Inflows")
plt.xlabel("Month")
plt.ylabel("SIP Inflow (Crore)")

plt.tight_layout()

plt.savefig(
    "Bluestock-Capstone/charts/sip_growth_trend.png"
)

plt.close()

print("Chart saved: sip_growth_trend.png")

# Investor Age Distribution

investors = pd.read_csv(
    "Bluestock-Capstone/data/raw/08_investor_transactions.csv"
)

age_counts = investors["age_group"].value_counts()

plt.figure(figsize=(8,5))

age_counts.plot(kind="bar")

plt.title("Investor Age Distribution")
plt.xlabel("Age Group")
plt.ylabel("Number of Transactions")

plt.tight_layout()

plt.savefig(
    "Bluestock-Capstone/charts/investor_age_distribution.png"
)

plt.close()

print("Chart saved: investor_age_distribution.png")

# Gender Distribution

gender_counts = investors["gender"].value_counts()

plt.figure(figsize=(6,4))

gender_counts.plot(kind="bar")

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Transactions")

plt.tight_layout()

plt.savefig(
    "Bluestock-Capstone/charts/gender_distribution.png"
)

plt.close()

print("Chart saved: gender_distribution.png")

# City Tier Distribution

city_tier_counts = investors["city_tier"].value_counts()

plt.figure(figsize=(6,4))

city_tier_counts.plot(kind="bar")

plt.title("City Tier Distribution")
plt.xlabel("City Tier")
plt.ylabel("Number of Transactions")

plt.tight_layout()

plt.savefig(
    "Bluestock-Capstone/charts/city_tier_distribution.png"
)

plt.close()

print("Chart saved: city_tier_distribution.png")

# Payment Mode Distribution

payment_counts = investors["payment_mode"].value_counts()

plt.figure(figsize=(8,5))

payment_counts.plot(kind="bar")

plt.title("Payment Mode Distribution")
plt.xlabel("Payment Mode")
plt.ylabel("Number of Transactions")

plt.tight_layout()

plt.savefig(
    "Bluestock-Capstone/charts/payment_mode_distribution.png"
)

plt.close()

print("Chart saved: payment_mode_distribution.png")

# State-wise Investment Analysis

state_counts = (
    investors.groupby("state")["amount_inr"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))

state_counts.plot(kind="bar")

plt.title("Top 10 States by Investment Amount")
plt.xlabel("State")
plt.ylabel("Total Investment Amount (INR)")

plt.tight_layout()

plt.savefig(
    "Bluestock-Capstone/charts/statewise_investments.png"
)

plt.close()

print("Chart saved: statewise_investments.png")

# Portfolio Sector Exposure

portfolio = pd.read_csv(
    "Bluestock-Capstone/data/raw/09_portfolio_holdings.csv"
)

sector_weights = (
    portfolio.groupby("sector")["weight_pct"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,6))

sector_weights.plot(kind="bar")

plt.title("Portfolio Sector Exposure")
plt.xlabel("Sector")
plt.ylabel("Total Weight (%)")

plt.tight_layout()

plt.savefig(
    "Bluestock-Capstone/charts/sector_exposure.png"
)

plt.close()

print("Chart saved: sector_exposure.png")