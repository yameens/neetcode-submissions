class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ["+", "*", "-", "/"]
        stack = []

        for token in tokens:
            if token not in operands: 
                stack.append(token)

            if token in operands: 
                itemOne = int(stack.pop())
                itemTwo = int(stack.pop())
                
                if token == "+":
                    result = itemOne + itemTwo
                elif token == "*":
                    result = itemOne * itemTwo
                elif token == "-":
                    result = itemTwo - itemOne  
                elif token == "/":
                    result = itemTwo / itemOne  
            
                stack.append(result)
        
        return int(stack.pop())
                