#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 16:37:11 2018

@author: yiqian
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        
        dic_1, result = {}, []
        
        for i in xrange(len(nums1)):
            dic_1[nums1[i]] = 1
            
        for i in xrange(len(nums2)):
            if nums2[i] in dic_1:
                result.append(nums2[i])
                
        return result
        
        
        """
        n1=len(nums1)
        n2=len(nums2)
        
        nums1.sort()
        nums2.sort()
        
        i=0;j=0
        
        resultlist=[]
        
        while i<n1 and j<n2:
            if nums1[i]==nums2[j]:
                resultlist.append(nums1[i])
                i+=1
                j+=1
            else:
                if nums1[i]>nums2[j]:
                    j+=1
                else:
                        i+=1
        return resultlist
        """