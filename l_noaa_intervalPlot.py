
"""  
Created on Tue Jun 13 09:03:00 2022

plot NOAA interval plots

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

os.chdir("D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
        "Documents\\UKLOS\\Data\\Climate\\kissrain\\3dayAccumulated")

dat = pd.read_csv("max_3day_accu.csv")
print(dat)

sns.set_context('notebook', font_scale = 1.3)

fig = plt.figure(figsize = (10,5))
# plt.fill_between()

plt.axhspan(6.09, 7.81, alpha = 0.45, color = "gray", label = "NOAA 5yr" )
plt.axhspan(7.16, 9.32, alpha = 0.45, color = "cadetblue", label = "NOAA 10yr" )
plt.axhspan(8.7, 12.6, alpha = 0.45, color = "gold", label = "NOAA 25yr" )
plt.axhspan(11, 18.2, alpha = 0.45, color = "violet", label = "NOAA 100yr" )

plt.scatter(dat['Event'], dat['max_3day_accu'], 
                c = "k", marker ='s' , s = 150,
                    edgecolor = 'k')
for i, txt in enumerate(dat['Name']):
    plt.annotate(txt, (dat['Event'][i] - 0.5, dat['max_3day_accu'][i] - 1.0))


# plt.fill_between(dat['event'], dat['max_3day_accu'], where = (dat['max_3day_accu'] > 6.09 ))

plt.ylabel('3 Day Maximum Accumulated Rainfall (in)')
plt.xlabel('Precipitation Events')
plt.title('NOAA Atlas 14 Precipitation (in) Frequency Estimates (at Kissimmee station)')
plt.legend(ncol = 2, fontsize = 15, loc = 'upper left')
plt.show()