#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 09:19:24 2018

@author: yiqian
"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(string, path, res, count):
            if count==3:
                if len(string)==1 and string[0]=='0':
                    res.append(path+string[:])
                elif len(string)>0 and len(string)<3 and string[0]!='0':
                    res.append(path+string[:])
                elif len(string)==3 and string[0]!='0' and string[:]<='255':
                    res.append(path+string[:])
                else:
                    return 
                
            if len(string)==0:
                return 
            if string[0]=='0':
                dfs(string[1:], path+string[0]+".", res, count+1)
            else:
                dfs(string[1:], path+string[0]+".", res, count+1)
                dfs(string[2:], path+string[0:2]+".", res, count+1)
                if string[0:3]>'255':
                    return 
                else:
                    dfs(string[3:], path+string[0:3]+".", res, count+1)
        
        res = []
        dfs(s, "", res, 0)
        return res