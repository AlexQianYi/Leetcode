#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 14:33:09 2018

@author: yiqian
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        res, path = [], []
        self.dfs(nums, 0, path, res)
        return res

    def dfs(self, nums, index, path, res):
        
        for i in xrange(index, len(nums)):
            if len(path) == len(nums):
                res.append(path)
                return
            else:
                if nums[i] not in path:
                    self.dfs(nums, i+1, path.append(nums[i]), res)
                else:
                    continue
        
        """
        return list(itertools.permutations(nums))
        """