class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l = 0
        sizeOne = len(s1)
        sizeTwo = len(s2)
        target = "".join(sorted(s1))

        for r in range(sizeTwo):
            capture = s2[l: r + 1]
            contender = "".join(sorted(capture))
            if contender == target: 
                return True
            elif (r - l + 1 >= sizeOne):
                l += 1
        
        return False