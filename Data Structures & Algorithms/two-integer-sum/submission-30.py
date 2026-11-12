class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        for i, num in enumerate(nums): 
            targets[num] = i
        
        for j, num in enumerate(nums): 
            if (target - num) in targets.keys() and j != targets[target - num]: 
                return [j, targets[target - num]]
        
        return -1

        
        