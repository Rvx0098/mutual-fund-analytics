import pandas as pd

df = pd.read_csv(
    "Bluestock-Capstone/data/raw/01_fund_master.csv"
)

print("\nUNIQUE FUND HOUSES")
print(df["fund_house"].unique())

print("\nUNIQUE CATEGORIES")
print(df["category"].unique())

print("\nUNIQUE SUB-CATEGORIES")
print(df["sub_category"].unique())

print("\nRISK CATEGORIES")
print(df["risk_category"].value_counts())

