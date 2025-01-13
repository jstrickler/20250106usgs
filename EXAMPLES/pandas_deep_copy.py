
# program to depict shallow copy
# in pandas dataframe
 
# import module
import pandas as pd
 
# assign dataframe
df = pd.DataFrame(['Mandy', 'Ron', 'Jacob', 'Bayek'], index=['a', 'b', 'c', 'd'], columns=['Name'])

print("Originals:")
print(f"df = \n{df}\n")
 
# shallow copy
copydf_shallow = df.copy(deep=False)
 
print(f"copydf_shallow = \n{copydf_shallow}\n")

# deep copy
copydf_deep = df.copy(deep=True)  # deep=True is default
 
print(f"copydf_deep = \n{copydf_deep}\n")
print('-' * 60)

# now change the indexes

copydf_shallow.index = ['w', 'x', 'y', 'z']
copydf_deep.index = ['alpha', 'beta', 'gamma', 'delta']

print("After changing indexes")
print(f"df = \n{df}\n")
print(f"copydf_shallow = \n{copydf_shallow}\n")
print(f"copydf_deep = \n{copydf_deep}\n")
print('-' * 60)

df.loc['a', 'Name'] = "WOMBAT"
print(f"{df.loc['a', 'Name'] = }\n")

print(f"df = \n{df}\n")
print(f"copydf_shallow = \n{copydf_shallow}\n")
print(f"copydf_deep = \n{copydf_deep}\n")
