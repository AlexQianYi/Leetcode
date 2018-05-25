#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 10:55:34 2018

@author: yiqian
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        error = abs(nums[0] + nums[1] + nums[2] - target)
        for i in range(len(nums)-2):
            #if i == 0 or nums[i] != nums[i-1]:
            sum2 = nums[i]
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                sum = nums[lo] + nums[hi] + sum2
                if sum - target == 0:
                    return target
                elif target - sum > 0:
                    if abs(sum-target)<error:
                        error = abs(sum-target)
                        result = sum
                    lo += 1
                else:
                    if abs(sum-target)<error:
                        error = abs(sum-target)
                        result = sum
                    hi -= 1
        return result
    
    
    """
    find the sum of 3 numbers which cloestest to the target
    which similar to the 3 sum
    fixed one number, then two pointer from low to higher
    """