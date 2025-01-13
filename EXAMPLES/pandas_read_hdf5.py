import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

H5_FILE = "../DATA/NEONDSTowerTemperatureData.hdf5"
H5_KEY = '/Domain_03/OSBS/min_1/boom_1/temperature'

df = pd.read_hdf(H5_FILE, key=H5_KEY)
start_time = df.iloc[0]['date']
index = pd.date_range(start_time, periods=len(df), freq='T', inclusive='both')
df.drop(['date'], axis=1, inplace=True)
df.index = index
print(df.info())
print('-' * 60)
print(df.describe())
print('-' * 60)

print(df)
print('-' * 60)

df_hourly = df[['min', 'max']].resample('1H').mean()
print(df_hourly)
#print(list(df_hourly))

df_hourly['min'].plot()
df_hourly['max'].plot()
plt.show()