#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 18:22:26 2018

@author: yiqian
"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s)-1
        flag = False
        while i<j and s[i] == s[j]:
            i += 1
            j -= 1
        if i>=j:
            return True
        if s[i+1] == s[j]:
            m, n, f = i+1, j, True
            while m<n:
                if s[m] != s[n]:
                    f = False
                    break
                m += 1
                n -= 1
            if f:
                return True
        if s[i] == s[j-1]:
            m, n, f = i, j-1, True
            while m<n:
                if s[m] != s[n]:
                    f = False
                    break
                m += 1
                n -= 1
            if f:
                return True
            else:
                return False
        else:
            return False