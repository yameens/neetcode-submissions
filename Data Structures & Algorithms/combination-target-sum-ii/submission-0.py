class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ## unique candidates eh ? 

        ## issue, there is repetition when it comes to the combinations !
        ## thus, we must sort once, and skip any repeats (sort candidates)

        ## do this after selecting the first value

        subset = []
        result = []
        candidates.sort() ## .sort method does so in place

        def dfs(total, i): 
            if total == target: 
                result.append(subset.copy())
                return
            elif total > target or i >= len(candidates): 
                return 
            
            subset.append(candidates[i])
            dfs(total + candidates[i], i + 1) 
            subset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]: 
                i += 1
            
            ## skips all of the repeats in the non selected version ! 
            dfs(total, i + 1)
        
        dfs(0, 0)
        return result

        