#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 09:33:49 2018

@author: yiqian
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        if len(nums)==1:
            return nums[0]
        
        if len(nums)==2:
            return max(nums[0], nums[1])
        
        fn_1 = nums[2]+nums[0]
        fn_2 = nums[1]
        fn_3 = nums[0]
        result = max(fn_1, fn_2)
        for i in range(3, len(nums)):
            result = max(max(fn_1, nums[i]+fn_3), nums[i]+fn_2)
            fn_3 = fn_2
            fn_2 = fn_1
            fn_1 = result
        return result
    
    
    """
    House robber
    robber can't rob adjacent house 
    DP algorithm
    x0, x1, x2, x3, x4, ... , xn
    f(n) = max(xn+f(n-2), xn+f(n-3), f(n-2))
    """