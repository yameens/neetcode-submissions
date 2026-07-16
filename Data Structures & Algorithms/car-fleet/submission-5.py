class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ## strategy
        ## create a new list with tuples
        ## then, sort the list in reverse (.sort(reverse=True))

        ## then, you need to understand that the top is going to reach the target first
        ## if the current reaches it faster, then no fleet, only if its slower then add one

        cars = []
        fleets = []
        for i, one in enumerate(position): 
            cars.append((position[i], speed[i]))
        
        cars.sort(reverse=True)

        for car in cars: 
            if fleets:
                top = fleets[-1]
                timeOne = (target - top[0]) / top[1]
                timeTwo = (target - car[0]) / car[1]
                if timeTwo > timeOne: 
                    fleets.append(car)
                ## append if the car does not catch up on time! 
            else: 
                fleets.append(car)
        
        return len(fleets)

            
        