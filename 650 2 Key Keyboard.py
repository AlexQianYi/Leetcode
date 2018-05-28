#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 10:05:32 2018

@author: yiqian
"""

class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 0
        if n==2:
            return n
        
        if self.isPrime(n):
            return n
        
        return self.search(n)
    
    def search(self, n):
        primeList = [2]
        for x in range(3, n):
            if self.isPrime(x):
                primeList.append(x)
                
        for i in range(len(primeList)-1, -1, -1):
            if n%primeList[i]==0:
                r1 = primeList[i]
                r2 = n/r1
                print(r1, r2)
                if r2 in primeList:
                    return r1+r2
                else:
                    return self.search(r2)+r1
        
    def isPrime(self, n):
        for i in range(2, int(math.sqrt(n))+1):
            if n%i ==0:
                return False
        return True
        
    
    
    """
    2 Keys Keyboard
    
    2 kind of operations
    1. Copy all: you can copy all the characters present on the notepad (partial copy is not allowed)
    2. Paste: You can paste the characters which are copied last time
    
    the problem N can be divide these situations:
        1. N is prime   then we need N operations
        2. N=r1*r2  and r1 r2 both prime then we need r1+r2 operations
        3. N=r1*r2 and r1 is prime, so we recursive use step 2 we need r1+step2(r2)
    """