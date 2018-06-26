#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 15:44:37 2018

@author: yiqian
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        one, two, three, four, five, six, seven, eight, nine = [],[],[],[],[],[],[],[],[]
        onev, twov, threev, fourv, fivev, sixv, sevenv, eightv, ninev = [],[],[],[],[],[],[],[],[]
        line = []
        count = 0
        for i in xrange(9):
            line = []
            for j in xrange(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in line:
                    return False
                else:
                    line.append(board[i][j])
                    
                if j==0:
                    if board[i][j] in onev:
                        return False
                    else:
                        onev.append(board[i][j])
                if j==1:
                    if board[i][j] in twov:
                        return False
                    else:
                        twov.append(board[i][j])
                if j==2:
                    if board[i][j] in threev:
                        return False
                    else:
                        threev.append(board[i][j])
                if j==3:
                    if board[i][j] in fourv:
                        return False
                    else:
                        fourv.append(board[i][j])
                if j==4:
                    if board[i][j] in fivev:
                        return False
                    else:
                        fivev.append(board[i][j])
                if j==5:
                    if board[i][j] in sixv:
                        return False
                    else:
                        sixv.append(board[i][j])
                if j==6:
                    if board[i][j] in sevenv:
                        return False
                    else:
                        sevenv.append(board[i][j])
                if j==7:
                    if board[i][j] in eightv:
                        return False
                    else:
                        eightv.append(board[i][j])
                if j==8:
                    if board[i][j] in ninev:
                        return False
                    else:
                        ninev.append(board[i][j])
                        
                if i>=0 and i<3 and j>=0 and j<3:            #one
                    if board[i][j] in one:
                        return False
                    else:
                        one.append(board[i][j])
                if i>=3 and i<6 and j>=0 and j<3:           #two
                    if board[i][j] in two:
                        return False
                    else:
                        two.append(board[i][j])
                if i>=6 and i<9 and j>=0 and j<3:           #three
                    if board[i][j] in three:
                        return False
                    else:
                        three.append(board[i][j])
                if i>=0 and i<3 and j>=3 and j<6:            #four
                    if board[i][j] in four:
                        return False
                    else:
                        four.append(board[i][j])
                if i>=3 and i<6 and j>=3 and j<6:           #five
                    if board[i][j] in five:
                        return False
                    else:
                        five.append(board[i][j])
                if i>=6 and i<9 and j>=3 and j<6:           #six
                    if board[i][j] in six:
                        return False
                    else:
                        six.append(board[i][j])
                if i>=0 and i<3 and j>=6 and j<9:            #seven
                    if board[i][j] in seven:
                        return False
                    else:
                        seven.append(board[i][j])
                if i>=3 and i<6 and j>=6 and j<9:           #eight
                    if board[i][j] in eight:
                        return False
                    else:
                        eight.append(board[i][j])
                if i>=6 and i<9 and j>=6 and j<9:           #nine
                    if board[i][j] in nine:
                        return False
                    else:
                        nine.append(board[i][j])
                count+=1
    
        return True