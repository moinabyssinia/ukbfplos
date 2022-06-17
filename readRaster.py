import numpy as np
import pandas as pd
import rasterio as rio
import matplotlib.pyplot as plt
from rasterio.plot import show
from matplotlib import pyplot


ds = rio.open('rastdif_7p56m_88_ft.tif')
print(ds.count)

arr = ds.read(1)
print(arr)


arr = np.where(((arr < -3.0001) | (arr > 3.0001)), np.nan, arr)

arrDf = pd.DataFrame(arr)
print(arrDf)

plt.hist(arrDf)
plt.ylabel('Number of cells')
plt.xlabel('Difference in DEM in feet')
plt.show()


plt.imshow(arr, cmap = "Greys")

fig, ax = plt.subplots(1,figsize = (10, 6))
image_hidden = ax.imshow(arr, cmap = 'gist_rainbow_r')

image = plt.imshow(arr, cmap = 'gist_rainbow_r')

cbar = plt.colorbar(image)
cbar.set_ticks([-3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5])


# fig.colorbar(image_hidden, ax = ax)
plt.title('Difference in DEMs in feet - both DEMs in NAVD88')
plt.show()

