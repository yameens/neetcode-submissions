class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == []: 
            return [[]]
        
        perms = self.permute(nums[1:]) ## only returning one result, really ingenious solution, because the permutations that are relevant are at the last level ([]) is the base case to be fully returned back up
        result = []

        for p in perms: 
            for i in range(len(p) + 1): 
                copy = p.copy()
                copy.insert(i, nums[0])
                result.append(copy)
        
        return result
