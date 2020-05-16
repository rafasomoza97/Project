# -*- coding: utf-8 -*-
"""
Created on Sat May 16 10:40:49 2020
Objective: read Clean Reduced Data and preprocess
@author: Rafael
"""

import os
import pandas as pd

PATH='C:/Users/Rafael/T-DAB/Robo Boats - General/Data/Jack Trigger/Clean Data reduced/'

dataset0=pd.read_csv(PATH+os.listdir(PATH)[0],
                     delimiter=',',
                      index_col='Unnamed: 0',
                     parse_dates=[['UT date', 'UT time']])
dataset1=pd.read_csv(PATH+os.listdir(PATH)[1],
                     delimiter=',', 
                     index_col='Unnamed: 0',
                     parse_dates=[['Date', 'Time']])
##Drop of redunant variables
dataset0.drop(['Unnamed: 0.1', 'local date', 'local time'], axis=1, inplace=True)

##Pass str data to boolean and float

dataset0['under sails']=dataset0['under sails'].map({'yes': True, 'no': False})

def str_percentage_to_float(tide):
    assert type(tide) == str
    if tide[-1]=='%':
        y=float(tide[:-1])/100
    return y
dataset0['pc_tide']=dataset0['pc_tide'].apply(lambda x: str_percentage_to_float(x))