import pandas as pd

names = 'term lastname firstname dob dod birthplace birthstate tookoffice leftoffice party'.split()
df = pd.read_table("../DATA/presidents.txt", delimiter=':', names=names)
print(df.birthstate.value_counts())
