class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "*", "-", "/"]

        for token in tokens: 
            if token not in operators: 
                stack.append(token)
            else: 
                tokenOne = int(stack.pop())
                tokenTwo = int(stack.pop())

                if token == "*": 
                    stack.append((tokenOne * tokenTwo))
                
                if token == "/": 
                    stack.append(int(tokenTwo / tokenOne))
                
                if token == "+": 
                    stack.append((tokenOne + tokenTwo))
                
                if token == "-": 
                    stack.append((tokenTwo - tokenOne))
        
        return int(stack.pop())

        
        