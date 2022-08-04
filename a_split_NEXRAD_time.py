"""  
Created on Tue Aug 02 16:00:00 2022

split timestamp to hr min sec
*this script is particularly used for 
*NEXRAD obtained form SJRWMD

@author: Michael Getachew Tadesse

"""

import os
import pandas as pd 


os.chdir('R:\\40715-013 UKFPLOS\\Received_Data_Models\\"\
        "FromSJRWMD\\Rainfall\\modified_files')

dat = pd.read_csv('2017b_Hourly_PIXEL.csv')

print(dat)


dat[['hour', 'min', 'sec']] = pd.DataFrame(dat['HOUR'].str.split(":", expand = True))

dat = dat[['PIXEL', 'DATES', 'hour', 'min', 'sec', 'RAIN_AVG']]

print(dat)

dat.to_csv('2017_split_time.csv')