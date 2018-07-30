#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:45:15 2018

@author: yiqian
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        result=""
        a=numerator//denominator
        if numerator<0 and denominator>0:
            numerator=-numerator
            result+="-"
        elif numerator>0 and denominator<0:
            denominator=-denominator
            result+="-"
        elif numerator<0 and denominator<0:
            denominator=-denominator
            numerator=-numerator
        
        a=numerator//denominator
        result+=str(a)
        flag=0
        b=(numerator%denominator)*10
        save_i={}
        i=0
        save_result=[]
        while b!=0:
            if flag==0:
                flag=1
                result+="."
            a=b//denominator
            if b in save_i:
                t=save_i[b]
                result+=''.join(save_result[:t])
                temp_s=''.join(save_result[t:])
                result+="("+temp_s+")"
                return result
            save_i[b]=i
            save_result.append(str(a))
            b=(b%denominator)*10
            i+=1
        result+=''.join(save_result)
        return result