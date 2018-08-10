#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 22:43:52 2018

@author: yiqian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        def dfs(node, path, result):
            if node.right == None and node.left == None:
                path += str(node.val)
                result.append(path)
                return 
            else:
                path = path + str(node.val) + "->"
                if node.left != None:
                    dfs(node.left, path, result)
                if node.right != None:
                    dfs(node.right, path, result)
                    
        if not root:
            return []
        result = []
        dfs(root, "", result)
        return result