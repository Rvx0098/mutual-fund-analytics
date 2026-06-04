import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(
    "Bluestock-Capstone/data/raw/05_category_inflows.csv"
)

pivot = df.pivot(
    index="category",
    columns="month",
    values="net_inflow_crore"
)

plt.figure(figsize=(14,8))

sns.heatmap(
    pivot,
    cmap="YlGnBu"
)

plt.title("Category Inflow Heatmap")

plt.tight_layout()

plt.savefig(
    "Bluestock-Capstone/charts/category_heatmap.png"
)

plt.show()