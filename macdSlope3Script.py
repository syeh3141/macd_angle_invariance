# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 09:16:39 2018

@author: syeh3
"""

import macd
import volume
import pandas as pd
import numpy as np
import math
import macdSlope3 as ms
import convertExceltoDataFrame
import returns
import json


convertExceltoDataFrame.convertExcelToDataFrame('historicalstockdata')

stocksDataListOutcome = convertExceltoDataFrame.stocksDataList

with open('slope_macdSlope2/indices.json') as infile:
    listOfIndices = json.load(infile)

stockReturns = {}

stockControlReturns = {}

stockReturnsandDate = {}

stockAngles = {}

for stock in stocksDataListOutcome:
    print(stock)
    stockData = stocksDataListOutcome[stock]
    macd.macdHistorical(stockData)
    volume.volumeAveHistorical(stockData)
    stockReturns[stock] = []
    stockReturnsandDate[stock] = []
    stockAngles[stock] = []
    stockControlReturns[stock] = []
    for index in listOfIndices[stock]: 
        #print(index)
        angle = ms.macdSlope3Historical(stockData, index) 
        if angle <= 2.75:
            stockAngles[stock].append([stockData['Date'][index], angle])

            stockReturns[stock].append(returns.returnsOfFiveDays(stockData, index))
            stockReturnsandDate[stock].append([stockData['Date'][index], returns.returnsOfFiveDays(stockData, index)])
            
        stockControlReturns[stock].append(returns.returnsOfFiveDays(stockData, index))
            
with open('slope_macdSlope2/returnsMACDSlope.json', 'w') as outfile:
    json.dump(stockReturns, outfile)
    
with open('slope_macdSlope2/returnsMACDSlope.txt', 'w') as outfile:
    json.dump(stockReturns, outfile)
    
with open('slope_macdSlope2/returnsandDateMACDSlope.json', 'w') as outfile:
    json.dump(stockReturnsandDate, outfile)
    
with open('slope_macdSlope2/returnsandDateMACDSlope.txt', 'w') as outfile:
    json.dump(stockReturnsandDate, outfile)
    
with open('slope_macdSlope2/angles.json', 'w') as outfile:
    json.dump(stockAngles, outfile)
    
with open('slope_macdSlope2/angles.txt', 'w') as outfile:
    json.dump(stockAngles, outfile)
    
with open('slope_macdSlope2/control.json', 'w') as outfile:
    json.dump(stockControlReturns, outfile)
    
with open('slope_macdSlope2/control.txt', 'w') as outfile:
    json.dump(stockControlReturns, outfile)
    