#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 19:50:07 2018

@author: yiqian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def TreeTravel(root, res):
            if root==None:
                return 
            if root.left==None:
                res.append(root.val)
                TreeTravel(root.right, res)
            else:
                TreeTravel(root.left, res)
                res.append(root.val)
                TreeTravel(root.right, res)
                
        res = []
        TreeTravel(root, res)
        return res