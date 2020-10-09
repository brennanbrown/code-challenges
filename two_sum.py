# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
class Solution:
    def two_sum(self, nums, target):
        table = dict()
        pair = []
        i = 0
        foundPair = False
        
        solution = False
        i = 0
        
        while i < len(nums):
            table[nums[i]] = i
            i += 1
        
        i = 0
        
        while i < len(nums) and not pair:
            compliment = target - nums[i]
            
            if compliment in table:
                if i != table[compliment]:
                    pair.append(i)
                    pair.append(table[compliment])
                    foundPair = True
                    
            i += 1
        
        return pair