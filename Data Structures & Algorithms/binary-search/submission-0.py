class Solution:
    def search(self, nums: List[int], target: int) -> int:

        right = len(nums) - 1
        left = 0

        while left <= right:  ## moves until unable to move again
            middle = (left + right) // 2 ## rounds up
            if nums[middle] > target: 
                right = middle - 1
            elif nums[middle] < target: 
                left = middle + 1 ## need to not include the middle
            else: 
                return middle
        
        return -1
            

        