import pandas as pd
import numpy as np

store=pd.read_csv('https://raw.githubusercontent.com/dia-27/Walmart_WeeklySalesPrediction/main/Datasets/stores.csv')
feat=pd.read_csv('https://raw.githubusercontent.com/dia-27/Walmart_WeeklySalesPrediction/main/Datasets/walmart_features.csv')
train=pd.read_csv('https://raw.githubusercontent.com/dia-27/Walmart_WeeklySalesPrediction/main/Datasets/walmart_train.csv')

store.head()
np.unique(store['Store'])
feat.head(10)
feat.isnull().sum()
feat['MarkDown1'] = feat['MarkDown1'].fillna(0)
feat['MarkDown2'] = feat['MarkDown2'].fillna(0)
feat['MarkDown3'] = feat['MarkDown3'].fillna(0)
feat['MarkDown4'] = feat['MarkDown4'].fillna(0)
feat['MarkDown5'] = feat['MarkDown5'].fillna(0)

from statistics import mean
feat['CPI'] = feat['CPI'].fillna(mean(feat['CPI']))
feat['Unemployment'] = feat['Unemployment'].fillna(mean(feat['Unemployment']))

feat['Store'].value_counts()[1]
feat.shape,train.shape,store.shape

data = pd.merge(feat, train, on=['Store','Date','IsHoliday'], how='inner')
# merging(adding) all stores info with new training data
final_data = pd.merge(data,store,how='inner',on=['Store'])

final_data.head()

final_data.shape
final_data.info()
