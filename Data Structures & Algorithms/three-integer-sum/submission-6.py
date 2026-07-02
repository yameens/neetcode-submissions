class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() ## don't assign to a new variable, just call
        final = []
        
        for i in range(len(nums)): ## a is the CURRENT value ! 
            l, r = i + 1, len(nums) - 1
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r: 
                result = nums[i] + nums[l] + nums[r]
                
                if result > 0: 
                    r -= 1
                elif result < 0:
                    l += 1
                elif result == 0: 
                    final.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                    ## how to take duplicate triplets ? 
            
        return final 
