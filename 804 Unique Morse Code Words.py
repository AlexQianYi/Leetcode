#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 15:53:46 2018

@author: yiqian
"""

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dic = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", \
               'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", \
               'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", \
               'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}
        
        dic_morse = {}
        result = 0
        for i in xrange(len(words)):
            temp_str = ""
            for j in xrange(len(words[i])):
                temp_str += dic[words[i][j]]
            if temp_str not in dic_morse:
                result += 1
                dic_morse[temp_str] = 1
        return result