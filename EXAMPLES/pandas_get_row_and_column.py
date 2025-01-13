import pandas as pd
import numpy as np

data = np.arange(9)
data.shape = 3,3
print(f"data:\n{data}")

index = 'Jan Feb Mar'.split()
columns = 'a b c'.split()
df = pd.DataFrame(data,index=index, columns=columns)
print(f"df:\n{df}\n")
df.loc['Jan', 'c'] = 4

print(f"df:\n{df}\n")

print(f"df.where(df == 4):\n{df.where(df == 4)}\n")

print(f"df.where(df == 4).stack():\n{df.where(df == 4).stack()}\n")

print(f"df.where(df == 4).stack()index:\n{df.where(df == 4).stack().index}\n")

print(f"list(df.where(df == 4).stack().index):\n{list(df.where(df == 4).stack().index)}\n")


