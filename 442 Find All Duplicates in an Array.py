#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 13:57:17 2018

@author: yiqian
"""

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []

        for num in nums:
            idx = abs(num) - 1

            if nums[idx] < 0:
                output.append(idx + 1)

            nums[idx] *= -1

        return output
    
    
    """
    The idea is we want to take advantage of the fact 
    that the numbers in the given list are between 1 and n. 
    With that in mind, we can see whether or not something 
    has been visited by using its 'sign' as a boolean flag. 
    If we have already seen something and are visiting it again, 
    that means it must have appeared twice, so we add it to the output.
    """