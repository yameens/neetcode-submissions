class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l, r = 0, len(heights) - 1

        while l < r: 
            current = (r - l) * min(heights[r], heights[l])
            maxWater = max(maxWater, current)
            if heights[l] < heights[r]: 
                l += 1
            else: 
                r -= 1
        
        return maxWater
    
