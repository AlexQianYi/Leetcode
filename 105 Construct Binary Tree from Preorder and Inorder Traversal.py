#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 10:38:46 2018

@author: yiqian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        def visitNode(preorder, inorder):
            if not inorder:
                return None
            indexroot = preorder[0]
            root = TreeNode(indexroot)
            index = inorder.index(indexroot)
            if len(inorder)-1==index:
                root.left = visitNode(preorder[1:], inorder[:index])
                return root
            elif index==0:
                root.right = visitNode(preorder[1:], inorder[1:])
                return root
            else:
                root.left = visitNode(preorder[1:index+1], inorder[0:index])
                root.right = visitNode(preorder[index+1:], inorder[index+1:])
                return root
        
        return visitNode(preorder, inorder)