#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 11:11:38 2018

@author: yiqian
"""


class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        a=[]
        an=[]
        for i in xrange(n):
            if i not in a and i not in an:
                j=i
                if nums[j]>0:
                    while j not in a:
                        if nums[j]<0 or j==(j+nums[j])%n:
                            break
                        a.append(j)
                        j=(j+nums[j])%n
                    if j in a:
                        return True                
                else:
                    while j not in a:
                        if nums[j]>0 or j==(j+nums[j])%n:
                            break
                        a.append(j)
                        j=(j+nums[j])%n
                    if j in an:
                        return True            
        return False