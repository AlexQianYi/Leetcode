#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 09:48:27 2018

@author: yiqian
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.guessNum(1, n)
    
    def guessNum(self, m, n):
        mid = (m+n)//2
        if guess(mid) == 0:
            return mid
        if guess(mid) == -1:
            return self.guessNum(1, mid)
        else:
            return self.guessNum(mid+1, n)