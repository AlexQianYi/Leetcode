#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 09:21:04 2018

@author: yiqian
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        far_pos = 0
        for i in xrange(len(nums)):
            if i>far_pos:
                return False
            far_pos = max(far_pos, i+nums[i])
        return True
    
    """
    beats 88%
    """