class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        subs = []

        ## we need to go through all option, maybe using i

        def recursion(i): 
            if i == len(s): 
                result.append(subs.copy())
            
            for j in range(i, len(s)): 
            
                palindrome = True
                t, u = i, j

                while t <= u: 
                    if s[t] != s[u]: 
                        palindrome = False
                        break
                    
                    t += 1
                    u -= 1
                
                if palindrome == True: 
                    subs.append(s[i: j + 1])
                    recursion(j + 1) 
                    subs.pop()
                
                ## only appending that case if it is a palindrome
                ## if so, recurse on top of it
                ## still on that event want to choose outside of it, so pop! 

        recursion(0) 

        return result


        
        