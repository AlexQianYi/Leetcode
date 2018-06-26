#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:25:07 2018

@author: yiqian
"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        #method 1
        if n==0:
            return 0
        
        res = [1]*(n+1)
        for i in xrange(1, n+1):
            temp = 0
            for j in xrange(1, i+1):
                temp = temp + res[j-1]*res[i-j]
            res[i] = temp
        return res[-1]
        
        #method 2
        """
        def numberTree(n):
            print(n)
            if n==1 or n==0:
                return 1
            if n==0:
                return 0
            if n==2:
                return 2
            res = 0
            for i in xrange(1,n+1):
                temp = numberTree(i-1)*numberTree(n-i)
                res += temp
            return res
                
        if n==0:
            return 0
        return numberTree(n)
        """