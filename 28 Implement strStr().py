#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 09:12:07 2018

@author: yiqian
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if (len(haystack)<len(needle)):
            return -1
        if needle=="":
            return 0
        
        for i in xrange(len(haystack)):
            j,k=0,i
            while haystack[k]==needle[j]:
                k+=1
                j+=1
                if j==len(needle) or k==len(haystack):
                    break
            if j==len(needle):
                return i
            if (len(haystack)-i-1)<len(needle):
                return -1
        
        return -1