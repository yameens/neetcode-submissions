class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        sortedOne = "".join(sorted(s1))

        for r in range(len(s2)):
            windowSize = len(s1)
            sortedTwo = "".join(sorted(s2[l:windowSize + l]))
            if sortedOne == sortedTwo:
                return True
            else: 
                l += 1
        
        return False
            
        