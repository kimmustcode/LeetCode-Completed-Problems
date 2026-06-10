# Runtime: 51 ms (23.6%) 
# Memory: 19.12 mb (68.88%)
class Solution:
    def reverse(self, x: int) -> int:
            revNum = '' 
            cleanNum = x
            isNeg = False
            
            if x < 0: 
                cleanNum = cleanNum * -1 
                isNeg = True 

            temp = cleanNum

            for i in range(len(str(cleanNum))):
                revNum = revNum + str(temp % 10)
                temp = temp // 10 

            if int(revNum) > pow(2, 31) - 1: 
                return 0

            return int(revNum) if not isNeg else -(int(revNum))
        