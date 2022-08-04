"""  
Created on Tue Aug 02 16:19:00 2022

adjust split time series for final read
*this script is particularly used for 
*NEXRAD obtained form SJRWMD

@author: Michael Getachew Tadesse

"""

import os
import pandas as pd 


os.chdir('R:\\40715-013 UKFPLOS\\Received_Data_Models\\FromSJRWMD\\Rainfall\\modified_files')


dat = pd.read_csv('2017_split_time.csv')
print(dat)

dat = dat[['PIXEL', 'date', 'hr_modified', 'mm', 'RAIN_AVG']]
dat.columns = ['pixel', 'date', 'hr', 'mm', 'rain_avg']

print(dat)

dat.to_csv('2017_roundedTime.csv')