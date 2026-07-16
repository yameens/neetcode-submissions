class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ## the number of fleets left, is the number of items in the stack

        fleets = []
        cars = []
        
        ## make a tuple for organization
        ## sort the list in terms of who is closest to the target. they start first
        ## there, you can easily pop to see who can catch up with who on time!
        

        for i, pos in enumerate(position):
            cars.append((position[i], speed[i]))
        
                                                    ## how do you sort again ? 
        
        cars.sort(reverse=True) 

        
        for car in cars: 
            if fleets:
                incumbant = fleets[-1]
                timeCurrent = (target - car[0]) / car[1]
                timeIncumbant = (target - incumbant[0]) / incumbant[1]
                if timeCurrent > timeIncumbant:
                    fleets.append(car) 
            else: 
                fleets.append(cars[0])               
        
        return len(fleets)



