#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 17:01:25 2018

@author: yiqian
"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    
                    result += 4
                    if i-1>-1 and grid[i-1][j]:
                        result -= 2
                    if j-1>-1 and grid[i][j-1]:
                        result -= 2
        return result