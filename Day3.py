"""
Day 3
Created on Sat Dec  3 07:01:26 2022
@author: Bryce Dunn
"""
import numpy as np
import pandas as pd
df = pd.read_csv("AOC3.csv", header=None, skip_blank_lines=False)
# String to store char priorities
priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# A function that will return the shared char between two halves of
# a given string
def ruckcheck(string):
    h = int(len(string)/2) # halfway point
    compartment1 = string[0:h]
    compartment2 = string[h:]
    for i in np.arange(h):
        check = compartment1[i] in compartment2
        if check == True:
            shared_char = compartment1[i]     
    return shared_char

priority_sum = 0

for i in np.arange(len(df)):
    temp = ruckcheck(df.iloc[i][0])
    priority_sum = priority_sum + priorities.find(temp)+1
    
print('The priority sum is: ',priority_sum)

# Part 2

def groupcheck(string1,string2,string3):
        for i in np.arange(len(string1)):
            check1 = string1[i] in string2
            check2 = string1[i] in string3
            if check1 == True and check2 == True:
                badge = string1[i]
        return badge
    
priority_sum2 = 0

for j in range(0,len(df)-2,3):
    s1 = df.iloc[j][0]
    s2 = df.iloc[j+1][0]
    s3 = df.iloc[j+2][0]
    
    temp2 = groupcheck(s1,s2,s3)
    priority_sum2 = priority_sum2 + priorities.find(temp2)+1
    
    
    
print("Group Priority Sum: ",priority_sum2)
