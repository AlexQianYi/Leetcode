#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 17:11:35 2018

@author: yiqian
"""

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or head.next == None:
            return True
        count = 0
        currHead = head
        while(currHead):
            count += 1
            currHead = currHead.next 
        numReverse = count/2
        count = 1
        currHead = head 
        while(count <= numReverse):
            currHead = currHead.next
            count += 1
        nextNode = currHead.next
        currHead.next = None 
        while(nextNode):
            temp = nextNode.next
            nextNode.next = currHead
            currHead = nextNode
            nextNode = temp 
        
        while(currHead):
            if currHead.val != head.val:
                return False
            currHead = currHead.next
            head = head.next
        
        return True