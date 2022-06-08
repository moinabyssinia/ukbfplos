
"""  
Created on Tue Jun 07 10:47:00 2022

plot STG FLOW time series

@author: Michael Getachew Tadesse
"""
import os
import datetime
import pandas as pd
import seaborn as sns
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt

home = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
        "Documents\\UKLOS\\Data\\Climate\\kissrain\\stg_flow_gateOp"

year = "2017.csv"
variable = "tailwater"

# variables
var = {
            "headwater" : ['-H', "Headwater (ft)"],
            "tailwater" : ['-T', "Tailwater (ft)"],
            "flow" : ['_F', "Flow (cfs)"]
            }

os.chdir(home)

structures = os.listdir()

sns.set_context("notebook", font_scale=1.0)
fig = plt.figure(figsize = (16, 6))

for ss in structures:
    os.chdir(os.path.join(home, ss))
    
    for ff in os.listdir():
        # print(ff)
        if ff.endswith(year):
            print(ss, ff)
            
            label = ss.upper()+ var[variable][0]
            
            dat = pd.read_csv(ff,header = None)
            
            dat.columns = ['date', 'id', 'dbkey', 'value', 'colx', 'qaqc']
            dat.drop(dat.tail(1).index, inplace = True)
 
            
            dat['date'] = pd.to_datetime(dat['date'], format='%m/%d/%Y %H:%M')
            
            
            df = dat[dat['id'] == label]
            
            if df.empty:
                continue            
            
            plt.plot(df['date'], df['value'], label = label, lw = 2)

            print(df[df['value'] == df['value'].max()])

plt.ylabel(var[variable][1])
plt.title(year.split('.csv')[0] + "Rainfall Event")
plt.legend(ncol = 5, loc = 'lower right', fontsize = 10)
plt.show()
            
        
        
