#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:52:08 2018

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
        m, res = prices[0],0
        for i in xrange(1, len(prices)):
            m = min(m, prices[i-1])
            if prices[i]-m > res:
                res = prices[i]-m
        return res
    
    """
    use m to maintain the smallest price in visited elements
    """