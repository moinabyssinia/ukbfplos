"""  
Created on Wed Aug 03 17:25:00 2022

separate by pixels - SWFWMD 

@author: Michael Getachew Tadesse

"""

import os
import pandas as pd 
import datetime


dir_in = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\SWFWMD\\rainfall\\"\
                "rawData\\2017"


dir_out = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\SWFWMD\\rainfall\\"\
                "pixel_rainfall_distributed\\2017"



os.chdir(dir_in)

dat = pd.read_csv("2017.csv")

# get unique pixels
pix = dat['pixel'].unique()


for pp in pix:
    df = dat[dat['pixel'] == pp]

    df = df[['pixel', 'datetime', 'value']]

    os.chdir(dir_out)

    df.to_csv(str(pp) + ".csv")

