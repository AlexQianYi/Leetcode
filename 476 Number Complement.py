#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 16:52:32 2018

@author: yiqian
"""

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        a = int(math.log(num, 2))
        if 2**a == num:
            return int(2**a - 1)
        a += 1
        n = 2**a-1
        return int(n)^num
    
    
    """
    Use xor can extramely acclerate speed
    """