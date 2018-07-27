#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 17:15:51 2018

@author: yiqian
"""

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in xrange(1, len(nums), 2):
            if i+1 <len(nums):
                nums[i], nums[i+1]  = nums[i+1], nums[i]