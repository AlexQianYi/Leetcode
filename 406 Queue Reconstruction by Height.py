#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 10:11:45 2018

@author: yiqian
"""

class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key=lambda x: (x[0],-x[1]), reverse=True)
        res = []
        for i in range(len(people)):
            res.insert(people[i][1],people[i])
        return res