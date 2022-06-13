
"""  
Created on Tue Jun 10 09:52:00 2022

percent difference of NEXRAD and Gage rainfall
for breakpoint data

using the resample function to sum from top to bottom

removing rows with 0 values of either gages/nexrad

@author: Michael Getachew Tadesse
"""
import os
import logging
import datetime
import numpy
import pandas as pd
import seaborn as sns
import matplotlib.colors as mcolors
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

nex = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
    "Documents\\UKLOS\\Data\\Climate\\kissrain\\rawdata"
gages = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
    "Documents\\UKLOS\\Data\\Climate\\kissrain\\analysis\\"\
        "comparison_NEX_Gages\\breakpoint"
stats = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
    "Documents\\UKLOS\\Data\\Climate\\kissrain\\analysis\\"\
        "comparison_NEX_Gages\\comparison_stats"
bk_stats = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
    "Documents\\UKLOS\\Data\\Climate\\kissrain\\analysis\\"\
        "comparison_NEX_Gages\\comparison_stats\\breakpoint"
geoRef = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
    "Documents\\UKLOS\\Data\\Climate\\kissrain\\analysis\\"\
        "comparison_NEX_Gages\\daily_NEXRAD"

# get names of gages
os.chdir(stats)
geoDat = pd.read_csv("nexrad_gages_comparison_percDiff.csv") 

getName = lambda x: x.split('_')[0]
geoDat['name'] = pd.DataFrame(list(map(getName, geoDat['gage'])))
# get unique names
gageUnq = geoDat['name'].unique()

# print(gageUnq)


# get list of BK gages
os.chdir(gages)
gList = os.listdir()

# nex data dictionary
nex_dict = { "2004" : ["cfij.out", "09/25/2004", "09/27/2004"], 
            "2008" : ["tsfay.out", "08/18/2008", "08/20/2008"], 
            "2011" : ["noname.out", "10/07/2011", "10/09/2011"], 
            "2017" : ["irma.out", "09/09/2017", "09/11/2017"] }

for gg in gageUnq:
    print(gg)
    
    for bk_gg in gList:
        if gg in bk_gg:
            
            os.chdir(gages)
            
            # print(gg, bk_gg)
            
            # get year
            y1 = bk_gg.split('.csv')[0].split('_')
            y2 = y1[len(y1) - 1]
            # print(y2)

            dat = pd.read_csv(bk_gg, header = None)[[0, 1, 2, 3]]
            dat.drop(dat.tail(1).index, inplace = True)
            dat.columns = ['date', 'station', 'dbkey', 'gage_value']
            dat['date'] = pd.to_datetime(dat['date'])
            dat = dat.sort_values(by = 'date')
            
            # # save raw data
            # os.chdir(bk_stats)
            # dat.to_csv(gg + y2 + "_gage.csv")
            
            # aggregate data every 15 min
            dat.set_index('date', inplace = True)
            # gage_agg_15m = dat.groupby(pd.Grouper(freq='15Min')).aggregate(numpy.sum)
            gage_agg_15m = dat.resample('15T', label = 'right',
                                        closed = 'right').sum()
            
            
            # os.chdir(bk_stats)
            # gage_agg_15m.to_csv(gg + y2 + "_gage15m.csv")
            # print(dat)
            
            
            # get corresponding nex data
            os.chdir(nex)
            df = pd.read_csv(nex_dict[y2][0], header = None)
            df.drop(df.tail(2).index, inplace = True)
            # print(df)
            
            # get corresponding nex pixel
            pixel = geoDat[geoDat['name'] == gg]['pixel'].unique()[0]
   
            # subset nex data
            nex_data = df[(df[4] == pixel) & 
                            (df[0] >= nex_dict[y2][1]) 
                                & (df[0] <= nex_dict[y2][2])][[0, 1, 4, 2]]
            nex_data.columns = ['day', 'time', 'pixel', 'nex_value']
            
            nex_data.reset_index(inplace = True)
            # print(nex_data)
            # print(dat)
            
            
            # combine day and time for nex data")
            getStr = lambda x: int(x)
            nex_data['time'] = pd.DataFrame(list(map(getStr, nex_data['time'])))

            
            nex_data['date'] = nex_data['day'] + " " + nex_data['time'].astype(str)
            nex_data['date'] = pd.to_datetime(nex_data['date'], format = "%m/%d/%Y %H%M")
            nex_data = nex_data[['date', 'pixel', 'nex_value']]
            nex_data = nex_data.sort_values(by = 'date')
            
            # os.chdir(bk_stats)
            # nex_data.to_csv(gg + y2 + "_nex.csv")
            
            # aggregate data every 15 min
            nex_data.set_index('date', inplace = True)
            # nex_agg_15m = nex_data.groupby(pd.Grouper(freq='15Min')).aggregate(numpy.sum)
            nex_agg_15m = nex_data.resample('15T', label = 'right',
                                closed = 'right').sum()
                        
            # os.chdir(bk_stats)
            # nex_agg_15m.to_csv(gg + y2 + "_nex15m.csv")
            
            
            # set index for plotting
            gage_agg_15m.reset_index(inplace = True)
            nex_agg_15m.reset_index(inplace = True)
            
            # merge nexrad and gage data
            datMerged = pd.merge(gage_agg_15m, nex_agg_15m, on = 'date', how = 'outer')

            # using the maximum of the percent difference
            datMerged['perc_diff'] = 2*100*(datMerged['gage_value'] - 
                                datMerged['nex_value'])/(datMerged['gage_value'] 
                                                + datMerged['nex_value'])
            # print(datMerged)
            
            # remove 0s and NaNs
            datMerged = datMerged[ ~( (datMerged['gage_value'].isna()) 
                                  | (datMerged['nex_value'].isna())  
                                  | (datMerged['gage_value'] == 0)
                                  | (datMerged['nex_value'] == 0)
                                                 ) ]
            datMerged.reset_index(inplace = True)
            
            print(datMerged[datMerged['perc_diff'] == max(datMerged['perc_diff'])])
            
            
            # datMerged.to_csv(gg + y2 + "_merged15m.csv")
            
            fig, axes = plt.subplots(2, 1, figsize = (16,8))
            # fig = plt.figure(figsize = (16,8))
            axes[0].plot(datMerged['date'], datMerged['gage_value'], label = gg, c = "blue")
            axes[0].plot(datMerged['date'], datMerged['nex_value'], label = pixel, c = "red")
            axes[0].set_title(gg + " " + y2 + " Rainfall Event")
            # reduce number of plot ticks
            axes[1].set_xlim([datMerged['date'][0], datMerged['date'][len(datMerged) - 1]])
            axes[0].xaxis.set_major_locator(mdates.HourLocator(interval=12))
            axes[0].set_ylabel('Breakpoint Rainfall (in)')
            axes[0].grid()
            axes[0].legend()
            
            axes[1].plot(datMerged['date'], datMerged['perc_diff'], c = "k")
            # reduce number of plot ticks
            axes[1].set_xlim([datMerged['date'][0], datMerged['date'][len(datMerged) - 1]])
            axes[1].xaxis.set_major_locator(mdates.HourLocator(interval=12))
            axes[1].set_ylabel('Percent Difference')
            axes[1].grid()
            # plt.show()
            
            # plt.savefig(gg + "_" + y2 + ".jpeg", dpi = 400)
