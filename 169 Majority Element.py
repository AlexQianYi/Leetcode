#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 13:59:10 2018

@author: yiqian
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        
        myset=set(nums)
        
        for i in myset:
            if nums.count(i)>int(n/2):
                return i
            
    """
    use set to eleminte duplicate elements
    then count
    """
    