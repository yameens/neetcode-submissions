class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
       # strategy
       # memory of constant counting. have a count length.
       # if the count is larger than "k",

        count = {}
        maxFrequency = 0
        left = 0
        resolution = 0

        for right in range(len(s)): 
            count[s[right]] = count.get(s[right], 0) + 1
            maxFrequency = max(maxFrequency, count[s[right]])
            
            if (right - left + 1) - maxFrequency > k: 
                count[s[left]] -= 1
                left += 1

            resolution = max(resolution, right - left + 1)

        return resolution
        