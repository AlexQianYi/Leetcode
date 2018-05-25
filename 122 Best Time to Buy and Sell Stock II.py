#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:37:49 2018

@author: yiqian
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        result = 0
        i = 0
        end = 0
        while i<len(prices):
            start = self.increaseStart(prices, end)
            if start == len(prices)-1:
                return result
            else:
                current = prices[start]
                end = self.increaseEnd(prices, start)
                result += prices[end]-current
                if end == len(prices)-1:
                    return result
                else:
                    i = end+1
                    continue
            
                
                    
    def increaseStart(self, seq, end):
        for i in range(end, len(seq)-1):
            if seq[i]>=seq[i+1]:
                continue
            else:
                return i
        return len(seq)-1
    
    def increaseEnd(self, seq, start):
        for i in range(start, len(seq)-1):
            if seq[i]<=seq[i+1]:
                continue
            else:
                return i
        return len(seq)-1
    
    """
    change a little compared to 121, we can have multiple transactions now
    so we need to do is find the every increase part of stock graph
    """