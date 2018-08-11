#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 11:31:29 2018

@author: yiqian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def dfs(node, nodelist):
            if node == None:
                return
            nodelist.append(node.val)
            dfs(node.left, nodelist)
            dfs(node.right, nodelist)
            
        nodelist = []
        dfs(root, nodelist)
        sortlist = sorted(nodelist)
        return sortlist[k-1]