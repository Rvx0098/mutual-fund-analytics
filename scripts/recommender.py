import pandas as pd

performance = pd.read_csv(
    "../Bluestock-Capstone/data/processed/07_scheme_performance_clean.csv"
)

risk = input(
    "Enter Risk Level (Low/Moderate/High): "
)

recommendations = (
    performance[
        performance["risk_grade"]
        .str.lower()
        ==
        risk.lower()
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print("\nTop Recommendations\n")

print(
    recommendations[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio",
            "return_5yr_pct"
        ]
    ]
)