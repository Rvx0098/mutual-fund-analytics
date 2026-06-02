import pandas as pd
import os

print("=" * 60)
print("SCRIPT STARTED")
print("=" * 60)

folder = "Bluestock-Capstone/data/raw"

print("\nCurrent Working Directory:", os.getcwd())
print("Folder Exists:", os.path.exists(folder))

if not os.path.exists(folder):
    print("\nERROR: Folder not found!")
    exit()

files = sorted(os.listdir(folder))

print("\nFiles Found:")
for f in files:
    print("-", f)

for file in files:
    if file.endswith(".csv"):
        path = os.path.join(folder, file)

        try:
            df = pd.read_csv(path)

            print("\n" + "=" * 60)
            print(f"FILE: {file}")
            print("=" * 60)

            print(f"Rows: {df.shape[0]}")
            print(f"Columns: {df.shape[1]}")

            print("\nColumn Names:")
            for col in df.columns:
                print(f"- {col}")

            print("\nFirst 3 Rows:")
            print(df.head(3))

        except Exception as e:
            print(f"\nERROR reading {file}")
            print(e)

print("\n" + "=" * 60)
print("SCRIPT FINISHED")
print("=" * 60)