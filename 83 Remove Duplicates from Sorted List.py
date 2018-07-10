#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 10:40:12 2018

@author: yiqian
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        fast, slow = head.next, head
        while True:
            if fast.val==slow.val:
                if fast.next == None:
                    slow.next = None
                    break
                else:              
                    fast = fast.next
            else:
                slow.next = fast
                slow = slow.next
                if fast.next==None:
                    break
                else:
                    fast = fast.next
                    
        return head