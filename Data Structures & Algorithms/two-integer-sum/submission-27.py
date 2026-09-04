class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## two pointer solution
        ## check if they add up to desired target, if less, adjust

        result = []
        for i, num in enumerate(nums): 
            result.append((num, i))

        
        
        result = sorted(result)
        l, r = 0, len(nums) - 1

        while l < r: 
            if (result[l][0] + result[r][0] - target) == 0: 
                return (sorted([result[l][1], result[r][1]]))
            elif result[l][0] + result[r][0] - target > 0: 
                r -= 1
            else: 
                l += 1
        
        return []
        