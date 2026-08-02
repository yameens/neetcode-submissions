class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        result = ""
        for char in s: 
            if char.isalnum(): 
                if char.isalpha():
                    result += (char.lower())
                else: 
                    result += (char)
        l, r = 0, len(result) - 1
        while l < r: 
            if result[l] != result[r]:
                return False
            l += 1
            r -= 1
    
        return True