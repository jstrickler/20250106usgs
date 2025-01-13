import pandas as pd
import numpy as np

# data from
# http://www.rita.dot.gov/bts/sites/rita.dot.gov.bts/files/publications/
# national_transportation_statistics/html/table_01_44.html

df = pd.read_csv('../DATA/airport_boardings.csv', thousands=',', index_col=1)

print(df.head(10), "\n")

# select rows through PHX where column name contains "Rank"
df1 = df.loc[:'PHX', (col for col in df.columns if 'Rank' in col)]
print(df1, '\n')

# select rows where row index starts with 'A'
df2 = df.loc[(row for row in df.index if row.startswith('A'))]
print(df2, '\n')

# alternate approach
df2 = df.loc[np.char.startswith(list(df.index.values), 'A')]
print(df2, '\n')


