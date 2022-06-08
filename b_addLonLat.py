
"""  
Created on Fri Jun 03 21:37:00 2022

add lon and lat to NEXRAD data

@author: Michael Getachew Tadesse
"""

import pandas as pd

geoDat = pd.read_csv("pixel_lon_lat.csv")
geoDat['HYDROID'] = geoDat['HYDROID'].astype(int)

nexDat = ["cfij_dailyNEXRAD", "irma_dailyNEXRAD", 
                    "noname_dailyNEXRAD", "tsfay_dailyNEXRAD"]

for ff in nexDat:
    df = pd.read_csv(ff + ".csv")
    df['pixel'] = df['pixel'].astype(int)
    # print(df)
    
    df['lon'] = 'nan'
    df['lat'] = 'nan'
    
    # get unique pixel IDs
    pixUnq = df['pixel'].unique()
    
    # print("{} / {}".format(count, len(pixUnq)))
    
    for pp in pixUnq:
        # print(geoDat[geoDat['HYDROID'] == pp]['CENTROID_X'].to_numpy()[0])
        
        # get lon/lat
        df.loc[df['pixel'] == pp, "lon"] = \
                geoDat[geoDat['HYDROID'] == pp]['CENTROID_X'].to_numpy()[0]
        df.loc[df['pixel'] == pp, "lat"] = \
                geoDat[geoDat['HYDROID'] == pp]['CENTROID_Y'].to_numpy()[0]
        
        # print(geoDat[geoDat['HYDROID'] == pp]['HYDROID'])

    
    print(df)
    
    df.to_csv(ff + ".LonLat.csv")
        