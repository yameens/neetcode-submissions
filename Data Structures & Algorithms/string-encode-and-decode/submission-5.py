class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for word in strs: 
            final += "#"
            final += str(len(word))
            final += "#"
            final += word
        return final

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s): 
            num = ""
            word = ""
            if s[i] == "#":
                i += 1
                while s[i] != "#": 
                    num += s[i]
                    i += 1
                i += 1
            
            final = int(num)
            
            for n in range(final): 
                word += s[n + i]
            i += final

            strs.append(word)
        
        return strs






