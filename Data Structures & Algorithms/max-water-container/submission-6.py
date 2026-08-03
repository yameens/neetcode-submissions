class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        l, r = 0, len(heights) - 1
        
        while l < r: 
            local = min(heights[l], heights[r]) * (r - l)
            maximum = max(maximum, local)
            ## conditions that move the pointer: 
            if heights[l] < heights[r]: 
                l += 1
            else: 
                r -= 1

                ## always moves to the taller ones! 
        
        return maximum
        