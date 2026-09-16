class Solution:
    def isValid(self, s: str) -> bool:
        ## stack as well
        close = {")": "(", "]":"[", "}":"{"}
        opens = ("(", "[", "{")
        stack = []

        for char in s: 
            if char in opens: 
                stack.append(char)
            
            if char in close: 
                if not stack: 
                    return False
                recent = stack.pop()
                if close[char] != recent: 
                    return False
        
        if stack: 
            return False

        return True


        