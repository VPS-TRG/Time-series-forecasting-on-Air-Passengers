import numpy as np
import pandas as pd
import matplotlib as plt
from matplotlib.pylab import rcParams
rcParams['figure.figsize']=10,6

dataset=pd.read_csv('AirPassangers.csv')

dataset['Month']=pd.to_datetime(dataset['Month'],infer_datetime_format=True)
indexedDataset = dataset.set_index(['Month'])
