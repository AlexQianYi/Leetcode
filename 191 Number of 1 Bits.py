#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 15:56:52 2018

@author: yiqian
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n>0:
            if n&1==1:
                result += 1
            n >>= 1
        return result
        
        """
        n1=bin(n)
        
        return n1.count("1")
        """
        
        
        
        """
        two method, one by Python method, other by bit calculation
        """