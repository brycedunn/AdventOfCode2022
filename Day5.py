# -*- coding: utf-8 -*-
"""
AOC Day 5
Created on Mon Dec  5 09:15:49 2022

@author: bryce dunn
"""
import pandas as pd
import numpy as np

df = pd.read_csv('input5.csv',header=None,)
stack = pd.read_csv('input5_boxconfig.csv',header=None,skip_blank_lines=False)
stack = stack.iloc[::-1].reset_index(drop=True)
stack = stack.drop([0,0])

# Let's get some 0 array indexing
df.iloc[:,3]=df.iloc[:,3]-1
df.iloc[:,5]=df.iloc[:,5]-1

# Concatenate a whole mess of NaN rows
nan = pd.DataFrame([np.nan])
for i in np.arange(40):
    stack = pd.concat([stack,nan],ignore_index=True)

def isNaN(num):
    return num != num

def detect_top_crate(stack,stack_num):
    if isNaN(stack.iloc[0,stack_num]) == True:
        top_crate = np.nan
        level = 0
       # print("Empty Col Detected!")
    test = isNaN(stack.iloc[:,stack_num])
    for i in np.arange(len(test)):
        if test[i] == False:
            level = i
            top_crate = stack.iloc[level,stack_num]   
    return top_crate, level

def move_crate(df,f,t):
    top_crate_from, top_level_from = detect_top_crate(df,f)
    top_crate_to, top_level_to = detect_top_crate(df,t)
    df.iloc[top_level_to+1,t] = df.iloc[top_level_from,f]
    df.iloc[top_level_from,f] = np.nan          
    return df

def word(df): # word up, homie
    word = ['']*9
    levels = ['']*9
    for i in np.arange(9):
        word[i],levels[i] = detect_top_crate(df, i)
    return word
 

for j in np.arange(len(df)):
    for k in np.arange(df.iloc[j,1]):
        move_crate(stack,df.iloc[j,3],df.iloc[j,5])

print("Top Crate Phrase:",word(stack))

# Part 2

def move_crates9001(stack,m,f,t):
    top_crate_from, top_level_from = detect_top_crate(stack,f)
    if m == 1:
        move_crate(stack,f,t)
    else:
        if top_crate_from == np.nan:
            return
        else:
            if m > top_level_from:
                m = top_level_from
            else:
                    m = m    
            for k in np.arange(m):
                move_crate(stack,f,9)
        
            for l in np.arange(m):
                move_crate(stack,9,t)

stack2 = pd.read_csv('input5_boxconfig.csv',header=None,skip_blank_lines=False)
stack2 = stack2.iloc[::-1].reset_index(drop=True)
stack2 = stack2.drop([0,0])
stack2['new'] = np.nan

for i in np.arange(40):
    stack2 = pd.concat([stack2,nan],ignore_index=True)

for j2 in np.arange(len(df)):
    move_crates9001(stack2,df.iloc[j2,1],df.iloc[j2,3],df.iloc[j2,5])

print("New Top Crate Phrase: ",word(stack2))











"""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠴⡶⠶⢒⡒⠶⠤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠛⠁⠀⠀⠀⠀⠀⠁⠀⠀⠙⠋⠑⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢓⣺⣮⣧⡀⠀⠀⠀⠀⠀⠀  ⠀⢠⣾⡗⣆⠀
⣰⡿⣿⣿⣄⠀⠀⠀⠀⠀⠀⣰⣯⣿⣿⣷⣶⣤⣤⡀⠀⠀⠀⠀⠀⣤⣶⣾⣿⢿⡿⢿⣷⡄⠀⠀⠀⠀⠀⣰⢿⣿⡿⠈⡇
⣿⣲⣼⣿⣿⣦⡀⠀⠀⠀⢠⡿⠋⠉⠁⠉⠉⠉⠙⢻⡀⠀⠀⠀⣰⠋⠉⠀⠀⠀⠀⠀⠹⣿⡄⠀⠀⣠⠞⠛⣪⣟⣧⣶⠟
⠙⠛⠻⠿⠷⣦⣉⡓⢦⣴⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⣴⣿⣠⣶⡶⠤⠀⠀⠀⢀⣿⣟⣷⣿⣧⠴⠋⠉⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⢻⡄⠙⠀⠀⠀⣠⣤⣤⣦⣤⣵⡂⠀⠀⠀⢸⣿⣿⣯⣴⣿⣷⠾⣿⣬⣿⣿⣾⡿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠈⠙⠿⠤⣿⣿⣷⡿⠋⠀⠀⠀⠀⠉⢻⡿⠾⠿⣿⣷⠿⠟⠋⠈⠈⢷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠀⠀⠀⠉⠛⠛⠉⡁⠀⠀⠀⠀⠀⠀⠀⠈⢿⡶⣤⡀⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⣠⣞⣀⣀⡀⠀⠀⠀⠀⢀⣠⣿⣷⣾⣷⣄⣀⡀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⣠⣶⠾⠋⠈⠙⠛⠛⠻⠶⣿⣿⣿⣿⣿⣿⡿⠿⠿⣉⠛⢷⠀⢠⠐⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⣼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⢀⣤⣿⣷⠘⡇⠀⠸⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠘⠁⠠⢴⣤⣄⣀⣠⣤⣤⣤⣤⣤⣤⣤⣴⣶⣶⣾⣿⣿⣿⢿⡄⢿⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠈⠙⢿⣉⢹⡏⢻⡟⠉⠛⡟⠉⢹⣇⣽⣿⣿⠟⣡⣿⣧⣿⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣷⣶⣾⡿⠿⢿⡿⠟⠋⣡⣾⡟⠹⣿⡿⣄⣼⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣉⣉⣉⣭⣤⣶⠟⣉⣸⡋⠀⣿⠀⣼⣿⡟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⢿⢿⣿⠁⢰⣇⣠⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠹⠆⠿⠀⣠⣥⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⢀⣤⣾⣷⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣄⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⣠⣶⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢤⣤⣤⣤⣤⣤⣶⣾⣿⠿⠟⠋⠀⠀⠀
"""