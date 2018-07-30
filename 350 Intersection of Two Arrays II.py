#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 09:16:49 2018

@author: yiqian
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        dic1, dic2 = {}, {}
        
        for i in xrange(len(nums1)):
            if nums1[i] in dic1:
                dic1[nums1[i]] += 1
            else:
                dic1[nums1[i]] = 1
        
        result = []
        for i in xrange(len(nums2)):
            if nums2[i] in dic1 and dic1[nums2[i]] > 0:
                result.append(nums2[i])
                dic1[nums2[i]] -= 1
        return result
    
    """
    beats 100
    """
        
        """
        a=set(nums1)
        b=set(nums2)
        
        j=a&b
        result=list(j)
        
        for i in j:
            f1=nums1.count(i)
            f2=nums2.count(i)
            if f1>1 and f2>1:
                n=min(f1,f2)
                while n>1:
                    result.append(i)
                    n=n-1
                    
        return result
        """