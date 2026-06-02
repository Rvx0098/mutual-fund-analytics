import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:rvdata@localhost:5432/bluestock_mf"
)

files = {
    "02_nav_history.csv": "nav_history",
    "03_aum_by_fund_house.csv": "aum_by_fund_house",
    "04_monthly_sip_inflows.csv": "monthly_sip_inflows",
    "05_category_inflows.csv": "category_inflows",
    "06_industry_folio_count.csv": "industry_folio_count",
    "07_scheme_performance.csv": "scheme_performance",
    "08_investor_transactions.csv": "investor_transactions",
    "09_portfolio_holdings.csv": "portfolio_holdings",
    "10_benchmark_indices.csv": "benchmark_indices"
}

base_path = "Bluestock-Capstone/data/raw"

for file, table in files.items():

    path = f"{base_path}/{file}"

    print(f"\nLoading {file} -> {table}")

    df = pd.read_csv(path)

    if table == "nav_history":
        df.rename(columns={"date": "nav_date"}, inplace=True)

    if table == "aum_by_fund_house":
        df.rename(columns={"date": "report_date"}, inplace=True)

    if table == "benchmark_indices":
        df.rename(columns={"date": "index_date"}, inplace=True)

    print(f"Rows: {len(df)}")

    df.to_sql(
        table,
        engine,
        if_exists="append",
        index=False
    )

    print("Done")

print("\nALL DATASETS LOADED SUCCESSFULLY")