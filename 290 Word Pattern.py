#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 16:40:20 2018

@author: yiqian
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dic, dic1= {}, {}
        string = str.split(' ')
        if len(string) != len(pattern):
            return False
        i = 0
        for ele in string:
            if ele not in dic and pattern[i] not in dic1:
                dic[ele] = pattern[i]
                dic1[pattern[i]] = 1
            elif ele in dic and pattern[i] in dic1:
                if dic[ele] != pattern[i]:
                    return False
            elif ele not in dic and pattern[i] in dic1 or ele in dic and pattern[i] not in dic1:
                return False

            i += 1
                    
        return True
    
    """
    beats 100%
    """