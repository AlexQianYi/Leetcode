#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 21:10:50 2018

@author: yiqian
"""

class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits)==1:
            return True
        
        if bits[-2]==0:
            return True
        
        return not self.isOneBitEnd(bits[:-1])
    
    def isOneBitEnd(self, bits):
        if len(bits)==1:
            return True
        else:
            if bits[-2]==0:
                return True
            else:
                if self.isOneBitEnd(bits[:-1]):
                    return False
                else:
                    return True
    
    """
    # whether is the final 1 bit 1
    def isOneBit1End(self, bits):
        if len(bits)==1:
            return True
        else:
            if bits[-2]==0:
                return True
            else:
                if self.isOneBit1End(bits[:-1]):
                    return False
                else:
                    return True
    
    # whether is the final 1 bit 0
    def isOneBit0End(self, bits):
        if len(bits)==1:
            return True
        else:
            if bits[-2]==0:
                return True
            else:
                if self.isOneBit1End(bits[:-1]):
                    return False
                else:
                    return True
    """
        
    
"""
in this question we need to find the explation of a given sequence, then determine whether the last number 0 is 1 bit
it must can be solved by recrusive, but we don't know whether it can be solve by DP
So I try to split original question by two sub question first:
        whether the final 1 is 1 bit
        whether the final 0 is 1 bit
but I found they they are same.....

    x x x x ... x t z
    1. if t is 0, z must be 1 bit final. Because 0 can't be the start of 2 bit
    2. if t is 1, and t is 1 bit final, it must combine with z as 11 or 10
    3. if t is 1, and t is 2 bit final, z must be 1 bit final
"""