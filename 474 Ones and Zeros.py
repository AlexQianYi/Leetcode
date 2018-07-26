#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 16:44:08 2018

@author: yiqian
"""

        
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        p=[[0 for x in range(n+1)] for t in range(m+1)]
        for s in strs:
            cost_zero,cost_one=self.cost(s)
            
            
            for i in range (m,cost_zero-1,-1):
                for j in range(n,cost_one-1,-1):
                    
                    p[i][j]=max(p[i][j],p[i-cost_zero][j-cost_one]+1)
        return p[m][n]
        
        
    def cost(self,s):
        cout_zero=0
        cout_one=0
        for i in range(len(s)):
            if s[i]=='0':
                cout_zero+=1
            elif s[i]=="1":
                cout_one+=1
        return cout_zero,cout_one