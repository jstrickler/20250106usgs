import pandas as pd

dataset = [
    ["Bob", "salaried"],
    ["Ali", "hourly"],
    ["Alonzo", "salaried"],
    ["Dominique", "hourly"],
    ["Connie", "contractor"],
]

df = pd.DataFrame(dataset)
df.columns = "Name", "EmployeeType"

print("df:")
print(df, "\n")

# get first three letters of string in column
print(df["EmployeeType"].str[0:3], '\n')

# get employee type as upper case
print(df["EmployeeType"].str.upper(), '\n')


