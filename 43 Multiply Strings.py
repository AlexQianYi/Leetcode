#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 15:37:24 2018

@author: yiqian
"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        table = [[0 for c in range(len(num2))] for r in range(len(num1))]
        
        for r in range(len(num1)):
            for c in range(len(num2)):
                table[r][c] = (int(num1[r]) * int(num2[c]))
        
        visited = {}
        currentDiagonals = [(len(num1)-1, len(num2)-1)]
        nextDiagonals = []     
        ret = []
        currentSum = 0
        
        while currentDiagonals:
            coord = currentDiagonals.pop()
            currentSum += table[coord[0]][coord[1]]
            
            left = (coord[0], coord[1]-1)
            if left[1] >= 0 and left not in visited:
                nextDiagonals.append(left)
                visited[left] = True
            
            up = (coord[0]-1, coord[1])
            if up[0] >= 0 and up not in visited:
                nextDiagonals.append(up)
                visited[up] = True
            
            if not currentDiagonals:
                ret.append(str(currentSum % 10))
                currentSum = currentSum / 10
                currentDiagonals = nextDiagonals
                nextDiagonals = []
                
        if currentSum > 0:
            ret.append(str(currentSum))
            
        return "".join(reversed(ret)).lstrip("0") or "0"