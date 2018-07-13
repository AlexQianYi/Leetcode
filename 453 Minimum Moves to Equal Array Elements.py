#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:09:52 2018

@author: yiqian
"""

class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums)-len(nums)*min(nums)
    
    """
    beats 100%
    increase 1 equal to minus 1 to the minimum element
    """