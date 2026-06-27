class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        ## pair them up
        ## sort them in reverse order 
        
        ## logic : the closest cars will only be caught up by the one before it if the one before it has
        ## a quicker arrival time. if thats the case, pop from the stack. 
        ## append arrival time in order, if the stack greater than two and index one is less than index two pop that

        pairsList = []
        finalStack = []

        for i in range(len(position)):
            pairsList.append((position[i], speed[i]))
            
        pairsList.sort(reverse=True)
        
        for pair in pairsList: 
            finalStack.append((target - pair[0]) / pair[1])
            if len(finalStack) >= 2 and finalStack[-1] <= finalStack[-2]:
                finalStack.pop()
        
        return len(finalStack)

            