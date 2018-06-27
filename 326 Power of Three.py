#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 09:41:59 2018

@author: yiqian
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and  1162261467%n==0
    
    """
    1162261467 is 3^19 and 3^20 is bigger than integer
    """
    