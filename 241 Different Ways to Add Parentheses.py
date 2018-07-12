#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 14:54:26 2018

@author: yiqian
"""

class Solution(object):
    def diffWaysToCompute(self, input):
            """
            :type input: str
            :rtype: List[int]
            """
            def helper(m, n, op):
                if op == "+":
                    return m + n
                elif op == "-":
                    return m - n
                else:
                    return m * n
            if input.isdigit():
                return [int(input)]
            ans = []
            for i in xrange(len(input)):
                if input[i] in "+-*":
                    left = self.diffWaysToCompute(input[:i])
                    right = self.diffWaysToCompute(input[i + 1:])
                    ans.extend([helper(l, r, input[i]) for l in left for r in right])
            return ans