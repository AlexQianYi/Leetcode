#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 13:50:16 2018

@author: yiqian
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums==[]:
            return 0
        c,l =0,0
        for i in xrange(0, len(nums)):
            if nums[i]!=val:
                nums[c] = nums[i]
                c+=1
                l+=1
        return l