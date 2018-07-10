#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 14:54:46 2018

@author: yiqian
"""

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        left, top = [], []
        for i in xrange(len(grid)):
            left.append(max(grid[i]))
        matrix = map(list,zip(*grid[::-1]))
        for i in xrange(len(matrix)):
            top.append(max(matrix[i]))
        
        result = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                result += (min(left[i], top[j]) - grid[i][j])
                
        return result
    
    """
    beat 99.9%
    """