#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 14:36:54 2018

@author: yiqian
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        if n==2:
            return "11"
        temp = "11"
        res = ""
        for i in xrange(n-2):
            cur = temp[0]
            count = 1
            for j in xrange(1, len(temp)):
                if temp[j]==cur:
                    count +=1
                else:
                    res  = res + str(count)+str(cur)
                    count = 1
                    cur = temp[j]
            res  = res + str(count)+str(cur)
            temp = res
            res =""
        return temp