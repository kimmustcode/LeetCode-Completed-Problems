# Runtime: 2838 ms (7.49%) 
# Memory: 12.24 mb (99.99%)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0 
        for num in nums: 
            c = target - num
            y = 0 
            for x in nums:
                if x == c and y != i: 
                    return [i, y]
                y += 1 
            i += 1