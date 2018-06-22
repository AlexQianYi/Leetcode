#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 09:05:25 2018

@author: yiqian
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        temp = digits[::-1]
        count, start = 0, 1
        for i in xrange(len(temp)):
            if temp[i]+count+start>9:
                temp[i] = temp[i]+count+start-10
                count = 1
            else:
                temp[i] = temp[i]+count+start
                count = 0
            start = 0
        if count:
            temp.append(1)
            
        return temp[::-1]
    
    
    """
    the list represent a number, plus 1 at end of list
    """