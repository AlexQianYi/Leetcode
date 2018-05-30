#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 23:48:20 2018

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
        
        l1List, l2List = [], []
        
        if l1==None:
            return l2
        if l2==None:
            return l1
        
        while l1!=None:
            l1List.append(l1.val)
            l1 = l1.next
        
        while l2!=None:
            l2List.append(l2.val)
            l2 = l2.next
            
        l1Len, l2Len = len(l1List), len(l2List)
        if l1Len>l2Len:
            maxList, minList = l1List, l2List
            maxL, minL = l1Len, l2Len
        else:
            maxList, minList = l2List, l1List
            maxL, minL = l2Len, l1Len
        
            
        i, c = -1, 0
        result = []
        
        while abs(i)<=maxL:
            if abs(i)>minL:
                if c==0:
                    result = maxList[:i+1] + result
                    return result
                else:
                    tempSum = (maxList[i] + c)%10
                    c = (maxList[i]+c)/10
                    result = [tempSum] + result
                    i -= 1
            else:
                tempSum = (maxList[i] + minList[i] + c)%10
                c = (maxList[i] + minList[i] + c)/10
                result = [tempSum] + result
                i -= 1
        if c==1:
            result = [1] + result

        Point = Head = ListNode(result[0])
        for i in range(1, len(result)):
            Head.next = ListNode(result[i])
            Head = Head.next
        return Point
        
    
    """
    Add Two Numbers II
    the input is two linked nodes
    """