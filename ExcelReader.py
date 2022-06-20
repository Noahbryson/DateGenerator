import pandas as pd
import math
import numpy as np
import os

def getSheet(file) :
    # wdir = os.getcwd()
    # filename = 'sam-noah-stl-adventure-goals.xlsx' #name of excel sheet to read in
    # file = wdir + '\\' + filename
    cols = [0,1,2,3]
    activities = pd.read_excel(file, header= 0, usecols=cols)
    keys = list(activities.columns.values)
    cleaned = {}
    for key in keys:
        cleaned[key] = list(activities[key].values)
        holder = [x for x in cleaned[key] if isinstance(x, str)]
        cleaned[key] = holder
    # print(activities, '\n', cleaned)
    return cleaned, keys