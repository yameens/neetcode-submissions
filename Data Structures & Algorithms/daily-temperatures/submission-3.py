class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ## objective : ith day: future warmer temperature for that ith day
        ## local number higher stored within index

        ## naive approach

                # results = []

                # for i in range(len(temperatures)): 
                #     local = 0
                #     found = False

                #     for j in range(i, len(temperatures)): 
                #         if temperatures[j] <= temperatures[i]:
                #             local += 1
                            
                #         if temperatures[j] > temperatures[i]: 
                #             found = True
                #             results.append(local)
                #             break

                #     if found == False:
                #         results.append(0)
                
                # return results

        # stack method. add everything onto a stack : 
        
        stack = []
        result = []
        for i in range(len(temperatures)): 
            result.append(0)

        for i, temperature in enumerate(temperatures): 
            while stack and temperature > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = i - stackIndex
            stack.append((temperature, i))
        
        return result

        

        


            


        