"""  
Created on Wed Aug 03 15:36:00 2022

find unique pixels that fall within the UKB model domain

@author: Michael Getachew Tadesse

"""

import os
import pandas as pd 
import datetime


dir_in = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\SWFWMD\\rainfall\\"\
                "rawData\\2011"
dir_mesh = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\"\
                "SWFWMD\\rainfall\\rawData"


# get unique values of pixel
os.chdir(dir_mesh)
rain_mesh = pd.read_csv('ukb_rain_mesh.csv')

pixel_unq = rain_mesh['pixel'].unique()


print(pixel_unq)



os.chdir(dir_in)

dat = pd.read_csv("15_min_2011_09_txt.txt", header = None)

dat.columns = ['pixel', 'datetime', 'value']

nn_pix = dat['pixel'].unique()


swf_pix = []

for nn in nn_pix:
    if nn in pixel_unq:
        swf_pix.append(nn)

        print(swf_pix)


swf_pix = pd.DataFrame(swf_pix)

swf_pix.to_csv("swf_unique_pixels.csv")
