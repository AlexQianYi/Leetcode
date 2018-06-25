#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:03:16 2018

@author: yiqian
"""

class Solution(object):
    def numIslands(self, grid):
        def visit(i, j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]=='1':
                grid[i][j]='2'
                map(visit, (i-1, i, i, i+1), (j, j+1, j-1, j))
                return
            return 
        
        res = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j]=='1':
                    visit(i, j)
                    res +=1
        return res