class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxLength = 0
        left = 0 
        seen = set()

        for right in range(len(s)): 
            
            while s[right] in seen: 
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength

    # the strategy
    # i need to account for non adjacent duplicate characters
    # thus, while the CURRENT letter is in the set, we remove the previous letters until it is non unique and we can start fresh again
    # the previous max is accounted for (right - left + 1), + 1 because zero based indexing

                
