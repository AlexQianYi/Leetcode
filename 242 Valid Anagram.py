#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 09:25:17 2018

@author: yiqian
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s)!=len(t):
            return False
        
        dic = {}
        for i in xrange(len(s)):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1
                
        for i in xrange(len(t)):
            if t[i] not in dic:
                return False
            elif dic[t[i]] == 0:
                return False
            else:
                dic[t[i]] -= 1
        return True
        
        
        """
        sset=set(s)
        tset=set(t)
        
        if len(sset)!=len(tset):
            return False
        
        for i in sset:
            if s.count(i)!=t.count(i):
                return False
        return True
        
        use count is more efficient 
        
        """
        
        
        