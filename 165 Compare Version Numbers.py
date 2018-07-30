#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 09:07:40 2018

@author: yiqian
"""

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l1, l2 = version1.split('.'), version2.split('.')
        lmin, lmax = min(len(l1), len(l2)), max(len(l1), len(l2))
        for i in xrange(lmin):
            if int(l1[i]) > int(l2[i]):
                return 1
            if int(l1[i]) < int(l2[i]):
                return -1
        if lmin == lmax:
            return 0
        if len(l1) < lmax:
            for i in xrange(len(l1), lmax):
                if int(l2[i]) != 0:
                    return -1
            return 0
        else:
            for i in xrange(len(l2), lmax):
                if int(l1[i]) != 0:
                    return 1
            return 0