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
    #triplist = []
    month.starttime = month.starttime.astype('datetime64')
    month.stoptime = month.stoptime.astype('datetime64')
    
    month['starthour'] = pd.to_datetime(month['starttime'], format='%H:%M').dt.hour
    month['endhour'] = pd.to_datetime(month['stoptime'], format='%H:%M').dt.hour
    month['count'] = 1
    
    month['startCounts'] = month.groupby(['start station name','starthour'])['starthour'].transform('count')
    month['endCounts'] = month.groupby(['end station name','endhour'])['endhour'].transform('count')

    

startjan = jan.drop_duplicates(['start station name', 'starthour'])[[4,5,6,15,18]]
startfeb = feb.drop_duplicates(['start station name', 'starthour'])[[4,5,6,15,18]]
startmar = mar.drop_duplicates(['start station name', 'starthour'])[[4,5,6,15,18]]
startapr = apr.drop_duplicates(['start station name', 'starthour'])[[4,5,6,15,18]]
startmay = may.drop_duplicates(['start station name', 'starthour'])[[4,5,6,15,18]]
startjun = jun.drop_duplicates(['start station name', 'starthour'])[[4,5,6,15,18]]
startjul = jul.drop_duplicates(['start station name', 'starthour'])[[4,5,6,15,18]]
startaug = aug.drop_duplicates(['start station name', 'starthour'])[[4,5,6,15,18]]
startsep = sep.drop_duplicates(['start station name', 'starthour'])[[4,5,6,15,18]]
startoct = octo.drop_duplicates(['start station name', 'starthour'])[[4,5,6,15,18]]
startnov = nov.drop_duplicates(['start station name', 'starthour'])[[4,5,6,15,18]]
startdec = dec.drop_duplicates(['start station name', 'starthour'])[[4,5,6,15,18]]




endjan = jan.drop_duplicates(['end station name', 'endhour'])[[8,9,10,16,19]]
endfeb = feb.drop_duplicates(['end station name', 'endhour'])[[8,9,10,16,19]]
endmar = mar.drop_duplicates(['end station name', 'endhour'])[[8,9,10,16,19]]
endapr = apr.drop_duplicates(['end station name', 'endhour'])[[8,9,10,16,19]]
endmay = may.drop_duplicates(['end station name', 'endhour'])[[8,9,10,16,19]]
endjun = jun.drop_duplicates(['end station name', 'endhour'])[[8,9,10,16,19]]
endjul = jul.drop_duplicates(['end station name', 'endhour'])[[8,9,10,16,19]]
endaug = aug.drop_duplicates(['end station name', 'endhour'])[[8,9,10,16,19]]
endsep = sep.drop_duplicates(['end station name', 'endhour'])[[8,9,10,16,19]]
endoct = octo.drop_duplicates(['end station name', 'endhour'])[[8,9,10,16,19]]
endnov = nov.drop_duplicates(['end station name', 'endhour'])[[8,9,10,16,19]]
enddec = dec.drop_duplicates(['end station name', 'endhour'])[[8,9,10,16,19]]


startcolnames = ['station','lat','lon','hour','startCounts']
endcolnames = ['station','lat','lon','hour','endCounts']

startmonths = [startjan, startfeb, startmar, startapr, 
              startmay, startjun, startjul, startaug, 
              startsep, startoct, startnov, startdec]

endmonths = [endjan, endfeb, endmar, endapr, 
              endmay, endjun, endjul, endaug, 
              endsep, endoct, endnov, enddec]

for month in startmonths:
    month.columns = startcolnames

for month in endmonths:
    month.columns = endcolnames



mergejan = pd.merge(startjan, endjan, on=['station','lat','lon','hour'], how = 'outer').fillna(0)
mergefeb = pd.merge(startfeb, endfeb, on=['station','lat','lon','hour'], how = 'outer').fillna(0)
mergemar = pd.merge(startmar, endmar, on=['station','lat','lon','hour'], how = 'outer').fillna(0)
mergeapr = pd.merge(startapr, endapr, on=['station','lat','lon','hour'], how = 'outer').fillna(0)
mergemay = pd.merge(startmay, endmay, on=['station','lat','lon','hour'], how = 'outer').fillna(0)
mergejun = pd.merge(startjun, endjun, on=['station','lat','lon','hour'], how = 'outer').fillna(0)
mergejul = pd.merge(startjul, endjul, on=['station','lat','lon','hour'], how = 'outer').fillna(0)
mergeaug = pd.merge(startaug, endaug, on=['station','lat','lon','hour'], how = 'outer').fillna(0)
mergesep = pd.merge(startsep, endsep, on=['station','lat','lon','hour'], how = 'outer').fillna(0)
mergeoct = pd.merge(startoct, endoct, on=['station','lat','lon','hour'], how = 'outer').fillna(0)
mergenov = pd.merge(startnov, endnov, on=['station','lat','lon','hour'], how = 'outer').fillna(0)
mergedec = pd.merge(startdec, enddec, on=['station','lat','lon','hour'], how = 'outer').fillna(0)

mergedfs = [mergejan, mergefeb, mergemar, mergeapr,
           mergemay, mergejun, mergejul, mergeaug,
           mergesep,mergeoct,mergenov,mergedec]

for month in mergedfs:
    month['Diff'] = month.startCounts - month.endCounts

mergejan.sort_values('hour').to_csv('diffjan.csv')
mergefeb.sort_values('hour').to_csv('difffeb.csv')
mergemar.sort_values('hour').to_csv('diffmar.csv')
mergeapr.sort_values('hour').to_csv('diffapr.csv')
mergemay.sort_values('hour').to_csv('diffmay.csv')
mergejun.sort_values('hour').to_csv('diffjun.csv')
mergejul.sort_values('hour').to_csv('diffjul.csv')
mergeaug.sort_values('hour').to_csv('diffaug.csv')
mergesep.sort_values('hour').to_csv('diffsep.csv')
mergeoct.sort_values('hour').to_csv('diffoct.csv')
mergenov.sort_values('hour').to_csv('diffnov.csv')
mergedec.sort_values('hour').to_csv('diffdec.csv')