# -*- coding: utf-8 -*-
"""
AOC Day 6
Created on Tue Dec  6 09:26:35 2022

@author: bryce dunn
"""
import numpy as np
with open('input6.txt') as MerryXmasKyleAndZach:
    datastream = MerryXmasKyleAndZach.readlines()

datastream = str(datastream)
ds= datastream[2:len(datastream)-2]

def checkerooni(s1,s2,s3,s4):
    check1 = s1 in s2+s3+s4
    check2 = s2 in s1+s3+s4
    check3 = s3 in s1+s2+s4
    check4 = s4 in s1+s2+s3
    if check1 == False and check2 == False and check3 == False and check4 == False:
        return True
    else:
        return False
    

start_of_packet = 0
for i in np.arange(len(ds)-3):
    test = checkerooni(ds[i][0],ds[i+1][0],ds[i+2][0],ds[i+3][0])
    if test == True:
        start_of_packet = i+4
        break
        
print("Characters Processed Before Start of Packet: ",start_of_packet)