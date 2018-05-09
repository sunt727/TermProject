import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

from sklearn.linear_model import LinearRegression
from sklearn.cluster import DBSCAN


##########---------- Popular Trips of the Year ----------##########

# Use a loop to read in the dataset and append to each dataset

# Read in the first dataset
data = pd.read_csv('201701-hubway-tripdata.csv')

# A loop to read and append all other 11 datasets
for i in range(2,13):
    newdata = pd.read_csv('2017' + '%02d' % i + '-hubway-tripdata.csv')
    data = data.append(newdata)

# Reset index and delete original index
data = data.reset_index()
data = data.iloc[:,1:]

# Change starttime and stoptime into datetime type
data.starttime = data.starttime.astype('datetime64')
data.stoptime = data.stoptime.astype('datetime64')
# Count the number of specific start station and end station in the whole year
data['Counts'] = data.groupby(['start station name','end station name'])['end station name'].transform('count')


##########---------- Popular Trips of the Month ----------##########
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
    month.stoptime = month.stoptime.astype('datetime64')
    month['Counts'] = month.groupby(['start station name','end station name'])['end station name'].transform('count')

    
# Append all
data = pd.DataFrame(columns=jan.columns)
for month in datalist:
    data = data.append(month)


# For each trip, only keep one record in each month
data_dropduplicate = pd.DataFrame(columns=jan.columns)

for month in datalist:
    month = month.drop_duplicates(['start station name','end station name'])
    data_dropduplicate = data_dropduplicate.append(month)

