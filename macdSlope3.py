# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 22:20:36 2018

@author: syeh3
"""

import macd
import volume
import pandas as pd
import numpy as np
import math

def macdSlope3DirectInput(stockString, date):
    """Input stock as a string and date of crossover and returns
    angle made with midpoints three days past and three days ahead of MACD
    line and Signal Line"""
    
    stock = pd.io.parsers.read_csv('presentstockdata/' + stockString + '.csv')
    macd.macd(stock)
    volume.volumeAve(stock)
    index = len(stock['date'])-1
    
    while index != -1:
        if stock['date'][index] == date:
            break
        index -= 1
        
    m3Before = stock['MACD Line'][index - 5]
    m1Before = stock['MACD Line'][index - 3]
    m1After = stock['MACD Line'][index - 2]
    m3After = stock['MACD Line'][index]
    s3Before = stock['Signal Line'][index - 5]
    s1Before = stock['Signal Line'][index - 3]
    s1After = stock['Signal Line'][index - 2]
    s3After = stock['Signal Line'][index]
    mid3Before = (m3Before + s3Before)/2
    mid3After = (m3After + s3After)/2
    
    print("mids")
    
    print(mid3Before, mid3After)
    
    slopeMACD = -(m1After - m1Before)
    slopeSignal = -(s1After - s1Before)
    eqs = np.array([[slopeMACD, 1], [slopeSignal, 1]])
    points = np.array([m1Before, s1Before])
    sol = np.linalg.solve(eqs, points)
    
    print("sols")
    
    print(sol)
    
    xcoor = sol[0]
    ycoor = sol[1]
    xDBefore = 2 + xcoor
    yDBefore = mid3Before - ycoor
    xDAfter = 3 - xcoor
    yDAfter = mid3After - ycoor
    
    print("coordinates")
    
    print(xDBefore, yDBefore, xDAfter, yDAfter)
    
    dBefore = math.sqrt(xDBefore**2 + yDBefore**2)
    dAfter = math.sqrt(xDAfter**2 + yDAfter**2)
    longest = math.sqrt(5**2 + (mid3Before - mid3After)**2)
    
    print("legs of triangles")
    
    print(dBefore,dAfter,longest)
    
    print(dBefore**2,dAfter**2,longest**2)
    
    valueOne = (dBefore**2 + dAfter**2 - longest**2)/(2*dBefore*dAfter)
    
    print(valueOne)
    
    return np.arccos(valueOne)

def macdSlope3Historical(stock, index):
    """Input stock as a DataFrame and index and returns
    angle made with midpoints three days past and three days ahead of MACD
    line and Signal Line"""
        
    m3Before = stock['MACD Line'][index - 5]
    m1Before = stock['MACD Line'][index - 3]
    m1After = stock['MACD Line'][index - 2]
    m3After = stock['MACD Line'][index]
    s3Before = stock['Signal Line'][index - 5]
    s1Before = stock['Signal Line'][index - 3]
    s1After = stock['Signal Line'][index - 2]
    s3After = stock['Signal Line'][index]
    mid3Before = (m3Before + s3Before)/2
    mid3After = (m3After + s3After)/2
    
    print("mids")
    
    print(mid3Before, mid3After)
    
    slopeMACD = -(m1After - m1Before)
    slopeSignal = -(s1After - s1Before)
    eqs = np.array([[slopeMACD, 1], [slopeSignal, 1]])
    points = np.array([m1Before, s1Before])
    sol = np.linalg.solve(eqs, points)
    
    print("sols")
    
    print(sol)
    
    xcoor = sol[0]
    ycoor = sol[1]
    xDBefore = 2 + xcoor
    yDBefore = mid3Before - ycoor
    xDAfter = 3 - xcoor
    yDAfter = mid3After - ycoor
    
    print("coordinates")
    
    print(xDBefore, yDBefore, xDAfter, yDAfter)
    
    dBefore = math.sqrt(xDBefore**2 + yDBefore**2)
    dAfter = math.sqrt(xDAfter**2 + yDAfter**2)
    longest = math.sqrt(5**2 + (mid3Before - mid3After)**2)
    
    print("legs of triangles")
    
    print(dBefore,dAfter,longest)
    
    print(dBefore**2,dAfter**2,longest**2)
    
    valueOne = (dBefore**2 + dAfter**2 - longest**2)/(2*dBefore*dAfter)
    
    print(valueOne)
    
    return np.arccos(valueOne)

    
    