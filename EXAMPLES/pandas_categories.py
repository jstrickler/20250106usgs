import pandas as pd
from printheader import print_header

# columns:
# Name,Position Title,Department,Employee Annual Salary
salaries = pd.read_csv(
    "../DATA/city-of-chicago-salaries.csv"
)

print_header("BASIC DATAFRAME (FIRST 5 ROWS)")
print(salaries.head())

print_header("VALUE COUNTS OF DEPARTMENTS:")
print(salaries['Department'].value_counts(), '\n')

print_header("WITHOUT CATEGORIES")
print(salaries.memory_usage(deep=True))
print()

salaries = pd.read_csv(
    "../DATA/city-of-chicago-salaries.csv",
    dtype={"Position Title": "category", "Department": "category"}
)
print_header("WITH CATEGORIES")
print(salaries.memory_usage(deep=True))
print() 
