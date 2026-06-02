import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:rvdata@localhost:5432/bluestock_mf"
)

df = pd.read_csv(
    "Bluestock-Capstone/data/raw/01_fund_master.csv"
)

print("Rows Found:", len(df))

df.to_sql(
    "fund_master",
    engine,
    if_exists="append",
    index=False
)

print("fund_master loaded successfully!")