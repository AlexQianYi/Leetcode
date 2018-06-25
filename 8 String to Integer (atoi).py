#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 17:28:53 2018

@author: yiqian
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        count=0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        temp = ""
        temp_str = ""
        
        for i in xrange(len(str)):
            if str[i] != " ":
                temp_str = str[i:]
                break
                
        if not temp_str:
            return 0
        
        for i in xrange(len(temp_str)):
            if temp_str[i]=="+" or temp_str[i]=="-" or (temp_str[i]>="0" and temp_str[i]<="9"):
                number = 0
                if temp_str[i] == "-" or temp_str[i] == "+":
                    if temp_str[i]=="-":
                        count +=1
                    i+=1
                while i < len(temp_str) and temp_str[i]>="0" and temp_str[i]<="9":
                    temp += temp_str[i]
                    number = number*10 + int(temp_str[i])
                    i+=1
                if temp=="":
                    return 0
                else:
                    res = pow(-1, count)*number
                    if res > INT_MAX:
                        return INT_MAX
                    if res < INT_MIN:
                        return INT_MIN
                    return res
            else:
                return 0
        return 0