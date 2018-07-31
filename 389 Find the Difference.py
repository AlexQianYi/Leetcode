#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 19:48:16 2018

@author: yiqian
"""

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic, result = {}, ""
        for ele in s:
            if ele not in dic:
                dic[ele] = 1
            else:
                dic[ele] += 1
        
        for ele in t:
            if ele not in dic:
                result += ele
            elif dic[ele] == 0:
                result += ele
            else:
                dic[ele] -= 1
        
        return result
    
    """
    beats 93.1%
    """