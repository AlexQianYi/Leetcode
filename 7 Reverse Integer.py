#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 16:30:54 2018

@author: yiqian
"""

class Solution(object):
    
    def subreverse(self, x):
        res = 0
        if x==0:
            return res
        while (x!=0):
            res = res*10 + (x%10)*10
            x = x/10
        return res/10
    
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>2147483647 or x<-2147483648:
            return 0
        if x>=0:
            res = self.subreverse(x)
            if res>2147483647:
                return 0
            return res
        else:
            res= -1*self.subreverse(abs(x))
            if res<-2147483648:
                return 0
            return res