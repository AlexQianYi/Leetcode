#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:19:05 2018

@author: yiqian
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = []
        nums.sort()
        #print(nums)
        for i in range(len(nums)-3):
            if i == 0 or nums[i] != nums[i-1]:
                sum1 = nums[i]
                for j in range(i+1, len(nums)-2):
                    if j == i+1 or nums[j] != nums[j-1]:
                        sum2 = nums[j]
                        lo, hi = j + 1, len(nums) - 1
                        while lo < hi:
                            #print(lo, hi)
                            sum = nums[lo] + nums[hi]
                            if sum+sum1+sum2 == target:
                                res.append([nums[i], nums[j], nums[lo], nums[hi]])
                                lo += 1
                                while lo < len(nums) and nums[lo] == nums[lo-1]:
                                    lo += 1
                                hi -= 1
                                while hi>=0 and nums[hi] == nums[hi+1]:
                                    hi -= 1
                            elif sum+sum1+sum2<target:
                                lo += 1
                            else:
                                hi -= 1
        return res
    
    """
    4 number sum to target
    """