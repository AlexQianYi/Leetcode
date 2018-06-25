#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:13:04 2018

@author: yiqian
"""

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        if left<10:
            for i in range(left, min(right, 9)+1):
                result.append(i)
        if right<10:
            return result
        for i in range(max(10, left), right+1):
            temp = i
            flag = True
            while temp>0:
                if temp%10 == 0 or i%(temp%10) != 0:
                    flag = False
                    break
                else:
                    temp = int(temp/10)
            if flag:
                result.append(i)
                
        return result
    
    
    """
    know the rules of self dividing number. EASY!
    """