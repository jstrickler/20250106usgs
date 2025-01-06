import pandas as pd
from printheader import print_header

DATA = [5, 10, 15]
INDEX = ['a', 'b', 'c']

# create from list
print_header("s1")
s1 = pd.Series(DATA)
print(s1, "\n")
print("s1[0]:", s1[0], "\n")
print()

# create from list and specify index names
print_header("s2")
s2 = pd.Series(DATA, index=INDEX)
print(s2, "\n")
print("s2['a']:", s2['a'])
print()

# create from one-column file
print_header("s3")
# .squeeze('columns') converts dataframe with single column into Series
s3 = pd.read_table("../DATA/float_values.txt", header=None).squeeze('columns')
print(s3, "\n")

# create from one-column file, and add time series as index
print_header("s4")
s4 = pd.read_table("../DATA/float_values.txt", header=None).squeeze('columns')
s4.index = pd.date_range('2023-01-01', periods=len(s4))  # days starting at 1/1/2023
print(s4, "\n")
