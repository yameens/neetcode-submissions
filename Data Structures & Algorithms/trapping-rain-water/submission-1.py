class Solution:
    def trap(self, height: List[int]) -> int:
    ## solution
    ## there is a left that is being updated, along with a right 

    ## we constantly look for the max, this is the heart of the computation
    ## min(leftMax, rightMax) - currentHeight
        ## we worry bar by bar, and focus on each bars contribution

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        result = 0

        while l < r: 
            if leftMax < rightMax:  
                l += 1
                leftMax = max(leftMax, height[l])
                result += leftMax - height[l]
                
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                result += rightMax - height[r]
                
        
        return result


     










        