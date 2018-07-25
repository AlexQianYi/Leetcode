#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 22:55:24 2018

@author: yiqian
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        my="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
           
        if n<27:
            return my[n-1]
        
        n=n-1
        result=""
        flag=0
        a=n%26
        n=n//26
        result=my[a]+result
        while n>0:
                if n<27:
                    result=my[n-1]+result
                    break
                a=n%26
                n=n//26 
                result=my[a-1]+result

            
        return result