#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 17:22:23 2018

@author: yiqian
"""

class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        p=[float('inf')]*(N+1)
        p[K]=0

        Max=0
        Max1=0

        for y in range(N):
            for i in range(len(times)):
                if p[times[i][0]]!=-1:
                    p[times[i][1]] = min(p[times[i][0]]+times[i][2], p[times[i][1]])
                Max1=max(Max1,p[times[i][1]])
            if Max==0:
                Max=Max1
            else:
                Max=min(Max,Max1)
            Max1=0

        del p[0]
        print p

        if float('inf') in p:
            return -1


        return(Max)