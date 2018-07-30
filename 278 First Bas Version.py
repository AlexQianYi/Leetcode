#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 17:12:56 2018

@author: yiqian
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1)==1:
            return 1
        else:
            front=1
        back=n
        temp=(front+back)//2
        
        while 1==1:
            if (back-front)==1:
                return back
            if isBadVersion(temp)==1:
                back=temp
            else:
                front=temp
            
            temp=(front+back)//2