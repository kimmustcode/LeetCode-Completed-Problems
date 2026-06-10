# Runtime: 685 ms (30.99%) 
# Memory: 19.44 mb (20.48%)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        pos = 0 
        currMax = s[0] 

        while pos < len(s): 
            i = 1
            currstr_odd = s[pos]
            while pos - i >= 0 and pos + i < len(s): 
                if s[pos - i] == s[pos + i]: 
                    currstr_odd = s[pos-i] + currstr_odd + s[pos + i]
                    i += 1 
                else:
                    break 
            
            currstr_even = ""
            if pos + 1 < len(s) and s[pos] == s[pos + 1]:
                currstr_even = s[pos] + s[pos + 1]
                j = 1
                while pos - j >= 0 and pos + 1 + j < len(s):
                    if s[pos - j] == s[pos + 1 + j]:
                        currstr_even = s[pos - j] + currstr_even + s[pos + 1 + j]
                        j += 1
                    else:
                        break

            if len(currstr_odd) > len(currMax):
                currMax = currstr_odd
            if len(currstr_even) > len(currMax):
                currMax = currstr_even

            pos += 1  
        
        return currMax 