#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 16:44:08 2018

@author: yiqian
"""

        
        """
        zeroNum, oneNum = self.cost(strs[0], 0), self.cost(strs[0], 1)
        if len(strs) == 1:
            if zeroNum<=m and oneNum<=n:
                return 1
            else:
                return 0
        
        if zeroNum<=m and oneNum<=n:
            return max(1+self.findMaxForm(strs[1:], m-zeroNum, n-oneNum), self.findMaxForm(strs[1:], m, n))
        else:
            return self.findMaxForm(strs[1:], m, n)
    
    def cost(self,s, num):
        count = 0
        for i in range(len(s)):
            if s[i]==str(num):
                count += 1
        return count 
        """
        
        """
        beautiful recursion, but time out limiation
        """