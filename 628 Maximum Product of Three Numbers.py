#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 09:25:56 2018

@author: yiqian
"""

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[0]*nums[1] > nums[-2]*nums[-3]:
            return nums[0]*nums[1]*nums[-1]
        else:
            return nums[-1]*nums[-2]*nums[-3]