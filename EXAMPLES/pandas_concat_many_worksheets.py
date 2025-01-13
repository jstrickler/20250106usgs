import pandas as pd

df_dict = pd.read_excel("../DATA/manysheets.xlsx", None)

df = pd.concat(df_dict.values(), ignore_index=True)

print(df)
print()

print(df.info())

