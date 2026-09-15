class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        keys = defaultdict(list)
        for string in strs: 
            ## count = defaultdict(int) ## can't be a dictionary, tuples of a dictionary only looks at the key!
            count = [0] * 26
            for char in string: 
                count[ord(char) - ord("a")] += 1
                ## each become a slot, 26 values, that we increment by frequency
            
            key = tuple(count)
            keys[key].append(string)
        
        result = []
        for key in keys: 
            result.append(keys[key])
        
        return result
    

    ## notes

    # initializing a list of a number, is [number] * frequency
    # tuples only grab the keys of a dictionary, not the values
    # ord puts a numerical value to each letter in the alphabet! so you can place in correct index by subtracting letter
        