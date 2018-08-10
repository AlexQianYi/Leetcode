#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 22:17:50 2018

@author: yiqian
"""

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        dic = {}
        for ele in secret:
            if ele in dic:
                dic[ele] += 1
            else:
                dic[ele] = 1
        bull, cow = 0, 0
        for i in xrange(len(guess)):
            if guess[i] == secret[i]:
                bull += 1
                dic[secret[i]] -= 1
        
        for i in xrange(len(guess)):
            if guess[i] in dic and dic[guess[i]] >0 and guess[i] != secret[i]:
                cow += 1
                dic[guess[i]] -= 1
        return str(bull) + "A" + str(cow) + "B"