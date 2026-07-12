class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
       ## need frequencies
       ## update if you have every item 
            ## start with updating the left
        
        need = {}
        for char in t: 
            need[char] = need.get(char, 0) + 1
        needLen = len(need)
        
        have = 0 ## total number
        windowMap = {}
        result = ""
        resultLength = float("inf")

        l = 0
        for r in range(len(s)): 
            windowMap[s[r]] = windowMap.get(s[r], 0) + 1
            
            if s[r] in t and windowMap[s[r]] == need[s[r]]:
                have += 1
            
            while have == needLen: 
                currentLength = r - l + 1
                if currentLength < resultLength: 
                    resultLength = currentLength
                    result = s[l:r + 1]

                windowMap[s[l]] -= 1

                if s[l] in t and windowMap[s[l]] < need[s[l]]:
                    have -= 1

                l += 1
                    
        
        return result
            
            
            




                

            
