#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 15:54:46 2018

@author: yiqian
"""

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        absList = []
        dic = {}
        for ele in arr:
            absList.append(abs(ele-x))
            if abs(ele-x) not in dic:
                dic[abs(ele-x)] = [ele]
            else:
                dic[abs(ele-x)].append(ele)
        result = []
        absList.sort()
        i = 0
        while i<k:
            l = len(dic[absList[i]])
            if l > 1:
                if k-i > l:
                    result += dic[absList[i]]
                    i += l-1
                else:
                    result += dic[absList[i]][:k-i]
                    break
            else:
                result.append(dic[absList[i]][0])
            i += 1
        result.sort()
        return result