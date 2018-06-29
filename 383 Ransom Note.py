#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 15:25:38 2018

@author: yiqian
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = {}
        for i in xrange(len(magazine)):
            if magazine[i] in dic:
                dic[magazine[i]] += 1
            else:
                dic[magazine[i]] = 1
        
        for i in xrange(len(ransomNote)):
            if ransomNote[i] not in dic or dic[ransomNote[i]] == 0:
                return False
            else:
                dic[ransomNote[i]] -= 1
        
        return True