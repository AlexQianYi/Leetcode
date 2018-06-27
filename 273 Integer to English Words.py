#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 13:59:47 2018

@author: yiqian
"""

class Solution(object):
    def __init__(self):
    self.lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    self.thousands = ["","Thousand","Million","Billion"]

def numberToWords(self, num):
    if num == 0:
        return "Zero"
    res = ""
    for i in range(len(self.thousands)):
        if num % 1000 != 0:
            res = self.helper(num*00) + self.thousands[i] + " " + res
        num /= 1000
    return res.strip()

def helper(self, num):
    if num == 0:
        return ""
    elif num < 20:
        return self.lessThan20[num] + " "
    elif num < 100:
        return self.tens[num/10] + " " + self.helper(num)
    else:
        return self.lessThan20[num/100] + " Hundred " + self.helper(num0)