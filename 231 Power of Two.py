#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 17:27:29 2018

@author: yiqian
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0 or n<0:
            return False
        return pow(2, int(math.log(n, 2))) == n
    
        """
        if n<=0:
            return False
        
        n1=bin(n).count("1")

            
        if n1==1:
            return True
        else:
            return False
        """
        
        """
        beats 100%
        """