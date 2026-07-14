class Solution:
    def isValid(self, param: str) -> bool:
        ## stack, last in is the first out ! 

        stack = []
        open = ["{", "(", "["]
        close = {"}" : "{", ")" : "(", "]" : "["}

        flag = True

        for char in param: 
            if char in open: 
                stack.append(char)
                
            if char in close.keys(): 
                if stack: 
                    current = stack.pop()
                    if current != close[char]: 
                        flag = False
                else: 
                    flag = False
            
        if stack: 
            flag = False

        return flag

            

        