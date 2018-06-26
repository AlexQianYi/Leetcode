#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:36:51 2018

@author: yiqian
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
            else:
                if i - dic[nums[i]]<=k:
                    return True
                dic[nums[i]] = i
                
        return False
    
    
    """
    find whether there is two elements meet following conditions:
        x[i] = x[j] i!=j
        and |i-j|<=k
    """