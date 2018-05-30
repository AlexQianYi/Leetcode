#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 19:19:42 2018

@author: yiqian
"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        result = ""
        
        l1, l2 = len(num1), len(num2)
        if l1>l2:
            maxStr, minStr = num1, num2
            maxL, minL = l1, l2
        else:
            maxStr, minStr = num2, num1
            maxL, minL = l2, l1
        
        if minStr == "0":
            return maxStr
            
        i, c = -1, 0
        
        while abs(i)<=maxL:
            if abs(i)>minL:
                if c==0:
                    result = maxStr[:i+1] + result
                    return result
                else:
                    tempSum = (int(maxStr[i]) + c)%10
                    c = (int(maxStr[i])+c)/10
                    result = str(tempSum) + result
                    i -= 1
            else:
                tempSum = (int(maxStr[i]) + int(minStr[i]) + c)%10
                c = (int(maxStr[i]) + int(minStr[i]) + c)/10
                result = str(tempSum) + result
                i -= 1
        if c==0:
            return result
        else:
            return "1"+result
                
        
        """
        add string
        """