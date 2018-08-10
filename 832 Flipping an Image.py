#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 21:51:46 2018

@author: yiqian
"""

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for line in A:
            temp = []
            for ele in line:
                if ele == 1:
                    temp.append(0)
                else:
                    temp.append(1)
            result.append(temp[::-1])
        return result