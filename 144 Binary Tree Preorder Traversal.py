#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 17:17:28 2018

@author: yiqian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
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
                res.append(root.val)
                TreeTravel(root.left, res)
                TreeTravel(root.right, res)
                
        res = []
        TreeTravel(root, res)
        return res