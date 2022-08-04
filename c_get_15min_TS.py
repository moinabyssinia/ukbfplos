"""  
Created on Tue Aug 02 16:44:00 2022

get fifteen minute time series NEXRAD

@author: Michael Getachew Tadesse

"""

import os
import pandas as pd 
import datetime


dir_in = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\"\
                "FromSFWMD\\rainfall_modified_files\\roundedTime"

out = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\FromSFWMD\\"\
                "rainfall_modified_files\\pixel_data_15min\\2017"

#########################################
os.chdir(dir_in)
dat = pd.read_csv("2017_roundedTime_v2.csv")
sd = '2017-09-01 00:15:00'
ed = '2017-10-30 23:00:00'
#########################################


print(dat)

# parsing data

# mark the full hour timesteps for later use

dat['fullHr'] = 'fh'

print(dat)


dat['datetime'] = dat['date'].astype(str) + " " + \
        dat['hr'].astype(str) + ":" + dat['mm'].astype(str)

dat['datetime'] = pd.to_datetime(dat['datetime'], format = '%m/%d/%Y %H:%M')

dat = dat[['pixel', 'datetime', 'value', 'fullHr']]

print(dat)



# generating timeseries that is hourly
full_date = pd.DataFrame(pd.date_range(sd, ed, freq = '0.25H'))
full_date['res'] = 'h'
full_date.columns = ['datetime', 'res']
print(full_date)

# get unique pixel values
pixels = dat['pixel'].unique()



for pp in pixels:
    os.chdir(dir_in)
    print(pp)
    df = dat[dat['pixel'] == pp]
    #print(df)

    df_15min = pd.merge(full_date, df, on = 'datetime', how = 'outer')
    df_15min = df_15min[['datetime', 'fullHr', 'pixel', 'value']]
    #print(df_hourly)

    # get date column

    df_15min['date'] = pd.to_datetime(df_15min['datetime']).dt.date

    # get hour column
    df_15min['hr'] = pd.to_datetime(df_15min['datetime']).dt.hour


    # cluster 4 timesteps toghether for distributing rain
    df_15min['cluster'] = 'nan'
    ii = 0
    cluster = 1
    while ii <= len(df_15min) - 4:
        print(ii+4)
        df_15min.iloc[ii:ii+4, 6] = cluster
        # print(df_15min)
        ii += 4
        cluster += 1


    # limit/bound time series to the above range
    df_15min = df_15min[(df_15min['datetime'] >= sd) & (df_15min['datetime'] <= ed)]

    os.chdir(out)
    df_15min.to_csv(str(pp) + '.csv')
    
