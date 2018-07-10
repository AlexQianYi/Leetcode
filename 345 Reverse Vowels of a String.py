#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 08:56:35 2018

@author: yiqian
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v="aeiouAEIOU"
        
        m1=[]
        m2=[]
        
        
        n=len(s)
        
        for i in range(0,n):
            if s[i] in v:
                m1.append(i)
                m2.append(s[i])
                
        m2=m2[::-1]
       
        
        n1=len(m1)
        
        s=list(s)
        for j in range(0,n1):
            temp=m1[j]
            s[temp]=m2[j]
            
        return "".join(s)
        """
        head, end = 0, len(s)-1
        head_find, end_find = False, False
        dic = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1, 'A':1, 'E':1, 'I':1, 'O':1, 'U':1}
        result_head, result_end = "", ""
        while head<=end:
            if s[head] in dic:
                head_find = True
            else:
                result_head += s[head]
                head += 1
            if s[end] in dic:
                end_find = True
            else:
                result_end = s[end] + result_end
                end -= 1
            if head_find and end_find:
                result_head += s[end]
                result_end = s[head] + result_end
                head_find, end_find = False, False
                head += 1
                end -= 1
                
        return result_head[:len(s) - len(result_end)] + result_end
        """