#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:13:37 2018

@author: yiqian
"""

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]
            
        return result
    
    """
    Given an array of 2n integers, your task is to group these integers into n pairs of integer, 
    say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
    
    if we want the sum of min pairs as large as possible, we need to construct every pair as close as possible
    so what we need to do is add up every 1st, 3nd, 5th... elements
    """