#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 17:10:43 2018

@author: yiqian
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        setNums = list(set(nums))
        
        result, l = [], len(nums)
        for i in xrange(len(setNums)):
            if nums.count(setNums[i]) > int(l/3):
                result.append(setNums[i])
        return result