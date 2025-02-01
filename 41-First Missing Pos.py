# Runtime: 43 ms (74.18%) 
# Memory: 20.3 mb (65.13)

class Solution(object):
    def firstMissingPositive(self, nums):
        bool_list = [False] * (len(nums) + 1)

        i = 0 

        for num in nums: 
            if 0 < num <= len(nums) :
                bool_list[num] = True
            i += 1 

        i = 0

        for item in bool_list: 
            if item == False and i != 0: 
                return i
            i += 1 
        return i 
    
        
            

        