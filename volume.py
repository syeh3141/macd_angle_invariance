# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 19:05:18 2018

@author: syeh3
"""

def volumeAve(stock):
    
    stock['Volume SMA'] = stock['volume'].rolling(50).mean()
    
def volumeAveHistorical(stock):
    
    stock['Volume SMA'] = stock['Volume'].rolling(50).mean()