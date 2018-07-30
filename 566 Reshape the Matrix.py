#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 16:21:43 2018

@author: yiqian
"""

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row, col, l, result = len(nums), len(nums[0]), [], []
        if row*col != r*c:
            return nums
        for i in xrange(row):
            for j in xrange(col):
                l.append(nums[i][j])
        
        count = 0
        for i in xrange(1, r+1):
            result.append([])
            for j in xrange(1, c+1):
                result[i-1].append(l[count])
                count += 1
        return result