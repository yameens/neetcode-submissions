class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ## trick: you iterate through the different k
        ## binary search through the reasonable ks

        l, r = 1, max(piles)
        sol = float("inf")

        while l <= r: 
            m = (l + r) // 2
            current = 0
            for pile in piles: 
                if m != 0: 
                    current += math.ceil(pile / m) ## spills over to the next integer
            if current > h: 
                l = m + 1
            else:
                r = m - 1
                sol = min(sol, m)
        
        return sol




