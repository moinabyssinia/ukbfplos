
"""  
Created on Fri Jun 06 11:29:00 2022

selected events of rainfall events
but every 15 mins

@author: Michael Getachew Tadesse
"""

import os
import pandas as pd

raw = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
        "Documents\\UKLOS\\Data\\Climate\\kissrain\\selected_events"
        
out = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
        "Documents\\UKLOS\\Data\\Climate\\kissrain\\plots_15min\\tsfay"

geoRef = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
                "UKLOS\\Data\\Climate\\kissrain\\daily_accumulated"

os.chdir(raw)

dat = pd.read_csv("tsfay_selected.csv")\
        [['date', 'min', 'value', 'timestep', 'pixelID']]

dat['lon'] = "nan"
dat['lat'] = "nan"

os.chdir(geoRef)
geoDat = pd.read_csv("tsfay_dailyNEXRAD.LonLat.csv")

# get unique pixel IDs
pixUnq = dat['pixelID'].unique()

for pp in pixUnq:
        # print(geoDat[geoDat['HYDROID'] == pp]['CENTROID_X'].to_numpy()[0])
        
        # get lon/lat
        dat.loc[dat['pixelID'] == pp, "lon"] = \
                geoDat[geoDat['pixel'] == pp]['lon'].to_numpy()[0]
        dat.loc[dat['pixelID'] == pp, "lat"] = \
                geoDat[geoDat['pixel'] == pp]['lat'].to_numpy()[0]
                

print(dat)

dat['datID'] = dat['date'].astype(str) + "_"+ dat['min'].astype(str)

print(dat)

os.chdir(out)

dat.to_csv("tsfay_selected_15min.csv")