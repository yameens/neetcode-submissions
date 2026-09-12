class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""

        for word in strs: 
            encode += "#"
            encode += str(len(word)) ## length could be greater than one digit / most important
            encode += "#"
            encode += word

        return encode

    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0

        ## accessing the last index means len - 1, which is goal (use less than)
        while i < len(s): 
        
            if s[i] == "#": 
                i += 1
                end = i

                while s[end] != "#": 
                    end += 1
                
                ## don't include end, because it will be left off on a hash: #
                length = s[i:end]
                i = end + 1
                word = ""

                for j in range(i, i + int(length)): 
                    word += s[j]
                
                decode.append(word)
                i += int(length)
        
        return decode
                

                
