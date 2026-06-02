from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:rvdata@localhost:5432/bluestock_mf"
)

with engine.connect() as conn:
    print("Connection Successful!")