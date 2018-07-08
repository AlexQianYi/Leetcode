#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 17:31:44 2018

@author: yiqian
"""

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        #mirror reject gray code!!
        #233333
        #wo shi tiancai
        if n==0:
            return [0]
        
        res = []
        upList = ["0"]
        downList = ["1"]
        
        for i in xrange(1, n):
            tempList = upList+downList
            for i in xrange(len(tempList)):
                if i >= len(upList):
                    upList.append("0"+tempList[i])
                else:
                    upList[i] = "0"+tempList[i]
                
                index = (-1)*i-1
                if i >= len(downList):
                    downList.append("1"+tempList[index])
                else:
                    downList[i] = "1"+tempList[index]

        
        for i in xrange(len(upList)):
            res.append(int(upList[i], 2))
        for i in xrange(len(downList)):
            res.append(int(downList[i], 2))
        return res