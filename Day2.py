import pandas as pd
import numpy as np
df = pd.read_csv('AOC2.csv',header=None)

score = 0

for i in np.arange(len(df)):
    if df.iloc[i][1] == 'X':
        df.iloc[i][1] = 'A'
    if df.iloc[i][1] == 'Y':
        df.iloc[i][1] = 'B'
    if df.iloc[i][1] == 'Z':
        df.iloc[i][1] = 'C'
        
    if df.iloc[i][1] == 'A':
        score = score + 1
    if df.iloc[i][1] == 'B':
        score = score + 2
    if df.iloc[i][1] == 'C':
        score = score + 3
        
    if df.iloc[i][1] == df.iloc[i][0]:
        score = score + 3
        
    if df.iloc[i][1] == 'A' and df.iloc[i][0]=='C':
        score = score + 6
        
    if df.iloc[i][1] == 'B' and df.iloc[i][0]=='A':
        score = score + 6
        
    if df.iloc[i][1] == 'C' and df.iloc[i][0]=='B':
        score = score + 6    
    
print("Total Score: ", score)

# part 2
dd = pd.read_csv('AOC2.csv',header=None)
score2 = 0

for i in np.arange(len(dd)):
    if dd.iloc[i][1] == 'X' and dd.iloc[i][0] == 'A':
        dd.iloc[i][1] = 'C'
    if dd.iloc[i][1] == 'X' and dd.iloc[i][0] == 'C':
        dd.iloc[i][1] = 'B'
    if dd.iloc[i][1] == 'X' and dd.iloc[i][0] == 'B':
        dd.iloc[i][1] = 'A'
    if dd.iloc[i][1] == 'Y':
        dd.iloc[i][1] = dd.iloc[i][0]
    if dd.iloc[i][1] == 'Z' and dd.iloc[i][0] == 'A':
        dd.iloc[i][1] = 'B'
    if dd.iloc[i][1] == 'Z' and dd.iloc[i][0] == 'C':
        dd.iloc[i][1] = 'A'
    if dd.iloc[i][1] == 'Z' and dd.iloc[i][0] == 'B':
        dd.iloc[i][1] = 'C'
        
    if dd.iloc[i][1] == 'A':
        score2 = score2 + 1
    if dd.iloc[i][1] == 'B':
        score2 = score2 + 2
    if dd.iloc[i][1] == 'C':
        score2 = score2 + 3
        
    if dd.iloc[i][1] == dd.iloc[i][0]:
        score2 = score2 + 3
        
    if dd.iloc[i][1] == 'A' and dd.iloc[i][0]=='C':
        score2 = score2 + 6
        
    if dd.iloc[i][1] == 'B' and dd.iloc[i][0]=='A':
        score2 = score2 + 6
        
    if dd.iloc[i][1] == 'C' and dd.iloc[i][0]=='B':
        score2 = score2 + 6
        
print("Decrypted Score: ",score2)