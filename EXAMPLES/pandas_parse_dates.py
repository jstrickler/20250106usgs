import pandas as pd


df = pd.read_csv('sharon_dates.txt', parse_dates=[0], header=None, names=['Date', 'Info'])


print(df)
