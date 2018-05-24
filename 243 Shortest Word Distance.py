#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 09:29:21 2018

@author: yiqian
"""

class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dis = {}
        dis[word1] = -1
        dis[word2] = -1
        dis_res = len(words)
        dis_temp = 0
        for i in range(len(words)):
            if words[i] in dis:
                dis[words[i]] = i
            
            if (dis[word1] >= 0) and (dis[word2] >= 0):
                dis_temp = abs(dis[word1] - dis[word2])
                if dis_temp<dis_res:
                    dis_res = dis_temp
        
        return dis_res
    
    
"""
1. use dic to optimal second search time
2. we only need to care about the position of two specific words
3. update the temperal distance when we find word1 or word2
4. the shorest distance between two specific words must be two adjacent word1 and word2 in words seq

x x 1 2 x 2 x
"""