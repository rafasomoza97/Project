# -*- coding: utf-8 -*-
"""
Created on Sat May 16 10:40:49 2020
Objective: read Clean Reduced Data and preprocess
@author: Rafael
"""

import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import normalize ##For L2 normalization
from tensorflow.keras import Input
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Conv2D
from math import radians
PATH='C:/Users/Rafael/T-DAB/Robo Boats - General/Data/Jack Trigger/Clean Data reduced/'
##Ensure reproductability of script

np.random.seed(42)

##Read data
dataset0=pd.read_csv(PATH+os.listdir(PATH)[0],
                      delimiter=',',
                      index_col='UT date_UT time',
                      parse_dates=[['UT date', 'UT time']])
dataset1=pd.read_csv(PATH+os.listdir(PATH)[1],
                      delimiter=',', 
                      index_col='Date_Time',
                      parse_dates=[['Date', 'Time']])
##Drop of redundant variables
dataset0.drop(['Unnamed: 0.1', 'Unnamed: 0', 'local date', 'local time'], axis=1, inplace=True)
dataset1.drop(['Unnamed: 0'], axis=1, inplace=True)
##Pass str data to boolean and float

dataset0['under sails']=dataset0['under sails'].map({'yes': True, 'no': False})

def str_percentage_to_float(tide):
    assert type(tide) == str
    if tide[-1]=='%':        
        return float(tide[:-1])/100
    else:
        return TypeError("str final character must be '%' ")
    
dataset0['pc_tide']=dataset0['pc_tide'].apply(lambda x: str_percentage_to_float(x))
# adrena_path='C:/Users/Rafael/T-DAB/Robo Boats - General/Data/Jack Trigger/Clean Data/RDR_nkz_1.csv'
# adrena_dataset=pd.read_csv(adrena_path,
#                            delimiter=',',
#                             index_col=0,
#                             parse_dates=[['Date','Time']])
# # adrena_dataset.drop(['Unnamed: 0','local date', 'local time'], axis=1, inplace=True)
# # adrena_dataset['under sails']=adrena_dataset['under sails'].map({'yes': True, 'no': False})
# adrena_red=adrena_dataset.head(100)

##Normalize velocities
speed=['AWS','TWS','VMG', 'Speed_ov_ground', 'Atlas current speed', 'Current_speed', 'Speed_ov_surface']
dataset0[speed]=dataset0[speed].apply(lambda x: x/np.max(x),raw=True)

##Normalize angle
angle=['AWA', 'TWD','Heading_True', 'Heading_ov_ground', 'Atlas current direction', 'Current_direction']
dataset0[angle]=dataset0[angle].apply(lambda x: radians(x)/(2*np.pi), raw=True)