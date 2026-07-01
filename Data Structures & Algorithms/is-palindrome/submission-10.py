class Solution:
    def isPalindrome(self, s: str) -> bool:
        ## clean list
        ## compare left and right pointers 

        lower = s.lower()
        palindrome = ""

        for char in lower: 
            if char.isalnum(): 
                palindrome += char
        
        left = 0
        right = len(palindrome) - 1

        while left < right: 
            if palindrome[left] != palindrome[right]: 
                return False

            left += 1
            right -= 1
        
        return True