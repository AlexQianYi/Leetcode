#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 09:43:45 2018

@author: yiqian
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in xrange(0, len(nums)-1,2):
            if nums[i]!=nums[i+1]:
                return nums[i]
        return nums[len(nums)-1]
    
    
    """
    find the single number in list
    sort first
    """