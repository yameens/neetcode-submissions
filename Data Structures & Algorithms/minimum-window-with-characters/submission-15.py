class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict

        substr = "" 
        l = 0
        frequency = defaultdict(int)
        window = defaultdict(int) ## frequency of the current window

        for char in t: 
            frequency[char] += 1
        
        need = len(frequency)
        have = 0

        for r in range(len(s)): 
            if s[r] in frequency: 
                window[s[r]] += 1
            
                if window[s[r]] == frequency[s[r]]: 
                    have += 1
            
            while have == need: 
                if substr == "" or (r - l + 1) < len(substr): 
                    substr = s[l: r + 1]

                if s[l] in frequency: 
                    window[s[l]] -= 1
                    if window[s[l]] < frequency[s[l]]:
                        have -= 1
                l += 1
        
        return substr