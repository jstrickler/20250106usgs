import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(
    'https://qrc.depaul.edu/Excel_Files/Presidents.xlsx',
    index_col="No",  # use term as row index
    sheet_name='Master',  # name of worksheet
    na_values='NA()')  # use NA() for missing values

print("First 5 rows")
print(df.head(), '\n')

print("First row")
print(df.loc[1], '\n')

party_counts = df['Political Party'].value_counts()
print("Party counts")
print(party_counts)

# plot the data
plt.figure(figsize=(20.0,8.0))  # set figure size
party_counts.plot(kind='barh')  # plot a horizontal bar graph
plt.savefig("parties.png")    # save graph to file
# plt.show()  # uncomment to display graph
