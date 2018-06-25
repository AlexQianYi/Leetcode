#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 08:50:20 2018

@author: yiqian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if root == None:
            return root
        
        tempNode = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tempNode)
        
        return root
    
    
    
    """
    Invert a binary tree
    left child as right, right as left
    """