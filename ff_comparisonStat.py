
"""  
Created on Tue Jun 09 11:47:00 2022

stats on comparison of NEXRAD and Gage rainfall

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

# start logging
os.chdir(stats)
logging.basicConfig(filename='analysis.log', encoding='utf-8', level=logging.DEBUG)

# empty dataframe
df = pd.DataFrame(columns = ['gage', 'pixel', 'lon', 'lat', 
                                    'event','corr', 'rmse', 'perc_diff'])

for gg in gages:
    # print(gg.split('.csv')[0])
    gname = gg.split('.csv')[0]
    

    os.chdir(home)
    for ff in flist:
        if gname in ff:
            dat = pd.read_csv(ff)
            
            
            dat['date'] = pd.to_datetime(dat['date'])
            dat['lon'] = 'nan'
            dat['lat'] = 'nan'
            dat['corr'] = 'nan'
            dat['rmse'] = 'nan'
            dat['perc_diff'] = 'nan'
            
    
            # select only non-nan rows
            dat = dat[~dat['nex_value'].isna()]
            
            if dat['gage_value'].isna().any():
                logging.info('{} missing data in {}'.format(gg, ff)) 
                dat = dat[~dat['gage_value'].isna()]
                
            if dat.empty:
                logging.info('{} empty data {}'.format(gg, ff))
                continue 
            
            print(dat[['nex_value', 'gage_value']])
            
            # get storm event year
            rainfallEvent = dat['date'].unique()[0].astype(str).split('-')[0]
            
            gage = gg.split('.csv')[0]
            pixel = dat['pixel'].unique()[0]
            lon = geoDat[geoDat['pixel'] == pixel]['lon'].unique()[0]
            lat = geoDat[geoDat['pixel'] == pixel]['lat'].unique()[0]
            corr = dat['gage_value'].corr(dat['nex_value'])
            rmse = mean_squared_error(dat['gage_value'], dat['nex_value'])
            
            # using the maximum of the percent difference
            perc_diff = max(2*100*(abs(dat['gage_value'] - \
                    dat['nex_value']))/(dat['gage_value'] + dat['nex_value']))
            # print(perc_diff)
            
            newdf = pd.DataFrame([gage, pixel, lon, lat, 
                                    rainfallEvent, corr, rmse, perc_diff]).T
            newdf.columns = ['gage', 'pixel', 'lon', 'lat', 
                                    'event','corr', 'rmse', 'perc_diff']
            df = pd.concat([df, newdf], axis = 0)
            # print(newdf)
os.chdir(stats)

df.to_csv("nexrad_gages_comparison.csv")