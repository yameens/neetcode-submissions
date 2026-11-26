class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ## backtracking, include an item and remove it
        result = []
        combination = []
        
        def dfs(i, target): 
            if target == 0: 
                result.append(combination.copy())
                return

            if i == len(nums) or target < 0: 
                return
            
            target -= nums[i]
            combination.append(nums[i])
            dfs(i, target)

            target += nums[i]
            combination.pop()
            dfs(i + 1, target)
        
        dfs(0, target)
        return result


        