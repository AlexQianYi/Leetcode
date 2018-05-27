#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 12:16:55 2018

@author: yiqian
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(eval('0b' + a) + eval('0b' + b))[2:]
    
    
    """
    add binary
    
    note: use bin() Function
    """