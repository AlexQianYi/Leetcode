#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 09:15:32 2018

@author: yiqian
"""

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic_pos = {}
        dic_time = {}
        max_count = 0
        
        for i in xrange(len(nums)):
            if nums[i] in dic_time:
                dic_time[nums[i]] += 1
                dic_pos[nums[i]][1] = i
                max_count = max(dic_time[nums[i]], max_count)
            else:
                dic_time[nums[i]] = 1
                dic_pos[nums[i]] = [i, i]
                max_count = max(1, max_count)
        
        result = len(nums)
        for key in dic_time:
            if dic_time[key] == max_count:
                result = min(result, dic_pos[key][1] - dic_pos[key][0]+1)
        return result
    
    
    """
    beats 99.52%
    """