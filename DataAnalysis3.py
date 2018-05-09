import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

from sklearn.linear_model import LinearRegression
from sklearn.cluster import DBSCAN

# Import datasets
jan = pd.read_csv('201701-hubway-tripdata.csv')
feb = pd.read_csv('201702-hubway-tripdata.csv')
mar = pd.read_csv('201703-hubway-tripdata.csv')
apr = pd.read_csv('201704-hubway-tripdata.csv')
may = pd.read_csv('201705-hubway-tripdata.csv')
jun = pd.read_csv('201706-hubway-tripdata.csv')
jul = pd.read_csv('201707-hubway-tripdata.csv')
aug = pd.read_csv('201708-hubway-tripdata.csv')
sep = pd.read_csv('201709-hubway-tripdata.csv')
octo = pd.read_csv('201710-hubway-tripdata.csv')
nov = pd.read_csv('201711-hubway-tripdata.csv')
dec = pd.read_csv('201712-hubway-tripdata.csv')


# For each month:
    # 1. Change datetime format
    # 2. Calculate the counts of specific trip

datalist = [jan, feb, mar, apr, 
            may, jun, jul, aug,
            sep, octo, nov,dec]

# 1. Change datetime format and calculate count
for month in datalist:
    month.starttime = month.starttime.astype('datetime64')
    month['starthour'] = pd.to_datetime(month['starttime'], format='%H:%M').dt.hour
    month['count'] = 1


jan['Counts'] = jan.groupby(['starthour'])['starthour'].transform('count')
feb['Counts'] = feb.groupby(['starthour'])['starthour'].transform('count')
mar['Counts'] = mar.groupby(['starthour'])['starthour'].transform('count')
apr['Counts'] = apr.groupby(['starthour'])['starthour'].transform('count')
may['Counts'] = may.groupby(['starthour'])['starthour'].transform('count')
jun['Counts'] = jun.groupby(['starthour'])['starthour'].transform('count')
jul['Counts'] = jul.groupby(['starthour'])['starthour'].transform('count')
aug['Counts'] = aug.groupby(['starthour'])['starthour'].transform('count')
sep['Counts'] = sep.groupby(['starthour'])['starthour'].transform('count')
octo['Counts'] = octo.groupby(['starthour'])['starthour'].transform('count')
nov['Counts'] = nov.groupby(['starthour'])['starthour'].transform('count')
dec['Counts'] = dec.groupby(['starthour'])['starthour'].transform('count')


jan = jan.drop_duplicates(['starthour'])
feb = feb.drop_duplicates(['starthour'])
mar = mar.drop_duplicates(['starthour'])
apr = apr.drop_duplicates(['starthour'])
may = may.drop_duplicates(['starthour'])
jun = jun.drop_duplicates(['starthour'])
jul = jul.drop_duplicates(['starthour'])
aug = aug.drop_duplicates(['starthour'])
sep = sep.drop_duplicates(['starthour'])
octo = octo.drop_duplicates(['starthour'])
nov = nov.drop_duplicates(['starthour'])
dec = dec.drop_duplicates(['starthour'])

jan = jan[['starthour','Counts']]
feb = feb[['starthour','Counts']]
mar = mar[['starthour','Counts']]
apr = apr[['starthour','Counts']]
may = may[['starthour','Counts']]
jun = jun[['starthour','Counts']]
jul = jul[['starthour','Counts']]
aug = aug[['starthour','Counts']]
sep = sep[['starthour','Counts']]
octo = octo[['starthour','Counts']]
nov = nov[['starthour','Counts']]
dec = dec[['starthour','Counts']]

jan.to_csv('jan1.csv')
feb.to_csv('feb1.csv')
mar.to_csv('mar1.csv')
apr.to_csv('apr1.csv')
may.to_csv('may1.csv')
jun.to_csv('jun1.csv')
jul.to_csv('jul1.csv')
aug.to_csv('aug1.csv')
sep.to_csv('sep1.csv')
octo.to_csv('oct1.csv')
nov.to_csv('nov1.csv')
dec.to_csv('dec1.csv')