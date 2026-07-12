class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        for l in range(len(nums)): 
            local = l
            currentMax = -float("inf")

            if local + k > len(nums): 
                break

            while local < l + k: ## local also increases
                currentMax = max(nums[local], currentMax)
                local += 1

            res.append(currentMax)

        return res
            
            


        