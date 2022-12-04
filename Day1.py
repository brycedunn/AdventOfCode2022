"""
Advent of Code Day 1
Created on Fri Dec  2 18:02:21 2022

@author: Bryce Dunn
"""
import numpy as np
import pandas as pd

# import csv as data frame
df = pd.read_csv("AOC1.csv", header=None, skip_blank_lines=False)

# concatenate a NaN row to the end of the data frame
nan = pd.DataFrame([np.nan])
df = pd.concat([df,nan],ignore_index=True)

# count number of NaNs to determine number of elves
number_of_nans = df.isnull().sum()
n = number_of_nans[0]

# Part 1
# initialize calorie counter
calorie_counter = np.zeros(n)

j = 0
calories = 0
for i in np.arange(len(df)):
    test = df.iloc[i].isnull()[0]
    if test == False:
        calories = df.iloc[i][0] + calories
    if test == True:
        calorie_counter[j]=calories
        j = j + 1
        calories = 0
        
print("Most total calories: ",calorie_counter.max())

# Part 2

sort = sorted(calorie_counter)
top3 = sort[-1]+sort[-2]+sort[-3]
"""
sort = df.sort_values(by=0,ascending=False,ignore_index=True)
top3 = sort.iloc[0][0] + sort.iloc[1][0] + sort.iloc[2][0]
"""
print("Total Calories Carried by Top 3 Elves: ", top3)
