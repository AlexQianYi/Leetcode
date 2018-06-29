#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 14:50:33 2018

@author: yiqian
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        if not head:
            return None
        visited = {}
        
        while head.next:
            if head.next in visited:
                return head.next
            else:
                visited[head]=1
                head=head.next
        return None