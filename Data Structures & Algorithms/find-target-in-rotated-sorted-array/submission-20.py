class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## strategy: 
            #a. find which half you are operating in. (is the left or the right half sorted?)
            #b. within that half, check where target lies

        
        l, r = 0, len(nums) - 1

        while l <= r: 
            m = (l + r) // 2

            if nums[m] == target: 
                return m
            
            if nums[l] <= nums[m]: 
                if nums[l] <= target < nums[m]: 
                    r = m - 1
                else: 
                    l = m + 1

            else:
                if nums[m] < target <= nums[r]: 
                    l = m + 1
                else: 
                    r = m - 1
        
        return -1
