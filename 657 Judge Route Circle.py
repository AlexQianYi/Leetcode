#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:54:38 2018

@author: yiqian
"""

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        upCount, downCount, leftCount, rightCount = 0, 0, 0, 0
        for i in range(len(moves)):
            if moves[i] == 'U':
                if downCount==0:
                    upCount += 1
                else:
                    downCount -= 1
            elif moves[i] == 'D':
                if upCount == 0:
                    downCount += 1
                else:
                    upCount -= 1
            elif moves[i] == 'L':
                if rightCount == 0:
                    leftCount += 1
                else:
                    rightCount -= 1
            else:
                if leftCount == 0:
                    rightCount += 1
                else:
                    leftCount -= 1
        if upCount==0 and downCount==0 and leftCount==0 and rightCount==0:
            return True
        else:
            return False