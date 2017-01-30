# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 14:13:40 2017

@author: Andrea
"""

''' Importing the libraries needed to analyse data '''
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
import numpy as np
import py

# Import data from text file and save it in a Data Frame:
main_df = pd.read_table(py._path.local.LocalPath() + '\electric.txt', \
    delim_whitespace = True, header = 1, index_col = None, \
    names = ['City','Grade','PretestTreat','PosttestTreat','PretestControl',\
        'PosttestControl','Dummy'], warn_bad_lines = True)

# Remove last line of data - request of excercise:
main_df = main_df[:len(main_df)-1]
        
# Show description of the DataFrame
print("Columns: " + str(main_df.columns))
print("Number of rows: " + str(len(main_df)))
print("Number of columns: " + str(len(main_df.columns)))

# Show first 2 lines in data frame
print('\n', main_df.loc[1:2])

# Last column "Dummy" is not used for the porpose of the analysis, and then it
# is dropped:
main_df = main_df.drop('Dummy', axis=1)

# Set "Grade" as a categorical variable:
main_df.Grade = main_df["Grade"].astype('category')

# Summarise statistics for test scores independently from City and Grade
score_label = ["PretestTreat", "PosttestTreat","PretestControl",\
"PosttestControl"] 
summary_total = main_df[score_label].describe()
print('\n', summary_total) 
print('\n')

# Summarise statisticsof test scores grouped by City and Grade:
#summary_city = main_df[["PretestTreat","PosttestTreat"]].groupby(by = "City").describe() 
summary_city = main_df.groupby(by = "City")
print(summary_city[score_label].describe())

summary_grade = main_df.groupby(by = "Grade")
print(summary_grade[score_label].describe())

#plt.figure(1)
#pd.DataFrame.hist(main_df, column = ['PretestTreat',], alpha = 0.5, by = ['Grade'])
main_df[['Grade','PretestTreat','PretestControl']].hist(orientation = 'vertical', \
            normed = True, alpha = 0.5, by = ['Grade'], \
            label = ['Treated Class', 'Control Class'])
plt.suptitle('Pretest Score by Grade')
plt.xlabel('Score')
plt.ylabel('Probability Density')
#plt.legend('Treated Class','Control Class')

# Plotting the distributions of test scores by grade:
#main_df.plot.hist(n)