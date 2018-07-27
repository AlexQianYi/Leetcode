#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 09:20:09 2018

@author: yiqian
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row
    
    """
    beats 100%
    """