#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 11:15:23 2018

@author: yiqian
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        dic = {}
        
        for i in xrange(len(nums)):
            if nums[i] not in dic:
                result.append(nums[i])
                dic[nums[i]] = 1
            else:
                result.remove(nums[i])
        return result