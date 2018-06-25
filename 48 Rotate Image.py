#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 16:37:54 2018

@author: yiqian
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix[0])
        time = l/2
            
        for i in xrange(time):
            for j in xrange(i, (l-1-i)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[l-1-j][i]
                matrix[l-1-j][i] = matrix[l-1-i][l-1-j]
                matrix[l-1-i][l-1-j] = matrix[j][l-1-i]
                matrix[j][l-1-i] = temp
                
                
        """
        rotate image
        
        [1, 2, 3]           [7, 4, 1]
        [4, 5, 6]    =>     [8, 5, 2]
        [7, 8, 9]           [9, 6, 3]
        
        we only need to operate left top corner of matrix
        use 1/4 time
        """
        