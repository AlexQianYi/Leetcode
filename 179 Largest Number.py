#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:52:55 2018

@author: yiqian
"""

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        

        Strnums = []
        for i in xrange(len(nums)):
            Strnums.append(str(nums[i]))
            
        def compare(i, j):
            if int(i+j)<int(j+i):
                return -1
            else:
                return 1
            return 0
        Strnums.sort(cmp=compare,reverse=True)
        return str(int("".join(Strnums)))
        
        """
        if nums.count(0) == len(nums):
            return "0"
        
        def compare(i, j):
            if int(Strnums[i]+Strnums[j])<int(Strnums[j]+Strnums[i]):
                Strnums[i], Strnums[j] = Strnums[j], Strnums[i]
            return
        
        Strnums = []
        for i in xrange(len(nums)):
            Strnums.append(str(nums[i]))
        
        for i in xrange(len(nums)):
            map(compare, (i for j in range(i+1, len(Strnums))), (j for j in range(i+1, len(Strnums))))
        
        result = ""
        for i in xrange(len(Strnums)-1, -1, -1):
            result = Strnums[i] + result
        return str(result)
        """