
"""  
Created on Tue Jun 07 16:14:00 2022

compute intensity - for hourly accumulated rainfall

@author: Michael Getachew Tadesse
"""
import os
import datetime
import pandas as pd
import seaborn as sns
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt

home = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
        "Documents\\UKLOS\\Data\\Climate\\kissrain\\selected_events"
os.chdir(home)

fname = "tsfay_selected.csv"

dat = pd.read_csv(fname)

# get unique pixels
pixelUnq = dat['pixelID'].unique()
# print(pixelUnq)

# empty dataframe
df = pd.DataFrame(columns = ['date', 'min', 'value', 'pixelID'])


for pp in pixelUnq:
    print(pp) 

    newDf = dat[dat['pixelID'] == pp][['date', 'min', 'value', 'pixelID']]
    
    hour_count = 100
    prev_count = 0
    
    while hour_count <= 2300:
                
        newDf_sub = newDf[(newDf['min'] > prev_count) & (newDf['min'] <= hour_count)]
        newDf_sub.reset_index(inplace = True)
        
        # print(newDf_sub)   
        
        if newDf_sub.empty:
            prev_count = hour_count
            hour_count += 100
            continue

        hr_agg = pd.DataFrame([newDf_sub['date'][0], hour_count, 
                    sum(newDf_sub['value']), newDf_sub['pixelID'][0]]).T
        hr_agg.columns = ['date', 'min', 'value', 'pixelID']
        # print(hr_agg)
        
        df = pd.concat([df, hr_agg], axis = 0)
        
        prev_count = hour_count
        
        hour_count += 100
    
    print(df)

df.to_csv(fname.split(".csv")[0] + "_hr_agg.csv")
        