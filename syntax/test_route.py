import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
from folium.features import GeoJson
import rasterio as rio
import rasterstats 
from shapely.geometry import Polygon, mapping, LineString
from geopy.distance import geodesic
import branca.colormap as cm

from route import *

shapefile = '../data/six_routes.shp'
route = 40
rasterfile = '../data/seattle_dtm.tif'
num_list = [48, 50, 75, 7, 45, 40]

def test_ss():
    m1, m2, m3, m4 = ss(shapefile, route, rasterfile)
    assert m1 == 0.03298497802659699
    assert m2 == 0.021674668871738113
    
    return
    
def test_stress_cal():
    temp = stress_cal(shapefile, num_list, rasterfile)
    assert type(temp) == pd.core.frame.DataFrame
    assert temp.iloc[0,1] == 0.06851640551856875
    
    return
    