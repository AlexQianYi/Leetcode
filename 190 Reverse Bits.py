#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 13:54:05 2018

@author: yiqian
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        string = str(bin(n).replace('0b', ''))
        if len(string) < 32:
            string = "0"*(32-len(string)) + string
        return int(string[::-1], 2)
    
    """
    beat 88.49%
    """