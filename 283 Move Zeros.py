#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 15:53:10 2018

@author: yiqian
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0  # records the position of "0"
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
                
                
                
        """
        move 0 to the end of the list
        two index, one from 0, one from end
        the end index record the last position of exchange
        """