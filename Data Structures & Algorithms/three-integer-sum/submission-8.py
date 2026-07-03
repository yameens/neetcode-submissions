class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        for i in range(len(nums)): 
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            
            while l < r: 
                remainder = nums[r] + nums[l] + nums[i]

                if remainder < 0: 
                    l += 1
                elif remainder > 0: 
                    r -= 1
                elif remainder == 0: 
                    results.append([nums[r], nums[l], nums[i]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                
        return results   

