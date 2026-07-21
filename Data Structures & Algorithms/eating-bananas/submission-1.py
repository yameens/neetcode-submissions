class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = max(piles)

        while l <= r: 
            totalTime = 0
            feasible = True
            k = (l + r) // 2

            for pile in piles: 
                totalTime += math.ceil(pile / k) ## rounds up

                if totalTime > h: 
                    feasible = False
                    break
                
            if feasible:
                result = min(result, k)
                r = k - 1
            
            if not feasible: 
                l = k + 1
        
        return result


        