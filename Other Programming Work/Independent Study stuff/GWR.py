# Load libraries
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from pylab import rcParams
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 72

import seaborn as sns
sns.set_style("darkgrid")
sns.set_context(context="paper", font_scale=1.5, rc=None)
sns.set(font="serif")

import plotly.express as px
import plotly.graph_objects as go

import geopandas as gpd
from geodatasets import get_path

import libpysal as ps
from libpysal  import weights
from libpysal.weights import Queen

import esda
from esda.moran import Moran, Moran_Local

import splot
from splot.esda import moran_scatterplot, plot_moran, lisa_cluster, plot_local_autocorrelation
from splot.libpysal import plot_spatial_weights

from giddy.directional import Rose

import statsmodels.api as sm
import statsmodels.formula.api as smf
from stargazer.stargazer import Stargazer, LineLocation

from spreg import OLS
from spreg import MoranRes
from spreg import ML_Lag
from spreg import ML_Error 

from mgwr.gwr import GWR, MGWR
from mgwr.sel_bw import Sel_BW
from mgwr.utils import shift_colormap, truncate_colormap

import warnings
warnings.filterwarnings('ignore') 
import time

#path_to_Seattledata=get_path("geoda seattle1")
#file1=open("C:/Users/NGong/OneDrive - Eastside Preparatory School/Documents/IS stuff/shapefile_storage/King_County_Tax_Parcel_Centroids_with_select_City_of_Seattle_geographic_overlays_-2100822306719281899.geojson")
#gdf  = gpd.read_file(file1)
#fig, ax = plt.subplots(figsize=(6, 6))
#gdf.plot(color = 'white', edgecolor = 'black', ax = ax)
#ax.set_title('Map of Seattle and centroids', fontsize=12)
#ax.axis("off")
file2=open("C:/Users/NGong/OneDrive - Eastside Preparatory School/Documents/IS stuff/shapefile_storage/2010HousingPerCity.geojson")
gdf1  = gpd.read_file(file2)
fig, ax = plt.subplots(figsize=(6, 6))
gdf1.plot(color = 'white', edgecolor = 'black', ax = ax)
gdf1.centroid.plot(ax=ax)
ax.set_title('Map of Seattle and centroids', fontsize=12)
ax.axis("off")
file3=open("C:/Users/NGong/OneDrive - Eastside Preparatory School/Documents/IS stuff/shapefile_storage/lightrail.geojson")
gdf2  = gpd.read_file(file3)
fig, ax = plt.subplots(figsize=(6, 6))
gdf2.plot(color = 'white', edgecolor = 'black', ax = ax)
ax.set_title('Map of Seattle and centroids', fontsize=12)
ax.axis("off")
#plt.savefig('myMap.png',dpi=150, bbox_inches='tight')
plt.show()
fig, ax = plt.subplots(figsize=(6, 6))

gdf.plot(column='PctBach', cmap = 'coolwarm', linewidth=0.01, scheme = 'FisherJenks', k=5, legend=True, legend_kwds={'bbox_to_anchor':(1.10, 0.96)},  ax=ax)
#gdf.plot(column='PctBach', cmap = 'coolwarm', linewidth=0.01, scheme = 'box_plot', k=5, legend=True, legend_kwds={'bbox_to_anchor':(1.10, 0.96)},  ax=ax)
ax.set_title('Population with BA degree (%)', fontsize=12)
ax.axis("off")
#plt.savefig('myMap.png',dpi=150, bbox_inches='tight')
plt.show()
y = gdf['PctBach'].values.reshape((-1,1)) # reshape is needed to have column array
y.shape
X = gdf[['PctFB', 'PctBlack', 'PctRural']].values
X.shape
u = gdf['X']
v = gdf['Y']
coords = list(zip(u,v))

gwr_selector = Sel_BW(coords, y, X)
gwr_bw = gwr_selector.search()
gwr_results = GWR(coords, y, X, gwr_bw).fit()
gwr_results.summary()