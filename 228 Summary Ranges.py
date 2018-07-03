#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 17:21:27 2018

@author: yiqian
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        count, start, cur, result = 1, nums[0], nums[0], []
        
        for i in xrange(1, len(nums)):
            if nums[i] == cur+1:
                cur = nums[i]
                count += 1
            else:
                if count == 1:
                    result.append(str(cur))
                    cur = nums[i]
                    start = nums[i]
                else:
                    result.append(str(start)+"->"+str(cur))
                    cur = nums[i]
                    start = nums[i]
                    count = 1
        if count == 1:
                result.append(str(cur))
        else:
                result.append(str(start)+"->"+str(cur))
        return result