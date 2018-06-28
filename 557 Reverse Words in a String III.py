#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 16:24:00 2018

@author: yiqian
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reS = s[::-1]
        s = reS.split()
        return " ".join(s[::-1])