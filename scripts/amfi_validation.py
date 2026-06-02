import pandas as pd

fund_master = pd.read_csv(
    "Bluestock-Capstone/data/raw/01_fund_master.csv"
)

nav_history = pd.read_csv(
    "Bluestock-Capstone/data/raw/02_nav_history.csv"
)

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print("Fund Master Codes:", len(fund_codes))
print("NAV Codes:", len(nav_codes))

print("\nMissing AMFI Codes:")
print(missing_codes)

if len(missing_codes) == 0:
    print("\nVALIDATION PASSED")
else:
    print("\nVALIDATION FAILED")