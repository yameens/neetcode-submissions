class Solution:
    def isValid(self, s: str) -> bool:
        matches = {')': '(', ']': '[', '}': '{'}
        open = ['(', '[', '{']
        recent = [ ]

        for character in s: 
            if character in open:
                recent.append(character)
            if character in matches.keys():
                if recent:
                    top = recent.pop()
                    if top != matches[character]:
                        return False
                else:
                    return False
        if recent:
            return False
        
        return True

        # every time you encounter a closed parenthesis, you pop from the stack
        # and match with the value of the match key
        