#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 17:36:19 2018

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