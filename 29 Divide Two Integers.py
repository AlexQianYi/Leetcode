#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 09:15:11 2018

@author: yiqian
"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        
        dividend=abs(dividend)
        divisor=abs(divisor)
        
        if dividend<divisor:
            return 0
        
        i=1
        res=0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if positive==0:
            res=-res
        return min(max(-2147483648, res), 2147483647)
    
    
    """
    increase divisor to decrease the sub time
    """