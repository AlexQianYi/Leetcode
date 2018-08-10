#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 22:45:54 2018

@author: yiqian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        def visitNode(root, deep ,deepList):
            
            if not root:
                return 
            if not root:
                deepList.append(deep)
            
            if root.left or root.right:
                if root.left:
                    visitNode(root.left, deep+1, deepList)
                if root.right:
                    visitNode(root.right, deep+1, deepList)
            else:
                deepList.append(deep)
        
        deepList = []
        visitNode(root, 1, deepList)
        return min(deepList)