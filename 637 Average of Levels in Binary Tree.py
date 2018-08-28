#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 23:22:40 2018

@author: yiqian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        nodeList = [[]]
        
        def visit(node, level):
            if not node:
                return 
            
            if len(nodeList) <= level:
                nodeList.append([])
            nodeList[level].append(node.val)
            visit(node.left, level+1)
            visit(node.right, level+1)
            
        visit(root, 0)
        result = []
        for line in nodeList:
            l = len(line)
            s = sum(line)
            result.append(float(s)/l)

        return result
        
        