#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 11:07:07 2018

@author: yiqian
"""

class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        
        if len(hand)<W or len(hand)%W!=0:
            return False
        
        hand.sort()
        
        temp_list = hand
        for i in range(int(len(hand)/W)):
            label, L = self.removeContinue(temp_list, W)
            if not label:
                return False
        return True
                
    def removeContinue(self, L, W):
        
        count, i = 1, 0
        start = L[0]
        L.remove(start)
        while count<W:
            if i<len(L):
                if L[i] == start:
                    i += 1
                else:
                    if L[i] -1 == start:
                        count += 1
                        start = L[i]
                        L.remove(start)
                    else:
                        return False, L
            else:
                return False, L
        return True, L
    
    """
    give a list, find whether it can be split to len(l)/W  W continues sub strings
    
    shun zi 
    """