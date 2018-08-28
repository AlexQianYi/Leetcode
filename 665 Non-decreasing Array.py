#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 20:37:30 2018

@author: yiqian
"""

class Solution(object):
    def checkPossibility(self, nums):
        can_modify = True
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if can_modify: # now is your chance to modify
                    if i == 1 or nums[i-2] <= nums[i]:
                        # if you can, modify the previous number
                        nums[i-1] = nums[i]
                    else:
                        # you have to modify the current number
                        nums[i] = nums[i-1]
                    can_modify = False
                else:
                    return False
        
        return True