#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 13:44:38 2018

@author: yiqian
"""

class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        k, start, end = 1, 1, n
        while True:
            if end == start or end == start+k:return end
            if (end-start)%(2*k)==0:
                end = end-k
            start = start+k
            k*=2
            if end == start or start == end-k:return start
            if (end-start)%(2*k)==0:
                start = start+k
            end = end-k
            k*=2