#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 16:47:40 2018

@author: yiqian
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in xrange(len(s)):
            if s[i]=="(":
                stack.append("(")
            if s[i]=="[":
                stack.append("[")
            if s[i]=="{":
                stack.append("{")
            if s[i]==")":
                if len(stack)==0:
                    return False
                temp = stack.pop()
                if temp!="(" :
                    return False
            if s[i]=="]":
                if len(stack)==0:
                    return False
                temp = stack.pop()
                if temp!="[" :
                    return False
            if s[i]=="}":
                if len(stack)==0:
                    return False
                temp = stack.pop()
                if temp!="{" :
                    return False
        if len(stack)!=0:
            return False
        else:
            return True