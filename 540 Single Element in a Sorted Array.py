#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 17:14:09 2018

@author: yiqian
"""

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i<len(nums):
            if i == len(nums)-1 or nums[i] != nums[i+1]:
                return nums[i]
            else:
                i += 2