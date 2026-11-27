class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        solution = []
        candidates.sort()

        def dfs(i, target): 
            if target == 0: 
                solution.append(combinations.copy())
                return 
            
            if i == len(candidates) or target < 0: 
                return 
            
            target -= candidates[i]
            combinations.append(candidates[i])
            dfs(i + 1, target) 

            target += candidates[i]
            combinations.pop()
            
            while (i + 1 < len(candidates)) and (candidates[i + 1] == candidates[i]):
                i += 1

            dfs(i + 1, target)
        
        dfs(0, target)

        return solution
            

        
        