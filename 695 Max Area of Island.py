#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 17:22:19 2018

@author: yiqian
"""

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def visit(i, j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]==1:
                grid[i][j]=2
                return 1+visit(i-1, j)+visit(i, j-1)+visit(i+1, j)+visit(i, j+1)
            else:
                return 0
        
        res = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j]==1:
                    res = max(res, visit(i, j))
        return res 
    
    
    """
    beats 99%
    """