class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0
        
        while l < r: 
            currentArea = (r - l) * min(heights[l], heights[r])

            if maxArea < currentArea: 
                maxArea = currentArea
            

            if heights[l] < heights[r]: 
                l += 1
            
            else: 
                r -= 1
        
        return maxArea