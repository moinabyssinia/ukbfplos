"""  
Created on Wed Aug 03 09:56:00 2022

distribute rainfall every 15 mins

@author: Michael Getachew Tadesse

"""

import os
import pandas as pd 
import datetime


dir_in = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\"\
        "FromSJRWMD\\Rainfall\\modified_files\\pixel_data_15min\\2017"

out = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\FromSJRWMD\\Rainfall\\"\
            "modified_files\\pixel_rainfall_distributed\\2017"



# get data
os.chdir(dir_in)

gList = os.listdir()

# print(gList)

for gg in gList:
    print(gg)

    os.chdir(dir_in)

    dat = pd.read_csv(gg)
    dat['distributed_rain'] = 0

    # get 'fh' rows 

    fhRows = dat[dat['fullHr'] == 'fh']
    fhRows.reset_index(inplace = True)
    # print(fhRows)

    for ff in range(len(fhRows)):
        cluster = fhRows['cluster'][ff]
        # print(dat[dat['cluster'] == cluster])      

        fhRain = fhRows['rain_avg'][ff]

        dat.loc[dat['cluster'] == cluster, 'distributed_rain'] = fhRain/4

        # print(dat[dat['cluster'] == cluster])

    os.chdir(out)
    dat.to_csv(gg)


