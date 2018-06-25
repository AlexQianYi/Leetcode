#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 14:51:22 2018

@author: yiqian
"""

class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow
    
    
    """
    implementation of pow operation
    use shift and logtic operation to decrease time of multiple
    """