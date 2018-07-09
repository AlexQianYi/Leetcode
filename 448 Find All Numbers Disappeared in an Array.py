#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 10:35:56 2018

@author: yiqian
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        result, zero = [i for i in xrange(1, len(nums)+1)], [0]
        
        for i in xrange(len(nums)):
            result[nums[i]-1] = 0
                
        return [i for i in result if i not in zero]