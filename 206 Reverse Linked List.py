#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 09:32:12 2018

@author: yiqian
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        NodeList = []
        while head:
            NodeList.append(head.val)
            head = head.next
        result = result_head = ListNode(0)
        
        for i in range(len(NodeList)-1, -1, -1):
            result_head.next = ListNode(NodeList[i])
            result_head = result_head.next
            
        return result.next