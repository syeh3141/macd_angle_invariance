# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 11:51:46 2018

@author: syeh3
"""

import json


def returnsClosetoClose(stockData, index, days):
    """Input DataFrame type of stock and index returns 
    returns after five days"""
    
    absoluteDifference = (stockData['Close'][index + days] - stockData['Close'][index])
    percentReturn = absoluteDifference/stockData['Close'][index]*100

    return percentReturn

def returnsOfFiveDays(stockData, index):
    """Input DataFrame type of stock and index returns 
    returns after five days"""
    
    absoluteDifference = (stockData['Close'][index + 5] - stockData['Open'][index])
    percentReturn = absoluteDifference/stockData['Open'][index]*100

    return percentReturn

def returnsOfFiveDaysClosetoClose(stockData, index):
    """Input DataFrame type of stock and index returns 
    returns after five days"""
    
    absoluteDifference = (stockData['Close'][index + 5] - stockData['Close'][index])
    percentReturn = absoluteDifference/stockData['Close'][index]*100

    return percentReturn


def returnsFromJson(file):
    
    count = 0
    totalCount = 0
    positivePercent = 0
    negativePercent = 0
    total = 0
    
    with open(file + '.json') as infile:
        returns = json.load(infile)
        
    for stock in returns:
        for num in returns[stock]:
            if num > 0:
                positivePercent += num
                count += 1
            if num <= 0:
                negativePercent += num
            total += num
            totalCount += 1
        
    print("Positives: " + str(count))
    print("Percent Positive: " + str(count/totalCount))
    print("Total: " + str(totalCount))
    print("Positive Total Percent: " + str(positivePercent))
    print("Negative Total Percent: " + str(negativePercent))
    print("Total Percentage: " + str(total))
        
    
        
        
        
        
        