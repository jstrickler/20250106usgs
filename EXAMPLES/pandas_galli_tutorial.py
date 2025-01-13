# based on: https://www.youtube.com/watch?v=vmEHCJofslg&t=764s
import pandas as pd

df = pd.read_csv('../DATA/pokemon_data.csv')

print(df.head())

print(df.columns, len(df.columns))

print(df.Name[:20])


print("0:")
print(df.iloc[0])
print("1:")
print(df.iloc[1])

for index, row in df.iterrows():
    print(index, row)
print('-' * 60)

print(df.loc[df['Type 1'] == 'Grass'])
print('-' * 60)

print(df.loc[(df['Speed'] > 100) & (df.Legendary)])

print(df.columns)

