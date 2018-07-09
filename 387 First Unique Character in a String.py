#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 14:19:39 2018

@author: yiqian
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        dic, queue = {}, []
        for i in xrange(len(s)):

            if s[i] in dic and dic[s[i]] != -1:
                queue.remove(dic[s[i]])
                dic[s[i]] = -1
            elif s[i] in dic and dic[s[i]] == -1:
                continue
            else:
                dic[s[i]] = i
                queue.append(i)
        
        if not queue:
            return -1
        else:
            return queue[0]