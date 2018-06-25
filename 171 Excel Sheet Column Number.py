#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 14:40:27 2018

@author: yiqian
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10,\
              'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20,\
              'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
        
        result, c = 0, 0
        for i in range(len(s)-1, -1, -1):
            result += dic[s[i]]*26**c
            c += 1
        return result