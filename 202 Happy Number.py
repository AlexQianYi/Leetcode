#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 14:11:23 2018

@author: yiqian
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic = {}
        while True:
            sum = 0
            while(n>0):
                sum = sum + (n%10)**2
                n = int(n/10)
            
            if sum in dic:
                return False
            else:
                if sum==1:
                    return True
                else:
                    dic[sum] = 1
            n = sum