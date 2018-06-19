#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 10:39:54 2018

@author: yiqian
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max = 0
        l = len(height)
        i, j = 0, l-1
        while j > i:
            cap = (j-i)*min(height[i], height[j])
            if cap > max:
                max = cap
            if height[i]>height[j]:
                j-=1
            else:
                i+=1

        return max
    
    
    
    """
    two pointer. one from left, one from right
    """