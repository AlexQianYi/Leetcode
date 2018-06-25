#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:41:31 2018

@author: yiqian
"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        result = [0]
        for i in range(1, num+1):
            result.append(result[i>>1]+i%2)
        return result
    
    """
    Counting Bits of every number
    
    (0) (1) (1 2) (1 2 2 3) (1 2 2 3 2 3 3 4) ......
    find rules 
    copy previous result -- 1st part
    add 1 to previouse result -- 2st part
    """