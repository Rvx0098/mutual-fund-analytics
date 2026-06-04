import pandas as pd
import matplotlib.pyplot as plt

nav = pd.read_csv(
    "Bluestock-Capstone/data/raw/02_nav_history.csv"
)

codes = nav["amfi_code"].unique()[:5]

plt.figure(figsize=(14,7))

for code in codes:

    temp = nav[
        nav["amfi_code"] == code
    ]

    plt.plot(
        temp["date"],
        temp["nav"],
        label=str(code)
    )

plt.legend()

plt.title("NAV Trend Analysis")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "Bluestock-Capstone/charts/nav_trend_analysis.png"
)

plt.show()