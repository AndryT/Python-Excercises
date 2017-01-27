# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 14:13:40 2017

@author: Andrea
"""

''' Importing the libraries needed to analyse data '''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import py

# Import data from text file and save it in a Data Frame:
main_df = pd.read_table(py._path.local.LocalPath() + '\electric.txt', \
    delim_whitespace = True, header = 0, index_col = None, \
    names = ['City','Grade','PretestTreat','PosttestTreat','PretestControl',\
        'PosttestControl','Dummy'], warn_bad_lines = True)
print(main_df.loc[1:2])
