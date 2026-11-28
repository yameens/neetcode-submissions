class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ## permutations, way of ordering 

        results = []
        permutation = []
        chosen = [False] * len(nums)

        def dfs(permutation): 
            if len(permutation) == len(nums): 
                results.append(permutation.copy())
                return
            
            for i in range(len(nums)): 
                if not chosen[i]: 
                    permutation.append(nums[i])
                    chosen[i] = True
                    dfs(permutation)
                
                    permutation.pop()
                    chosen[i] = False
        
        dfs(permutation)
        return results
                
                
                
            
            
            
            
            
        


        