#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 13:49:13 2018

@author: yiqian
"""

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        result = [[-1 for x in range(len(matrix[0]))] for y in range(len(matrix))]
        count = len(matrix)*len(matrix[0])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    result[i][j] = 0
                    count -= 1
        
        current = 0
        while count>0:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if result[i][j] == current:
                        if i-1>=0 and result[i-1][j]==-1:
                            result[i-1][j] = current+1
                            count -= 1
                        if i+1<len(matrix) and result[i+1][j]==-1:
                            result[i+1][j] = current+1
                            count -= 1
                        if j-1>=0 and result[i][j-1]==-1:
                            result[i][j-1] = current+1
                            count -= 1
                        if j+1<len(matrix[0]) and result[i][j+1]==-1:
                            result[i][j+1] = current+1
                            count -= 1
            current += 1
                
        return result
                
        
    
    """
    in this problem, we need to calculate the distance of i, j, to the nearest "0"
    at begining, I try to use DFS, but the deep of recursion is large
    So I change strategy, fresh matrix every distance until whole matrix have been visited
    But this strategy may not good for sparse "0" matrix
    """