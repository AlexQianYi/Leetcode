#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 16:10:16 2018

@author: yiqian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and root.right:
            return 1 + self.countNodes(root.left) +self.countNodes(root.right)
        elif root.left and not root.right:
            return 1 + self.countNodes(root.left)
        elif root.right and not root.left:
            return 1 + self.countNodes(root.right)
        else:
            return 1