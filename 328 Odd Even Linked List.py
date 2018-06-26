#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:25:30 2018

@author: yiqian
"""

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next: return head
        
        odd = head
        even = head.next
        firstEven = even
        
        while even and even.next:
            tempOdd = even.next
            tempEven = tempOdd.next
            
            odd.next = tempOdd
            tempOdd.next = firstEven
            even.next = tempEven

            odd = tempOdd
            even = tempEven
        
        return head
    
    
    """
    Odd Even link list
    
    1-2-3-4-5-6-7-8-9
    
    1-odd
    2-even
    2-firsteven
    
    3-tempodd
    4-tempeven
    
    1-next - 3
    3-next - 2
    2-next - 4
    3-odd
    4-even
    
    """