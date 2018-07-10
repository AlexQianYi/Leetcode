#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 09:04:41 2018

@author: yiqian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSameTree(p, q):
            if p and q:
                return p.val == q.val and isSameTree(p.left, q.right) and isSameTree(p.right, q.left)
            return p is q
        
        if not root:
            return True
            
        return isSameTree(root.left, root.right)