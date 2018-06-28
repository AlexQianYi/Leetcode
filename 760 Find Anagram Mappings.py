#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 10:29:56 2018

@author: yiqian
"""

class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        result, dic_B = [], {}
        for i in xrange(len(B)):
            if B[i] in dic_B:
                dic_B[B[i]].append(i)
            else:
                dic_B[B[i]] = [i]
        
        for i in xrange(len(A)):
            result.append(dic_B[A[i]][0])
            del dic_B[A[i]][0]
        
        return result