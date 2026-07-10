class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      ## look for the longest frequency
      ## left and right sliding window 

        l = 0
        maxCount = 0
        count = {}
        res = 0

        for r in range(len(s)): 
            count[s[r]] = count.get(s[r], 0) + 1
            maxCount = max(maxCount, count[s[r]])
            if (r - l + 1) - maxCount > k: 
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

        



