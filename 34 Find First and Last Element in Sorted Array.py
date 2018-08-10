#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 22:48:06 2018

@author: yiqian
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]

        low, high = 0, len(nums) - 1
        res=[0,0]
        find = 0
        ff1,ff2=0,0

        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                find = 1
                temp1,temp2 = mid,mid
                while (nums[temp1]==target or nums[temp2]==target) and (ff1==0 or ff2==0):
                    if nums[temp1]==target:
                        res[0] = temp1
                        if temp1-1>=0:
                            temp1 -=1
                        else:
                            ff1 =1
                    else:
                        ff1=1
                    if nums[temp2]==target:
                        res[1] = temp2
                        if temp2+1<=len(nums)-1:
                            temp2 +=1
                        else:
                            ff2 =1
                    else:
                        ff2=1
                break
            if nums[mid]>target:
                high = mid - 1
            else:
                low = mid + 1
        if find:
            return res
        else:
            return [-1,-1]