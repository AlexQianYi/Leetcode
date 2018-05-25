#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:07:15 2018

@author: yiqian
"""

class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        re_nums = nums
        result = 0
        visit = {}
        i = 0
        re = len(re_nums)
        while re!=0 and re>result:
            if re_nums[i] in visit:
                i += 1
                continue
            temp_point = re_nums[i]
            count = 1
            re -=1
            visit[temp_point] = 1
            while not (re_nums[temp_point] in visit):
                temp_point = re_nums[temp_point]
                count += 1
                visit[temp_point] = 1
                re-=1
            visit[temp_point] = 1
            if count > result:
                result = count
            i+=1
        return result
    
    """
    find the longest "ring" seq S[i] = {A[i], A[A[i]], A[A[A[i]]], ... 
    at first, I uesd list to store the elements which have been visited, but the time is over limited
    So dictionary is better, cut down the time of re-visit
    """