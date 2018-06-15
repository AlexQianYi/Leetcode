#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 14:13:16 2018

@author: yiqian
"""

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        final_S, final_T = "", ""
        
        i = 0
        while i<len(S):
            if S[i] == '#':
                final_S = final_S[:len(final_S)-1]
            else:
                final_S += S[i]
            i += 1
            
        i = 0
        while i<len(T):
            if T[i] == '#':
                final_T = final_T[:len(final_T)-1]
            else:
                final_T += T[i]
            i += 1
        
        return final_S==final_T
            
    
    """
    
    string handle problem
    when get '#' backspace
    """