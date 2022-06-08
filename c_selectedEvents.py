
"""  
Created on Fri Jun 06 09:38:00 2022

selected events of rainfall events

@author: Michael Getachew Tadesse
"""

import os
import pandas as pd

raw = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
        "Documents\\UKLOS\\Data\\Climate\\kissrain\\rawdata"
        
out = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
        "Documents\\UKLOS\\Data\\Climate\\kissrain\\selected_events"

os.chdir(raw)

dat = pd.read_csv("tsfay.out", header = None)

dat.drop(dat.tail(2).index, inplace = True)

print(dat)

newDat = dat[dat[0] == "08/19/2008"]
print(newDat)


os.chdir(out)
newDat.to_csv("tsfay_selected.csv")