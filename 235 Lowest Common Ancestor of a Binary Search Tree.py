#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 16:16:28 2018

@author: yiqian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        while root:
            if root.val > q.val and root.val > p.val:
                root = root.left
            elif root.val < q.val and root.val <p.val:
                root = root.right
            else:
                return root
            
            
        """
        find lowest common ancestor problem 
        the main idea is 
        if   node x is the lowes common ancestor of node p and q
             p.val < x.val < q.val
        """