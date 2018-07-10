#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 14:39:06 2018

@author: yiqian
"""

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num <= 0:
            return (False)
        
        while num % 2 == 0 and num != 1:
            num = num / 2
            
        while num % 3 == 0 and num != 1:
            num = num / 3
            
        while num % 5 == 0 and num != 1:
            num = num / 5
            
        return ( num == 1 )
    
    """
    beat 100%
    """