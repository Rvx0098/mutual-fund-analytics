import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "Bluestock-Capstone/data/raw/06_industry_folio_count.csv"
)

plt.figure(figsize=(12,6))

plt.plot(
    df["month"],
    df["total_folios_crore"],
    marker="o"
)

plt.title("Industry Folio Growth")

plt.xlabel("Month")
plt.ylabel("Folios (Crore)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "Bluestock-Capstone/charts/folio_growth.png"
)

plt.show()