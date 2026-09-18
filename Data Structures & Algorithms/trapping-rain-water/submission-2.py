class Solution:
    def trap(self, height: List[int]) -> int:
        ## total amount of water. we need water sandwiched between two tall pillars
        ## two pillars where min middle heights not blocking

        l, r = 0, len(height) - 1
        result = 0
        leftMax, rightMax = height[l], height[r]

        while l < r: 
            ## so each one is actually limited by the min of that side
            ## if the max of the min side is smaller, we take that accumulate - whatever is there
            ## always bounded by the smaller
            if leftMax < rightMax: 
                l += 1
                leftMax = max(height[l], leftMax)
                result += (leftMax - height[l])
                
            else: 
                r -= 1
                rightMax = max(height[r], rightMax)
                result += (rightMax - height[r])
                
            
        return result

            
                





        