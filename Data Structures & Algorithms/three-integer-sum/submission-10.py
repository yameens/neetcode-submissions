class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        ## three sum baby, lets get it and run away maybe? 
        
        ## map out three of these indices. there is a left and a current index
        ## the current index is i. you can't really get a more efficient solution than that, right ? 
        ## anytime the values are the same, just skip over them. we kind of DO NOT want duplicates, right? 

        
        nums.sort()
        result = []

        for i in range(len(nums)): 
            
            if 1 <= i and nums[i] == nums[i - 1]: 
                continue
            
            if i + 1 >= len(nums): 
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r: 
                remainder = nums[l] + nums[r] + nums[i]
                if remainder < 0: 
                    l += 1

                elif remainder > 0: 
                    r -= 1

                elif remainder == 0: 
                    result.append([nums[l], nums[r], nums[i]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: 
                        l += 1

                    r -= 1
                    while nums[r] == nums[r + 1] and l < r: 
                        r -= 1
        
        return result

        ## guard rails. but you need to run two pointers for every i. really close but KEEP on hustling through! this is really important! keep on moving through!
        ## keep going through all the guard rails you can. 

        
            