class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ## it is sorted. how it compares to the result, we shift the pointer

        l, r = 0, len(numbers) - 1

        while l < r: 
            if numbers[l] + numbers[r] < target: 
                l += 1
            elif numbers[l] + numbers[r] > target: 
                r -= 1
            elif numbers[l] + numbers[r] == target: 
                return [l + 1, r + 1]
        
        return -1
        