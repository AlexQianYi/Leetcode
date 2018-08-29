#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 00:17:16 2018

@author: yiqian
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        
        dic = {}
        for i in xrange(1, len(nums)+1):
            dic[i] = 1
            
        max_pos = 1
        for i in xrange(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] = 0
            if max_pos < nums[i]:
                max_pos = nums[i]
        
        min_val = float('inf')
        for key in dic:
            if key < min_val and dic[key] != 0:
                min_val = key
        
        if min_val < len(nums)+1:
            return min_val
        else:
            return max_pos+1