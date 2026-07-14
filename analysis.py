import pandas as pd
df = pd.read_csv("data.csv")
print("Number of rows", len(df))
print("mean sale amount", df["amount"].mean())
