#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 10:23:12 2018

@author: yiqian
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums)
        
        low, high = 0, len(nums)
        mid = int((low+high)/2)
        
        if nums[low]>nums[mid]:
            return min(self.findMin(nums[low:mid+1]), nums[mid])
        else:
            return min(self.findMin(nums[mid:high]), nums[low])