class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lMax = 0
        rMax = 0
        total = 0
        while l < r: 
            lMax = max(height[l], lMax)
            rMax = max(height[r], rMax)
            currentHeight = min(lMax, rMax)

            if lMax < rMax: 
                total += currentHeight - height[l]
                l += 1
            else: 
                total += currentHeight - height[r]
                r -= 1
        
        return total



        