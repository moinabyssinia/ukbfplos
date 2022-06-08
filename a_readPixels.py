
"""  
Created on Fri Jun 03 16:18:00 2022

read NEXRAD rainfall values

@author: Michael Getachew Tadesse
"""

import pandas as pd


#################
# choose file
#################
fileName = ["cfij", "irma", "noname", "tsfay"]


for ff in fileName:
    print(ff)

    dat = pd.read_csv(ff+".out", header = None)

    date_unq = sorted(dat[0][:-2].unique()) # removing the last two rows
    pixel_unq = sorted(dat[4][:-2].unique())


    print(pd.DataFrame(date_unq))

    # aggregate rainfall into daily format

    # empty dataframe
    pixelDat = pd.DataFrame(columns = ['date', 'pixel', 'value']) 


    # aggregate rainfall data
    count = 1

    for dd in date_unq:
        print("{} / {}".format(count, len(date_unq)))
        for pp in pixel_unq:
            df = dat[(dat[0] == dd) & (dat[4] == pp)]       
            # print(df) 
            rainAgg = sum(df[2][:])
            newDf = pd.DataFrame([dd, pp, rainAgg]).T
            newDf.columns = ['date', 'pixel', 'value']
            pixelDat = pd.concat([pixelDat, newDf], axis = 0)
        # print(pixelDat)

        count += 1
    pixelDat.to_csv(ff + "_dailyNEXRAD.csv")