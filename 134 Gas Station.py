#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 15:57:51 2018

@author: yiqian
"""

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        f = map(lambda x,y: x-y, gas, cost)
        if sum(gas) - sum(cost) <0:
            return -1
        lowest_gas, temp_gas, index = float('inf'), 0, 0
        for i in xrange(len(f)):
            temp_gas += f[i]
            if temp_gas < lowest_gas:
                index = i
                lowest_gas = temp_gas
        return (index+1)%len(gas)
    
    
    """
    beats 98%
    
    the trick of this problem is find the hardest time, which means the lowest gas we have during the trip
    after this time, things get better
    """