#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 09:16:26 2018

@author: yiqian
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        temp_sum_dic = {0:nums[0]}
        result = nums[0]
        for i in range(1, len(nums)):
            if temp_sum_dic[i-1]>0:
                temp_sum_dic[i] = temp_sum_dic[i-1] + nums[i]
            else:
                temp_sum_dic[i] = nums[i]
            result = max(result, temp_sum_dic[i])
        
        return result