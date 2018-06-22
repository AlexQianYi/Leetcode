#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 15:47:31 2018

@author: yiqian
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
    
        slow = head
        if head.next:
            fast = head.next
        else:
            return False
        
        while slow is not fast:
            if slow.next:
                slow = slow.next
            else:
                return False
            if not fast.next or not fast.next.next:
                return False
            else:
                fast = fast.next.next

        return True
    
    """
    determine whether there is a cycle in linked list
    two pointers, one fast one slow
    if there is cycle, the fast pointer must can catch slow pointer 
    """