class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        close = 0
        open = 0
        result = []
        sub = []

        def recursion(close, open): 
            if (close + open) == (2 * n): 
                result.append("".join(sub))
                return
             
            if (close + open) > (2 * n):    
                return
            
            if open < n: 
                sub.append("(")
                recursion(close, open + 1)
                sub.pop()
            
            if close < open: 
                sub.append(")")
                recursion(close + 1, open)
                sub.pop()

        recursion(0, 0)

        return result


        