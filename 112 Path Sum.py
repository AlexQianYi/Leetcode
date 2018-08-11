#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 23:12:06 2018

@author: yiqian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        def visitNode(root, tempsum ,sumList):
            
            if root.left or root.right:
                if root.left:
                    visitNode(root.left, tempsum+root.val, sumList)
                if root.right:
                    visitNode(root.right, tempsum+root.val, sumList)
            else:
                sumList.append(tempsum+root.val)
        
        sumList = []
        visitNode(root, 0, sumList)
        print(sumList)
        if sum in sumList:
            return True
        else:
            return False