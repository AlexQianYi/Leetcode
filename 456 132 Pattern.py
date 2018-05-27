#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 19:59:03 2018

@author: yiqian
"""

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        min_nums = [nums[0]]
        min_val = nums[0]
        for i in range(1, len(nums)):
            if min_val < nums[i]:
                min_nums.append(min_val)
            else:
                min_nums.append(nums[i])
                min_val = nums[i]
        stack = [nums[-1]]
        print(min_nums)
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > min_nums[i]:
                while stack and stack[-1] <= min_nums[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        return False
    
    
    """
    132 Pattern
    
    visit seq from start to end
    using a list to store the every min number from now
    
    
    """