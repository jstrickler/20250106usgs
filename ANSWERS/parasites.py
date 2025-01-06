import pandas as pd

df = pd.read_csv('../DATA/parasite_data.csv')

print(df)
print()

df2 = df[df['ShannonDiversity'] >= 1.0]
print(df2)
print()


print(df2.values, '\n')

print(len(df), len(df2))
