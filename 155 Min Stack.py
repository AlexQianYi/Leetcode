#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 14:32:01 2018

@author: yiqian
"""

class MinStack(object):

    def __init__(self):
        self.q = []

# @param x, an integer
# @return an integer
    def push(self, x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin));


    def pop(self):
        self.q.pop()


# @return an integer
    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][0]


# @return an integer
    def getMin(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
            
        
        """
        minStack simple implement
        two operation: push() and pop() same as normal stack
        two attributes: top() like pop()
                        getMin() get min elements in remain stacks
        """