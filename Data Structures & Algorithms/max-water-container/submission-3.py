class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ## looking for max between two
        ## value you are optimizing is lower of the heights x bars between
        ## must check out every combination ? 

        ## do you need to get a distance for every one ? 
        
        l = 0
        r = len(heights) - 1
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