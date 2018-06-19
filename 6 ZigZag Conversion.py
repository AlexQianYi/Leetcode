#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 10:49:04 2018

@author: yiqian
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        group_num = 2*numRows-2
        l = len(s)
        if (l<=numRows or numRows == 1):
            return s
        result = ""
        
        if (l%group_num==0):
            num_group = l/group_num
        else:
            num_group = l/group_num+1
        
        for i in xrange(num_group):
            if i*group_num >= l:
                break
            result += s[i*group_num]
        
        for j in xrange(1, numRows-1):
            for i in xrange(num_group):
                if i*group_num+j >= l:
                    break
                result += s[i*group_num+j]
                if (i+1)*group_num-j >= l:
                    break
                result += s[(i+1)*group_num-j]
        for i in xrange(num_group):
            if i*group_num+numRows-1 >= l:
                break
            result += s[i*group_num+numRows-1]
            
        return result