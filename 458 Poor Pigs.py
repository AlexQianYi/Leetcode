#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 16:12:10 2018

@author: yiqian
"""

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        if buckets==1:
            return 0
        
        # time to test 
        n=minutesToTest//minutesToDie+1
        
        
        result=1
        t=n
        
        while t<buckets:
            t=t*n
            result+=1
        
        return results