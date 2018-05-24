#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 11:20:17 2018

@author: yiqian
"""

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if not (len(s)==len(t)):
            return False
        
        sSort = sorted(s)
        tSort = sorted(t)
        
        return sSort == tSort
    
    """
    1. sort two strings first 
    2. then compare
    """