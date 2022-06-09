
"""  
Created on Tue Jun 08 16:00:00 2022

plot comparisons

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
        "comparison_NEX_Gages\\nex_gage_comp"
gages = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
    "Documents\\UKLOS\\Data\\Climate\\kissrain\\analysis\\"\
        "comparison_NEX_Gages\\daily_Gage"
    
os.chdir(gages)
gages = os.listdir()


os.chdir(home)

flist = os.listdir()
print(flist)


for gg in gages:
    print(gg.split('.csv')[0])
    gname = gg.split('.csv')[0]
    
    fig, axes = plt.subplots(2, 2, figsize = (15,7))   
    fig.patch.set_edgecolor('black')
    fig.patch.set_linewidth('2')
    
    i = 0
    j = 0
    os.chdir(home)
    for ff in flist:
        if gname in ff:
            dat = pd.read_csv(ff)
            
            
            dat['date'] = pd.to_datetime(dat['date'])
    
            
            dat = dat[~dat['nex_value'].isna()] 
            
            rainfallEvent = dat['date'].unique()[0].astype(str).split('-')[0]
            
            print(dat)
            
            axes[i,j].plot(dat['date'], dat['gage_value'], c = 'blue', 
                        label = ff.split("_")[0], lw = 2.5)
            axes[i,j].plot(dat['date'], dat['nex_value'], '--', c = 'red', 
                        label = int(dat['pixel'].unique()[0]), lw = 2)
            axes[i,j].legend()
            axes[i,j].set_title(rainfallEvent + " Rainfall Event")
            axes[i,j].set_ylabel('Daily Accumulated Rainfall (in)')
            
            # reduce number of plot ticks
            axes[i,j].xaxis.set_major_locator(plt.MaxNLocator(4))
            
            # adjust panel counters
            
            if j == 1:
                j = 0
                i += 1
            else:
                j += 1
    # plt.show()
    plt.savefig(gg + ".jpeg", dpi = 400)
    