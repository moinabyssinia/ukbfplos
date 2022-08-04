"""  
Created on Wed Aug 03 16:56:00 2022

combine SWFWMD NEXRAD datasets

@author: Michael Getachew Tadesse

"""

import os
import pandas as pd 
import datetime


os.chdir("R:\\40715-013 UKFPLOS\\Received_Data_Models\\"\
            "SWFWMD\\rainfall\\rawData")

swf_ukb = pd.read_csv('swf_unique_pixels.csv')

print(swf_ukb)


dir_in = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\SWFWMD\\rainfall\\"\
                "rawData\\2017"


os.chdir(dir_in)

nexList = os.listdir()


# empty dataframe

dat_combined = pd.DataFrame(columns = ['pixel', 'datetime', 'value'])

for nn in nexList:
    print(nn)

    dat = pd.read_csv(nn, header = None)

    dat.columns = ['pixel', 'datetime', 'value']

    df = pd.merge(swf_ukb, dat, on = 'pixel', how = 'inner')

    df = df[(df['datetime'] >= '09/01/2017 00:00') & 
                    (df['datetime'] < '11/01/2017 00:00')]

    dat_combined = pd.concat([dat_combined, df], axis = 0)


dat_combined.to_csv("2017.csv")



