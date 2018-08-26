#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 13:25:03 2018

@author: yiqian
"""

class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numbers = []
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.numbers.append(number)
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        dic = {}
        for i in xrange(len(self.numbers)):
            if value - self.numbers[i] in dic:
                return True
            else:
                dic[self.numbers[i]] = 1
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)