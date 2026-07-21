class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = max(piles)
        

        while l <= r: 
            feasible = True
            k = (r + l) // 2
            timeCompleted = 0

            for pile in piles: 
                timeCompleted += math.ceil(pile / k)

                if timeCompleted > h: 
                    feasible = False
                    break

            if feasible == False: 
                l = k + 1
            elif feasible == True: 
                r = k - 1
                result = min(result, k)

        return result


