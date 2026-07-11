class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l = 0 
        need = {} ## here, need is simply the characters and count necessary. 

        for c in t: 
            need[c] = need.get(c, 0) + 1
        
        needLen = len(need) ## here, access the length of values
        have = 0
        haveCount = {}

        res, resLen = "", float("infinity")

        for r in range(len(s)): 
            haveCount[s[r]] = haveCount.get(s[r], 0) + 1
            
            if s[r] in need and haveCount[s[r]] == need[s[r]]:
                have += 1
            
            while have == needLen:
                resLen = min(resLen, r - l + 1)
                if (r - l + 1) == resLen: 
                    res = s[l:r + 1]
                haveCount[s[l]] -= 1

                if s[l] in need and haveCount[s[l]] < need[s[l]]: ## we only care about count of current letters
                    have -= 1

                
                l += 1


        
        return res

            




                

            
