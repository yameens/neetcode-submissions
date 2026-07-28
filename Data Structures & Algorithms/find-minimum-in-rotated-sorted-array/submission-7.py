class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        ## testing understanding of binary logic

        ## minimum, understand hwo rotations operate, left side and a right side

        l, r = 0, len(nums) - 1
        minim = max(nums)

        while l <= r: 
            middle = (l + r) // 2
            minim = min(minim, nums[middle])

            if nums[middle] <= nums[r]: 
                r = middle - 1
            else: 
                l = middle + 1
        
        return minim

