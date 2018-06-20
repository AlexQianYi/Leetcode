#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 16:34:56 2018

@author: yiqian
"""

class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        if a == -b:
            return 0
        if abs(a) > abs(b):
            a, b = b, a
        if a < 0:
            return -self.getSum(-a, -b)
        while b:
            c = a & b
            a ^= b
            b = c << 1
        return a
    
    
    