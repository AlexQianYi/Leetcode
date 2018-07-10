#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 10:25:47 2018

@author: yiqian
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dic_s, dic_t = {}, {}
        for i in xrange(len(s)):
            if s[i] in dic_s and t[i] not in dic_t :
                return False
            elif s[i] not in dic_s and t[i] in dic_t:
                return False
            elif s[i] in dic_s and t[i] in dic_t:
                if dic_s[s[i]] != dic_t[t[i]]:
                    return False
            else:
                dic_s[s[i]], dic_t[t[i]] = i, i
        return True