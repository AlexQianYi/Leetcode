#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 23:05:56 2018

@author: yiqian
"""

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        save={}
        def helper(node):
            if node is None:
                return None
            current=UndirectedGraphNode(node.label)
            save[node]=current
            
            for n in node.neighbors:
                if n in save:
                    current.neighbors.append(save[n])
                    continue
                else:
                    save[n]=helper(n)
                    current.neighbors.append(save[n])
            
            return current
        return helper(node)