"""  
Created on Wed Aug 03 17:42:00 2022

create dfs0 files

@author: Michael Getachew Tadesse

"""

import os
import pandas as pd 
import datetime
import mikeio
from mikeio.eum import ItemInfo, EUMType, EUMUnit
from mikecore.DfsFile import DataValueType

dir_in = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\FromSJRWMD\\Rainfall\\"\
                "modified_files\\pixel_rainfall_distributed\\2017"
dir_out = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\FromSJRWMD\\Rainfall\\"\
                "modified_files\\pixel_rainfall_distributed\\2017_dfs0"


os.chdir(dir_in)

pixList = os.listdir()

for pp in pixList:
    print(pp)

    os.chdir(dir_in)

    df = pd.read_csv(pp, parse_dates=True, 
                index_col='datetime', na_values=-99.99)
    df = df[['distributed_rain']]

    item = ItemInfo(EUMType.Rainfall, EUMUnit.inch, data_value_type = DataValueType.StepAccumulated)

    da = mikeio.DataArray(df['distributed_rain'], time = df.index, item = item)

    ds = mikeio.Dataset([da])

    os.chdir(dir_out)

    ds.to_dfs(pp.split('.csv')[0] + ".dfs0")