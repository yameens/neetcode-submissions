class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## sliding window
        ## snapshot until unique (not in the set)

        l = 0
        seen = set()
        maxLength = 0

        for r in range(len(s)): 
            
            while l < r and s[r] in seen: 
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            maxLength = max(maxLength, r - l + 1)
                
        return maxLength

        