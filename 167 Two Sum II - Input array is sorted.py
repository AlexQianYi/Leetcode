#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 16:58:12 2018

@author: yiqian
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dic = {}
        
        for i in xrange(len(numbers)):
            if numbers[i] in dic:
                return [dic[numbers[i]]+1, i+1]
            else:
                dic[target-numbers[i]] = i