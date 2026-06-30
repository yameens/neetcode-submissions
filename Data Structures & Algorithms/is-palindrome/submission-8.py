class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lowerString = ""

        for char in s: 
            if char.isalnum():
                lowerString += char
        
        lowerString = lowerString.lower()

        ## processing is complete. 
        ## now this is a double pointer, start from beginning and compare with end

        lastIndex = len(lowerString) - 1
        firstIndex = 0

        while firstIndex < lastIndex: 
            if lowerString[firstIndex] != lowerString[lastIndex]:
                return False
            firstIndex += 1
            lastIndex -= 1
        
        return True
        
        