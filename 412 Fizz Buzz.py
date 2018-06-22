#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 16:13:29 2018

@author: yiqian
"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        result = []
        for i in range(1, n+1):
            if i%15 == 0:
                result.append('FizzBuzz')
            elif i%5 == 0:
                result.append('Buzz')
            elif i%3 == 0:
                result.append('Fizz')
            else:
                result.append(str(i))
        return result
    