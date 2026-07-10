class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        sortedOne = "".join(sorted(s1))

        for r in range(len(s2)): 
            windowSize = len(sortedOne)
            sortedTwo = "".join(sorted(s2[l:l + windowSize]))

            if sortedOne == sortedTwo: 
                return True
                
            l += 1
        return False



    