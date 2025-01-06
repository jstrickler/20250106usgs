import pandas as pd
from printheader import print_header

cols = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
index = ['a', 'b', 'c', 'd', 'e', 'f']
values = [
    [100, 110, 120, 130, 140],
    [200, 210, 220, 230, 240],
    [300, 310, 320, 330, 340],
    [400, 410, 420, 430, 440],
    [500, 510, 520, 530, 540],
    [600, 610, 620, 630, 640],
]

df = pd.DataFrame(values, index=index, columns=cols)  # create dataframe
print_header('DataFrame df')
print(df, '\n')

df2 = df.drop(['beta', 'delta'], axis=1)  # drop columns beta and delta (axes: 0=rows, 1=columns)
print_header("After dropping beta and delta:")
print(df2, '\n')

print_header("After dropping rows b, c, and e")
df3 = df.drop(['b', 'c', 'e'])  # drop rows b, c, and e
print(df3)

print_header(" In-place drop")
df.drop(['beta', 'gamma'], axis=1, inplace=True)
print(df, "\n")

df.drop(['b', 'c'], inplace=True)
print(df)
print('-' * 60)

# dropping N/A values

values2 = [
    [100, 110, 120, 130, 140],
    [200, 210, 220, 230, 240],
    [300, 310, 320, 330, 340],
    [400, pd.NA, 420, 430, 440],
    [500, 510, 520, pd.NA, 540],
    [600, 610, 620, 630, 640],
]

df2 = pd.DataFrame(values2, index=index, columns=cols)  # create dataframe
print_header('DataFrame df2')
print(df2, '\n')

na1 = df2.dropna(axis=1)  # drop columns with N/A
print_header("Dataframe na1")
print(na1, '\n')

na2 = df2.dropna(axis=0)  # drop rows with N/A (default value for axis)
print_header("Dataframe na2")
print(na2, '\n')

df2.dropna(inplace=True, axis=1)
print_header("Dataframe df2")
print(df2, '\n')
