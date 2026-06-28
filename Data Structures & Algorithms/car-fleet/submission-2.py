class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        ## logic. 
        ## cars that are right behind and get to the arrival before
        ## these cars are going to catch up and be part of the same fleet
        ## and since they are part of the same fleet, pop the other one
        ## pair them up to make popping easier

        pairs = []
        proximity = []
        iterations = len(position)
        for i in range(iterations): 
            pairs.append((position[i], speed[i]))
        
        pairs.sort(reverse=True)
        
        for pair in pairs: 
            proximity.append((target - pair[0]) / pair[1])
            if len(proximity) >= 2 and proximity[-1] <= proximity[-2]:
                proximity.pop()
        
        return len(proximity)


            