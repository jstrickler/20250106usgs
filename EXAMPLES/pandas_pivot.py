import pandas as pd

DATA_FILE_NAME = "../DATA/FremontBridge.csv"

df = pd.read_csv(DATA_FILE_NAME)

print(df.head())

df_p = df.pivot(columns="Date")

print(df_p.head())