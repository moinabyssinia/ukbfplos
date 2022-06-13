
"""  
Created on Tue Jun 10 12:13:00 2022

aggregate gage and nexrad data
every 15 min

@author: Michael Getachew Tadesse
"""
import os
import logging
import datetime
import numpy
import pandas as pd
import seaborn as sns
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error


home = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
    "Documents\\UKLOS\\Data\\Climate\\kissrain\\analysis\\"\
        "comparison_NEX_Gages\\comparison_stats\\breakpoint"
geoRef = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
    "Documents\\UKLOS\\Data\\Climate\\kissrain\\analysis\\"\
        "comparison_NEX_Gages\\daily_NEXRAD"
        

os.chdir(home)

dat = pd.read_csv("ALL2R2004_gage.csv")
dat.drop('Unnamed: 0', axis = 1, inplace = True)
dat['date'] = pd.to_datetime(dat['date'])
dat.set_index('date', inplace = True)
print(dat)

agg_15m = dat.groupby(pd.Grouper(freq='15Min')).aggregate(numpy.sum)

print(agg_15m)

agg_15m.to_csv("ALL2R_agg15m.csv")