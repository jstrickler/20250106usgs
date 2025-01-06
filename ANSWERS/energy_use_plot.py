import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


col_names = ['Desc',"1960","1965","1970","1975","1980","1985","1990","1991",
    "1992","1993","1994","1995","1996","1997","1998","1999","2000",
    "2001","2002","2003","2004","2005","2006","2007","2008","2009",
    "2010","2011"
]

df = pd.read_csv(
    '../DATA/energy_use_quad.csv',
    names = col_names,    
)

print(df.head())

# plt.xlabel('Year')
# plt.ylabel('Gigawatts')
print('-' * 60)


d2 = df.transpose()
print(d2.head())
print(d2.iloc[0])

# plt.plot(df.transpose()['Residential and commercial'])
# plt.show()

