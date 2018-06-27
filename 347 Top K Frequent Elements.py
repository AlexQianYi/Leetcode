#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 13:58:38 2018

@author: yiqian
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic_count = {}
        fre_min_count = 0
        
        for i in xrange(len(nums)):
            if nums[i] in dic_count:
                dic_count[nums[i]] += 1
            else:
                dic_count[nums[i]] = 1
        
        result = []
        setNums = list(set(nums))
        for i in xrange(k):
            temp_max = dic_count[setNums[0]]
            max_label = setNums[0]
            for j in xrange(1, len(setNums)):
                if dic_count[setNums[j]] > temp_max:
                    temp_max = dic_count[setNums[j]]
                    max_label = setNums[j]
            result.append(max_label)
            setNums.remove(max_label)
        return result