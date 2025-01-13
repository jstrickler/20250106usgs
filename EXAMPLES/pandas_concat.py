import pandas as pd
import numpy as np

dataset1 = np.full((3, 3), "10")
dataset2 = np.full((5, 3), "20")

df1 = pd.DataFrame(dataset1)
df2 = pd.DataFrame(dataset2)

print("df1:")
print(df1, '\n')
print("df2:")
print(df2, '\n')

df_rows = pd.concat([df1, df2])
print("df_rows:")
print(df_rows, '\n')

df_columns = pd.concat([df1, df2], axis=1)
print("df_columns")
print(df_columns)

