#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:06:46 2018

@author: yiqian
"""

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        result = []
        for i in xrange(len(s)-9):
            if s[i:i+10] not in dic:
                dic[s[i:i+10]] = 1
            else:
                result.append(s[i:i+10])
        return list(set(result))