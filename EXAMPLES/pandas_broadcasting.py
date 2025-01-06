import pandas as pd
from printheader import print_header

columns = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']  # column labels
rows = pd.date_range('2013-01-01 00:00:00', periods=6, freq='D')  # date range to be used as row indexes

values = [  # sample data
    [100, 110, 120, 930, 140],
    [250, 210, 120, 130, 840],
    [300, 310, 520, 430, 340],
    [275, 410, 420, 330, 777],
    [300, 510, 120, 730, 540],
    [150, 610, 320, 690, 640],
]

df = pd.DataFrame(values, rows, columns)  # create dataframe from data
print_header("Basic DataFrame:")
print(df)
print()

print_header("Triple all values")
print(df * 3)
print()  # multiply every value by 3

print_header("Multiply column gamma by 1.5")
df['gamma'] *= 1.5  # multiply values in column 'gamma' by 1.
print(df)
print()

def square_root(n):
    return n ** .5

df['alpha'] = square_root(df['alpha'])
print_header("Apply square_root() to column alpha")
print(df, '\n')

