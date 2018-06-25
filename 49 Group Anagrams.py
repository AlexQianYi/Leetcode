#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 14:57:11 2018

@author: yiqian
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def sortString(s):
            l = list(s)
            l.sort()
            res = "".join(l)
            return res
        
        temp  = []
        indexList = []
        res = []
        for i in xrange(len(strs)):
            temp.append(sortString(strs[i]))
            #print(res)
            if temp[i] in indexList:
                index = indexList.index(temp[i])
                res[index].append(strs[i])
            else:
                res.append([strs[i]])
                indexList.append(temp[i])
        
        return res
    
    
    """
    find the words which have same characters
    """