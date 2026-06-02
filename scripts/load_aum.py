import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:rvdata@localhost:5432/bluestock_mf"
)

df = pd.read_csv(
    "Bluestock-Capstone/data/raw/03_aum_by_fund_house.csv"
)

df.rename(
    columns={"date": "report_date"},
    inplace=True
)

df.to_sql(
    "aum_by_fund_house",
    engine,
    if_exists="append",
    index=False
)

print("AUM table loaded successfully!")