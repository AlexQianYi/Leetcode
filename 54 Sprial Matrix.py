#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 09:46:51 2018

@author: yiqian
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])
    
    
    """
    learn use matrix[::-1] to turn matrix
    """