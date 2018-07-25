#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 22:47:12 2018

@author: yiqian
"""

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        i = 0
        for j in xrange(1, len(num)):
            for k in xrange(j+1, len(num)):
                if j>1 and num[0] == '0' or k-j>1 and num[j] == '0':
                    continue
                tempStr = str(int(num[:j]) + int(num[j:k]))
                if tempStr == num[k:k+len(tempStr)]:
                    if k+len(tempStr) == len(num):
                        return True
                    if self.isAdditiveNumber(num[j:]):
                        return True
        return False
    
    """
    just follow the rule of question
    """