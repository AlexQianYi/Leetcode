#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:09:24 2018

@author: yiqian
"""

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0 for i in xrange(amount+1)]
        dp[0] = 1
        for ele in coins:
            for i in xrange(ele, amount+1):
                dp[i] += dp[i-ele]
                
        return dp[amount]