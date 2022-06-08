
"""  
Created on Wed Jun 01 14:47:00 2022

check NEXRAD pixels - get unique values

@author: Michael Getachew Tadesse
"""

import pandas as pd

cfij = pd.read_csv("cfij.out", header = None)

print(cfij)

print(cfij[4].unique())

unq = pd.DataFrame(cfij[4].unique())
unq.to_csv("cfij_unqPixels.csv")