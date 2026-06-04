import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "Bluestock-Capstone/data/raw/03_aum_by_fund_house.csv"
)

df["date"] = pd.to_datetime(df["date"])

pivot = df.pivot(
    index="fund_house",
    columns="date",
    values="aum_crore"
)

pivot.plot(
    kind="bar",
    figsize=(14,7)
)

plt.title("AUM Growth by Fund House")
plt.ylabel("AUM (Crore)")
plt.tight_layout()

plt.savefig(
    "Bluestock-Capstone/charts/aum_growth.png"
)

plt.show()