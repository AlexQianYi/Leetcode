#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 16:49:23 2018

@author: yiqian
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val>l2.val:
            head = temp = l2
            l2 = l2.next
        else:
            head = temp = l1
            l1 = l1.next
        
        while l1 or l2:
            if not l1:
                while l2:
                    temp.next = l2
                    temp = temp.next
                    l2 = l2.next
                break                
            if not l2:
                while l1:
                    temp.next = l1
                    temp = temp.next
                    l1 = l1.next
                break   
            if l1.val>l2.val:
                temp.next = l2
                temp = temp.next
                l2 = l2.next
            else:
                temp.next = l1
                temp = temp.next
                l1 = l1.next
        return head