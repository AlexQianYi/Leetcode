#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 10:06:00 2018

@author: yiqian
"""

class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        
        max_gap = 0
        start = 0
        
        i = 0
        while seats[i] == 0:
            i += 1
            max_gap += 1
        
        max_gap *=2
        gap = 0
        i+= 1
        while i<len(seats):
            if seats[i]==1:
                if gap>max_gap:
                    max_gap = gap
                gap = 0
            else:
                gap += 1
            i += 1
        if gap>int((max_gap-1)/2)+1:
            return gap
        else:
            return int((max_gap-1)/2)+1
        
        
"""
    calculcate the max distance to the closest person in row
    two sides situation need to consider
    
    0,0,0,1,1.....
    .....1,0,0,0,0,0
""""