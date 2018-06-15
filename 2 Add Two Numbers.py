#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 14:29:28 2018

@author: yiqian
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = n =  ListNode(0)
        c = 0
        tmp=0
        while l1!=None or l2!=None or c:
            v1=v2=0
            if l1!=None:
                v1 = l1.val
                l1 = l1.next
            if l2!=None:
                v2 = l2.val
                l2 = l2.next
            c, tmp = divmod(v1+v2+c, 10)
            n.next = ListNode(tmp)
            n = n.next
        return res.next
    
    
    """
    ListNode visit problem 
    """