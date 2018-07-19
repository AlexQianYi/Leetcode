#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 21:37:35 2018

@author: yiqian
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp = ListNode(0)
        if head == None:
            return head
        while head!=None and head.val == val:
            head = head.next
        if head == None:
            return None
        result = head
        
        while head.next:
            print(head.val)
            if head.next.val == val:
                dummp = head.next
                while dummp!=None and dummp.val == val:
                    dummp = dummp.next
                if dummp == None:
                    head.next = None
                    break
                else:
                    head.next = dummp
            head = head.next
        return result