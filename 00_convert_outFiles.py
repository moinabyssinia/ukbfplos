"""  
Created on Wed Aug 03 10:34:00 2022

convert .out to .csv

@author: Michael Getachew Tadesse

"""

import os
import pandas as pd 


dir_in = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\FromSFWMD\\kissrain"

out = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\FromSFWMD\\"\
        "rainfall_modified_files\\rawData"


os.chdir(dir_in)

nexList = ['irma.out', 'noname.out']

for nn in nexList:
    print(nn)

    os.chdir(dir_in)

    dat = pd.read_csv(nn, header = None, dtype = str)
    print(dat)

    dat = dat.iloc[:-2, :5]

    dat.columns = ['date', 'hhmm', 'value', 'min', 'pixel']
    dat = dat[['date', 'hhmm', 'value', 'pixel']]

    # get string version of hhmm
    getStr  = lambda x: x.split('.0')[0]
    dat['hh_mm'] = pd.DataFrame(list(map(getStr, dat['hhmm'])))


    dat = dat[['date', 'hh_mm', 'value', 'pixel']]
    
    print(dat)

    os.chdir(out)
    dat.to_csv(nn.split('.out')[0] + '.csv')