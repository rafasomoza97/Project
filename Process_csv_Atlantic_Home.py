# -*- coding: utf-8 -*-
"""
Created on Sat May 16 12:44:11 2020

@author: Rafael
"""

import os
import pandas as pd
import time
PATH='C:/Users/Rafael/T-DAB/Robo Boats - General/Data/Jack Trigger/Atlantic Home/rapport/'

data=pd.DataFrame(columns=pd.read_csv(PATH+os.listdir(PATH)[0], delimiter=';',encoding="ISO-8859-1").columns)

for filename in os.listdir(PATH):
    day=filename[:10]
    day=day.replace('_', ' ')
    mydateparser = lambda x: pd.datetime.strptime(day+' '+x, "%d %m %Y %H:%M:%S")
    try:
        file=pd.read_csv(PATH+filename, delimiter=';',
                         parse_dates=['Date_Time'],
                         date_parser=mydateparser,
                         index_col=['Date_Time'],
                         encoding = "ISO-8859-1")
        data=data.append(file, ignore_index=False)
    except ValueError:
        pass
    