#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 14:33:39 2018

@author: yiqian
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        res = 0
        temp = s[::-1]
        if len(s)==1:
            return dic[s]
        res = dic[temp[0]]
        print(temp)
        for i in xrange(1, len(temp)):
            if dic[temp[i]] >= dic[temp[i-1]]:
                res += dic[temp[i]]
            else:
                res -= dic[temp[i]]
        
        return res
    
    
    """
    Roman string convert to Integer
    need to consider the position of character (add or sub)
    """