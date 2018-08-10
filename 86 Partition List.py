#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 23:09:42 2018

@author: yiqian
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head==None:
            return head
        big, small = ListNode(0), ListNode(0)
        bighead, smallhead = big, small
        while head:
            if head.val<x:
                small.next = head
                small = small.next
                head = head.next
            else:
                big.next = head
                big = big.next
                head = head.next
        big.next = None
        small.next = bighead.next
        return smallhead.next
    
    
    """
    maintain two list, one small, one big
    """