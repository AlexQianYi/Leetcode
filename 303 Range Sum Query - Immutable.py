#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 16:18:00 2018

@author: yiqian
"""

class NumArray(object):

    def __init__(self, nums):
        self.dp = nums
        for i in xrange(1, len(nums)):
            self.dp[i] += self.dp[i-1]

    def sumRange(self, i, j):
        return self.dp[j] - (self.dp[i-1] if i > 0 else 0)
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)