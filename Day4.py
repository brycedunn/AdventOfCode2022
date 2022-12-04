"""
AOC4
Created on Sun Dec  4 07:33:58 2022

@author: Bryce Dunn
"""
import numpy as np
import pandas as pd
df = pd.read_csv("input4dash.csv", header=None, skip_blank_lines=False)

contained_pairs = 0
overlap_pairs = 0

for i in np.arange(len(df)):
    
    num_rooms1 = 1+(df.iloc[i,1]-df.iloc[i,0])
    num_rooms2 = 1+(df.iloc[i,3]-df.iloc[i,2])
    
    if num_rooms1 > 1:
        elf1 = set(np.arange(df.iloc[i,0],df.iloc[i,1]+1))
    if num_rooms2 > 1:
        elf2 = set(np.arange(df.iloc[i,2],df.iloc[i,3]+1))
        
    if num_rooms1 == 1:
        elf1 = set(df.iloc[i,0].flatten())
    if num_rooms2 == 1:
        elf2 = set(df.iloc[i,2].flatten())
    
    if elf1.issubset(elf2) or elf2.issubset(elf1):
        contained_pairs = contained_pairs+1   
    
    if len(elf1.intersection(elf2)) > 0:
        overlap_pairs = overlap_pairs +1

print("Contained Pairs: ", contained_pairs)    
print("Overlapping Pairs: ",overlap_pairs)


# Part 2

