#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 12:13:45 2018

@author: yiqian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """

        def visit(node, nodeList):
            if node == None:
                return
            if node.left != None:
                visit(node.left, nodeList)
            nodeList.append(node.val)
            if node.right != None:
                visit(node.right, nodeList)
            return 
        
        nodeList = []
        visit(root, nodeList)
        print(nodeList)
        for i in xrange(len(nodeList)-1):
            if nodeList[i] == p.val:
                return nodeList[i+1]
        return None