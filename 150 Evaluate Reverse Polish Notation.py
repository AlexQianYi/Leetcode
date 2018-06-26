#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 15:34:49 2018

@author: yiqian
"""

import operator

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = list()
        ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
        for token in tokens:
            if token in ops:
                t1 = int(stack.pop())
                t2 = int(stack.pop())
                res = ops[token](t2, t1)
                stack.append(res)
            else:
                stack.append(token)
        return int(stack.pop())
    
    """
    basic Polish calculation
    but the divide operation is kind of different
    the main idea is use stack !!
    """
    
    
"""
class Solution(object):
    def evalRPN(self, tokens):

        :type tokens: List[str]
        :rtype: int

        op = ["+", "-", "*", "/"]
        i = 0
        number = []
        while i<len(tokens):
            if tokens[i] in op:
                num2 = number.pop()
                num1 = number.pop()
                res = self.calculation(tokens[i], num1, num2)
                number.append(res)
            else:
                number.append(tokens[i])
            i+=1
        return int(number[0])
    
    def calculation(self, op, nums1, nums2):
        print(nums1, op, nums2)
        if op=='+':
            return str(int(nums1) + int(nums2))
        if op=='-':
            return str(int(nums1) - int(nums2))
        if op=='*':
            return str(int(nums1) * int(nums2))
        if op=='/':
            if abs(int(nums1))<abs(int(nums2)):
                return str(0)
            else:
                return str(int(int(nums1) / int(nums2)))
"""