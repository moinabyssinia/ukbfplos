
"""  
Created on Tue Jun 09 09:00:00 2022

get three day rainfall depth

@author: Michael Getachew Tadesse
"""
import os
import datetime
import pandas as pd
import seaborn as sns
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt

home = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
    "Documents\\UKLOS\\Data\\Climate\\kissrain\\daily_accumulated"
threeDay = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
    "Documents\\UKLOS\\Data\\Climate\\kissrain\\3dayAccumulated"
    
os.chdir(home)

storm = "tsfay_dailyNEXRAD.LonLat.csv"
start = "08/18/2008"
end = "08/20/2008"

dat = pd.read_csv(storm)[['date', 'pixel', 'value', 'lon', 'lat']]
dat = dat[(dat['date'] >= start) & (dat['date'] <= end)]
# print(dat)

# get unique pixels
unqPixels = dat['pixel'].unique()
# print(unqPixels)


# empty dataframe
dat_3day = pd.DataFrame(columns = ['pixel','value', 'lon', 'lat'])

for pp in unqPixels:
    df = dat[dat['pixel'] == pp]
    # print(df)
    
    newdf = pd.DataFrame([df['pixel'].unique()[0], 
                          sum(df['value']), df['lon'].unique()[0], 
                                df['lat'].unique()[0]]).T
    
    newdf.columns = ['pixel','value', 'lon', 'lat']
    
    dat_3day = pd.concat([dat_3day, newdf], axis = 0)

print(dat_3day)

os.chdir(threeDay)

saveName = storm.split('dailyNEXRAD.LonLat.csv')[0] + \
    "_".join(start.split('/')) + "_" + '_'.join(end.split('/')) + ".csv"
print(saveName)
dat_3day.to_csv(saveName)

