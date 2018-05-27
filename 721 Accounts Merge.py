#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 12:10:52 2018

@author: yiqian
"""

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        result = []
        userDic = {}
        userList = []
        userListIndex = 0
        resultIndex = 0
        
        tempList = []
        
        for i in range(len(accounts)):
            name = accounts[i][0]
            if name in userDic:
                originUserIndex = userDic[name]
                for j in range(len(userList[originUserIndex])):              
                    find = False
                    k, m = 1, 0
                    tempList = accounts[i][1:]
                    while k<len(accounts[i]):
                        if accounts[i][k] in result[userList[originUserIndex][j]]:
                            del tempList[m]
                            find = True
                            m -= 1
                        k += 1
                        m += 1

                    if find:
                        print(tempList)
                        result[userList[originUserIndex][j]] = result[userList[originUserIndex][j]] + tempList
                            
                if not find:
                    result.append(accounts[i])
                    userList[originUserIndex].append(resultIndex)
                    resultIndex += 1
                    
            else:
                userDic[name] = userListIndex
                result.append(accounts[i])
                userList.append([resultIndex])
                resultIndex += 1
                
        return result
        
    
    """
    merge the same person's email accounts
    """