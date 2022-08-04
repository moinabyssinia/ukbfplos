"""  
Created on Wed Aug 03 10:48:00 2022

split timestamp to hr min sec
*this script is particularly used for 
*NEXRAD obtained form SFWMD

@author: Michael Getachew Tadesse

"""

import os
import pandas as pd 
import datetime

dir_in = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\FromSFWMD\\"\
        "rainfall_modified_files\\rawData"

os.chdir(dir_in)

dat = pd.read_csv('2017.csv', dtype = str)

print(dat)

# dat['hour'] = pd.to_datetime(dat['hh_mm']).dt.hour
# dat['min'] = dat['hhmm'].str.split('.0')

# print(dat)

# dat = dat[['pixel', 'date', 'hour', 'min', 'value']]

# print(dat)


# dat.to_csv('2017_split_time.csv')