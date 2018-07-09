#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 15:33:23 2018

@author: yiqian
"""

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                neighbor_num = self.getNeighborNum(board, i, j)
                if board[i][j] > 0 :
                    if neighbor_num+board[i][j]-1 > 3 or neighbor_num+board[i][j]-1 < 2:
                        board[i][j] = 0
                    else:
                        board[i][j] = 1
                    board = self.setNeighborNum(board, i, j)
                else:
                    if abs(board[i][j] - neighbor_num) == 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                    
    def setNeighborNum(self, board, i, j):
        # 9 
        if i+1<len(board) and j+1<len(board[0]):
            if board[i+1][j+1]>0:
                board[i+1][j+1] += 1
            else:
                board[i+1][j+1] -= 1
        # 7
        if i+1<len(board) and j-1>=0:
            if board[i+1][j-1]>0:
                board[i+1][j-1] += 1
            else:
                board[i+1][j-1] -= 1
        # 8
        if i+1<len(board):
            if board[i+1][j]>0:
                board[i+1][j] += 1
            else:
                board[i+1][j] -= 1
        # 6
        if j+1<len(board[0]):
            if board[i][j+1]>0:
                board[i][j+1] += 1
            else:
                board[i][j+1] -= 1
        return board
                    
    
    def getNeighborNum(self, board, i, j):
        result = 0
        # 9 
        if i+1<len(board) and j+1<len(board[0]) and board[i+1][j+1]>0:
            result += 1
        # 7
        if i+1<len(board) and j-1>=0 and board[i+1][j-1]>0:
            result += 1
        # 8
        if i+1<len(board) and board[i+1][j]>0:
            result += 1
        # 6
        if j+1<len(board[0]) and board[i][j+1]>0:
            result += 1
        return result
    
    
    
    """
    beat 100% of results! 
    
    |1|2|3|   | | | |
    |4|5|6|   | |*|6|
    |7|8|9|   |7|8|9|
    
    rules:
        only visit 6,7,8,9 nodes
        if * > 0:
            update x, x=6,7,8,9
            if x>0:
                x += 1
            else:
                x -= 1
            if x-1+N>2 and <4 (N is number of 6,7,8,9>0):
                x = 1
            else:
                x = 0
        else: (* <0)
            if abs(x-N) == 3:
                x = 1
            else:
                x = 0