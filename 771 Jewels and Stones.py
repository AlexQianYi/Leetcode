#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 16:11:16 2018

@author: yiqian
"""

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        if not J:
            return 0
        S_dic = {}
        
        for i in range(len(S)):
            if S[i] in S_dic:
                S_dic[S[i]] += 1
            else:
                S_dic[S[i]] = 1
        
        result = 0
        for i in range(len(J)):
            if J[i] in S_dic:
                result += S_dic[J[i]]
                
        return result