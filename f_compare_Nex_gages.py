"""  
Created on Tue Jun 08 14:43:00 2022

compare NEXRAD and Gage rainfall data

@author: Michael Getachew Tadesse
"""
import os
import datetime
import pandas as pd
import seaborn as sns
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt

home = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
    "Documents\\UKLOS\\Data\\Climate\\kissrain\\analysis\\"\
        "comparison_NEX_Gages"
gages = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
    "Documents\\UKLOS\\Data\\Climate\\kissrain\\analysis\\"\
        "comparison_NEX_Gages\\daily_Gage"
nexrad = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
    "Documents\\UKLOS\\Data\\Climate\\kissrain\\analysis\\"\
        "comparison_NEX_Gages\\daily_NEXRAD"
out = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
    "Documents\\UKLOS\\Data\\Climate\\kissrain\\analysis\\"\
        "comparison_NEX_Gages\\nex_gage_comp"


os.chdir(home)

gage_nex = pd.read_csv("cal_vald_gages_data_v3.csv")

os.chdir(gages)

flist = os.listdir()

for ff in flist:
    os.chdir(gages)
    # print(ff)
    dat = pd.read_csv(ff)
    
    station_id = dat['Station'].unique()[0] + "_" + str(dat['DBKEY'].unique()[0])
    print(station_id)
    
    dat['date'] = pd.to_datetime(dat['Daily Date'])
    
    dat = dat[['date', 'Station', 'DBKEY', 'Data Value']]
    dat.columns = ['date', 'Station', 'DBKEY', 'gage_value']
    
    # find closest NEXRAD pixel
    nex_closest = gage_nex[gage_nex['station'] == 
                            station_id]['closest_NEX_pixel'].values[0]
    print(ff, nex_closest)
    
    # get nexrad data
    os.chdir(nexrad)
    nexList = os.listdir()
    
    for nex in nexList:
        os.chdir(nexrad)
        
        print(ff, nex)
        df = pd.read_csv(nex)
        df = df[df['pixel'] == nex_closest]
        
        print(df)
        
        df['date'] = pd.to_datetime(df['date'])
        df = df[['date', 'pixel', 'value']]
        df.columns = ['date', 'pixel', 'nex_value']   
        
        # merge nex and gages
        dfMerged = pd.merge(dat, df, on = 'date', how = 'outer')
        # print(dfMerged)
    
        os.chdir(out)
        dfMerged.to_csv(ff.split('.csv')[0] + "_" + nex)