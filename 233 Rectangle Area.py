#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 09:03:05 2018

@author: yiqian
"""

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        total_area = abs(C-A)*abs(D-B) + abs(E-G)*abs(H-F)
        
        if ((min(E, G)>=min(A, C) and min(E, G)<=max(A, C)) or (min(A, C)>=min(E, G) and min(A, C)<=max(E, G))) and\
        ((min(F, H)>=min(B, D) and min(F, H)<=max(B, D)) or (min(B, D)>=min(F, H) and min(B, D)<=max(F, H))):
            
            inter_area = abs(max(min(A, C), min(E, G)) - min(max(A, C), max(E, G))) * abs(max(min(B, D), min(F, H)) - min(max(B, D), max(F, H)))
                
            return total_area - inter_area
        else:
            return total_area
        
        
        """
        calculate the area which covered by rectangle 
        
        Tips: too much min max will decrease effect
        sort parameters first 
        """