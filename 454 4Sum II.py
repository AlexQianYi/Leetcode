#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 10:46:02 2018

@author: yiqian
"""

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        
        dicAB = {}
        for i in range(len(A)):
            for j in range(len(B)):
                temp_sumAB = A[i]+B[j]
                dicAB[temp_sumAB] = dicAB.get(temp_sumAB, 0) + 1
                    
                    
        count = 0
        for i in range(len(C)):
            for j in range(len(D)):
                if 0-C[i]-D[j] in dicAB:
                    count += dicAB.get(0-C[i]-D[j])
        
        return count
    
    
    """
    4 Sum problem, but the input form is different
    Input 
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]

    use dictionary to reduce visit/find time
    """