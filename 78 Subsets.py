#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 10:09:28 2018

@author: yiqian
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, index, path, res):
            res.append(path)
            for i in xrange(index, len(nums)):
                dfs(nums, i+1, path+[nums[i]], res)
        
        res = []
        dfs(sorted(nums), 0, [], res)
        return res