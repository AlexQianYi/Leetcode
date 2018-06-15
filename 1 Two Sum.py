#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 14:28:05 2018

@author: yiqian
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        
        buff={}
        for i in xrange(len(nums)):
            if nums[i] in buff:
                return [buff[nums[i]], i]
            else:
                buff[target-nums[i]]=i
                
                
                
    """
    two sum problem 
    use dictionary to store the Target-sum[i]
    """