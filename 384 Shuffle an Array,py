#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 15:59:36 2018

@author: yiqian
"""

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.mynums=nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.mynums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        return random.sample(self.mynums, len(self.mynums))
    
"""
learn random.sample(list, n)
randomly choose n elements from list as a new list 



"""
"""
    
import random
class Solution(object):

    def __init__(self, nums):
        :type nums: List[int]
        self.pos_dic = {}
        self.nums = nums
        self.shuffle_result = []
        for i in xrange(len(nums)):
            self.pos_dic[nums[i]] = i
            
        self.permutation_list = list(itertools.permutations(self.nums))
        

    def reset(self):
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        return self.nums

        

        

    def shuffle(self):
        Returns a random shuffling of the array.
        :rtype: List[int]

        return self.permutation_list[random.randint(0, len(self.permutation_list)-1)]
"""
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()