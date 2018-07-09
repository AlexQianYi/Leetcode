#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 11:30:29 2018

@author: yiqian
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        tempListV = []
        tempListH = []
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j]==0:
                    tempListV.append(j)
                    tempListH.append(i)
        
        for i in tempListH:
            for k in xrange(len(matrix[0])):
                matrix[i][k] = 0
        
        for j in tempListV:
            for k in xrange(len(matrix)):
                matrix[k][j] = 0
                
    
    
    """
    use two lists to save the col and ros which need to set as zero
    very effective
    """