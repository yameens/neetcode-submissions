class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## always iterating r on its own, adjusting the left pointer
        ## whenever their is not enough space (current window - max freq) greater than how much we must replace, remove the frequency of the current left pointer and advance
        ## the largest freq matters so we don't waste time 

        maxFreq = 0
        solution = 0
        freq = {}
        l = 0

        for r in range(len(s)): 
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxFreq = max(maxFreq, freq[s[r]])
            while (r - l + 1) - maxFreq > k: 
                freq[s[l]] -= 1
                l += 1
            solution = max(solution, r - l + 1)
        
        return solution