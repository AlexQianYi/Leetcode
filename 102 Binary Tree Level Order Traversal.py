#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 09:38:06 2018

@author: yiqian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        def append(Node, index, levelList, res):
            if Node:
                res[index].append(Node.val)
            
            if Node.left or Node.right:
                if index+1 not in levelList:
                    res.append([])
                    levelList.append(index+1)
                if Node.left:
                    append(Node.left, index+1, levelList, res)
                if Node.right:
                    append(Node.right, index+1, levelList, res)
                    
        index, res = 0, [[]]
        levelList = [0]
        append(root, index, levelList, res)
        return res