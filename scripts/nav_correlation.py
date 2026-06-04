import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

nav = pd.read_csv(
    "Bluestock-Capstone/data/raw/02_nav_history.csv"
)

codes = nav["amfi_code"].unique()[:10]

nav = nav[
    nav["amfi_code"].isin(codes)
]

pivot = nav.pivot(
    index="date",
    columns="amfi_code",
    values="nav"
)

returns = pivot.pct_change()

corr = returns.corr()

plt.figure(figsize=(10,8))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title("NAV Return Correlation Matrix")

plt.tight_layout()

plt.savefig(
    "Bluestock-Capstone/charts/nav_correlation_matrix.png"
)

plt.show()