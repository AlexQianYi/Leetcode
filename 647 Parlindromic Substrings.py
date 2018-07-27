#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 09:04:47 2018

@author: yiqian
"""

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = len(s)
        for i in xrange(2, len(s)+1):
            for j in xrange(len(s)):                
                if i%2 == 0:                      
                    if s[j:j+int(i/2)] == s[j+int(i/2):j+i][::-1] and len(s[j:j+int(i/2)])!=0:
                        result += 1
                else:         
                    if s[j:j+int((i-1)/2)] == s[j+int((i-1)/2)+1:j+i][::-1] and len(s[j:j+int((i-1)/2)])!=0:
                        result += 1
        return result
    
    """
    i: the length of substring
    j: the startposition of substring
    """