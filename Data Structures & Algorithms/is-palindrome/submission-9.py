class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lower = s.lower()
        result = ""

        for char in lower: 
            if char.isalnum(): 
                result += char
        
        left = 0
        right = len(result) - 1

        while left < right: 
            if result[left] != result[right]:
                return False
            left += 1
            right -= 1
        
        return True
        