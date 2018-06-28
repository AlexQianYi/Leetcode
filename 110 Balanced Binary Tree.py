#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 10:14:42 2018

@author: yiqian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        
        def visitNode(root, deep ,deepList):
            print(deepList)
            
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
        
        deepList = [0]
        visitNode(root, 0, deepList)
        if max(deepList)-min(deepList)<=1:
            return True
        else:
            return False