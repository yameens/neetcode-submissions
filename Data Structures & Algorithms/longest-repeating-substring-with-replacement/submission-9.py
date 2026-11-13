class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        characters = {}
        maxFrequency = 0
        solution = 0
        l = 0

        for r in range(len(s)): 
            characters[s[r]] = 1 + characters.get(s[r], 0)
            maxFrequency = max(maxFrequency, characters[s[r]])
            
            while (r - l + 1) - maxFrequency > k: 
                characters[s[l]] -= 1
                l += 1
            
            solution = max(solution, r - l + 1)
        
        return solution


        
        