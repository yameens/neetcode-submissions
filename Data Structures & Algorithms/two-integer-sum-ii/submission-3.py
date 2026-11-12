class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        ## always equal or the same, so must skip over double element indices
        s = numbers
        l, r = 0, len(s) - 1

        while l < r: 
            if s[l] + s[r] > target: 
                value = s[r]
                r -= 1
                while value == s[r]: 
                    r -= 1
                
            elif s[l] + s[r] < target: 
                value = s[l]
                l += 1
                while value == s[l]: 
                    l += 1

            elif s[l] + s[r] == target: 
                return [l + 1, r + 1]
        
        return -1

        