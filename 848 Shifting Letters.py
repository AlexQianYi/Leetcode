#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 10:10:44 2018

@author: yiqian
"""

class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        
        sum = 0
        for i in range(len(shifts)-1, -1, -1):
            sum += shifts[i]
            shifts[i] = sum
        
        for i in range(len(S)):
            CharAscii = ord(S[i])
            sub = CharAscii-ord('a')
            CharAscii = (shifts[i]+sub)%26+ord('a')
            S = S[:i]+chr(CharAscii)+S[i+1:]
            
        return S
    
    
"""
shifting lower letters
 input two lists
     S: letters need to be shifted
     shifts: shifts[i] = x
     0-i need to be shift x
"""