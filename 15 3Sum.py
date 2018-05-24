#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 23:55:54 2018

@author: yiqian
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return map(list, res)
    
    
    """
    3 Sum problem
    fix one number, then small two bound from left and right of sorted num seq
    use set to remove the duplicate result
    """