
"""  
Created on Tue Jun 09 14:32:00 2022

percent difference of NEXRAD and Gage rainfall

@author: Michael Getachew Tadesse
"""
import os
import logging
import datetime
import pandas as pd
import seaborn as sns
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

home = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
    "Documents\\UKLOS\\Data\\Climate\\kissrain\\analysis\\"\
        "comparison_NEX_Gages\\nex_gage_comp"
gages = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
    "Documents\\UKLOS\\Data\\Climate\\kissrain\\analysis\\"\
        "comparison_NEX_Gages\\daily_Gage"
stats = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
    "Documents\\UKLOS\\Data\\Climate\\kissrain\\analysis\\"\
        "comparison_NEX_Gages\\comparison_stats"
geoRef = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
    "Documents\\UKLOS\\Data\\Climate\\kissrain\\analysis\\"\
        "comparison_NEX_Gages\\daily_NEXRAD"

# georeference file
os.chdir(geoRef)
geoDat = pd.read_csv("cfij_dailyNEXRAD.LonLat.csv") 

# get gages list
os.chdir(gages)
gages = os.listdir()

# get nexrad data 
os.chdir(home)
flist = os.listdir()
print(flist)

# empty dataframe
df = pd.DataFrame(columns = ['gage', 'pixel', 'lon', 'lat', 
                                    'event', 'gage_value', 'nex_value','perc_diff'])

eventDat = {
    "2004" : "09/26/2004",
    "2008" : "08/19/2008",
    "2011" : "10/08/2011",
    "2017" : "09/10/2017"
}


for gg in gages:
    # print(gg.split('.csv')[0])
    gname = gg.split('.csv')[0]
    

    os.chdir(home)
    for ff in flist:
        if gname in ff:
            dat = pd.read_csv(ff)
            dat.drop('Unnamed: 0', axis = 1, inplace = True)
            
            dat['date'] = pd.to_datetime(dat['date'])
            dat['lon'] = 'nan'
            dat['lat'] = 'nan'
            dat['perc_diff'] = 'nan'
            
    
            # select only non-nan rows
            dat = dat[~dat['nex_value'].isna()]
            
            if dat['gage_value'].isna().any():
                logging.info('{} missing data in {}'.format(gg, ff)) 
                dat = dat[~dat['gage_value'].isna()]
                
            if dat.empty:
                logging.info('{} empty data {}'.format(gg, ff))
                continue 
            
            # print(dat[['nex_value', 'gage_value']])
            
            # get storm event year
            rainfallEvent = dat['date'].unique()[0].astype(str).split('-')[0]
            # print(rainfallEvent)
    
            # print(eventDat[rainfallEvent])
            # print(dat[dat['date'] == eventDat[rainfallEvent]])
            
            datEvent = dat[dat['date'] == eventDat[rainfallEvent]]
            # print(datEvent)
            
            # gage or nexrad maynot exist
            if datEvent.empty:
                continue
            
            gage = gg.split('.csv')[0]
            pixel = datEvent['pixel'].values[0]
            print(pixel)
            lon = geoDat[geoDat['pixel'] == pixel]['lon'].unique()[0]
            lat = geoDat[geoDat['pixel'] == pixel]['lat'].unique()[0]
            gage_value = datEvent['gage_value'].values[0]
            nex_value = datEvent['nex_value'].values[0]
            
            
            # using the maximum of the percent difference
            perc_diff = max(2*100*(abs(datEvent['gage_value'] - datEvent['nex_value']))/(datEvent['gage_value'] + datEvent['nex_value']))
            # print(perc_diff)
            
            newdf = pd.DataFrame([gage, pixel, lon, lat, 
                                    rainfallEvent, gage_value, nex_value, perc_diff]).T
            newdf.columns = ['gage', 'pixel', 'lon', 'lat', 
                                    'event', 'gage_value', 'nex_value','perc_diff']
            df = pd.concat([df, newdf], axis = 0)
            # print(newdf)
os.chdir(stats)

df.to_csv("nexrad_gages_comparison_percDiff.csv")