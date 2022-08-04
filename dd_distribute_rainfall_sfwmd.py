"""  
Created on Wed Aug 03 14:43:00 2022

assign 0 rainfall to empty cells

@author: Michael Getachew Tadesse

"""

import os
import pandas as pd 
import datetime


dir_in = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\FromSFWMD\\"\
                "rainfall_modified_files\\pixel_data_15min\\2017"

out = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\FromSFWMD\\"\
                "rainfall_modified_files\\pixel_rainfall_distributed\\2017"



# get data
os.chdir(dir_in)

gList = os.listdir()

# print(gList)

for gg in gList:
    print(gg)

    os.chdir(dir_in)

    dat = pd.read_csv(gg)
    dat['distributed_rain'] = 0

    # print(dat)

    # get 'fh' rows 

    dat.loc[dat['fullHr'] == 'fh', 'distributed_rain'] = dat[dat['fullHr'] == 'fh']['value']

        # print(dat[dat['cluster'] == cluster])

    os.chdir(out)
    dat.to_csv(gg)


