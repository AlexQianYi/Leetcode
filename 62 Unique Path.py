#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 17:04:36 2018

@author: yiqian
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def jiecheng(n):
            if n==1 or n==0:
                return 1
            else:
                return n*jiecheng(n-1)
        def Cmn(m, n):
            i = jiecheng(m+n)
            j = jiecheng(m)*jiecheng(n)
            return i/j
        
        return Cmn(m-1,n-1)