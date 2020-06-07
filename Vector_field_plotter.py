# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 18:15:33 2020
Plot ship course using dataset csv_clean_reduced_data
Plots sailboat trajectory and vectors fields with true wind velocty and Boat velocty
@author: Rafael
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from math import radians
import os
PATH='C:/Users/Rafael/T-DAB/Robo Boats - General/Data/Jack Trigger/Clean Data reduced/'

##Ensure reproductability of script

np.random.seed(42)

##Read data
dataset0=pd.read_csv(PATH+os.listdir(PATH)[0],
                      delimiter=',',
                      index_col='UT date_UT time',
                      parse_dates=[['UT date', 'UT time']])
plt.figure(figsize=(10,10))
colors=cm.rainbow(np.linspace(0,1, dataset0.shape[0]))

##Location
plt.scatter(dataset0['Longitude'], dataset0['Latitude'], c=colors, label='Ship location')

##Wind vector field
U=(dataset0['TWS']*np.cos(dataset0['TWD'].apply(lambda x: radians(x))))[0:1999:100]
V=(dataset0['TWS']*np.sin(dataset0['TWD'].apply(lambda x: radians(x))))[0:1999:100]
plt.quiver(dataset0['Longitude'][0:1999:100], dataset0['Latitude'][0:1999:100],U, V, angles='xy',
           color='blue', label='Airflow')

##Ship speed vector field
U=(dataset0['Speed_ov_surface']*np.cos(dataset0['Heading_ov_ground'].apply(lambda x: radians(x))))[0:1999:100]
V=(dataset0['Speed_ov_surface']*np.sin(dataset0['Heading_ov_ground'].apply(lambda x: radians(x))))[0:1999:100]
plt.quiver(dataset0['Longitude'][0:1999:100], dataset0['Latitude'][0:1999:100],U, V, angles='xy', color='red', label='Ship Course')
plt.legend(loc='best')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('C:/Users/Rafael/Pictures/vector.jpg')
plt.show()