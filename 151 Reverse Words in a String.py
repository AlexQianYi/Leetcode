#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 16:21:57 2018

@author: yiqian
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        temp_s = s.split()
        if len(temp_s) == 0:
            return ""
        result = temp_s[-1]
        for i in range(len(temp_s)-2, -1, -1):
            result = result + " " + temp_s[i]
            
        return result
        
        """
        if not s:
            return s
        x = 0
        while x<len(s) and s[x]==" ":
            x+=1
        if x==len(s):
            return ""
        res = ""
        cur = x
        print(x)
        for i in xrange(x, len(s)):
            print(res)
            if s[i]==" ":
                res = s[cur:i]+res
                res = " "+res
                cur = i+1
        res = s[cur:]+res
        y=0
        while y<len(res) and res[y]==" ":
            y+=1
        return res[y:]
        """
        
        
        """
        two methods, one use split method, other use normal methods
        """