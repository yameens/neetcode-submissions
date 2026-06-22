class Solution:
    def isValid(self, s: str) -> bool:
        # parse through the string
        # add each instance of an open into a stack
        # if you see a predefined close, pop and compare to a map (keys) 

        count = {'}': '{', ')': '(', ']': '['}
        open = ['(', '[', '{']
        recent = []

        for character in s: 
            if character in open: 
                recent.append(character)
            if character in count.keys():
                if not recent: 
                    return False
                else:
                    boot = recent.pop()
                    if count[character] != boot:
                        return False
        if recent:
            return False
        return True
        