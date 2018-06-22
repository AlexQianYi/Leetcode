#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 16:00:04 2018

@author: yiqian
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1: return 1
        if n==2: return 2
        res = [1,2]
        for i in xrange(2,n):
            temp = res[i-1]+res[i-2]
            res.append(temp)
        return res[n-1]
    
    
    """
    calculate how many method to get to n stairs
    
    f(n) = f(n-1) + f(n-2)
    
    """