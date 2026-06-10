# Runtime: 192 ms (8.67%) 
# Memory: 17.98 mb (100%)
class Solution:
    def checkRepeat(self, array) -> bool:
        return len(array) == len(set(array))

    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        window = [] 
        max = 1

        for char in s: 
            window.append(char)
            if len(window) >= 2: 
                check = self.checkRepeat(window)                
                done = False 

                while done == False and len(window) >= 2:
                    if check == True and len(window) >= max:
                        max = len(window)
                        done = True
                    elif check == False: 
                        window.pop(0)
                    else:
                        done = True
                    
                    check = self.checkRepeat(window)
        return max

