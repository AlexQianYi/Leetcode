#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 10:05:01 2018

@author: yiqian
"""

class Solution(object):
    
    def letterCombinations(self, digits):
        if not digits:
            return []
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        self.dfs(digits, dic, 0, "", res)
        return res

    def dfs(self, digits, dic, index, path, res):
        if len(path) == len(digits):
            res.append(path)
            return 
        for i in xrange(index, len(digits)):
            for j in dic[digits[i]]:
                self.dfs(digits, dic, i+1, path+j, res)
                
                
    
    """
    DFS
    path save the temp string of buttons
    if the length of path equal to digits then result append string
    
    
    generate all combination can use DFS algorithm!!!
    """