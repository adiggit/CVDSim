# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:31:35 2018

@author: adith
"""
import numpy as np
import collections as col
import math as m
import random

grid=np.zeros((20,20))
for i in np.arange(20):
    grid[i][0] = 2
    
def count(x,i):
   return (x==i).sum()
   

T = 1173
k1 = 3.2E-12 * (T**(0.5)) * m.exp(-3430/T)
km1 =  3.2E-13 * (T**(0.5)) * m.exp(-7850/T)
k2 = 9.6E-13 * (T**(0.5))
Hs = 1.84E13
H2 = 1.65E17
CH3 = 1.44E13
PAds = 0.075
AdsRate = (PAds*CH3*3757*m.sqrt(T)/4)/1.56E15
Bulk = count(grid,1)
Hydr = count(grid,2)
DHydr = count(grid,3)
Ads = count(grid,4)
DAds = count(grid,5)


while(Bulk < 350):
    Bulk = count(grid,1)
    Hydr = count(grid,2)
    DHydr = count(grid,3)
    Ads = count(grid,4)
    DAds = count(grid,5)
    toplist=[]
    for i in np.arange(20):
        for j in np.arange(20):
            if grid[i][j]==0:
                toplist.append(j-1)
                break
    topvalues=[]
    for i in np.arange(20):
        for j in np.arange(20):
            if grid[i][j]==0:
                topvalues.append(grid[i][j-1])
                break
    
    Arate = k1*Hs*Hydr
    Drate = (k2*Hs + km1*H2 ) * DHydr
    AdsorptionRate= AdsRate*(Hydr + DHydr)
    AdsAct = k1*Hs*Ads
    AdsDeAct = (k2*Hs + km1*H2 ) * DAds

    for i in np.arange(1,19):
        for j in np.arange(20):
            if grid[i][j] == 4 and (grid[i+1][j] in (2,4)  or grid[i-1][j]
            in (2,4)):
                grid[i][j]=2
    for i in (0):
        for j in np.arange(20):
            if grid[i][j] == 4 and (grid[i+1][j] in (2,4)):
                grid[i][j]=2
    for i in (19):
        for j in np.arange(20):
            if grid[i][j] == 4 and ( grid[i-1][j] in (2,4)):
                grid[i][j]=2
    r = random.uniform(0,1)
    kTot = Arate + Drate + AdsorptionRate + AdsAct + AdsDeAct
    klist = (Arate, Drate, AdsorptionRate, AdsAct, AdsDeAct)
    partialSums = [], sum=0
    for i in np.arange(5):
        sum += klist[i]
        partialSums.append(sum)
    partialSums[:] = [float(x) for x in partialSums]
    partialSums[:] = [x/ kTot for x in partialSums]
    partialSums = [0] + partialSums
    t = 0
    for i in np.arange(5):
        if partialSums[i] <= r <= partialSums[i+1]:
            t=i
    if i==0:
       index1 = random.choice(np.where(topvalues==2)[0])
       index2 = toplist[index1]
       grid[index1,index2]=3
    if i==1:
        index1 = random.choice(np.where(topvalues==3)[0])
        index2 = toplist[index1]
        grid[index1,index2]=2
    if i==2:
        index1 = random.choice(np.where(topvalues==3 or topvalues==5)[0])
        index2 = toplist[index1]
        grid[index1,index2+1]=4
    if i==3:
        index1= random.choice(np.where(topvalues==4)[0])
        index2= toplist[index1]
        grid[index1,index2]=5
    if i==4:
        index1=random.choice(np.where(topvalues==5)[0])
        index2=toplist[index1]
        
        
        
    
        
        
                
            
    






