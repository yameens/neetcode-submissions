class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        middle = 0

        ## binary search, wipe out half of the possible solutions

        while l <= r:
            middle = (r + l) // 2
            if target > nums[middle]: 
                l = middle + 1
            elif target < nums[middle]: 
                r = middle - 1
            elif target == nums[middle]:
                return middle
        return -1
        