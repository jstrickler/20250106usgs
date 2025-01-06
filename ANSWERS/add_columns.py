import pandas as pd

df = pd.read_csv("../DATA/sales_records.csv")

df.info() # view original columns
print()

df["Total Revenue"] = df["Units Sold"] * df["Unit Price"]

df["Total Cost"] = df["Units Sold"] * df["Unit Cost"]

df["Total Profit"] = df["Total Revenue"] - df["Total Cost"]

df.info()  # show added columns
print()

print(f"df.iloc[1]:\n{df.iloc[1]}\n")  # one row, showing added columns with values
