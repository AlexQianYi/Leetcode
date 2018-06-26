#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 14:52:46 2018

@author: yiqian
"""

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        
        def visit(i, j):
            if 0<=i<len(board) and 0<=j<len(board[0]) and board[i][j]=='X':
                board[i][j]='O'
                map(visit, (i-1, i, i, i+1), (j, j+1, j-1, j))
                return
            return 
        
        res = 0
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j]=='X':
                    visit(i, j)
                    res +=1
        return res