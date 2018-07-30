#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 16:05:13 2018

@author: yiqian
"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack, result, dic = [], [0 for i in xrange(len(temperatures))], {}
        for i in xrange(len(temperatures)):
            if not stack:
                stack.append([temperatures[i], i])
            else:
                if temperatures[i] > stack[-1][0]:
                    while stack and temperatures[i] >stack[-1][0]:
                        result[stack[-1][1]] = i-stack[-1][1]
                        stack.pop()
                stack.append([temperatures[i], i])
        while stack:
            result[stack[-1][1]] = 0
            stack.pop()
        return result