#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 11:03:06 2018

@author: yiqian
"""

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        if x==0 and y==0:
            return 0
        else:
            return ((x%2)^(y%2)) + self.hammingDistance(x>>1, y>>1)
        
        
    """
    use xor operation and right shift
    """