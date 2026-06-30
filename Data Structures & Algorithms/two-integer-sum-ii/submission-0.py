class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # map with indices
        # if target - map is a value in the key list, return index

        # no duplicates, map is fine ! 

        indexMap = {}
        for i, number in enumerate(numbers): 
            indexMap[number] = i
        
        for i in range(len(numbers)): 
            otherNumber = target - numbers[i]
            if otherNumber in indexMap.keys():
                return([i + 1, indexMap[otherNumber] + 1])
    
        return -1
        
        