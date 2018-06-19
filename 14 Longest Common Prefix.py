#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 10:44:33 2018

@author: yiqian
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        long_prefix=""
        if strs==[]:
            return long_prefix
        if len(strs)==1:
            return strs[0]
        i,j = 0,0
        false = 0
        while True:
            if i>= len(strs[0]):
                break
            long_prefix += strs[0][i]
            for k in xrange(1, len(strs)):
                if len(long_prefix) > len(strs[k]):
                    long_prefix = long_prefix[:-1]
                    false = 1
                    break
                if strs[k][i] != long_prefix[i]:
                    long_prefix = long_prefix[:-1]
                    false = 1
                    break
            if false==1:
                break
            i += 1
        
        return long_prefix
    
    """
    """