# Runtime - 0 ms (100%) 
# Memory - 12.3 mb (62.77%)

class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        status = nums[0] % 2 
        for num in nums: 
            # if even
            if num % 2 > 0: 
                if status == 0: 
                    return False
                else: 
                    status = 0 
            # if even
            else:
                if status == 1: 
                    return False
                else: 
                    status = 1 
            
        return True
        