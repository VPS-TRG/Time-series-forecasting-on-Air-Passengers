import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
rcParams['figure.figsize']=10,6

dataset=pd.read_csv('AirPassengers.csv')

dataset['Month']=pd.to_datetime(dataset['Month'],infer_datetime_format=True)
indexedDataset = dataset.set_index(['Month'])

print(indexedDataset.head(4))
print(indexedDataset.tail(4))
plt.xlabel("Date")
plt.ylabel("Number of air passengers")
plt.plot(indexedDataset)
plt.show()
#plt.savefig('plots/1.png')

rolmean=indexedDataset.rolling(window=12).mean()
rolstd= indexedDataset.rolling(window=12).std()
print(rolmean,rolstd)