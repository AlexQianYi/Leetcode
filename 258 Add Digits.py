#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 19:43:03 2018

@author: yiqian
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num<10:
            return num
        elif num%9==0:
            return 9
        else:
            return num%9
        
        
        """
        given a non-negative integer num, repeatedly add all its digits until the result has only one digit
        
        
        """