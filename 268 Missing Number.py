#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 16:53:03 2018

@author: yiqian
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        return int(l * (l + 1) / 2 - sum(nums))