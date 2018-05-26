#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 12:35:18 2018

@author: yiqian
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        start, end = -2, -1
        
        for i in range(len(flowerbed)):
            if flowerbed[i]==1:
                end = i
                count += self.helper(start, end)
                start = end
        if start!= len(flowerbed)-1:
            count += self.helper(start, len(flowerbed)+1)
        return count >= n

    def helper(self, start, end):
        print(start, end)
        if end - start <= 3:
            return 0
        else:
            return (end-start-3-1)/2+1
        
        
        
        """
        the adjacent places can't put flowers 
        1. write a helper function to calculate the available positions between two adjacent "1"
        2. consider the start part and end part situation
        
        """