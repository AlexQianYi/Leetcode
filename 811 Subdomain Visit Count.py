#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 13:10:59 2018

@author: yiqian
"""

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dic = {}
        for ele in cpdomains:
            list1 = ele.split(" ")
            time = list1[0]
            org_domain = list1[1]
            list2 = org_domain.split('.')
            list2 = list2[::-1]
            temp = list2[0]
            if temp not in dic:
                dic[temp] = int(time)
            else:
                dic[temp] += int(time)
            for i in xrange(1, len(list2)):
                temp = list2[i] + "." + temp
                if temp not in dic:
                    dic[temp] = int(time)
                else:
                    dic[temp] += int(time)
        
        result = []
        for key in dic:
            result.append(str(dic[key]) + " " + key)
            
        return result
                
        