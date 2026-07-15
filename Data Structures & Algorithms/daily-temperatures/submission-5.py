class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ## waiting room method
        ## think hard, i believe its a tuple of index and temperature

        newTemps = []
        for i, temperature in enumerate(temperatures): 
            newTemps.append((temperature, i))

        waitingRoom = []
        result = []

        for i in range(len(temperatures)): 
            result.append(0)

        for i, temperature in enumerate(newTemps): 
            if waitingRoom: 
                waiting = waitingRoom[-1]
                while waiting[0] < temperature[0] and waitingRoom: 
                    result[waiting[1]] = temperature[1] - waiting[1]
                    waitingRoom.pop()
                    if waitingRoom: 
                        waiting = waitingRoom[-1]

            waitingRoom.append(temperature)
        
        return result

                
        

        


            


        