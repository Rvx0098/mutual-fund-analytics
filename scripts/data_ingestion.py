import pandas as pd
import os

DATA_FOLDER = "Bluestock-Capstone/data/raw"

print("=" * 80)
print("DATA INGESTION REPORT")
print("=" * 80)

for file in sorted(os.listdir(DATA_FOLDER)):

    if file.endswith(".csv"):

        path = os.path.join(DATA_FOLDER, file)

        print("\n" + "=" * 80)
        print(f"FILE: {file}")
        print("=" * 80)

        df = pd.read_csv(path)

        print("\nSHAPE:")
        print(df.shape)

        print("\nDATA TYPES:")
        print(df.dtypes)

        print("\nFIRST 5 ROWS:")
        print(df.head())

        print("\nMISSING VALUES:")
        print(df.isnull().sum())

        print("\nDUPLICATES:")
        print(df.duplicated().sum())

print("\nDATA INGESTION COMPLETED")