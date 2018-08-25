#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 18:50:24 2018

@author: yiqian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def visit(start, t):
            if not t and not start:
                return True

            if ((start == None) and t) or ((t == None) and start) or (start.val != t.val):
                return False
            else:
                left = visit(start.left, t.left)
                right = visit(start.right, t.right)
                return left and right
            
        def findnode(s, x):
            if not s:
                return False
            if s.val == x:
                if visit(s, t):
                    return True
            findnode(s.left, x) or findnode(s.right, x)
        
        if findnode(s, t.val) == False:
            return False
        else:
            return True