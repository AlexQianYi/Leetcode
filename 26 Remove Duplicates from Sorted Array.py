#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 11:20:47 2018

@author: yiqian
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 0
        c,l =1,1
        for i in xrange(1, len(nums)):
            if nums[i]!=nums[i-1]:
                nums[c] = nums[i]
                c+=1
                l+=1
        return l
    
    
    """
    remove duplicate elements
    
    implement: move the duplicate elements to the end of array
    """